from NotesCore.NotesManager import NotesManager
from NotesCore.ConsoleCore import parser, help_msg

note_manager = NotesManager()

print("Welcome to NotesRSCX! (v0.0.0.0.0.1)")
help_msg()

while True:
    parser(input(">>> "))
