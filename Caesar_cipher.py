alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
proceed = True

def decrypt(encrypted_text,shifted):
    plain_text = ""
    encrypted_text = list(encrypted_text)

    for x in encrypted_text:
        i = alphabet.index(x)
        i = i - shifted
        plain_text = plain_text + alphabet[i]
    print("Your Decrypted text is :{}".format(plain_text))  

def encrypt(plain_text,to_shift):
    plain_text = list(plain_text)
    encrypted_text = ""
    to_shift = to_shift % 25

    for x in plain_text:
        if x in alphabet :
            i = alphabet.index(x)
            i = i + to_shift
            i = i % 26
            encrypted_text = encrypted_text + alphabet[i]
    print("Your Encrypted text is :{}".format(encrypted_text))

while proceed:
    direction = "e"#input("Type 'e' to encrypt, type 'd' to decrypt:\n")
    text = "zulu" #input("Type your message:\n").lower()
    shift = 5 #int(input("Type the shift number:\n"))

    if direction == "e":
        encrypt(plain_text=text , to_shift=shift)
    elif direction == "d":
        decrypt(shifted=shift, encrypted_text=text)
    else:
        print("Double check yr input.")