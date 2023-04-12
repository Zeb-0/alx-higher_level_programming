class Student:
    """
    Represents a student with first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Returns a dictionary representation of the Student instance '''
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json_data):
        for i, value in json.items():
            setattr(self, i, value)

