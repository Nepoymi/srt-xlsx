# [RU/[EN](https://github.com/Nepoymi/srt-xlsx/blob/main/README_eng.md)]

# [УСТАНОВКА(ru)](https://github.com/Nepoymi/srt-xlsx/blob/main/Install_rus.md) / [INSTALLATION(en)](https://github.com/Nepoymi/srt-xlsx/blob/main/Install_eng.md)

# srt-xlsx
На просторах интернета уже есть [файл для преобразования .srt в .xlsx](https://gist.github.com/b-adams/ee9fd90f3d85bb2a2da1).
Однако я, спользуя его, нашёл ряд недостатков:
 - Скрипт не гибкий - файл субтитров должен находится в той же папке, что и скрипт и должен называться "Wildlife.srt", файл таблицы тоже будет в той же папке и будет называться "Subtitle.xlsx"
 - Отсуствует первая строка - при переносе в таблицу пропадает первая строка
 - Сама таблица не оформленна - все ячейки имеют изначальный размер, так что текст выходит за их рамки
 - Странно работает перенос строк - при переносе строк в субтитрах (\n) создаётся новая ячейка

### Import-файл (.srt, открытый в AegisSub)
![Изначаниый файл сабов](https://github.com/Nepoymi/srt-xlsx/blob/main/images/input%20srt.png)
### Export-файл (.xslx, открытый в Microsoft Excel)
![Старый файл таблицы](https://github.com/Nepoymi/srt-xlsx/blob/main/images/output%20old%20xslx.png)

## Моя модификаия и дополнение

Я решил исправить все волнующие меня вышеперечисленные недостатки
 - Скрипт стал гибким - при его запуске вы сами выбираете любой файл в любой папке и выбираете куда/как сохранить файл .xslx
 - Первая строка снова на месте)
 - Ячейки стали шире - для индекса - 10, для таймингов - 30, для текста - 80.
 - Нормальный перенос строк - при переносе строк в субтитрах в таблице тоже переносятся строки

### Import-файл (.srt, открытый в AegisSub)
![Изначаниый файл сабов](https://github.com/Nepoymi/srt-xlsx/blob/main/images/input%20srt.png)
### Export-файл (.xslx, открытый в Microsoft Excel)
![Новый файл таблицы](https://github.com/Nepoymi/srt-xlsx/blob/main/images/output%20new%20xslx.png)

Также я сделал обратный скрипт - из такой таблицы .xlsx в субтитры .srt

### Import-файл (.xslx, открытый в Microsoft Excel)
![Новый файл таблицы](https://github.com/Nepoymi/srt-xlsx/blob/main/images/output%20new%20xslx.png)
### Export-файл (.srt, открытый в AegisSub)
![Конечный файл сабов](https://github.com/Nepoymi/srt-xlsx/blob/main/images/output%20srt.png)

Как видите, субтитры отлично перенеслись туда-обратно без каких-либо изменений

### Изначальный и конечный файлы (.srt, открытыев AegisSub)
![Изначаниый файл сабов](https://github.com/Nepoymi/srt-xlsx/blob/main/images/input%20srt.png)
![Конечный файл сабов](https://github.com/Nepoymi/srt-xlsx/blob/main/images/output%20srt.png)
