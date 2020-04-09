#import libraries
import string
import random

# get user details
def get_details():
    first_name = input("Enter your First Name below \n")
    second_name = input("Enter your Second Name below \n")
    user_email = input("Enter your Email Address below \n")
    details = [first_name, second_name, user_email]
    return details

# genereate random password using user details
def gen_password(details):
    characters = string.ascii_letters
    length = 5
    random_password = ''.join(random.choice(characters) for p in range(length))
    password = str(details[0][0:2] + details[1][-2] + random_password)
    return password
#main program
status = True
container = []
while status:
    #get user details
    details = get_details()

    #show generated password
    password = gen_password(details)
    print("Your password is: " + str(password))
    #ask if he/she is satisfied with the password
    password_agree = input(str("Do you like the generated password? Enter Yes if Yes, No if No and provide password)"))

    password_loop = True
    while password_loop:
        if password_agree =="Yes":
            #add password to user details
            details.append(password)

            #add user details to overall container
            container.append(details)
            password_loop = False
        else:
            #enter a password longer than or equal to 7
            user_password = input(str("Enter password longer than or equal to 7"))

            #password length loop
            pass_len = True
            while pass_len:
                if len(user_password) >= 7:
                    #add password to user details
                    details.append(user_password)
                    #add user details to container
                    container.append(details)
                    #break out of password length check loop
                    pass_len = False
                    #break out of the whole password loop
                    password_loop = False
                else:
                    print("Your password is less than 7")
                    user_password = input(str("Enter password longer than or equal to 7"))
    #new user
    new_user = input(str("Would you like to enter a new user? Yes or No"))
    if(new_user == "No"):
        status = False
        for item in container:
            print(item)
    else:
        status = True



