#Decoder code

def decoder(password):
    pass_str = str(password)
    pass_list = list(pass_str)
    value= []
    for c in pass_list:
        value.append(int(c) // 3)
        final = ''.join(map(str, value))
    return final

