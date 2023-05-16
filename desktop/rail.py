def rail_fence_encrypt(message, rails):
    fence = [[] for _ in range(rails)]
    print(fence)
    rail = 0
    direction = 1

    for char in message:
        fence[rail].append(char)
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    encrypted_message = ''
    for rail in fence:
        encrypted_message += ''.join(rail)

    return encrypted_message


def rail_fence_decrypt(encrypted_message, rails):
    rail = 0
    direction = 1
    fence = [[] for i in range(rails)]
    for i in range(len(encrypted_message)):
        fence[rail].append(None)
        rail += direction
        if rail == 0 or rail == rails -1:
            direction *= -1
    index = 0
    rail = 0
    
    for rail in fence:
        for i in range(len(rail)):
            rail[i] = encrypted_message[index]
            index += 1
    decrypted_message = ""

    rail = 0
    direction = 1

    for i in range(len(message)):
        decrypted_message += fence[rail].pop(0)

        rail += direction
        if (rail ==0) or rail == rails-1:
            direction *= -1
    return decrypted_message





# Example usage:
message = "GeeksforGeeks"
rails = 3

encrypted = rail_fence_encrypt(message, rails)
print("Encrypted message:", encrypted)

decrypted = rail_fence_decrypt(encrypted, rails)
print("Decrypted message:", decrypted)
