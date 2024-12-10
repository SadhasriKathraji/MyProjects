alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    cipher_text = ""
    for letter in plain_text: #hello                   #h
        if letter in alphabet:
            position = alphabet.index(letter)          #7
            new_position = (position + shift_key)%26   #7+1=8     # %26 prevents the list out of range error in case of large shift keys
            cipher_text+=alphabet[new_position]        #i
        else:
            cipher_text+=letter
    print("Here's the text after encryption:",cipher_text)   #ifmmp

def decryption(c_text,s_key):
    plainText = ""
    for letter in c_text: #ifmmp           #i
        if letter in alphabet:
            pos = alphabet.index(letter)   #8
            new_pos = (pos - s_key)%26          #8-1 = 7
            plainText += alphabet[new_pos] #h
        else:
            plainText += letter
    print("Here's the text after decryption:",plainText)

want_to_end = False
while not want_to_end:
    what_to_do = input("Type 'encrpt' for encryption, type 'decrpt' for decryption:\n")
    text = input(f"Type your message:\n")
    shift = int(input("Type the shift number:\n")) #1
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(c_text=text,s_key=shift)
    play_again = input("want to continue, yes or no:").lower()
    if play_again=="no":
        want_to_end=True
        print("Thankyou...")

