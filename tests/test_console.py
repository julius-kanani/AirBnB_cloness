#!/usr/bin/python3
"""Unittest module for the console"""
import unittest
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from unittest.mock import patch
import io


class TestCommand(unittest.TestCase):
    """Tests for the console"""

    def setUp(self):
        """Function used to empty file.json"""
        FileStorage._FileStorage__objects = {}
        FileStorage().save()

    def test_right_prompt(self):
        """verify that the prompt is correct"""
        self.assertEqual(HBNBCommand().prompt, '(hbnb) ')

    def test_with_help(self):
        """test the help command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help")
        output = '\nDocumented commands (type help <topic>):\n'
        output += '========================================\n'
        output += 'EOF  all  count  create  destroy  help  quit  show  update'
        output += '\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help create")
        output = 'Create an instance, print its id and save it\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help show")
        output = 'Show string representation of an instance\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        output = 'Destroy an instance with its id\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help all")
        output = 'Print the string representation of all instances\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help update")
        output = 'Adding or updating attribute of an instance\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        output = 'Ctrl + D to exit the program\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        output = 'Quit command to exit the program\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help help")
        output = 'List available commands with "help" or detailed help with'
        output += ' "help cmd".\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help count")
        output = 'Count the number of instances of a class\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help hello")
        output = '*** No help on hello\n'
        self.assertEqual(f.getvalue(), output)

    def test_create(self):
        """test the create command"""
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create")
        opt = '** class name missing **\n'
        self.assertEqual(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create NotClass")
        opt = "** class doesn't exist **\n"
        self.assertEqual(f.getvalue(), opt)

    def test_create_default(self):
        """test the create command via default"""
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("NotClass.create()")
        opt = "** class doesn't exist **\n"
        self.assertEqual(f.getvalue(), opt)

    def test_show(self):
        """test the show command"""
        self.setUp()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show NotClass")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234")
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {id}")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'BaseModel.{id}':
                my_obj = v
        output = f"[BaseModel] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"show User {id}")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'User.{id}':
                my_obj = v
        output = f"[User] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show User 1234")
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"show State {id}")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'State.{id}':
                my_obj = v
        output = f"[State] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show State 1234")
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"show City {id}")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'City.{id}':
                my_obj = v
        output = f"[City] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show City 1234")
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"show Amenity {id}")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'Amenity.{id}':
                my_obj = v
        output = f"[Amenity] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show Amenity 1234")
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"show Place {id}")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'Place.{id}':
                my_obj = v
        output = f"[Place] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show Place 1234")
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"show Review {id}")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'Review.{id}':
                my_obj = v
        output = f"[Review] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show Review 1234")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_show_default(self):
        """test the show command via default"""
        self.setUp()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show("1234")')
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show('{id}')")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'BaseModel.{id}':
                my_obj = v
        output = f"[BaseModel] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('User.show("1234")')
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"User.show('{id}')")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'User.{id}':
                my_obj = v
        output = f"[User] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('State.show("1234")')
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"State.show('{id}')")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'State.{id}':
                my_obj = v
        output = f"[State] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('City.show("1234")')
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"City.show('{id}')")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'City.{id}':
                my_obj = v
        output = f"[City] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('Amenity.show("1234")')
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show('{id}')")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'Amenity.{id}':
                my_obj = v
        output = f"[Amenity] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('Place.show("1234")')
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show('{id}')")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'Place.{id}':
                my_obj = v
        output = f"[Place] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('Review.show("1234")')
        self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show('{id}')")
        for k, v in FileStorage._FileStorage__objects.items():
            if k == f'Review.{id}':
                my_obj = v
        output = f"[Review] ({id}) {my_obj.__dict__}\n"
        self.assertEqual(f.getvalue(), output)

    def test_count_default(self):
        """test the count command via default"""
        self.setUp()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
            HBNBCommand().onecmd("BaseModel.create()")
            HBNBCommand().onecmd("User.create()")
            HBNBCommand().onecmd("User.create()")
            HBNBCommand().onecmd("User.create()")
            HBNBCommand().onecmd("City.create()")
            HBNBCommand().onecmd("Place.create()")
            HBNBCommand().onecmd("Amenity.create()")
            HBNBCommand().onecmd("State.create()")
            HBNBCommand().onecmd("Review.create()")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
        self.assertEqual(f.getvalue(), "2\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        self.assertEqual(f.getvalue(), "3\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
        self.assertEqual(f.getvalue(), "1\n")

    def test_destroy(self):
        """test the destroy command"""
        self.setUp()

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {id[:-1]}")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.count()")
        self.assertEqual(f.getvalue(), "0\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {id[:-1]}")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"User.count()")
        self.assertEqual(f.getvalue(), "0\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"destroy City {id[:-1]}")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"City.count()")
        self.assertEqual(f.getvalue(), "0\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Place {id[:-1]}")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"Place.count()")
        self.assertEqual(f.getvalue(), "0\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"destroy State {id[:-1]}")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"State.count()")
        self.assertEqual(f.getvalue(), "0\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Amenity {id[:-1]}")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.count()")
        self.assertEqual(f.getvalue(), "0\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Review {id[:-1]}")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"Review.count()")
        self.assertEqual(f.getvalue(), "0\n")

    def test_destroy_default(self):
        """test the destroy command via default"""
        self.setUp()

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy(\"{id[:-1]}\")")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.count()")
        self.assertEqual(f.getvalue(), "0\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy(\"{id[:-1]}\")")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"User.count()")
        self.assertEqual(f.getvalue(), "0\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy(\"{id[:-1]}\")")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"City.count()")
        self.assertEqual(f.getvalue(), "0\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy(\"{id[:-1]}\")")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"Place.count()")
        self.assertEqual(f.getvalue(), "0\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"State.destroy(\"{id[:-1]}\")")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"State.count()")
        self.assertEqual(f.getvalue(), "0\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy(\"{id[:-1]}\")")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.count()")
        self.assertEqual(f.getvalue(), "0\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
        self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
        id = f.getvalue()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
        self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy(\"{id[:-1]}\")")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"Review.count()")
        self.assertEqual(f.getvalue(), "0\n")

    def test_all(self):
        """test the all command"""
        self.setUp()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertEqual(f.getvalue(), "[]\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "BaseModel":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all User")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "User":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all City")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "City":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create State")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all State")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "State":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create Place")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all Place")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "Place":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Amenity")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all Amenity")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "Amenity":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all Review")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "Review":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

    def test_all_default(self):
        """test the all command via default"""
        self.setUp()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
        self.assertEqual(f.getvalue(), '[]\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("NotClass.all()")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
            HBNBCommand().onecmd("BaseModel.create()")
            HBNBCommand().onecmd("BaseModel.create()")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "BaseModel":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        self.assertEqual(f.getvalue(), '[]\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "User":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
        self.assertEqual(f.getvalue(), '[]\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
            HBNBCommand().onecmd("State.create()")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "State":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
        self.assertEqual(f.getvalue(), '[]\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
            HBNBCommand().onecmd("City.create()")
            HBNBCommand().onecmd("City.create()")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "City":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
        self.assertEqual(f.getvalue(), '[]\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "Amenity":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
        self.assertEqual(f.getvalue(), '[]\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
            HBNBCommand().onecmd("Place.create()")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "Place":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
        self.assertEqual(f.getvalue(), '[]\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
            HBNBCommand().onecmd("Review.create()")
            HBNBCommand().onecmd("Review.create()")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
        all = f.getvalue()
        all_v = []
        for v in FileStorage._FileStorage__objects.values():
            if v.__class__.__name__ == "Review":
                all_v.append(str(v))
        self.assertEqual(all, f'{all_v}\n')

    def test_update(self):
        """test the update command"""
        self.setUp()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update")
        self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 121212")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        id = f.getvalue()[:-1]

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {id}")
        self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {id} \"name\"")
        self.assertEqual(f.getvalue(), "** value missing **\n")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {id} name \"Betty\"")
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update User {id} name \"Betty\"")
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update City {id} name \"Betty\"")
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {id} name \"Betty\"")
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update State {id} name \"Betty\"")
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update Amenity {id} name \"Betty\"")
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f"update Review {id} name \"Betty\"")
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

    def test_update_default(self):
        """test the update command via default"""
        self.setUp()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("Bar")')
        self.assertEqual(f.getvalue(), '** no instance found **\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
        id = f.getvalue()[:-1]

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.update("{id}"')
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.update("{id}", "name"')
        self.assertEqual(f.getvalue(), '** value missing **\n')

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.update("{id}", "name", "Betty"')
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('User.update("Bar")')
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'User.update("{id}"')
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'User.update("{id}", "name"')
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'User.update("{id}", "name", "Betty"')
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('State.update("Bar")')
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'State.update("{id}"')
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'State.update("{id}", "name"')
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'State.update("{id}", "name", "Betty"')
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('City.update("Bar")')
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'City.update("{id}"')
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'City.update("{id}", "name"')
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'City.update("{id}", "name", "Betty"')
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('Amenity.update("Bar")')
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'Amenity.update("{id}"')
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'Amenity.update("{id}", "name"')
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'Amenity.update("{id}", "name", "Betty"')
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('Place.update("Bar")')
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'Place.update("{id}"')
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'Place.update("{id}", "name"')
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'Place.update("{id}", "name", "Betty"')
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('Review.update("Bar")')
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'Review.update("{id}"')
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'Review.update("{id}", "name"')
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'Review.update("{id}", "name", "Betty"')
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Betty")

    def test_update_default_dict(self):
        """test the update command via default with a dictionary"""
        self.setUp()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
        id = f.getvalue()[:-1]
        input = 'BaseModel.update("{}", {})'.format(id,
                                                    {"name": "Joe", "age": 89})
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(input)
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Joe")
                self.assertEqual(v.age, 89)

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
        id = f.getvalue()[:-1]
        input = 'User.update("{}", {})'.format(id,
                                               {"name": "Joe", "age": 89})
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(input)
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Joe")
                self.assertEqual(v.age, 89)

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
        id = f.getvalue()[:-1]
        input = 'State.update("{}", {})'.format(id,
                                                {"name": "Joe", "age": 89})
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(input)
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Joe")
                self.assertEqual(v.age, 89)

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
        id = f.getvalue()[:-1]
        input = 'City.update("{}", {})'.format(id,
                                               {"name": "Joe", "age": 89})
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(input)
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Joe")
                self.assertEqual(v.age, 89)

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
        id = f.getvalue()[:-1]
        input = 'Place.update("{}", {})'.format(id,
                                                {"name": "Joe", "age": 89})
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(input)
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Joe")
                self.assertEqual(v.age, 89)

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
        id = f.getvalue()[:-1]
        input = 'Amenity.update("{}", {})'.format(id,
                                                  {"name": "Joe", "age": 89})
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(input)
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Joe")
                self.assertEqual(v.age, 89)

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
        id = f.getvalue()[:-1]
        input = 'Review.update("{}", {})'.format(id,
                                                 {"name": "Joe", "age": 89})
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(input)
        for v in FileStorage._FileStorage__objects.values():
            if v.id == id:
                self.assertEqual(v.name, "Joe")
                self.assertEqual(v.age, 89)

    def test_quit(self):
        """test the quit command"""
        with self.assertRaises(SystemExit):
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("quit")
        with self.assertRaises(SystemExit):
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("quit show")

    def test_EOF(self):
        """test with EOF"""
        with self.assertRaises(SystemExit):
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("EOF")
        with self.assertRaises(SystemExit):
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("EOF create")

    def test_empty_line(self):
        """test with an empty line"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("")
        self.assertEqual(f.getvalue(), "")

    def test_wrong_command(self):
        """test with a non existing command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("hello")
        self.assertEqual(f.getvalue(), "*** Unknown syntax: hello\n")


if __name__ == '__main__':
    unittest.main()
