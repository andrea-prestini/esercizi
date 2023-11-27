has_money = True
has_time = True
has_friends = True
has_internet = True


""" Versione errata
def myFunc():
    if has_money:

        if has_time:

            if has_friends:

                if has_internet:

                    return ("Benissimo!")
"""

# Versione corretta


def myFunc():
    if not has_money:
        return f'No money'
    if not has_time:
        return f'No time'
    if not has_friends:
        return f'No friends'
    if not has_internet:
        return f'No internet'
    if True:
        return "Benissimo"


print(myFunc())
