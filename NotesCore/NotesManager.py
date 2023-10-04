import time

from NotesCore.DatabaseManager import DatabaseManager


class NotesManager(object):
    db_manager = None

    def __init__(self):
        """
        Initializes the class and sets up the `db_manager` attribute.

        Parameters:
            None

        Returns:
            None
        """
        self.db_manager = DatabaseManager('notes.db')

    def save(self, **content):
        """
        Save the content to the database.

        Args:
            **content: A dictionary of content to be saved.
                title (str): The title of the content.
                body (str, optional): The body of the content. Defaults to "".

        Returns:
            None
        """
        title = ""
        body = ""
        if len(content) == 2:
            title = content['title']
            body = content['body']
        elif len(content) == 1:
            title = content['title']
        time = self.get_time()
        self.db_manager.query(
            "INSERT INTO notes (title, body, create_time) VALUES ('{}', '{}', '{}')".format(title, body, time)
        )

    def get_time(self):
        """
        Get the current local time and format it as a string.

        Returns:
            string: The formatted local time string.
        """
        local_time = time.localtime()
        string_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        return string_time

    def delete(self, note_id):
        """
        Deletes a note from the database.

        Args:
            note_id (int): The ID of the note to be deleted.

        Returns:
            int: The number of rows affected by the deletion.
        """
        status = self.db_manager.query("DELETE FROM notes WHERE note_id=" + str(note_id) + ";"
                                       )
        return status.rowcount

    def search(self, query="", limit=1):
        """
        Search for notes in the database based on the given query.

        Args:
            query (str, optional): The search query. Defaults to "".
            limit (int, optional): The maximum number of results to return. Defaults to 1.

        Returns:
            list: A list of dictionaries representing the matching notes. Each dictionary
                  contains the following keys:
                  - "_id" (int): The unique identifier of the note.
                  - "title" (str): The title of the note.
                  - "body" (str): The body of the note.
                  - "create_date" (str): The creation date of the note.

                  If the limit is set to 1, a list with a single dictionary will be returned.
        """
        list_text = []
        if limit == 1:
            for row in self.db_manager.query(
                    "select * from notes where title LIKE '%" + query + "%' or body LIKE '%" + query + "%'"):
                note_text = {}
                note_text["_id"] = row[0]
                note_text["title"] = row[1]
                note_text["body"] = row[2]
                note_text["create_date"] = row[3]
                list_text.append(note_text)
        elif limit > 1:
            for row in self.db_manager.query(
                    "select * from notes where title LIKE '%" + query + "%' or body LIKE '%" + query + "%' limit '" + str(limit) + "'"):
                note_text = {}
                note_text["_id"] = row[0]
                note_text["title"] = row[1]
                note_text["body"] = row[2]
                note_text["create_date"] = row[3]
                list_text.append(note_text)
        return list_text

    def view(self, note_id=""):
        """
        Retrieves the title and body of a note from the database based on the provided `note_id`.

        Parameters:
            note_id (str): The ID of the note to retrieve from the database. Defaults to an empty string.

        Returns:
            dict: A dictionary containing the title and body of the note retrieved from the database.
        """
        note_text = {}

        for row in self.db_manager.query(
                "select * from notes where note_id = '" + note_id + "'"
        ):
            note_text["title"] = row[1]
            note_text["body"] = row[2]
        return note_text

    def view_all(self):
        """
        Retrieves all the notes from the database and returns them as a list of dictionaries.

        Returns:
            list: A list of dictionaries representing the notes. Each dictionary contains the fields:
                - "_id" (int): The unique identifier of the note.
                - "title" (str): The title of the note.
                - "body" (str): The body of the note.
                - "create_date" (str): The creation date of the note.
        """
        list_text = []
        for row in self.db_manager.query("SELECT * FROM notes"):
            note_text = {}
            note_text["_id"] = row[0]
            note_text["title"] = row[1]
            note_text["body"] = row[2]
            note_text["create_date"] = row[3]
            list_text.append(note_text)
        return list_text
