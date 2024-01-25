#!/usr/bin/python3
""" Console Module """

import cmd
import uuid
from datetime import datetime

class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""
    prompt = "$$$$$"
    def do_greet(self, person):
        print("Hello,", person)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
