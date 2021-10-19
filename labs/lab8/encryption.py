def encode_better(s, k):
    acc = " "
    for i in range(len(s)):
        c = s[i]
        key = k[i % len(k)]
        key = ord(key) - 97
        y = ord(c) + key
        z = chr(y)
        acc += z
    return acc

def encode(message, key):
    acc = ""
    for i in message:
        x = ord(i)
        y = x + key
        acc+= chr(y)
    return acc