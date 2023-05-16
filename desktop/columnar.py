# option 1
import math
def encrypt(message, keyword):
    message = message.upper().replace(" ", "")
    keyword = keyword.upper()
    key_table = sorted(keyword)
    copy_key = keyword
    rows =  int(math.ceil(float(len(message)) / len(keyword)))
    cols = len(keyword)

    matrix = []
    for i in range(rows):
        col = [0] * cols
        matrix.append(col)
    
    if (len(message) < rows*cols):
        while len(message) != rows*cols:
            message += "X"
    print("18", message)
    for i in range(len(message)):
        row = i//cols 
        col = i%cols
        matrix[row][col] = message[i]
    ciphertext = ""
    
    for i in range(len(keyword)):
        index = copy_key.index(key_table[i])
        copy_key = copy_key.replace(key_table[i], "8", 1)
        for j in range(rows):
            ciphertext += matrix[j][index]
    return ciphertext

def decrypt(message, keyword):
    message = message.upper().replace(" ", "")
    keyword = keyword.upper()
    key_table = sorted(keyword)
    copy_key = keyword
    rows =  int(math.ceil(float(len(message)) / len(keyword)))
    cols = len(keyword)

    matrix = []
    for i in range(rows):
        col = [0] * cols
        matrix.append(col)
    index = 0
    for i in range(cols):
        cindex = copy_key.index(key_table[i])
        copy_key = copy_key.replace(key_table[i], "9", 1)
        for j in range(rows):
            matrix[j][cindex] = message[index]
            index += 1
    decrypted_message = ""
    for i in range(rows):
        for j in range(cols):
            decrypted_message += matrix[i][j]
    decrypted_message.rstrip("X")
    return decrypted_message
msg = 'we are the best'
print("Message", msg.upper().replace(" ", ""))
keyword = "HEAVEN"
enc = encrypt(msg, keyword)
print("Encrypted Message:", enc)
dec = decrypt(enc, keyword)
print("Decrypted Message:", dec)



# option 2
text = 'helloab'
key = 'hack' # 2 0 1 3
key = [ord(i) for i in key]
sk = sorted(key)
print("key : ",key)
print("sorted key : ",sk)
priority = []
for i in key:
    priority.append(sk.index(i))
print(priority)
priority2 = [i for i in priority]
if len(text) % len(key) != 0:
    text += '#' * (len(key) - (len(text) % len(key)))
res = [text[i:i+len(key)] for i in range(0, len(text), len(key))]
for i in res:
    print(i)
cipher = ''
for _ in range((len(key))):
    i = priority.index(min(priority))
    for j in range(len(res)):
        cipher += res[j][i]
    priority[i] = 10000
print("Cipher : ",cipher)
# deciphering starts
i=0
c=2
j=0
d=[[0 for _ in range(len(res[0]))] for _ in range(0,len(res))]
while i!=len(cipher):
     text=cipher[i:c]
     c+=2
     i+=2
     pos=priority2.index(j)
     print(pos)
     d[0][pos]=text[0]
     d[1][pos]=text[1]
     j+=1
print(d)