from function import start_chat ,add_status,add_friend,send_message,read_message
from steganography.steganography import Steganography
from datetime import datetime
from spy_details import spy,friends
status_message = ['diksha','chandel']


print "Hello! Welcome in spy chat application.Let\'s get started.."
question = "Continue as " +spy['salutation'] + " " +spy['name'] + "(Y/N)?"
existing = raw_input(question)

if (existing.upper() == "Y"):
    start_chat(spy['name'],spy['age'],spy['rating'])

elif (existing.upper() == "N"):
    spy_name = raw_input("welcome to spy chat,you must tell me your name first: ")
    if len(spy_name) > 0:
        spy_salutation = raw_input("Should I call you Mr. or Ms.?: ")
        spy_age = raw_input("What is your age?")
        spy_age = int(spy_age)
        spy_rating = raw_input("What is your spy rating?")
        spy_rating = float(spy_rating)
        spy_is_online = True
        if spy_age > 12 and spy_age < 50:
            print "Authentication complete. Welcome " + spy_name + " age: " + spy_age+ " and rating of: " + spy_rating + " Proud to have you onboard"

            start_chat(spy_name, spy_age, spy_rating)

        else:
            print"Sorry! you are not correct age to be a spy.."

    else:
        print("Error")

else:
    print("plz enter either y or n:")