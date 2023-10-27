#Decoder code

def decode(user_password):
    decoded_password = ""
    for digit in user_password:
        the_password = str((int(digit)-3)%10)
        decoded_password += user_password
    return decoded_password

