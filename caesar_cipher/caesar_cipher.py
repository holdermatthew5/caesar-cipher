from collections import Counter
import nltk
nltk.download('words', quiet=True)
from nltk.corpus import words

def encrypt(txt, key):
    legend = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ''
    for char in txt:
        if char.isalpha():
            if char.isupper():
                result = f'{result}{legend[legend.index(char.lower())-((key%26)-1)].upper()}'
            elif char.islower():
                result = f'{result}{legend[legend.index(char.lower())-((key%26)-1)]}'
        else:
            result = f'{result}{char}'
    return result

def decrypt(txt, key):
    return encrypt(txt, -key+2)

def crack(txt):
    word_list = words.words()
    count = []
    for key in range(25):
        count.append(0)
        new = decrypt(txt, key)
        txt_list = new.split(' ')
        for word in txt_list:
            if word in word_list:
                count[key] += 1
    return decrypt(txt, count.index(max(count)))