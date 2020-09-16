vowels = ('a','e','i','o','u')
str = input("Enter a string: ")
new_message = ""
for letters in str:
    if letters not in vowels:
        new_message = new_message + letters
print(f"message without vowels {new_message} ")
