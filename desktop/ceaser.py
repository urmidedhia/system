def encryption(key, plaintext):
    ciphertext = ''

    for i in plaintext:
        if i.isalpha():
            intermediate = (ord(i) - 65) + key
            intermediate = intermediate % 26
            intermediate += 65
            ciphertext += chr(intermediate)
        elif i.isdigit():
            intermediate = (ord(i) - 48) + key
            intermediate = intermediate % 9
            ciphertext += str(intermediate)
    
    return ciphertext

def decryption(key, ciphertext):
    plaintext = ''

    for i in ciphertext:
        if ord(i) > 64 and ord(i) < 91:
            intermediate = (ord(i) - 65) - key
            intermediate = intermediate % 26
            intermediate += 65
            plaintext += chr(intermediate)
        elif ord(i) > 47 and ord(i) < 58:
            intermediate = (ord(i) - 48) - key
            intermediate = intermediate % 9
            plaintext += str(intermediate)
    
    return plaintext

pt = input('Enter Plain Text: ')
k = int(input('Enter Key: '))

ct = encryption(k, pt)
pt = decryption(k, ct)

print('Cipher Text:', ct)
print('Plain Text:', pt)