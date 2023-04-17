#!/usr/bin/python3

''' defines a class Base '''
import os
import turtle
import csv
import json


class Base:
    ''' class Base '''
    __nb_objects = 0
    def __init__(self, id=None):
        ''' new Base instance '''
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns json tring rep of a dictionary '''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation of list_objs to a file
        '''
        file_name = cls.__name__ + '.json'
        with open(file_name, 'w') as json_file:
            if list_objs is None:
                json_file.write('[]')
            else:
                list_dict = [ob.to_dictionary() for ob in list_objs]
                json_file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        '''
        returns list of the JSON string representation json_string
        '''
        json_string = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)
        return (json_string_list)

    @classmethod
    def create(cls, **dictionary):
        '''return class instance from a dictionary of attribute '''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_class = cls(1, 1)
            else:
                new_class = cls(1)
            new_class.update(**dictionary)
            return new_class

    @classmethod
    def load_from_file(cls):
        ''' return a list of class instances '''
        file_name = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                my_str = my_file.read()
                list_dictionaries = cls.from_json_string(my_str)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' CSV serialization of list of objects to file '''
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())


    @classmethod
    def load_from_file_csv(cls):
        ''' return list of classes instance from CSV file '''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def draw(list_rectangles, list_squares):
        ''' use turtle module to draw rectangle and square

        params:
            list_rectangles : rectangle list objects
            list_squares: square list objects
        '''
        ttl = turtle.Turtle()
        ttl = screen.bgcolor('#b9332c')
        ttl.pensize(3)
        ttl.shape('turtle')

        ttl.color('ffffff')
        for rec in list_rectangles:
            ttl.showturtles()
            ttl.up()
            ttl.goto(rec.x, rec.y)
            ttl.down()

            for i in range(2):
                ttl.forward(rec.width)
                ttl.left(90)
                ttl.forward(rec.height)
                ttl.left(90)
            ttl.hideturtle()

        ttl.color('#A52A2A')
        for sq in list_squares:
            ttl.showturtle()
            ttl.up()
            ttl.goto(sq.x, sq.y)
            ttl.down()
            for i in range(2):
                ttl.forward(sq.width)
                ttl.left(90)
                ttl.forward(sq.height)
                ttl.left(90)
            ttl.hideturtle()

        tutle.exitonclick()
