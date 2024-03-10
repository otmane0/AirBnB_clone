from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.now()
        # Additional logic to save the object's state (e.g., to a database or file)

# Example usage:
obj = BaseModel()
print(obj.created_at)  # Output: Current datetime
print(obj.updated_at)  # Output: Same as created_at
obj.save()
print(obj.updated_at)

print(obj.updated_at)
print(obj.updated_at)
