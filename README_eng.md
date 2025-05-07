# [[RU](https://github.com/Nepoymi/srt-xlsx/blob/main/README.md)/EN]

# srt-xlsx
There is already [file for converting .srt to .xlsx](https://gist.github.com/b-adams/ee9fd90f3d85bb2a2da1).
However, using it, I found a number of disadvantages:
 - The script is not flexible - the subtitle file should be in the same folder as the script and should be called “Wildlife.srt”, the table file will also be in the same folder and will be called “Subtitle.xlsx”
 - The first line is missing - the first line is missing when transferring to the table.
 - The table itself is not designed - all the cells have the original size, so the text goes beyond their boundaries
 - Row transfer works strangely - when moving rows in subtitles (\n), a new cell is created.

### Import file (.srt opened in AegisSub)
![Original Sub file](https://github.com/Nepoymi/srt-xlsx/blob/main/images/input%20srt.png)
### Export file (.xslx opened in Microsoft Excel)
![Old table file](https://github.com/Nepoymi/srt-xlsx/blob/main/images/output%20old%20xslx.png)

### My modification and addition

I decided to fix all the flaws I was worried about above
 - The script became flexible - when you run it, you select any file in any folder and choose where/how to save the .xslx file.
 - The first line is back in place)
 - Cells became wider - for index - 10, for timings - 30, for text - 80.
 - Normal row transfer - when you move rows in subtitles in the table, the rows are also moved.

### Import file (.srt, opened in AegisSub)
![Original Sub file](https://github.com/Nepoymi/srt-xlsx/blob/main/images/input%20srt.png)
### Export-file (.xslx, opened in Microsoft Excel)
![New table file](https://github.com/Nepoymi/srt-xlsx/blob/main/images/output%20new%20xslx.png)

I also made a reverse script - from such a .xlsx table to .srt subtitles

### Import file (.xslx opened in Microsoft Excel)
![New table file](https://github.com/Nepoymi/srt-xlsx/blob/main/images/output%20new%20xslx.png)
### Export file (.srt opened in AegisSub)
![Final Sub file](https://github.com/Nepoymi/srt-xlsx/blob/main/images/output%20srt.png)

As you can see, the subtitles transferred back and forth just fine without any modifications

### Original and final files (.srt, opened in AegisSub)
![Original Sub file](https://github.com/Nepoymi/srt-xlsx/blob/main/images/input%20srt.png)
![Final Sub file](https://github.com/Nepoymi/srt-xlsx/blob/main/images/output%20srt.png)
