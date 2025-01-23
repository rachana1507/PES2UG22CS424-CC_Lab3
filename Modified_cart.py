import json

import products
from cart import dao
from products import Product
import ast

class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])




def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []
    
    items = []
    for cart_detail in cart_details:
        # Safely parse the contents
        evaluated_contents = ast.literal_eval(cart_detail['contents'])
        items.extend(evaluated_contents)
    
    # Fetch products in one step using list comprehension
    return [products.get_product(i) for i in items]


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)



