# this is a small python project where the project opens a file that has a storyline
# it reads through the storyline and replace some keywords based on the user inputs
#  the program can create different stories based on user inputs.
# its just a fun story telling game with basic python functionalities
with open('story.txt', 'r') as f:
   story = f.read()

start_of_word = -1
words = set()

target_start = '<'
target_end = '>'

for i, char in enumerate(story):
   if char == target_start:
      start_of_word = i

   if char == target_end and start_of_word != -1:
      word = story[start_of_word: i +1]
      words.add(word)
      start_of_word = -1

answers = {}
for i in words:
   answer = input(f'Enter the word for {i}: ')
   answers[i] = answer

for word in words:
   story = story.replace(word, answers[word]) 

print(story)