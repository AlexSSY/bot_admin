storage = {}


def store(user_id, key, value):
    user_storage = storage.get(user_id, {})
    user_storage[key] = value


def retrieve(user_id, key, default=None):
    return storage.get(user_id, {}).get(key, default)


def delete(user_id, key=None):
    if key is None:
        storage.pop(user_id, None)
    else:
        storage.get(user_id, {}).pop(key, None)


class Stack:
    def __init__(self):
        """Initializes an empty list to store stack elements."""
        self.items = []

    def is_empty(self):
        """Checks if the stack is empty."""
        return self.items == []

    def push(self, item):
        """Adds an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item from the top of the stack.
        Raises an IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        """Returns the item at the top of the stack without removing it.
        Raises an IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek into an empty stack.")
        return self.items[-1]

    def size(self):
        """Returns the number of items in the stack."""
        return len(self.items)
    

stacks = {}


def get_user_stack(user_id: int) -> Stack:
    existing_stack = stacks.get(user_id)

    if existing_stack is None:
        new_stack = Stack()
        stacks[user_id] = new_stack
        return new_stack
    
    return existing_stack
