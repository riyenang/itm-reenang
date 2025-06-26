def shift_letter(letter, shift):
    if letter == " ":
        return " "
    shifted_guide = ((ord(letter) - ord('A')) + shift) % 26
    return chr(shifted_guide + ord('A'))

def caesar_cipher(message, shift):
    result = ""
    for char in message:
        if char == " ":
            result += " " #to leave space be
        else:
            letter_guide = ord(char) - ord('A')
            shifted_guide = (letter_guide + shift) % 26
            result += chr(shifted_guide + ord('A'))
    return result

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " " #to leave space be
    letter_guide = ord(letter) - ord('A')
    shift_guide = ord(letter_shift) - ord('A') #let to num
    shifted_guide = (letter_guide + shift_guide) % 26
    return chr(shifted_guide + ord('A'))

def vigenere_cipher(text, keyword):
    encrypt = ""
    position = 0 

    for char in text:
        if char == " ":
            encrypt += " " #leave space be
        else:
            letter_guide = ord(char) - ord("A") #let to num
            key_guide = ord(keyword[position % len(keyword)]) - ord("A")
            shifted = (letter_guide + key_guide) % 26
            encrypt += chr(shifted + ord("A")) #back to let
        position += 1

    return encrypt

def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += "_" #for underscore if needed
    encoded = ""
    rows = len(message) // shift #row count
    for position in range(len(message)):
        guide = (position // shift) + rows * (position % shift)
        encoded += message[guide] #column fix
    return encoded

def scytale_decipher(message, shift):
    col_num = len(message) // shift
    decoded = [""] * len(message) #blank msg

    for position in range(len(message)):
        decoded_pos = (position // shift) + col_num * (position % shift)
        decoded[decoded_pos] = message[position] #returning encrypted

    return "".join(decoded)
