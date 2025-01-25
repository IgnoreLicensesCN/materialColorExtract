def hashStringLikeJava(s:str):
    hashCode = 0
    for char in s:
        hashCode = (hashCode * 31 + ord(char)) & (2 ** 32 - 1)  # unsigned
    if hashCode & 2 ** 31:
        hashCode -= 2 ** 32  # make it signed
    return hashCode