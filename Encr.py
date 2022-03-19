alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2","3", "4", "5", "6", "7", "8", "9"]
print("Welcome to Caeser cipher encryptor\n")

run = True
while run:
    enterDirection = input("Type 'encode' to encrypt and 'decode' to decrypt data:\n").lower()
    
    #Validation for inputting something other than encode or decode
    if enterDirection == "encode" or enterDirection == "decode":
        text = input("\nEnter the message:\n").lower() #The text we are inputting
        
        #Getting the step
        msgArray = text.split(" ")
        stepArray = msgArray[-1]
        splitStep = []

        #Putting only the number part of step as step 
        print(stepArray)
        for i in stepArray:
            if i in numbers:
                splitStep.append(i)
            print(splitStep)
            step_noInt = "".join(splitStep)
            print(step_noInt)
        
        step = int(step_noInt)

        def caeser(start_text, shift_amount, cipher_direction):
            encoded_text_with_step = ""
            if cipher_direction == "decode":
                shift_amount *= -1
            for i in start_text:
                if i in alphabet:
                    position = alphabet.index(i)
                    new_pos = position + shift_amount
                    encoded_text_with_step += alphabet[new_pos]
                else:
                    encoded_text_with_step += i
            # we are encoding the shift now!

            array_of_endtext_with_step = encoded_text_with_step.split()
            array_of_endtext_with_step.pop()
            # print(array_of_endtext_with_step)
            endtext_without_step = "".join(array_of_endtext_with_step)
            encoded_shift = ""
            # step = str(step)
            for i in str(step):
                encoded_shift += alphabet[int(i)]
            final_text = f"{endtext_without_step} {encoded_shift}"
            # print(final_text)

        step = step % 26
        caeser(text, step, enterDirection)
        choice = input(
            "\nDo you want to Continue encrypting? Type 'Y' or 'N':\n").lower()
        if choice == "n":
            run = False
    else:
        print("Syntax error, You have to write encode or decode only")
        choice = input("Type y to try again and n to stop:\n").lower()
        if choice == 'n':
            run = False

print("Hope encrypting was fun :)")
