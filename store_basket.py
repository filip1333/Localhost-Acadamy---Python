# Basket class						
# 	it is to have a list of items, discount % on the basket, discount code
# 	it is to count the price of the whole basket, count the number of items in the whole basket, add and take into account the discount				

# Class of the item						
# 	it is to have Name, category, quantity, price, discount % on the item
class Item:

    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self._count = 0

    def __str__(self):
        return f'Item: {self.name}, category: {self.category}, price: {self.price}'

    def __repr__(self):
        return f"name='{self.name}', category='{self.category}', price='{self.price}'"
    
    def set_discount(self):
        match self.quantity:
            case 0 | 1:
                discount = 0
            case 2:
                discount = 2
            case 3 | 4 | 5:
                discount = 3
            case _:
                discount = 5
        self.discount = discount
        return discount

    def items_dicounts(self):
        discount_items_price = round(
                                    (self.price * self.quantity) 
                                    - (self.quantity
                                    * self.price
                                    * (self.set_discount() / 100)
                                      ),
                                    2)
        items_discount_text = f"With {self.quantity} {self.name}'s you have a {self.set_discount()}% discount on them, their price is {discount_items_price}."
        return items_discount_text

class Basket:

    def __init__(self, items_list):
        self.items_list = items_list
        self._count = 0

    def nested_get(self, nested_key):
        valid_code = {
            'CD29E': {
                'code_number': 0.1, 'code_procentage': 10
                },
            'FT38C': {
                'code_number': 0.05, 'code_procentage': 5
                }
            }
        for k in nested_key:
            valid_code = valid_code.get(k, None)
            if valid_code is None:
                return None
        return valid_code

    @property
    def count_items(self):
        return self._count

    @count_items.setter
    def count_items(self, *item):
        count = sum(item.quantity for item in self.items_list)
        self._count = count

    def add_item(self, new_basket_item):
        self.items_list.append(new_basket_item)
        self.count_items =+ 1

    def remove_item(self, item_in_basket):
        self.items_list.remove(item_in_basket)
        self.count_items =- 1

    def calculate_price(self):
        # total price depending on quantity = price*quantity, discount/100 is percentage discount on price and difference in the mathematical operation deducts the total price with all discounts 
        self.total_basket = round(
                                sum(
                                    (item.price * item.quantity)
                                    - (item.quantity
                                       * item.price
                                       * (item.set_discount() / 100)
                                      ) for item in self.items_list
                                    ),
                                2)
        return self.total_basket

    def items_in_basket_discounts(self):
        discounts_all_items = []
        for item in self.items_list:
            discounts_all_items.append(item.items_dicounts())
        total_basket_text = f'Total basket price: {self.calculate_price()}.'
        discounts_all_items.append(total_basket_text)
        price_with_item_discounts = ' '.join(discounts_all_items)
        return price_with_item_discounts

    def display_basket(self, code=None):
        str_basket = 'Your basket is: '
        for item in self.items_list:
            str_basket+= f'<{item}>,'
        all_basket_txt = f'{str_basket} your total price is {self.calculate_price()}'
        match code:
            case None:
                return f'{all_basket_txt}'
            case 'CD29E' | 'FT38C':
                code_discount_on_basket = round(self.calculate_price() - (self.calculate_price() * self.nested_get([code, 'code_number'])),  2)
                code_txt = f'your discount with code {code} is {self.nested_get([code, "code_procentage"])}%, price with this: {code_discount_on_basket}'
                return f'{all_basket_txt}, but {code_txt}'
            case code if code != ['CD29E', 'FT38C']:
                code_txt = f'your code {code} is invalid, no discount from it'
                return f'{all_basket_txt} and {code_txt}'

        # if code == None:
        #     return f'{all_basket_txt}'
        # elif code == 'CD29E' or code == 'FT38C':
        #     code_discount_on_basket = round(self.calculate_price() - (self.calculate_price() * self.nested_get([code, 'code_number'])),  2)
        #     code_txt = f'your discount with code {code} is {self.nested_get([code, "code_procentage"])}%, price with this: {code_discount_on_basket}'
        #     return f'{all_basket_txt}, but {code_txt}'
        # elif code != ['CD29E', 'FT38C']:
        #     code_txt = f'your code {code} is invalid, no discount from it'
        #     return f'{all_basket_txt} and {code_txt}'

first = Item(name='Banana', category='fruit', quantity=3, price=2.0)
second = Item(name='Vanilla donut', category='candy', quantity=11, price=2.5)
third = Item(name='Chocholate muffin', category='candy', quantity=2, price=2.5)
bas = Basket([first, second, third])
bas.count_items = first, second, third
print(bas.count_items)
print(bas.calculate_price())
bas.add_item(Item(name='Persil', category='Household chemistry', quantity=3, price=5.0))
print(bas.count_items)
print(bas.calculate_price())
bas.remove_item(first)
print(bas.count_items)
print(bas.calculate_price())
bas.remove_item(second)
print(bas.count_items)
print(bas.calculate_price())
# print(second.set_discount())
# print(bas.display_basket('FT38C'))
# print(bas.display_basket('CD29E'))
# print(first.items_dicounts())
# print(bas.items_in_basket_discounts())
# print(bas.display_basket('h'))
# print(bas.display_basket('UUU'))
# print(bas.display_basket('987654321'))
# print(bas.display_basket())

