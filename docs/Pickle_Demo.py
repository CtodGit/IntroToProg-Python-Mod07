# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Creating a simple demonstration of pickling persistence with
# error handling and catching, it's a guess the password minigame
# ChangeLog (Who,When,What):
# CTodhunter,06.01.2020, wrote script for assignment, tested code and file
# CTodhunter,06.02.2020, added comments for assignment

# --------------------------------------------------------------------------------------------------- #


# Data ______________________________________________________________________________________________ #
# Declare variables and constants, import modules pickle and time
import pickle
import time

strAnswer = ''
correct = 'the password'
file_name = 'C:\\_PythonClass\\Assignment07\\Pickle_Try.dat'
objFile = None
T_minus = 1234
# --------------------------------------------------------------------------------------------------- #


# Processing _________________________________________________________________________________________#

# Starting with error handling, trying to open file, if file exists, assigns current
# value to T_minus variable from pickle.load of file_name, then closes the file.
try:

        objFile = open(file_name, 'rb')
        print('File Exists')

        T_minus = pickle.load(objFile)
        T_minus += 1
        objFile.close()

# catching an exception of type FileNotFoundError, creating a new file, dumping default
# T_minus value via pickle.dump(), closing objFile when complete, prints note to user that
# a new log has been created.
except (FileNotFoundError):
        T_minus = 11
        objFile = open(file_name, 'wb+')
        pickle.dump(T_minus, objFile)
        objFile.close()
        print('Creating new log...')
# --------------------------------------------------------------------------------------------------- #



# Main() _____________________________________________________________________________________________#

print('''

                         _   _                                                      _ 
                        | | | |                                                    | |
                        | |_| |__   ___   _ __   __ _ ___ _____      _____  _ __ __| |
                        | __| '_ \ / _ \ | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |
                        | |_| | | |  __/ | |_) | (_| \__ \__ \\\ V  V / (_) | | | (_| |
                         \__|_| |_|\___| | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
                                         | |                                          
                                         |_|                                          
''')



# Starting a while loop, using error handling as a switch for kicks (could have been just if else)

# Code first tries the following
# if: I'm testing if the user has enter 'the password', if they have, if case is true, code executes message
# to user, resets T_minus value to 10, opens the file, dumps the new reset value, closes the file, and exits.

# else: if the user has not entered the password, than T_minus docs one try, I then open the file, dump the
# updated value, close the file, and then intentionally code a ZeroDivision error to force a caught exception

# Code excepts ZeroDivision error if user entered wrong password, inputs current tries left to user, gives
# option to exit if they don't know the password with another if/else pair. If exit than file opens, dumps
# current T_minus value, closes file, than exits program.

while True:


        try:

                if strAnswer == correct:
                        print('''
                        
                          _____            _                                     _     _ _   _ 
                         / ____|          | |                                   | |   (_) | | |
                        | |     ___   ___ | |    _   _  ___  _   _    __ _  ___ | |_   _| |_| |
                        | |    / _ \ / _ \| |   | | | |/ _ \| | | |  / _` |/ _ \| __| | | __| |
                        | |___| (_) | (_) | |_  | |_| | (_) | |_| | | (_| | (_) | |_  | | |_|_|
                         \_____\___/ \___/|_( )  \__, |\___/ \__,_|  \__, |\___/ \__| |_|\__(_)
                                            |/    __/ |               __/ |                    
                                                 |___/               |___/                     
                        ''')
                        T_minus = 10
                        objFile = open(file_name, 'wb')
                        pickle.dump(T_minus, objFile)
                        objFile.close()
                        exit()
                else:
                        T_minus -= 1
                        objFile = open(file_name, 'wb')
                        pickle.dump(T_minus, objFile)
                        objFile.close()
 # here is the forced divide by zero
                        e = T_minus/0

# this is where the exception let's the user know they have T_minus tries left to guess the password
        except ZeroDivisionError:
                strAnswer = input(f'You have {str(T_minus)} try/tries left to enter the password, or '
                                  f'type exit to give up: ')

# the program will exit here if the user wants, but it will save the number of attemps for the next time
# the program is executed (this way they can't have unlimited attempts)
                if strAnswer.lower() == 'exit':

                        objFile = open(file_name, 'wb+')
                        pickle.dump(T_minus, objFile)
                        objFile.close()
                        exit()

# if the user fails to enter 'the password' after ten tries, a fake message is printed to screen
                elif T_minus == 0:
                        print('Erasing hard disk....')
# the program will pause for 5 seconds as if it was actually erasing something (it's not don't worry)
                        time.sleep(5)
                        print('Hard disk erased, goodbye!')
                        time.sleep(1)
# after one final goodbye message and a one second pause, an infinite while loop is created to panic the user
# again... it's just a joke
                        while True:
                                print("01010111011", end='')
# message with tries left will continue to display until they either exit or get the correct answer
                else:
                        continue


# --------------------------------------------------------------------------------------------------- #




