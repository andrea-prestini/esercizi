import random


def rock_paper_scissors():
    print("Let's play Rock Paper Scissors")

    r = "sasso"
    p = "carta"
    s = "forbici"
    all_choises = [r, p, s]

    user = input(f"Enter a choice {r}, {p}, {s}: ")

    if user not in all_choises:
        print("Invalid choice")
        return

    computer = random.choice(all_choises)

    print(f"User chose {user}, Computer chose {computer}")

    # r>s, p>r, s>p

    if user == computer:
        print("Pareggio")
    elif (user == "r" and computer == "s"):
        print("Hai vinto tu...")
    elif (user == p and computer == "r"):
        print("Hai vinto tu...")
    elif (user == "s" and computer == "p"):
        print("Hai vinto tu...")
    else:
        print("Ha vinto il computer, sorry!")
