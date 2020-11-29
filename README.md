# [fb2 file renamer](https://rvildanov93.github.io/fb2-file-renamer/)

This python script unpacks `.zip` files that contains `.fb2` files inside and then renames `.fb2` files according to its `<book-title>` tags. If there are no `.zip` files in the specified directory, skips the unpacking part.

This version of script can rename russian book-titles only. I will hopefully work on other functionality later.
Firstly, script checks for the `.zip` files in the specified directory (`directory` variable) and upacks files to the same directory with deleting the original ones.
Then it checks for the `.fb2` files in the directory and finds its tag text, renames the file with this text and prints the list of renamed `.fb2` files in the console.
Script should work fine with Python v3.7 and later.

## Status

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/rvildanov93/fb2-file-renamer/master/LICENSE)

## Download and Installation

To begin using this script, choose one of the following options to get started:

- Clone the repo:

`git clone https://github.com/rvildanov93/fb2-file-renamer.git`

- [or Download on GitHub](https://github.com/rvildanov93/fb2-file-renamer.git)

Also you have to install [langdetect](https://pypi.org/project/langdetect/) python module via console command:

`pip install langdetect`

## Usage
First you have to copy directory path of your zipped books folder to paste it in the script later. In the example bellow directory path is `C:\Users\RAMIL\Desktop\books`.

<img src ="https://raw.githubusercontent.com/rvildanov93/fb2-file-renamer/master/img/zipped_folder_.png">

Each `.zip` file contains `.fb2` file inside. We are going to change the name of `.fb2` file written in english according to its `<book-title>` xml tag which written in russian.

<img src ="https://raw.githubusercontent.com/rvildanov93/fb2-file-renamer/master/img/fb2_example_.png">

If you open `.fb2` file in the text editor you will see `<book-title>` tag inside structured xml code.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink">
<description>
  <title-info>
    <genre>adv_animal</genre>
    <genre>sci_biology</genre>
    <genre>sci_popular</genre>
    <genre>science</genre>
    <author>
      <first-name>Конрад</first-name>
      <middle-name>Захариас</middle-name>
      <last-name>Лоренц</last-name>
    </author>
    <book-title>Кольцо царя Соломона</book-title>
```

Open `fb2_file_renamer.py` file in your Python interpreter ([PyCharm](https://www.jetbrains.com/pycharm/) for example) and paste your directory path you copied earlier in the `directory` variable value. Then change backslashes in pasted string to forward slashes so Python can read your file path.

```python
# insert your directory in the "directory" variable
directory = 'C:/Users/RAMIL/Desktop/books/'
```

Finally run the script and you will see the list of renamed files in the console. If there are no `.fb2` files in the specified directory script prints out message: "There are no `.fb2` files in folder".

```sh
renamed file: Архетипы и коллективное бессознательное.fb2
renamed file: Кольцо царя Соломона.fb2
renamed file: Мир как воля и представление.fb2
renamed file: Потерянный рай.fb2
```

You will see only renamed `.fb2` files in specified folder. `zip` archives will be deleted automatically.

<img src ="https://raw.githubusercontent.com/rvildanov93/fb2-file-renamer/master/img/final_result_.png">

## Bugs and Issues

Have a bug or an issue with this script? [Open a new issue](https://github.com/rvildanov93/fb2-file-renamer/issues) here on GitHub or write me a message on the [ramilvildanov.ru](https://ramilvildanov.ru).

## About

fb2 file renamer was created by and is maintained by **[Ramil Vildanov](https://ramilvildanov.ru/)**.

- <https://twitter.com/rvildanov93>
- <https://github.com/rvildanov93>

## Copyright and License

Copyright 2019-2020 Ramil Vildanov. Code released under the [MIT](https://raw.githubusercontent.com/rvildanov93/fb2-file-renamer/master/LICENSE) license.
