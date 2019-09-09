# import necessary modules first
import os, zipfile, xml.etree.ElementTree as ET
from langdetect import detect
sign = ':' # for checking if there is a colon (":") in the <book-title> tag text
# insert your directory path in the "directory" variable
directory = 'C:/Users/rriza/Desktop/1/'
reference = '{http://www.gribuser.ru/xml/fictionbook/2.0}'
file_extension = ".fb2"
zip_extension = ".zip"

# checks for the .zip files in the directory and unzip it to the same directory with deleting the original zip file
os.chdir(directory) # change directory from working dir to dir with files
for item in os.listdir(directory): # loop through items in dir
    if item.endswith(zip_extension): # check for ".zip" extension
        full_path = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(full_path) # create zipfile object
        zip_ref.extractall(directory) # extract file to dir
        zip_ref.close() # close file
        os.remove(full_path) # delete zipped file
print("\n")

# fb2-book title finder
# checks for the .fb2 files in the directory and finds its <book-title> tag text and renames the file with this text
for file in os.listdir(directory):
    if file.endswith(file_extension): # checks for .fb2 files in the directory
        #print("initial file name: " + file)
        root = ET.parse(directory + file).getroot()
# checks the third hierarchy layer of xml structure to find the <book-title> tag text
        for i in root:
            for x in i:
                for y in x:
                    if y.tag == reference + 'book-title' and detect(y.text) == 'ru': # put preferred language instead of "ru"
                        bt = y.text # puts <book-title> tag text in the "bt" variable
                        if bt.find(sign) > 0: # checks for the colon sign (":") in the <book-title> tag text
                            #print("found ':' sign in the book title")
                            bt = bt[0:bt.find(sign)] # if <book-title> tag text have
                            # colon in it, delete the colon and text after the colon
                            #print(bt)
                        dst = bt + file_extension
                        src = directory + file
                        dst = directory + dst
                        os.rename(src, dst) # rename file according to its <book-title> tag text
    else:
        print("There are no " + file_extension + " files in folder") # if there are no .fb2 files in the directory prints out this message
for file in os.listdir(directory):
    if file.endswith(file_extension):
        print("renamed file: " + file) # prints out all renamed files
