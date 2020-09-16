dict = {"a":"e","b":"f","c":"g","d":"h","e":"i",
        "1":"6","2":"7","3":"8","4":"9","":""}
encryption
message = input("Enter >> ").lower()
encrypted = ''
for letters in message:
    if letters in dict:
        # replacing the key with values in the message i.e. encryption
        encrypted += dict[letters]
    else:
        encrypted += letters
print(encrypted)
