# fb2-file-renamer
<img src ="https://raw.githubusercontent.com/rvildanov93/fb2-file-renamer/master/file_renamer_cover_for_gh.jpg" width=50%px height =50%px >
This python script unpacks ".zip" files that contains ".fb2" files inside and then renames ".fb2" files according to its &lt;book-title> tags. If there are no ".zip" files in the directory, skips the unpacking part.

Firstly, script checks for the ".zip" files in the specified directory ("directory" variable) and upacks files to the same directory with deleting the original ones.

Then it checks for the ".fb2" files in the directory and finds its <book-title> tag text, renames the file with this text and prints the list of renamed ".fb2" files in the console.

Script should work fine with Python 3.7.
