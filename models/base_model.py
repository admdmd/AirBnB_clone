#!/usr/bin/python3
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    super class for the Airbnbclone project
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises attributes for ID creation and updates
        """

        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for tag, value in kwargs.items():
                if "created_at" == tag:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        time_format)
                elif "updated_at" == tag:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        time_format)
                elif "__class__" == tag:
                    pass
                else:
                    setattr(self, tag, value)
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        output the class name, id, and the dictionary
        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        instance method to update current datetime,
        invoke save and save to serializes file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary of basemodel with string formats of times
        """

        dic_out = self.__dict__.copy()
        dic_out["__class__"] = self.__class__.__name__
        dic_out["created_at"] = self.created_at.isoformat()
        dic_out["updated_at"] = self.updated_at.isoformat()
        return dic_out
