import sys
from anagram import detect_anagrams

# generate all possible anagrams of correct length
def possible_anagrams(word, lines):
    word.trimspaces() #eh
    for word in lines:
        
        
    
# program start

if len(sys.argv) < 2:
    print('error in input')
    exit(1)

with open('dictionary.txt') as f:
    lines = f.read().splitlines()
for line in lines:
    print('line of lines: ' + line)

print('starting logic')

print(detect_anagrams(sys.argv[1], lines))

print('end of program')
