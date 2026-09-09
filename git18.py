# Python-project-18

sentence = input("Enter a sentence: ")

words = sentence.split()               # break sentence into list of words
reversed_words = [word[::-1] for word in words]   # reverse each word
result = " ".join(reversed_words)      # join them back into a sentence

print("Reversed words:", result)