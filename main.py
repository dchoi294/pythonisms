import time

class MyCustomCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)


# Usage examples
my_collection = MyCustomCollection()
my_collection.add_item(1)
my_collection.add_item(2)
my_collection.add_item(3)

# Use in for loop
for item in my_collection:
    print(item)

# Use in list comprehension
squared_items = [item**2 for item in my_collection]

# Convert to list
list_items = list(my_collection)


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by function {func.__name__}: {end_time - start_time}")
        return result
    return wrapper

@calculate_time
def my_function():
    # code to be timed
    time.sleep(1)

# Usage examples
my_function()


class MyCustomDataStructure:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        if isinstance(other, MyCustomDataStructure):
            return self.data == other.data
        return False

    def __bool__(self):
        return bool(self.data)

# Usage examples
my_data_structure_1 = MyCustomDataStructure([1, 2, 3])
my_data_structure_2 = MyCustomDataStructure([1, 2, 3])
my_data_structure_3 = MyCustomDataStructure([])

# Using __eq__ to compare two instances
print(my_data_structure_1 == my_data_structure_2)  # True
print(my_data_structure_1 == my_data_structure_3)  # False

# Using __bool__ to determine truthiness
if my_data_structure_1:
    print("my_data_structure_1 is truthy")
else:
    print("my_data_structure_1 is falsy")
if my_data_structure_3:
    print("my_data_structure_3 is truthy")
else:
    print("my_data_structure_3 is falsy")
