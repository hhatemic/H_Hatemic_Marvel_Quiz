database = [

    {
        "name": "Spider-Man",
        "red": True, "big": False,
        "mask": True, "good": True
    },

    {
        "name": "Hulk",
        "red": False, "big": True,
        "mask": False, "good": True
    },

    {
        "name": "Thanos",
        "red": False, "big": False,
        "mask": False, "good": False
    },

    {
        "name": "Galactus",
        "red": True, "big": False,
        "mask": True, "good": False
    }

]


def take_chance(answer, property):
    if answer == "y":
        answer = True
    else:
        answer = False

    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)
        print(len(database))

    if len(database) == 1:
        print("I think your character is " + database[0]["name"])
        quit()


ans = input("Is your character red? [Y/N]")
take_chance(ans, "red")

ans = input("Is your character big? [Y/N]")
take_chance(ans, "big")

ans = input("Does your character wear a mask? [Y/N]")
take_chance(ans, "mask")

ans = input("Is your character a good guy? [Y/N]")
take_chance(ans, "good")
