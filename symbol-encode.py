alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
"0", "1", "2", "3", "4", "5", "6", "7", "8", "9","0", "1", "2", "3", "4", "5", "6", "7", "8", "9","0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
"0", "1",]
symbols = ['✹','✿','✄','⍟','௹','﹄','♞','♚','♟','☁','♨','☽','↕','⌤','☊','☧','☢','卐','❧','유','∎','∴','⊶','㊂','⍋','⊘','✹','✿','✄','⍟','௹','﹄','♞','♚','♟','☁','♨','☽','↕','⌤','☊','☧','☢','卐','❧','유','∎','∴','⊶','㊂','⍋','⊘']
symbols4numbers = ['⌨','©','🏚','🏞','🏘','🏗','🏛','➿','🪚','⌦','⌨','©','🏚','🏞','🏘','🏗','🏛','➿','🪚','⌦'
,'⌨','©','🏚','🏞','🏘','🏗','🏛','➿','🪚','⌦','⌨','©','🏚','🏞','🏘','🏗','🏛','➿','🪚','⌦'
,'⌨','©','🏚','🏞','🏘','🏗','🏛','➿','🪚','⌦','⌨','©']

print("Welcome to Caeser cipher encryptor\n")
notStep = []
def numCheck():
        #Putting only the number part of step as step
        splitStep = []
        step_string = ''
        for i in enterStep:
            if i in numbers:
                splitStep.append(i)
            elif enterStep != ' ':
                notStep.append(i)
            step_string = "".join(splitStep)
        return step_string
# function base:
def caeser(start_text, shift_amount, process):
    if process == "encode":
        encoded_text = ""
        for i in start_text:
            if i in alphabet:
                position = alphabet.index(i)
                new_pos = position + shift_amount
                encoded_text += symbols[new_pos]
            elif i in numbers:
                position = numbers.index(i)
                new_pos = position + shift_amount
                encoded_text += symbols4numbers[new_pos]

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
            if i in symbols:
                position = symbols.index(i)
                new_pos = position + shift_amount
                decoded_message += alphabet[new_pos]
            elif i in symbols4numbers:
                position = symbols4numbers.index(i)
                new_pos = position + shift_amount
                decoded_message += numbers[new_pos - 6]
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
      
        if enterDirection == "encode":
            enterStep = input("\nEnter the step number:\n")
            stepAsString = numCheck() #numCheck() would contain return value

            while stepAsString == "":
                notStep = []
                stepAsString = input("\nPlease enter a number:\n")
                stepAsString = numCheck()
           
            if notStep != []:
                rem_step = "".join(notStep)
                print(f"\nFor your information these characters are not used in the step: {rem_step}")
            
            step = int(stepAsString)
            stepForAlphabet = step % 26
            caeser(enterMessage, stepForAlphabet, enterDirection)
            #Step is divided so the step cannot be above 25

       #------------------------------------------------------------------------------------------

        if enterDirection == "decode":
            enterMessage = enterMessage.split()
            EncodedStringStep = enterMessage.pop()
            message_without_step = ' '.join(enterMessage)
            
            string_stepNum = ""
            for i in EncodedStringStep:
                string_stepNum += str(alphabet.index(i))
                step = int(string_stepNum) * -1
            stepForAlphabet = step % 26
            caeser(message_without_step, stepForAlphabet, enterDirection)
        
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
