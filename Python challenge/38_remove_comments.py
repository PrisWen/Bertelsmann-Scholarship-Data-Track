#Python uses the # character to mark the beginning of a comment. The comment ends at the end of the line containing the # character. 
#In this exercise, you will create a program that removes all of the comments from a Python source file. Check each line in the file to determine if a # character is present. 
#If it is then your program should remove all of the characters from the # character to the end of the line (we’ll ignore the situation where the comment character occurs inside of a string). Save the modified file using a new name that will be entered by the user. 
#The user will also enter the name of the input file. Ensure that an appropriate error message is displayed if a problem is encountered while accessing the files. 

#Run: 38_remove_comments.py element_1.txt new_file.txt

from sys import argv
# parameter command line
if len(argv)<3:
    print("Please enter file names separated by space")
    quit()

my_file = argv[1]
# New file
with open(argv[2], 'w') as new_file:
    #open file
    try:
        with open(my_file, 'r') as file:
            for content in list(file):
                content = content.strip()
                if content[0] != '#':
                    new_file.write(content + '\n')
    except:
        print('Error in file', my_file)
        quit()

