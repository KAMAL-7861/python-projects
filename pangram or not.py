import string

def is_pangram(sentence):
    sentence = sentence.lower()
    return all(char in sentence for char in string.ascii_lowercase)

sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
