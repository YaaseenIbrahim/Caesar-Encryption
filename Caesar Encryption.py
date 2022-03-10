alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
print("Welcome to Caeser cipher encryptor\n")
run = True
while run:
    enterDirection = input("Type 'encode' to encrypt and 'decode' to decrypt data:\n").lower()
    text = input("\nEnter the message:\n").lower()
    div = True
    while div:
        msgArray = text.split(" ")
        indexOf_Array = len(msgArray) - 1
        finalElement = msgArray[indexOf_Array]
        step = int(finalElement)
        if step % 26 == 0:
            print("Step/key number invalid, kindly enter another key\n")
        else:
            div = False

    def caeser(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for i in start_text:
            if i in alphabet:
                position = alphabet.index(i)
                new_pos = position + shift_amount
                end_text += alphabet[new_pos]
            else:
                end_text += i
        print(f"Your {cipher_direction}d data = {end_text}")
    step = step % 26
    if enterDirection == "encode" or enterDirection == "decode":
        caeser(text, step, enterDirection)
        choice = input("\nDo you want to Continue encrypting? Type 'Y' or 'N':\n").lower()
        if choice == "n":
            run = False
    else:
        print("Syntax error, You have to write encode or decode only")
        choice = input("Type y to try again and n to stop:\n").lower()
        if choice == 'n':
            run = False

print("Hope encrypting was fun :)")
