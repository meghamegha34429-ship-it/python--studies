def get_movies(actor):
    if actor.lower() == "vijay":
        return ["Ghilli", "Thuppakki", "Mersal", "Master", "Leo",
                "Bigil", "Kaththi", "Theri", "Sarkar", "Pokkiri"]
    elif actor.lower() == "ajith":
        return ["Mankatha", "Billa", "Vedalam", "Viswasam", "Veeram",
                "Valimai", "Aarambam", "Citizen", "Dheena", "Yennai Arindhaal"]
    else:
        return None

actor = input("Enter actor name: ")
x = int(input("Enter top number: "))

movies = get_movies(actor)

if movies is None:
    print("Actor not found")
else:
    for i in range(x):
        print(i + 1, ".", movies[i])
