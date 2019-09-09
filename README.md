# fb2-file-renamer
This python script unpacks ".zip" files that contains ".fb2" files in it and then renames ".fb2" files according to its &lt;book-title> tags. If there are no ".zip" files in the directory, skips the unpacking part.

First script checks for the ".zip" files in the directory ("directory" variable) and upacks it to the same directory with deleting the original ".zip" file.

Then it checks for the ".fb2" files in the directory and finds its <book-title> tag text, renames the file with this text, and prints out the list of renamed ".fb2" files.

Script should work fine with Python 3.7.
