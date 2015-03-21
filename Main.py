__author__ = 'Sean'
import pickle
import getpass
import sys
import time


def intro():
    print("""
         #####################################################################
         #####################################################################
         ### _,  __, _,    _, _ ___ _ __,   __,  _, ___  _, __,  _,  _, __,###
         ### |   |_) |     |\ |  |  | | \   | \ / \  |  / \ |_) / \ (_  |_ ###
         ### | , |_) | ,   | \|  |  | |_/   |_/ |~|  |  |~| |_) |~| , ) |  ###
         ### ~~~ ~   ~~~   ~  ~  ~  ~ ~     ~   ~ ~  ~  ~ ~ ~   ~ ~  ~  ~~~###
         #####################################################################
         #####################################################################
          """)



def username_password():
    print("\nWelcome please enter your username and password.")
    while True:
        try:
            user_name = input("\nUsername: ")
            pass_word = getpass.getpass("\nPassword: ")
            users = ["Sean"]
            passwords = ["Password", "Letmein",]
            if user_name in users and pass_word in passwords:
                print("\nWelcome", user_name, "these are your options..")
                break
            elif user_name in users and pass_word not in passwords:
                print("\nINCORRECT PASSWORD SUPPLIED")
            elif user_name not in users and pass_word in passwords:
                print("\nINCORRECT USER ID SUPPLIED")
            elif user_name not in users and pass_word not in passwords:
                print("\nINCORRECT USERNAME AND PASSWORD SUPPLIED")
        except ValueError:
            print("\nCommand not recongnised")


def exit():
    print("\nThank you for using/updating the database")
    print("\nProgram Author: Sean Boyd")
    input("\nPress enter to close")
    sys.exit()


def remove_id():
    my_dict = {}
    my_dict = pickle.load(open("dict_save.p", "rb"))
    print("Please type the LBL number you wish to remove")
    lbl = input("LBL : ")
    if lbl in my_dict:
        del my_dict[lbl]
        print("\nOkay I have deleted that.")
        pickle.dump(my_dict, open ("dict_save.p", "wb"))
        print("\nYou will be returned to the menu")
        time.sleep(2)
        menu()
    else:
        print("\nThat is not in the database, you will be returned to the menu")
        time.sleep(2)
        menu()


def menu():
    while True:


        print("""
                               _______________________________
                              | _, _ __, _, _ _,_             |
                              | |\/| |_  |\ | | |             |
                              | |  | |   | \| | |             |
                              | ~  ~ ~~~ ~  ~ `~'             |
                              | 1. ID LOOKUP                  |
                              | 2. REMOVE ID                  |
                              | 3. EXIT PROGRAM               |
                              |_______________________________|
                                                 """)

        user_choice = input("\nWhat do you want to do?:")
        if int(user_choice) == 1:
            main()
        elif int(user_choice) == 2:
            remove_id()
        elif int(user_choice) == 3:
            exit()
        else:
            print("That was not an option")


def main():
    try:

        my_dict = {}
        my_dict = pickle.load(open("dict_save.p", "rb"))
    except EOFError:
        my_dict = {}

    while True:
        try:

            lbl = input("\nLBL Number: ")

            if lbl in my_dict:
                agent_id = my_dict[lbl]
                print("\nAgent ID associated with that number", agent_id )
                input("\nPress Enter to return to menu")
                time.sleep(2)
                menu()


            elif lbl not in my_dict:
                agent_id = input("\nCould not find LBL, please add : ")
                my_dict[lbl] = agent_id
                pickle.dump(my_dict, open ("dict_save.p", "wb"))
                print("\nOkay I have added that for you.")
                input("\nPress Enter to return to menu")
                time.sleep(2)
                menu()
            else:
                print("\nNot Recognized")

        except EOFError:
            my_dict = {}



intro()
username_password()
menu()
input("Press any key to exit")
