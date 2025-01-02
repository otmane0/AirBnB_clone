#!/usr/bin/python3
"""Make consol"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import sys
import shlex


class HBNBCommand(cmd.Cmd):
    """Console class for back-end"""
    prompt = "(hbnb) "

    classes_list = ["BaseModel", "User", "Amenity", "City", "Place", "Review", "State"]
    class_objects = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
    }

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """C-d command to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line handling"""
        pass

    def chick_name(self, line):
        """chick class_name of all obj"""
        if not line:
            print("** class name missing **")
            return False
        atrs = line.split()[0]
        if not atrs in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return False

        return True

    def chick_id(self, line):
        """Chick id of all obj"""
        parts = shlex.split(line)
        if len(parts) < 2:
            print("** instance id missing **")
            return False
        class_name = parts[0]
        class_id = parts[1]
        full_instance = f"{class_name}.{class_id}"
        from models import storage
        if full_instance not in storage.all():
                print("** no instance found **")
                return False
        return True

    def chick_atr_name_val(self, line):
        """Chick specefic atribute name and value"""
        parts = shlex.split(line)
        if len(parts) < 3:
            print("** attribute name missing **")
            return False
        if len(parts) < 4:
            print("** value missing **")
            return False
        return True

    def do_create(self, line):
        """Create command to create a new instance"""
        if not self.chick_name(line):
            return

        ins_name = shlex.split(line)[0]

        new_instance = HBNBCommand.class_objects.get(ins_name)()

        new_instance.save()  # Save to JSON file (new_instance is Basemodel)
        print(new_instance.id)

    def do_show(self, line):
        """Show the string presentation of class"""
        if not self.chick_name(line):
            return
        elif not self.chick_id(line):
            return
        class_name = shlex.split(line)[0]
        class_id = shlex.split(line)[1]
        instance = f"{class_name}.{class_id}"
        from models import storage
        instance = storage.all().get(instance)

        print(instance)

    def do_destroy(self, line):
        """Destroy an Obj, then save the update"""
        if not self.chick_name(line):
            return
        elif not self.chick_id(line):
            return
        class_name = shlex.split(line)[0]
        class_id = shlex.split(line)[1]
        instance = f"{class_name}.{class_id}"
        from models import storage
        # Get the instance from storage
        new_instance = storage.all().get(instance)

        if new_instance:
            # Remove the instance from storage
            del storage.all()[instance]
            storage.save()  # Save the updated storage (JSON file)

    def do_all(self, line):
        """Print all string representations of instances based on the class name or all instances."""
        from models import storage
        all_instances = storage.all()
        list_string = []

        if line:
            class_name = shlex.split(line)[0]
            if class_name not in HBNBCommand.classes_list:
                print("** class doesn't exist **")
                return
            # Filter instances based on class name
            list_string = [str(obj) for key, obj in all_instances.items() if key.startswith(f"{class_name}.")]
        else:
            # Include all instances
            list_string = [str(obj) for obj in all_instances.values()]

        print(list_string)


    def do_update(self, line):
        """Update the instance, and save the changes"""
        from models import storage
        if not self.chick_name(line):
            return
        elif not self.chick_id(line):
            return
        elif not self.chick_atr_name_val(line):
            return

        not_atr = ["id", "created_at", "updated_at"]

        cl_name, cl_id, cl_atr, cl_val = shlex.split(line)

        if cl_atr in not_atr:
            return
        else:
            try:
                my_class = f"{cl_name}.{cl_id}"
                anstence = storage.all().get(my_class)
                if isinstance(getattr(anstence, cl_atr, None), int): # getattr(object, attribute_name, default_value)
                    setattr(anstence, cl_atr, int(cl_val))
                if isinstance(getattr(anstence, cl_atr, None), float):
                    setattr(anstence, cl_atr, float(cl_val))
                if isinstance(getattr(anstence, cl_atr, None), str):
                    setattr(anstence, cl_atr, str(cl_val))
                if isinstance(getattr(anstence, cl_atr, None), bool):
                    setattr(anstence, cl_atr, bool(cl_val))

                storage.save()
            except AttributeError:
                return








# BaseModel


if __name__ == '__main__':
    HBNBCommand().cmdloop()






