alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
print("Welcome to Caeser cipher encryptor or something i forgot. anyways\n")
run = True
while run:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt data:\n").lower()
    text = input("\nEnter the message:\n").lower()
    div = True
    while div:
        mesg_array = text.split(" ")
        index_array = len(mesg_array) - 1
        f_element = mesg_array[index_array]
        step = int(f_element)
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
    if direction == "encode" or direction == "decode":
        caeser(start_text=text, shift_amount=step, cipher_direction=direction)
        choice = input("\nDo you want to Continue encrypting? Type 'Y' or 'N':\n").lower()
        if choice == "n":
            run = False
    else:
        print("Syntax error, You have to write encode or decode only")
        choice = input("Type y to try again and n to stop:\n").lower()
        if choice == 'n':
            run = False

print("Hope encrypting was fun :)")
