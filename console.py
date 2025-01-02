class Test:
    """Class to demonstrate a console-based project."""

    def __init__(self):
        """Initialize with a list of data."""
        self.data = []

    def create(self, item):
        """Add a new item to the list."""
        self.data.append(item)

    def show(self, index):
        """
        Display a specific item in the list by its index.

        Parameters:
        - index: The position of the item in the list.

        Returns:
        - The item at the specified index.
        """
        try:
            return self.data[index]
        except IndexError:
            return f"Index {index} is out of range."

    def destroy(self, index):
        """
        Remove an item from the list by its index.

        Parameters:
        - index: The position of the item to remove.

        Returns:
        - A success message or an error if the index is invalid.
        """
        try:
            self.data.pop(index)
            return f"Item at index {index} removed."
        except IndexError:
            return f"Index {index} is out of range."

    def all(self):
        """
        Return a list of all items.

        Returns:
        - A formatted string of all items.
        """
        if not self.data:
            return "No items in the list."
        return '\n'.join([f"{i}: {item}" for i, item in enumerate(self.data)])

    def update(self, index, new_item):
        """
        Update an item at a specific index.

        Parameters:
        - index: The position of the item to update.
        - new_item: The new value to assign.

        Returns:
        - A success message or an error if the index is invalid.
        """
        try:
            self.data[index] = new_item
            return f"Item at index {index} updated to '{new_item}'."
        except IndexError:
            return f"Index {index} is out of range."
