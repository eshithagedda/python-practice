print("Enter Credentials!")
user = str(input("Please enter your username: "))
pass2 = input("Please enter your password: ")

print('LOGIN')
inputuser = str(input("Enter your username: "))
inputpass = input("Enter your password: ")

if inputuser == user:
    if inputpass == pass2:
        print("Logged in")

else:
    print("oops :(")