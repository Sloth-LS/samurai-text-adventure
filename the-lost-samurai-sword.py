# THE SAMURAI WHO LOST HIS SWORD
# A simple text adventure. Run with: py game.py

# ---------------------------------------------------------------
# 1. THE WORLD
# ---------------------------------------------------------------
rooms = {
    "house": {
        "name": "Your House",
        "description": "Your tiny house. It smells like old rice and broken dreams.\n"
                       "Your cat Mochi is sleeping on a pillow. She looks very wise.",
        "exits": {"north": "village"},
        "items": ["rice ball"],
        "person": "mochi",
    },
    "village": {
        "name": "The Village",
        "description": "The village square. An old lady points at you and laughs.\n"
                       "'Look! The samurai without a sword! HAHAHA!'",
        "exits": {"south": "house", "north": "temple", "west": "tea house", "east": "forest"},
        "items": [],
        "person": "old lady",
    },
    "tea house": {
        "name": "The Tea House",
        "description": "A cozy tea house. A ninja in black clothes is sitting in the corner.\n"
                       "He is very bad at hiding. He is also very drunk.",
        "exits": {"east": "village"},
        "items": [],
        "person": "ninja",
    },
    "temple": {
        "name": "The Temple",
        "description": "A quiet temple. A monk is meditating. His stomach is growling loudly.\n"
                       "There is a locked door in the back.",
        "exits": {"south": "village"},
        "items": [],
        "person": "monk",
    },
    "forest": {
        "name": "The Bamboo Forest",
        "description": "Tall green bamboo everywhere. A big panda is sitting on a rock...\n"
                       "...and it is using YOUR SWORD as a toothpick!",
        "exits": {"west": "village", "south": "bridge"},
        "items": [],
        "person": "panda",
    },
    "bridge": {
        "name": "The Bridge",
        "description": "Your rival Kenji the Slightly Better is waiting for you.",
        "exits": {},
        "items": [],
        "person": None,
    },
}

# ---------------------------------------------------------------
# 2. THE PLAYER
# ---------------------------------------------------------------
current_room = "house"
inventory = []
mochi_talks = 0
door_open = False
game_over = False


def show_room():
    room = rooms[current_room]
    print("\n=== " + room["name"] + " ===")
    print(room["description"])
    if room["items"]:
        print("You see: " + ", ".join(room["items"]))
    print("Exits: " + ", ".join(room["exits"]))


def talk():
    global mochi_talks, game_over
    person = rooms[current_room]["person"]
    if person == "mochi":
        mochi_talks += 1
        if mochi_talks == 1:
            print("Mochi opens one eye. 'Meow.'")
        elif mochi_talks == 2:
            print("Mochi sighs. 'Meow... you are so stupid, Takeshi.'")
            print("Wait. Did the cat just TALK?")
        else:
            print("Mochi stands up on two legs and pulls out a tiny katana.")
            print("'I am the real samurai of this house. You are just my pet human.'")
            print("'I will fight Kenji myself. Go and make me some fish.'")
            print("\n*** SECRET ENDING: THE CAT WAS THE SAMURAI ALL ALONG ***")
            game_over = True

    elif person == "old lady":
        print("'A samurai without a sword is just a man in a dress! HAHAHA!'")

    elif person == "ninja":
        print("The ninja hiccups. 'Psst... I saw everything... *hic*'")
        print("'A PANDA took your sword. In the forest. It was... *hic*... majestic.'")

    elif person == "monk":
        print("The monk speaks in a haiku:")
        print("   'Hungry is my soul")
        print("    Rice would make me very glad")
        print("    Key for the rice, yes'")

    elif person == "panda":
        if "sword" in inventory:
            print("The panda looks sad. It misses the toothpick.")
        else:
            print("The panda looks at you. It keeps picking its teeth with your sword.")
            print("It will not give it back. Maybe it wants something better to chew on?")

    else:
        print("There is nobody here. You talk to yourself. It is the best talk you've had all day.")


def take(item):
    room = rooms[current_room]
    if item in room["items"]:
        room["items"].remove(item)
        inventory.append(item)
        print("You take the " + item + ".")
    else:
        print("There is no " + item + " here.")


def give(item):
    person = rooms[current_room]["person"]
    if item not in inventory:
        print("You don't have a " + item + ".")
    elif item == "rice ball" and person == "monk":
        inventory.remove("rice ball")
        inventory.append("key")
        print("The monk eats the rice ball in one bite. He smiles.")
        print("He gives you a temple key. 'For the door,' he says. Not a haiku. He is too happy.")
    elif item == "bamboo" and person == "panda":
        inventory.remove("bamboo")
        inventory.append("sword")
        print("The panda drops your sword and starts eating the bamboo. Om nom nom.")
        print("You pick up your sword. It is very sticky. And covered in panda spit. Gross.")
    elif person == "mochi":
        print("Mochi looks at the " + item + ". Mochi is not impressed.")
    else:
        print("Nobody here wants that.")


