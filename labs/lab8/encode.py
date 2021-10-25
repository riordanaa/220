def encode(message,key):
    m = ""
    for c in message:
        i = ord(c)
        z= i+key
        m = m+chr(z)
    return m