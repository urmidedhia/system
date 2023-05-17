import multiprocessing
import time

para = "In ECB mode, the plaintext is divided into blocks of fixed length, typically 64 or 128 bits, and each block is encrypted independently using the same key. The encryption of each block is performed in isolation, so the encryption of one block does not affect the encryption of the next block. The resulting ciphertext blocks are then concatenated to produce the encrypted message."

def decToBin(dec):
    return bin(dec).replace("0b", "")

ascii_vals = [ord(char) for char in para]
binary_vals = [decToBin(num) for num in ascii_vals]
combined = ""
for el in binary_vals:
    combined += el

blocks = []
start = 0
end = len(combined)
for i in range(start, end, 128):
    x = i
    blocks.append(combined[x:x + 128])
    if len(blocks[len(blocks) - 1]) < 128:
        shortBlock = blocks[len(blocks) - 1]
        while len(shortBlock) != 128:
            shortBlock += '0'
        blocks[len(blocks) - 1] = shortBlock

def shiftLeft(arr, t):
    lFirst = arr[0:t]
    lSec = arr[t:]
    return lSec + lFirst

class Process(multiprocessing.Process):
 
    def __init__(self, arr, t):
        super(Process, self).__init__()
        self.arr = arr
        self.t = t

                 
    def run(self):
        lFirst = self.arr[0:self.t]
        lSec = self.arr[self.t:]
        binString = (lSec + lFirst)
        binString += '00000'
        n = 7
        chunks = [binString[i:i+n] for i in range(0, len(binString), n)]
        for chunk in chunks:
            ascii_int = int(chunk, 2)
            print(chr(ascii_int), end="")
           
for elem in blocks:
    p = Process(elem, 3)
    p.start()
    p.join()

# option
def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

def ecb_encrypt(plaintext, key, t, mode):
    binary_plaintext = text_to_binary(plaintext)

    padding_length = 128 - len(binary_plaintext) % 128
    binary_plaintext += '0' * padding_length

    blocks = [binary_plaintext[i:i+128] for i in range(0, len(binary_plaintext), 128)]

    ciphertext_blocks = []
    for block in blocks:
        if mode == 'left':
            block = block[t:] + block[:t] 
        elif mode == 'right':
            block = block[-t:] + block[:-t]

        

        ciphertext_blocks.append(block)

    ciphertext_binary = ''.join(ciphertext_blocks)
    ciphertext = binary_to_text(ciphertext_binary)

    return ciphertext

plaintext = "This is a sample plaintext to be encrypted using ECB mode."
key = "secretkey"
t = 3
mode = 'left'

ciphertext = ecb_encrypt(plaintext, key, t, mode)

print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)

def ecb_decrypt(ciphertext, key, t, mode):
    binary_ciphertext = text_to_binary(ciphertext)

    blocks = [binary_ciphertext[i:i+128] for i in range(0, len(binary_ciphertext), 128)]

    plaintext_blocks = []
    for block in blocks:
        decrypted_block = block
        if mode == 'left':
            decrypted_block = decrypted_block[-t:] + decrypted_block[:-t]  
        elif mode == 'right':
            decrypted_block = decrypted_block[t:] + decrypted_block[:t]  

        plaintext_blocks.append(decrypted_block)

    plaintext_binary = ''.join(plaintext_blocks)
    plaintext = binary_to_text(plaintext_binary)

    return plaintext

decrypted_text = ecb_decrypt(ciphertext, key, t, mode)

print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)