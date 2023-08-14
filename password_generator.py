import random
def password(num):
    char="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*abcdefghijklmnopqrstuvwxyz"
    passwd=""
    for i in range(num):
        passwd=passwd+random.choice(char)
    return passwd

def main():
    name=input("Enter Username:")
    num=int(input("Enter Length Of Password You Want:"))
    passwd=password(num)
    print("Here's, your Generated Password:",passwd,"\n")

while True:
    print("1.Enter 1 for Turning ON Password Generator")
    print("2.Enter 2. to Exit Password Generator")
    ch=int(input("Enter:"))
    if(ch==1):
        main()
    else:
        print("Turned OFF")
        break
