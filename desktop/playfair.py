# EXP 2: PLAYFAIR CIPHER

from itertools import zip_longest
from functools import reduce

n = 0

def chunk_string(string, chunk_size):
    for i in range(0, len(string), chunk_size):
      print(string[i:i+chunk_size])
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

def generate_key(key):
    key = key.upper()
    key = "".join(sorted(set(key), key=key.index))
    key += "".join(chr(i) for i in range(65, 91) if chr(i) not in key)
    key += "".join(chr(i) for i in range(48, 58))
    p = chunk_string(key, 6)
    # print("Key: ", chunk_string(key, 6))
    return key

def split_pairs(message):
    message = message.upper().replace(" ", "")
    message = [c1+c2 if c2  else c1+"XX" for c1, c2 in zip_longest(message[::2], message[1::2])]
    return message

def get_indices(char, key):
    index = key.index(char)
    row, col = index // 6, index % 6
    return row, col

def encrypt(message, key):
    
    key = generate_key(key)
    message = split_pairs(message)

    def encrypt_digraph(digraph):
        (r1, c1), (r2, c2) = get_indices(digraph[0], key), get_indices(digraph[1], key)
        if r1 == r2:
            return key[r1*6 + (c1+1)%6] + key[r2*6 + (c2+1)%6]
        elif c1 == c2:
            return key[((r1+1)%6)*6 + c1] + key[((r2+1)%6)*6 + c2]
        else:
            return key[r1*6 + c2] + key[r2*6 + c1]

    ciphertext = reduce(lambda x, y: x + y, [encrypt_digraph(d) for d in message])
    print('Encrypted Ciphertext: ', ciphertext)
    return ciphertext

def decrypt(ciphertext, key):
    key = generate_key(key)

    def decrypt_digraph(digraph):
        (r1, c1), (r2, c2) = get_indices(digraph[0], key), get_indices(digraph[1], key)
        if r1 == r2:
            return key[r1*6 + (c1-1)%6] + key[r2*6 + (c2-1)%6]
        elif c1 == c2:
            return key[((r1-1)%6)*6 + c1] + key[((r2-1)%6)*6 + c2]
        else:
            return key[r1*6 + c2] + key[r2*6 + c1]

    plaintext = reduce(lambda x, y: x + y, [decrypt_digraph(d) for d in split_pairs(ciphertext)])
    return plaintext.lower().replace("x", "")

# plain_text = "jazz"
# key = "monarchy"
plain_text = input("Enter plain text: ")
n = plain_text.index(' ')
key = input("Enter key: ")
print('<-----ENCRYPTION----->')
ct = encrypt(plain_text, key)
print('<-----DECRYPTION----->')
dt = decrypt(ct, key)
output = dt[:n] + ' ' + dt[n:]
print("Decrypted Plain Text: ", output)

# enter 2 words w space uske liye bhi chalega and they will like, for eg: hello world