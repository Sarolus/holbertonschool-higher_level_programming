#!/usr/bin/python3

"""
    Student Class Module
"""


class Student():
    """
        Define a student class.
    """
    def __init__(self, first_name, last_name, age):
        """
            Constructor method

            Args:
                first_name = Student First Name.
                last_name = Student Last Name.
                age = Student Age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Retrieve a dictionary representation of
            a Student instance.
        """
        if attrs is not None:
            return {k: val for k, val in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
            Replace all attributes of the Student
            instance.
        """
        for key, value in json.items():
            self.__setattr__(key, value)
