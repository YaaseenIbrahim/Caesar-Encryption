alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("Welcome to Caeser cipher encryptor\n")

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

        encoded_shift = ""

        for i in str(step):
            encoded_shift += alphabet[int(i)]
        final_text = f"{encoded_text} {encoded_shift}"
        print("\nHere is your code:", f"\n{final_text}")

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
    enterDirection = input("Type 'encode' to encrypt and 'decode' to decrypt data:\n").lower()

    # Validation for inputting something other than encode or decode
    if enterDirection == "encode" or enterDirection == "decode":
        enterMessage = input("\nEnter the message:\n").lower()
        arrayText = enterMessage.split()  # Makes text array with all words spillted

        if enterDirection == "encode":
            # Getting the step
            
            stepLetter = arrayText.pop() #Takes oout the last word of text which should be our step
            text = ' '.join(arrayText)
            
        #    testing
            
            #Putting only the number part of step as step
            splitStep = []
            for i in stepLetter:
                if i in numbers:
                    splitStep.append(i)
                step_string = "".join(splitStep)

            if step_string == "":
                print("SYNTAX ERROR, You must enter a number value for the Step")
               
            else:
                step = int(step_string)
                stepForAlphabet = step % 26
                caeser(text, stepForAlphabet, enterDirection)
            #Step is divided so the step cannot be above 25

            

       #------------------------------------------------------------------------------------------

        if enterDirection == "decode":
            
            EncodedStringStep = arrayText.pop()
            message_without_step = ' '.join(arrayText)
            
            string_stepNum = ""
            for i in EncodedStringStep:
                string_stepNum += str(alphabet.index(i))
                step = int(string_stepNum) * -1
            step = step % 26
            caeser(message_without_step, step, enterDirection)
        
        rep = True
        while rep:  # Validation for if its not Y or N
            choice = input("\nDo you want to Continue encrypting? Type 'Y' or 'N':\n").lower()
            if choice == 'n' or choice == 'y':
                rep = False
        if choice == "n":
                run = False
    else:
        print("SYNTAX ERROR, You have to write encode or decode only")
        choice = input("Type y to try again and n to stop:\n").lower()
        if choice == 'n':
            run = False

print("Hope encrypting was fun :)")
