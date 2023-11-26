""" Mistake:attenzione al trattamento degli oggetti in Python
item presenta una forte problematica
"""


def add_item(item: str, items: list = None):
    if not items:
        items: list = []

    items.append(item)
    print(f'ID {id(items)}:', items)
    return items


list_a = add_item('a')
list_b = add_item('b')

print(list_a)
print(list_b)
