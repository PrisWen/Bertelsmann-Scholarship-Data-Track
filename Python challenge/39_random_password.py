#While generating a password by selecting random characters usually creates one that is relatively secure, it also generally gives a password that is difficult to memorize. As an alternative, some systems construct a password by taking two English words and concatenating them. While this password may not be as secure, it is normally much easier to memorize.Write a program that reads a file containing a list of words, randomly selects two of them, and concatenates them to produce a new password. When producing the password ensure that the total length is between 8 and 10 characters, and that each word used is at least three letters long. Capitalize each word in the password so that the user can easily see where one word ends and the next one begins. Finally, your program should display the password for the user.


#Run: 39_random_password.py names.txt

from sys import argv
import random
try: 
    name_file = argv[1]
    lines = open(name_file).read().splitlines()
    while 1:
        # choosing 2 words
        w1 = random.choice(lines)
        w2 = random.choice(lines)
        password = w1 + w2

        # total length is between 8 and 10 characters, at least three letters by word
        if(8 < len(password) < 10 and len(w1) >= 3 and len(w2) >= 3):
            print('Password is:',w1.capitalize()+ w2.capitalize())
            break
except:
    print('Error in file')
