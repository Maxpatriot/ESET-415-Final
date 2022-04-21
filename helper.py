class client:
    firstname = ""
    lastname = ""
    major = ""
    hometown = ""
    username = ""
    password = ""

def rsa_encryption(msg, e, n):
    output = ""
    for c in msg:
        output += (chr(ord(c)**e)%n)
    return output