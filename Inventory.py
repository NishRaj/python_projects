class Inventory:
    def __init__(self,max_capacity):
        self._max_capacity = max_capacity
        self._items = {}
        self._capacity = 0
    
    def add_item(self,name,price,quantity):
        if self._capacity + quantity > self._max_capacity:
            return False
        if name in self._items:
            return False
        self._items[name] = {'name':name,'price':price,'quantity':quantity}
        self._capacity += quantity
        return True
    def print_items(self):
        for k,v in self._items.items():
            print(f"{k} --> {v}")
    def delete_item(self, name):
        if name in self._items:
            self._capacity -= self._items[name].get('quantity')
            del self._items[name]
            return True
        return False
    def get_most_stocked_item(self):
        if len(self._items) == 0:
            return None  
        qty = 0
        most_stocked_item = None
        for key, value in self._items.items():
            if value.get("quantity") > qty:
                qty = value.get("quantity")
                most_stocked_item = key
        return most_stocked_item
    def get_items_in_price_range(self, min_price, max_price):
        lst_of_items_in_price_range = []
        for k,v in self._items.items():
            if min_price <= v.get("price") <= max_price:
                lst_of_items_in_price_range.append(k)
        return lst_of_items_in_price_range
   
inventory = Inventory(10)
print(inventory.add_item('Chocolate', 4.99, 3))
print(inventory.add_item('Cereal', 6.99, 1))
print(inventory.add_item('Milk', 3.99, 2))
print(inventory.add_item('Butter', 2.99, 1))
print(inventory.add_item('Milk', 3.99, 2))
#inventory.print_items()
#print(inventory.del_item('Chocolate'))
inventory.print_items()
#print(inventory.add_item('Milk', 3.99, 2))
#inventory.print_items()
print(inventory.get_most_stocked_item())
print(inventory.get_items_in_price_range(0,6))