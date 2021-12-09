database = [

    {
        "name": "Spider-Man",
        "red": True, "big": False,
        "mask": True, "good": True,
        "weapon": False, "kill": False
    },

    {
        "name": "Hulk",
        "red": False, "big": True,
        "mask": False, "good": True,
        "weapon": False, "kill": False
    },

    {
        "name": "Thanos",
        "red": False, "big": False,
        "mask": False, "good": False,
        "weapon": True, "kill": True
    },

    {
        "name": "Galactus",
        "red": True, "big": True,
        "mask": True, "good": False,
        "weapon": False, "kill": False
    },

    {
        "name": "Thor",
        "red": False, "big": False,
        "mask": False, "good": True,
        "weapon": True, "kill": True
    },

    {
        "name": "Deadpool",
        "red": True, "big": False,
        "mask": True, "good": False,
        "weapon": True, "kill": True
    }

]


def take_chance(answer, property):
    if answer == "y":
        answer = True
    else:
        answer = False

    to_remove=[]


    for d in database:
        if d[property] != answer:
            to_remove.append(d)
            # print(d)

    for i in to_remove:
        database.remove(i)
        # print(len(database))
        # print("characters left: ", database)

    if len(database) == 1:
        print("I know it! It's " + database[0]["name"] + "! :)")
        print("That was fun!")
        quit()
    if len(database) == 0:
        print("I'm not sure who that is, please try again. :(")
        quit()


print("Hello, and welcome to the Marvel Quiz!")

ans = input("Does your character have a weapon? [Y/N]")
take_chance(ans, "weapon")

ans = input("Is your character red? [Y/N]")
take_chance(ans, "red")

ans = input("Is your character big? [Y/N]")
take_chance(ans, "big")

ans = input("Does your character wear a mask? [Y/N]")
take_chance(ans, "mask")

ans = input("Does your character have a high kill count? [Y/N]")
take_chance(ans, "kill")

ans = input("Is your character a good guy? [Y/N]")
take_chance(ans, "good")
