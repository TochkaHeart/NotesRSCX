import sys

from NotesCore.NotesManager import NotesManager
note_manager = NotesManager()


def help_msg():
    """
    Prints a help message displaying the available commands and returns True.

    Returns:
        bool: True if the help message is printed successfully.
    """
    print("Commands:")
    print("    save <note_title>")
    print("    view <note_id>")
    print("    delete <note_id>")
    print("    search <query>")
    print("    view_all")
    print("    help")
    print("    quit\n")
    return True


def parser(text):
    """
    Parses the given text to execute different commands.

    Args:
        text (str): The input text containing the command and its arguments.

    Returns:
        bool or None: Returns True for successful execution of certain commands
                     and None for invalid commands or arguments.

    Raises:
        IndexError: If the input text does not contain enough arguments.
    """
    try:
        cmd = text.split(" ")[0]
        if cmd == "save":
            note_title = text.split(" ")[1]
            note_body = input("Note body: ")
            note_manager.save(title=note_title, body=note_body)
            return print("Note saved.")

        elif cmd == "view":
            note_id = text.split(" ")[1]
            note = note_manager.view(note_id)
            return print(f"Title: {note['title']}\nBody: {note['body']}\n\n")
        elif cmd == "view_all":
            notes = note_manager.view_all()
            if notes == []:
                print("No notes found.")
            else:
                for note in notes:
                    print(f"Note #{note['_id']}\nTitle: {note['title']}\nBody: {note['body']}\n\n")
            return True
        elif cmd == "delete":
            note_id = text.split(" ")[1]
            note_manager.delete(note_id)
            return print(f"Note {note_id} deleted.")
        elif cmd == "search":
            query = text.split(" ")[1]
            notes = note_manager.search(query)

            if len(notes) == 1:
                print(f"Found {len(notes)} notes:")
                print(f"Note #{notes[0]['_id']}\nTitle: {notes[0]['title']}\nBody: {notes[0]['body']}\n\n")
            elif len(notes) > 1:
                print(f"Found {len(notes)} notes:")
                for note in notes:
                    print(f"Note #{note['_id']}\nTitle: {note['title']}\nBody: {note['body']}\n\n")
            else:
                print("No notes found.")
            return True
        elif cmd == "quit":
            print("Bye!")
            return sys.exit(0)
        elif cmd == "help":
            return help_msg()
        else:
            print("Invalid command!")
            return help_msg()
    except IndexError:
        print("Invalid argument!\n\n")
        return help_msg()
