
def encoder():
    holder = [*pw]  # holder is a container, pw is turned into str list
    holder = [int(x) for x in holder]  # every item in holder list is turned into integer
    holder = [x + 3 for x in holder]  # add 3 for each item
    enc_pw = [x % 10 if x >= 10 else x for x in holder]  # if item is >= 10, then use % to get ones position
    complete = "".join((str(x) for x in enc_pw))  # converts the manipulated list back to string
    return complete

def decode():
    holder = [*encoded]
    holder = [int(x) for x in holder] #this turns the characters in the number string from str to int to allow for manipulation
    holder = [x - 3 for x in holder] #this lowers the value of every digit in the password string by 3
    complete = "".join((str(x) for x in enc_pw))
    return complete


if __name__ == "__main__":
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")   # prints menu for user, asks for number input
        x = int(input("Please enter an option: "))
        if x == 1:
            pw = input("Please enter your password to encode: ")   # "pw" stores password from user
            print("Your password has been encoded and stored!\n")
        if x == 2:
            encoded = encoder()
            print(f"The encoded password is {encoded}, and the original password is {pw}.\n")
        if x == 3:
            quit()