def use(item):
    global door_open
    if item not in inventory:
        print("You don't have a " + item + ".")
    elif item == "key" and current_room == "temple" and not door_open:
        door_open = True
        rooms["temple"]["items"].append("bamboo")
        print("You unlock the door. Inside is a room full of... bamboo. Fancy temple bamboo.")
    elif item == "sword":
        print("You swing your sword. HAIIII-YAA! Some panda spit flies off.")
    else:
        print("Nothing happens.")


def go(direction):
    global current_room, game_over
    room = rooms[current_room]
    if direction not in room["exits"]:
        print("You can't go that way. You walk into a wall. Very samurai.")
        return

    current_room = room["exits"][direction]
    show_room()

    # The final duel happens as soon as you walk onto the bridge
    if current_room == "bridge":
        if "sword" in inventory:
            print("\nYou pull out your sword. It drips with panda spit.")
            print("Kenji looks at it. He looks at you. He throws up a little.")
            print("'I... I give up. That is disgusting.'")
            print("\n*** YOU WIN! You are the greatest samurai in Japan! (kind of) ***")
        else:
            print("\nYou have no sword! You pull out... nothing. You try karate.")
            print("Kenji pokes you once. You fall into the river.")
            print("The village makes a song about you. It is very popular.")
            print("\n*** GAME OVER ***")
        game_over = True


def show_help():
    print("\n------------- HOW TO PLAY -------------")
    print("Type a command and press Enter.")
    print("")
    print("MOVING AROUND")
    print("  go north      (or just: north / n)")
    print("  go south      (or just: south / s)")
    print("  go east       (or just: east / e)")
    print("  go west       (or just: west / w)")
    print("")
    print("DOING THINGS")
    print("  look              look around the room again")
    print("  take <item>       pick something up   (example: take rice ball)")
    print("  give <item>       give something away (example: give rice ball)")
    print("  use <item>        use something       (example: use key)")
    print("  talk              talk to the person in the room")
    print("  inventory / i     see what you are carrying")
    print("")
    print("OTHER")
    print("  help              show this list again")
    print("  quit              give up (coward)")
    print("")
    print("TIPS")
    print("  - Talk to everyone. People give clues!")
    print("  - People might want something from you.")
    print("  - Don't go to the bridge without your sword...")
    print("  - There are secret commands. Try being a samurai!")
    print("---------------------------------------")


# ---------------------------------------------------------------
# 3. THE GAME LOOP
# ---------------------------------------------------------------
print("========================================")
print("   THE SAMURAI WHO LOST HIS SWORD")
print("========================================")
print("You are Takeshi, the most feared samurai in Japan (says you).")
print("Tomorrow you fight your rival Kenji the Slightly Better.")
print("There is just one problem... you lost your sword. Again.")
print("")
print("YOUR GOAL: Find your sword and win the duel at the bridge!")
show_help()
input("\nPress Enter to start your adventure...")
show_room()

while not game_over:
    words = input("\n> ").lower().split()
    if not words:
        continue

    command = words[0]
    thing = " ".join(words[1:])  # "rice ball" is two words

    if command == "go":
        go(thing)
    elif command in ("north", "south", "east", "west"):
        go(command)
    elif command in ("n", "s", "e", "w"):
        shortcuts = {"n": "north", "s": "south", "e": "east", "w": "west"}
        go(shortcuts[command])
    elif command == "look":
        show_room()
    elif command == "take":
        take(thing)
    elif command == "give":
        give(thing)
    elif command == "use":
        use(thing)
    elif command == "talk":
        talk()
    elif command in ("inventory", "i"):
        print("You have: " + (", ".join(inventory) if inventory else "nothing. Not even a sword."))
    elif command == "help":
        show_help()
    elif command == "bow":
        print("You bow deeply. Your back cracks. The whole village hears it.")
    elif command == "meditate":
        print("You find inner peace. Then you remember you lost your sword.")
    elif command == "scream":
        print("HAIIII-YAAA! A bird falls out of a tree from shock.")
    elif command == "quit":
        print("You run away and become a fisherman. Nobody is surprised.")
        break
    else:
        print("You don't know how to do that. A real samurai would know.")

input("\nPress Enter to close...")