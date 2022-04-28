import json

class Client:
    firstname = ""
    lastname = ""
    major = ""
    hometown = ""
    username = ""
    password = ""

    def __init__(self, data:list):
        self.lastname, self.firstname, self.major, self.hometown, self.username, self.password = data

    def toJSON(self):
        return json.dumps(self.__dict__)

def rsa_encryption(msg, e, n):
    output = ""
    for c in msg:
        output += chr((ord(c)**e)%n)
    return output

def printMenu():
    print("---------------------")
    print("/ Commands          /")
    print("/                   /")
    print("/ REGISTER          /")
    print("/ LOGIN             /")
    print("/ VIEW_REGISTRATION /")
    print("---------------------")
