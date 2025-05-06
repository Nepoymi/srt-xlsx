# Установка

Сначала скачаем python и все зависимости:

## Windows

https://www.python.org/downloads/

Важно: При установке отметьте галочку "Add Python to PATH" и убедитесь, что "Tcl/Tk and IDLE" включено (это установит Tkinter).

Далее в cmd:

`python -m ensurepip --upgrade`

`pip install xlsxwriter openpyxl`

## Linux:

### Ubuntu/Debian:

`sudo apt-get update`

`sudo apt-get install python3 python3-tk python3-pip`

### Fedora:

`sudo dnf install python3 python3-tkinter python3-pip`

### Arch/Manjaro:

`sudo pacman -S python tk python-pip`

### openSUSE:

`sudo zypper install python3 python3-tk python3-pip`

# Установка скрипта:

Я не буду пояснять как ставить git на винду и на все линуксы, сами разберётесь, думаю. Либо просто пропустите первый две команды, скачайте репозиторий с сайта и просто в терминале введите `сd /путь/до/папки/srt-xlsx`
 
`git clone https://github.com/Nepoymi/srt-xlsx.git`

`cd srt-xslx`

`python srt_to_xslx.py`

или

`python xslx_to_srt.py`
