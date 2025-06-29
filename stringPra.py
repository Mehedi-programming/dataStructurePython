import sys

print('word counter=>')
word=input('Enter your word:')
WORD=word.split()
print(len(WORD))

print('character counter=>')
character=input('Enter your character:')
print(len(character))

print('sentence counter=>.')
sentence=input('Enter your paragraph:')
count=0
for i in sentence:
    if i=='.':
        count+=1
print(f'Number of sentence: {count}')

print('Enter your paragraph:')
paragraphs = sys.stdin.read()
print("Number of paragraphs:", len(paragraphs.splitlines()))
