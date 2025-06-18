print("Welcome to Word Frequency Counter")
input = input("Enter a sentence : ")
splitted = input.split()
counts = {word : splitted.count(word) for word in splitted}
print("Words with Frequencies : ",counts)