from Plotto_plotter.plotter.core import *
from random import shuffle, randint

storyline = Storyline(soup, {}, "my_story")
for letter in ["A", "B", "C"]:
    storyline.get_clause(letter)
    
try:
    for i in range(5):
        storyline.expand_story()
except NameError:
    storyline.print_story()
else:
    storyline.print_story()

k = 2
print("OLD STORY: ")
story = storyline.story_plain_text
print("\n".join(story))

start = randint(0, len(story) - k)
end = start + k

last_5 = story[start:end]
shuffle(last_5)
new_story = story[0:start] + last_5 + story[end:]
print("NEW STORY: ")
print("\n".join(new_story))
