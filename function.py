
from steganography.steganography import Steganography
from spy_details import spy,friends
from datetime import datetime
friends1 = []
STATUS_MESSAGE = ['Good Morning','Bussy','urgent']
friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []


def start_chat(spy_name,spy_age,spy_rating):
    current_status_message = None
    spy_name = spy['salutation'] + " " + spy['name']


    show_menu = True
    while show_menu:
        menu_choices = ("What do you want to do ? \n 1. Add a status update\n 2. Add a Friend\n 3. send a secret message \n 4. Read a secret message \n 5. Exit\n")

        menu_choice = raw_input(menu_choices)
        menu_choice = int(menu_choice)
        if(menu_choice == 1):
            current_status_message = add_status(current_status_message)


        elif(menu_choice==2):
            number_of_friends = add_friend()
            print"You have %d friends"% (number_of_friends)
        elif(menu_choice==3):
            send_message()

        elif(menu_choice==4):
            read_message()

        else:
            show_menu = False
            print("Exit")



# add a status
def add_status(current_status_message):

    if current_status_message != None:
        print "Your current status message is %s \n " + current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (Y/N)")
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0 :
            STATUS_MESSAGE.append(new_status_message)
            updated_status_message = new_status_message
            print STATUS_MESSAGE

        else:
            print ("You don't enter any message ")

    elif default.upper() == 'Y':
        ver = 1
        for message in STATUS_MESSAGE:
            print "%d. %s" % (ver,message)
            ver = ver + 1


        message_selection = int(raw_input("\nChoose from the above messages "))
        if len(STATUS_MESSAGE) >= message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection - 1]

        else:
            print("The option you choose is not valid!")


        if updated_status_message:
            print 'Your updated status message is: %s' % (updated_status_message)
        else:
            print 'You did not update your status message'

        return updated_status_message


#add a friend
def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend['salutation'], friend['name'],friend['rating'])


        item_number =item_number+1
    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position
#function to define select a friend
def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend['name'],friend['age'],friend['rating'])


        item_number =item_number+1
    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position






#function to define add a friend

def add_friend():

    new_name = raw_input("Please add your friend's name:")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")
    new_name = new_name + " " + new_salutation
    new_age = raw_input("Age?")
    new_rating = raw_input("Spy rating?")

    new_age = int(new_age)
    new_rating = float(new_rating)
    if len(new_name) > 0 and new_age > 12 and new_rating >= new_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends_name)
#function to define send message
def send_message():
    friend_choice = select_a_friend()

    image_name = raw_input("What is the name of the image?")
    path = "secret1.jpg"
    input = raw_input("What do you want to say?")
    Steganography.encode(image_name,path, input)
    new_chat = {
        "message": input,
        "time": datetime.now(),
        "sent_by_me": True
    }
    friends[friend_choice]['chats'].append(new_chat)
    print "Your secret message image is ready!"





#function to define read message
def read_message():
  sender = select_a_friend()

  output_path = raw_input("What is the name of the file?")
  secret_text = Steganography.decode(output_path)
  new_chat = {
      "message": secret_text,
      "time": datetime.now(),
      "sent_by_me": False
  }

  friends[sender]['chats'].append(new_chat)
  print "Your secret message has been saved!"


