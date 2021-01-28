#When one writes a function, it is generally a good idea to include a comment that outlines the function’s purpose, its parameters and its return value. However, sometimes comments are forgotten, or left out by well-intentioned programmers that plan to write them later but then never get around to it. Create a Python program that reads one or more Python source files and identifies functions that are not immediately preceded by a comment. For the purposes of this exercise, assume that any line that begins with def, followed by a space, is the beginning of a function definition. Assume that the comment character, #, will be the first character on the previous line when the function has a comment. Display the names of all of the functions that are missing comments, along with the file name and line number where the function definition is located.The user will provide the names of one or more Python files as command line arguments, all of which should be analyzed by your program. An appropriate error message should be displayed for any files that do not exist or cannot be opened. Then your program should process the remaining files.

#Run: 43_missing_comments.py 43_comments1.py 43_comments2.py 43_comments3.py

from sys import argv

# parameter command line
if len(argv)<2:
    print("Please enter file names separated by space")
    quit()

name_files = argv[1:]


for name in name_files:
    try:
        #open files
        file = open(name, "r")
        previous_line = ' '
        nro_line = 1
        for line in file:
            #find function and check if previous line is a comment
            if(line.startswith('def ') and previous_line[0] !='#'):
                #print name function, name file and line number of functions that are not commented
                print('Name function: {} Name file: {} Line number {}'.format(line[4:line.index('(')],name,nro_line))
            previous_line = line
            nro_line +=1 
        file.close()
    except:
        print('Error in file', name)