alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("Welcome to Caeser cipher encryptor\n")

run = True
while run:
    enterDirection = input("Type 'encode' to encrypt and 'decode' to decrypt data:\n").lower()

    # Validation for inputting something other than encode or decode
    if enterDirection == "encode" or enterDirection == "decode":
        # The text we are inputting
        enterMessage = input("\nEnter the message:\n").lower()

        if enterDirection == "decode":
            text_array = enterMessage.split()
            step_as_letter = text_array[-1]
            if len(step_as_letter) > 9:
                split_of_step_as_letter = step_as_letter.split()

        # Getting the step
        arrayText = enterMessage.split() #Makes text array with all words spillted
        stepLetter = arrayText.pop() #Takes oout the last word of text which should be our step
        splitStep = []
        text = ' '.join(arrayText)
        
        #Putting only the number part of step as step
        for i in stepLetter:
            if i in numbers:
                splitStep.append(i)
            stepNoInt = "".join(splitStep)
        step = int(stepNoInt)

        # function base:
        def caeser(start_text, shift_amount, cipher_direction):
            encoded_text = ""
            if cipher_direction == "decode":
                shift_amount *= -1
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
        # end of function - - - - - - - - - - - - - -
        
        # step is divided so the step cannot be above 25
        stepForAlphabet = step % 26
        caeser(text, stepForAlphabet, enterDirection)
        choice = input("\nDo you want to Continue encrypting? Type 'Y' or 'N':\n").lower()
        if choice == "n":
            run = False
    else:
        print("Syntax error, You have to write encode or decode only")
        choice = input("Type y to try again and n to stop:\n").lower()
        if choice == 'n':
            run = False

print("Hope encrypting was fun :)")
