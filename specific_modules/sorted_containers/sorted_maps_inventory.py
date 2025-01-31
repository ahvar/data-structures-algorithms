from sortedcontainers import SortedDict


class Product:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def __eq__(self, other):
        return self._id == other.id

    def __lt__(self, other):
        return self._id < other.id

    def __gt__(self, other):
        return self._id > other.id

    def __hash__(self):
        return hash((self._id, self._name))

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name


# TODO: Define a Product class with attributes id (integer) and name (string).
# Ensure this class supports comparison based on the id only for sorting.

# TODO: Create an instance of SortedDict named inventory
inventory = SortedDict([])
ball = Product(3, "ball")
sock = Product(5, "sock")
phone = Product(7, "phone")
piano = Product(4, "piano")
tv = Product(1, "television")
oatmeal = Product(6, "oatmeal")

inventory[ball] = 4
inventory[sock] = 56
inventory[phone] = 32
inventory[piano] = 33
inventory[tv] = 2
inventory[oatmeal] = 44
# TODO: Add some Product objects to inventory with different ids and names, associating each Product with an integer stock quantity.

# TODO: Use the bisect_left method to find the index of the first Product object with an id not less than a specified value.
value = 3
index = None
for item in inventory:
    if item.id >= value:
        index = inventory.bisect_left(item)
if index:
    product, qty = inventory.peekitem(index)
    print("ID: {}, Name: {}".format(product.id, product.name))
else:
    print("not found")

# TODO: Use the peekitem method to display the Product and its stock quantity at the found index.
