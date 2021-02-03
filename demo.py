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


print("OLD STORY: ")
story = storyline.story_plain_text
print("\n".join(story))

start = randint(0, len(story) - 2)
end = start + 2

last_5 = story[start:end]
shuffle(last_5)
new_story = story[0:start] + last_5 + story[start + 2:]
print("NEW STORY: ")
print("\n".join(new_story))
