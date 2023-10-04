import sqlite3


class DatabaseManager(object):
    def __init__(self, db):
        """
        Initializes a new instance of the class.

        Parameters:
            db (str): The name of the database to connect to.

        Returns:
            None
        """
        self.connection = sqlite3.connect(db)
        self.connection.commit()
        self.cursor = self.connection.cursor()

    def query(self, query):
        """
        Executes a SQL query on the database.

        Args:
            query (str): The SQL query to execute.

        Returns:
            The result of the executed query.
        """
        with self.connection:
            self.cursor.execute(query)
            self.connection.commit()
            return self.cursor

    def __del__(self):
        """
        Destructor method called when the object is no longer in use.
        Closes the connection to the database.
        """
        self.connection.close()
