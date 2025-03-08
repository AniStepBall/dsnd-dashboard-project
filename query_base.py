# Import any dependencies needed to execute sql queries
import sqlite3
import pandas as pd

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase:

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ""

    # Define a `names` method that receives
    # no passed arguments
    def names(self):

        # Return an empty list
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id):

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        conn = sqlite3.connect("employee_events.db")

        query = f"""
        SELECT
            event_date,
            SUM(positive_events) AS total_positive,
            SUM(negative_events) AS total_negative
        FROM {self.name}
        GROUP BY event_date
        ORDER BY event_date;
        """

        df = pd.read_sql_query(query, conn, params=(id,))

        conn.close()
        return df



    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes(self, id):

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        conn = sqlite3.connect("employee_events.db")

        query = f"""
        SELECT
            notes.note_date,
            notes.note
        FROM notes
        JOIN {self.name} ON notes.{self.name}_id = {self.name}.id
        """

        df = pd.read_sql_query(query, conn, params=(id,))
        conn.close()
        return df
