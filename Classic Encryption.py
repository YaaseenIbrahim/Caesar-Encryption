alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("Welcome to Caeser cipher encryptor\n")
spaceArr = [""]


def numCheck():
    """Only takes numbers into account"""
    #Putting only the number part of step as step
    notStep = []
    splitStep = []
    step_string = ''
    for i in enterStep:
        if i in numbers:
            splitStep.append(i)
        elif i != ' ':
            notStep.append(i)
    step_string = "".join(splitStep)
    rem_step = ''
    if notStep != []:
        rem_step = "".join(notStep)
        print(f"\nFor your information these characters are not used in the step: {rem_step}")

    return step_string


def hasAnyNums(num):
    """Checks if the input has any numbers"""
    countNum = 0
    for i in num:
        if i in numbers:
            countNum += 1
        if countNum > 0:
            return True
    return False

def spaceCheck(spac):
    """Checks if the entire string is empty"""
    count = 0
    spacAsArr = spac.split(" ")
    for i in spacAsArr:
        if i in spaceArr:
            count += 1
    if len(spacAsArr) == count:
        return True
    return False

# function base:


def caeser(start_text, shift_amount, process):
    if process == "encode":
        encoded_text = ""
        for i in start_text:
            if i in alphabet:
                position = alphabet.index(i)
                new_pos = position + shift_amount
                encoded_text += alphabet[new_pos]
            else:
                encoded_text += i
                             
        print("\nHere is your code:", f"\n{encoded_text}")

    if process == "decode":
        decoded_message = ""
        for i in start_text:
            if i in alphabet:
                position = alphabet.index(i)
                new_pos = position + shift_amount
                decoded_message += alphabet[new_pos]
            else:
                decoded_message += i
        print("\nHere is your decoded message:", f"\n{decoded_message}")

# end of function - - - - - - - - - - - - - -


run = True
while run:
    enterDirection = input( "Type 'encode' to encrypt and 'decode' to decrypt data:\n").lower()

    # Validation for inputting something other than encode or decode
    if enterDirection == "encode" or enterDirection == "decode":
        enterMessage = input("\nEnter the message:\n").lower()

        # When they input blank for enterMessage
        while spaceCheck(enterMessage):
            enterMessage = input("\nERROR, You left it blank! Please write something\n")

        if enterDirection == "encode":
            enterStep = input("\nEnter the step number:\n")
            
            # Checking if step has any numbers
            while not hasAnyNums(enterStep):
                enterStep = input("\nPlease enter a number:\n")

            stepAsString = numCheck() #Only taking number part of step
            step = int(stepAsString)
            stepForAlphabet = step % 26
            caeser(enterMessage, stepForAlphabet, enterDirection)
            #Step is divided so the step cannot be above 25

       #------------------------------------------------------------------------------------------

        if enterDirection == "decode":
            
            step = int(input("\nEnter the step number:\n")) * -1
            stepForAlphabet = step % 26
            caeser(enterMessage, stepForAlphabet, enterDirection)

        rep = True
        while rep:  # Validation for if its not Y or N
            choice = input( "\nDo you want to Continue encrypting? Type 'Y' or 'N':\n").lower()
            if choice == 'n' or choice == 'y':
                encodedStepString = ""
                rem_step = ''
                rep = False
        if choice == "n":
            run = False
    else:
        print("SYNTAX ERROR, You have to write encode or decode only")
        choice = input("Type y to try again and n to stop:\n").lower()
        if choice == 'n':
            run = False

print("Hope encrypting was fun :)")
