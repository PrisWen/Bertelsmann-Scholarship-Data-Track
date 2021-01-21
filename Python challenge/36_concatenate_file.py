#Display one or more files whose names are provided as command line parameters. 
#The files are displayed in the same order that they appear on the command line.
#Create a Python program that performs this task. It should generate an appropriate error message for any file that cannot be displayed, and then proceed to the next file. Display an appropriate error message if your program is started without any command line parameters.

#Run: concatenate_file.py elements.txt elements2.txt

from sys import argv

# parameter command line
if len(argv)<2:
    print("Please enter file names separated by space")
    quit()

my_files = argv[1:]
# Concatenate in new file
with open('new_file.txt', 'w') as new_file:
    #open file by file
    for file_name in my_files:
        try:
            with open(file_name, 'r') as file:
                for content in list(file):
                    new_file.write(content)
                new_file.write('\n')
        except:
            print('Error in file', file_name)
            continue

