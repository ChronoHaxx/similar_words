#importing googletrans translator to translate the word
from googletrans import Translator
#import time for delay to prevent crashing
import time
#importing from difflib to compare between two words the similarity ratio
from difflib import SequenceMatcher

#defining translator as Translator object..
translator = Translator()

#testing
text = input()

translation = translator.translate(text, dest='jw', src='auto')

text = translation.origin
text_translated = translation.text

#print(text) testing
print(text_translated)

#compare two words
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

print(similar(text, text_translated))

#opening the words_list file and extracted into an array of strings, line.rstrip() used to remove newline char in .txt file
words_list = [line.rstrip() for line in open('words_list.txt')]
print(words_list)

similar_words = []

for word in words_list :
    time.sleep(.4)
    translation_en_to_malay = translator.translate(word, dest='ms', src='en')
    text_ms = translation_en_to_malay.text
    print(text_ms)
    time.sleep(.4)
    translation_jawa = translator.translate(text_ms, dest='jw', src='auto')
    text_jawa = translation_jawa.text
    print(text_jawa)
    print(similar(text_ms, text_jawa))
    if similar(text_ms, text_jawa) > 0.5 :
        similar_words += text_ms + ' | ' + text_jawa

print(similar_words)