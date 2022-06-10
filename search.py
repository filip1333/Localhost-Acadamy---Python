# Create fuction that searches trough list of items
# if given key is in item, it returns item and it's index

# e.g.
# result = find_item(list, 'el')
# print(result) --> ['eleven', 12]
def check_list(list_: list, key: str):
    result = []
    for index, element in enumerate(list_):
        output_list = [element, index]
        if key.lower() in element:
            result.append(output_list)
    if len(result) > 0:
        return result
    else:
        return ['Element not in list', None]


shopping_list = ['apple', 'banana', 'strawberry', 'peach', 'raspberry', 'beer', 'tabacco', 'whiskey', 'pepper']

print(check_list(shopping_list, 'ban'))
print(check_list(shopping_list, 'rr'))
print(check_list(shopping_list, 'per'))
print(check_list(shopping_list, 'PP'))
print(check_list(shopping_list, 'lublin'))
print(check_list(shopping_list, 'Straw'))
print(check_list(shopping_list, 'er'))  
