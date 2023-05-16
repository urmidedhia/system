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
