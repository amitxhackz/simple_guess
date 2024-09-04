#### made by amitxhackz   #### 

our_password = "pass123"
your_answer = ""
number_of_try = 0
number_max_of_try = 8
Max_try = "not reached"

while your_answer != our_password and Max_try != "Reached":
    if number_of_try < number_max_of_try:
        your_answer = input("What is the Password: ")
        number_of_try = number_of_try + 1
        if your_answer != our_password:
            print("Wrong Password! Try again.")

    else:
        Max_try = "Reached"

if Max_try == "Reached":
    print("Your Account Blocked")

else:
    print("Access Granted!")
