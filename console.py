#!/usr/bin/python3
"""Make console"""

import cmd
from models.base_model import BaseModel
from models import storage
import shlex

class HBNBCommand(cmd.Cmd):
    """Console class for back-end"""
    prompt = "(hbnb) "

    classes_list = ["BaseModel"]
    class_objects = {
        "BaseModel": BaseModel,
    }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Handle empty line"""
        pass

    def check_name(self, line):
        """Check class name"""
        if not line:
            print("** class name missing **")
            return False
        class_name = line.split()[0]
        if class_name not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return False
        return True

    def check_id(self, line):
        """Check instance id"""
        parts = shlex.split(line)
        if len(parts) < 2:
            print("** instance id missing **")
            return False
        class_name = parts[0]
        class_id = parts[1]
        full_instance = f"{class_name}.{class_id}"
        if full_instance not in storage.all():
            print("** no instance found **")
            return False
        return True

    def check_attr_name_val(self, line):
        """Check attribute name and value"""
        parts = shlex.split(line)
        if len(parts) < 3:
            print("** attribute name missing **")
            return False
        if len(parts) < 4:
            print("** value missing **")
            return False
        return True

    def do_create(self, line):
        """Create a new instance"""
        if not self.check_name(line):
            return
        class_name = shlex.split(line)[0]
        new_instance = HBNBCommand.class_objects[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Show the string representation of an instance"""
        if not self.check_name(line):
            return
        if not self.check_id(line):
            return
        class_name, class_id = shlex.split(line)
        instance = storage.all()[f"{class_name}.{class_id}"]
        print(instance)

    def do_destroy(self, line):
        """Destroy an instance"""
        if not self.check_name(line):
            return
        if not self.check_id(line):
            return
        class_name, class_id = shlex.split(line)
        instance = f"{class_name}.{class_id}"
        del storage.all()[instance]
        storage.save()

    def do_all(self, line):
        """Print all string representations of instances"""
        all_instances = storage.all()
        list_string = []
        if line:
            class_name = shlex.split(line)[0]
            if class_name in HBNBCommand.classes_list:
                for key, obj in all_instances.items():
                    if key.startswith(f"{class_name}."):
                        list_string.append(str(obj))
            else:
                print("** class doesn't exist **")
                return
        else:
            for obj in all_instances.values():
                list_string.append(str(obj))
        print(list_string)

    def do_update(self, line):
        """Update an instance"""
        if not self.check_name(line):
            return
        if not self.check_id(line):
            return
        if not self.check_attr_name_val(line):
            return
        parts = shlex.split(line)
        class_name, class_id, attr_name, attr_value = parts
        instance = storage.all()[f"{class_name}.{class_id}"]
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            setattr(instance, attr_name, attr_type(attr_value))
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
