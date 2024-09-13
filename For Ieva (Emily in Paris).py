#Ieva emily in paris episode
import random
f = open("Emily_in_Paris_Season_5_Custom_Episode.txt",'r')
a = f.read()
print(a)
#Characters and their dialogues
characters = {
   "Emily": [
       "I think we can approach this from a different angle.",
       "Rome is so different, but I love the energy!",
       "This new Italian campaign has to be perfect!",
       "I’m starting to feel like I belong in Italy now."
   ],
   "Sylvie": [
       "Emily, you should've stayed in Paris.",
       "I knew you'd eventually fall in love with another city.",
       "I don't miss you causing chaos in the office.",
       "Enjoy your new adventure in Rome, Emily."
   ],
   "Mindy": [
       "Eurovision was incredible! I can't believe I won!",
       "I missed performing with my ex in the band.",
       "Looks like I'm back where I belong—with my music and my love.",
       "Emily, you should've seen the performance!"
   ],
   "Camille": [
       "I’m happier now than I ever was.",
       "Our family is everything I dreamed of.",
       "I'm focusing on my new life and child.",
       "Love is what matters most."
   ]
}
#Scene settings
settings = [
   "Emily's Apartment",
   "A Rome Piazza",
   "A Parisian Café",
   "Mindy's Eurovision Stage",
   "Camille's New Home",
   "The Seine Riverbank",
   "A snowy village in Antarctica"
]
#Generate a random scene
def generate_scene():
   setting = random.choice(settings)
   character1 = random.choice(list(characters.keys()))
   character2 = random.choice(list(characters.keys()))
   #Ensure two different characters are talking
   while character1 == character2:
       character2 = random.choice(list(characters.keys()))
   dialogue1 = random.choice(characters[character1])
   dialogue2 = random.choice(characters[character2])
   return setting, character1, dialogue1, character2, dialogue2
#Function to generate a script
def generate_script(filename, num_scenes=10):
   with open(filename, 'w') as file:
       file.write("Emily in Paris - Season 5, Episode 1\n")
       file.write("------------------------------------------------------------\n")
       #Generate random scenes
       for scene_num in range(1, num_scenes + 1):
           setting, character1, dialogue1, character2, dialogue2 = generate_scene()
           #Write the scene
           file.write(f"Scene {scene_num}: {setting}\n")
           file.write("------------------------------------------------------------\n")
           file.write(f"{character1.upper()}\n")
           file.write(f"{dialogue1}\n\n")
           file.write(f"{character2.upper()}\n")
           file.write(f"{dialogue2}\n\n")
       #Write epilogue scenes (your custom plot)
       file.write("------------------------------------------------------------\n")
       file.write("Epilogue Scenes\n")
       file.write("------------------------------------------------------------\n")
       #Illegitimate daughter plotline
       file.write("Scene: A snowy village in Antarctica\n")
       file.write("------------------------------------------------------------\n")
       file.write("ILLEGITIMATE DAUGHTER\n")
       file.write("I moved to Antarctica from New York, and now I have cold feet for the rest of my life.\n\n")
       #Camille's happy ending
       file.write("Scene: Camille's New Home\n")
       file.write("------------------------------------------------------------\n")
       file.write("CAMILLE\n")
       file.write("I'm living happily with my girlfriend and our adopted child. This is the life I've always wanted.\n\n")
       #Emily's new life in Rome
       file.write("Scene: A Rome Piazza\n")
       file.write("------------------------------------------------------------\n")
       file.write("EMILY\n")
       file.write("I moved to Rome for the new Italian guy. Paris feels like a lifetime ago, and I don't even think about that dumb chef anymore.\n\n")
       #Mindy's Eurovision success
       file.write("Scene: Mindy's Eurovision Stage\n")
       file.write("------------------------------------------------------------\n")
       file.write("MINDY\n")
       file.write("I went to Eurovision and won! Now I'm back with my ex-boyfriend, and we’re performing together in the band again.\n\n")
       file.write("------------------------------------------------------------\n")
       file.write("End of Episode\n")
#Call the function to create the script
generate_script("Emily_in_Paris_Season_5_Custom_Episode.txt", num_scenes=10)
print("Script with custom epilogue generated!")
