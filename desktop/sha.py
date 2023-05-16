import hashlib

def calculate_hash(message):
    sha1 = hashlib.sha1()
    sha1.update(message.encode())
    return sha1.hexdigest()

def verify_integrity(message, hash_value):
    calculated_hash = calculate_hash(message)
    if calculated_hash == hash_value:
        print("Integrity verified: Message has not been tampered with.")
    else:
        print("Integrity check failed: Message may have been tampered with.")


message = "Hello, World!"
hash_value = "2fd4e1c67a2d28fced849ee1bb76e7391b93eb12"

calculated_hash = calculate_hash(message)
print("Calculated Hash:", calculated_hash)

verify_integrity(message, hash_value)