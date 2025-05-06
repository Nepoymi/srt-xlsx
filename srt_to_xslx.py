# Перед выполнением - pip install xlsxwriter
import xlsxwriter
import re
import logging
from tkinter import Tk, filedialog

def parse_subtitles(lines):
    line_index = re.compile(r'^\s*\d+\s*$')
    line_timestamp = re.compile(r'^\s*\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}\s*$')
    line_seperator = re.compile(r'^\s*$')

    current_record = {'index': None, 'timestamp': None, 'subtitles': []}
    state = 'seeking'

    for line in lines:
        line = line.strip('\n').strip('\ufeff')
        
        if state == 'seeking':
            if line_index.match(line):
                current_record['index'] = line.strip()
                state = 'timestamp'
            elif line_seperator.match(line):
                continue
            else:
                logging.error(f'Unexpected data (seeking): [{line}]')

        elif state == 'timestamp':
            if line_timestamp.match(line):
                current_record['timestamp'] = line.strip()
                state = 'subtitles'
            else:
                logging.error(f'Unexpected data (timestamp): [{line}]')
                state = 'seeking'

        elif state == 'subtitles':
            if line_seperator.match(line):
                yield current_record
                state = 'seeking'
                current_record = {'index': None, 'timestamp': None, 'subtitles': []}
            else:
                current_record['subtitles'].append(line)

        else:
            logging.error(f'Unknown state: {state}')
    
    if current_record['index']:
        yield current_record

def write_to_excel(records, workbook, worksheet):
    worksheet.write(0, 0, "Index")
    worksheet.write(0, 1, "Timestamp")
    worksheet.write(0, 2, "Subtitles")
    
    wrap_format = workbook.add_format({'text_wrap': True})
    
    for row_num, record in enumerate(records, 1):
        worksheet.write(row_num, 0, record['index'])
        worksheet.write(row_num, 1, record['timestamp'])
        subtitle_text = '\n'.join(record['subtitles'])
        worksheet.write(row_num, 2, subtitle_text, wrap_format)
        
    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 80)

def convert():
    root = Tk()
    root.withdraw()
    
    # Выбор исходного файла
    input_filename = filedialog.askopenfilename(
        title="Выберите SRT файл",
        filetypes=[("SRT файлы", "*.srt"), ("Все файлы", "*.*")]
    )
    if not input_filename:
        return
    
    # Выбор выходного файла
    output_filename = filedialog.asksaveasfilename(
        title="Сохранить как XLSX",
        defaultextension=".xlsx",
        filetypes=[("Excel файлы", "*.xlsx"), ("Все файлы", "*.*")]
    )
    if not output_filename:
        return
    
    with open(input_filename, 'r', encoding='utf-8') as f:
        records = list(parse_subtitles(f))
        
        workbook = xlsxwriter.Workbook(output_filename)
        worksheet = workbook.add_worksheet()
        
        write_to_excel(records, workbook, worksheet)
        workbook.close()

if __name__ == "__main__":
    convert()
