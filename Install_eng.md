# Installation

First download python and all dependencies:

## Windows

https://www.python.org/downloads/

Important: When installing, check “Add Python to PATH” and make sure “Tcl/Tk and IDLE” is enabled (this will install Tkinter).

Next, in cmd:

`python -m ensurepip --upgrade`.

`pip install xlsxwriter openpyxl`.

## Linux:

### Ubuntu/Debian:

`sudo apt-get update`.

`sudo apt-get install python3 python3-tk python3-pip`

`pip install xlsxwriter openpyxl`

### Fedora:

`sudo dnf install python3 python3-tkinter python3-pip`

`pip install xlsxwriter openpyxl`

### Arch/Manjaro:

`sudo pacman -S python tk python-pip`.

`pip install xlsxwriter openpyxl`

### openSUSE:

`sudo zypper install python3 python3-tk python3-pip`

`pip install xlsxwriter openpyxl`

## install the script:

I won't explain how to install git on windup and all linux, you'll figure it out on your own, I think. Either just skip the first two commands, download the repository from the site and just type `cd /path/to/folder/srt-xlsx` in the terminal
 
`git clone https://github.com/Nepoymi/srt-xlsx.git`

`cd srt-xslx`

`python srt_to_xslx.py`

or

`python xslx_to_srt.py`
