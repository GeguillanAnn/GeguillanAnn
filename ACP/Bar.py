import os 
import datetime
import csv
import sys
import time

class Bar():
    def open():
        while True:
            os.system('cls')
            print("Welcome to Luffy's"
                    "\n\nWhat do you want to do?"
                    "\t1. View menu.\n"
                    "\t2. Add Food\n"
                    "\t3. Serve Food\n"
                    "\t4. View Food Served\n"
                    "\t5. Close System\n")
            getChoice()
    
    def _getChoice():
        while True:
            os.system('cls')
            try:
                input = Input.string("-> ")
                int [i] = Inreger.parseInt(input)
                if (i < 1 and i > 5):
                    raise Exception()
                performAction(i)
            except(NumberFormatException):
                print("Input must be a number.")
            except(ChoiceException):
                print("Input must be any of the ff: (1,2,3,4)")
                pass
    
    def _performAction(int choice):
        input_1 = str(input("Select Your Choice: ")).upper()
        time.sleep(1) # sleep 1 second
        os.system("cls")
        if input == 1:
            showMenu("")
            break
        elif input == 2:
            addFood("")
            break

