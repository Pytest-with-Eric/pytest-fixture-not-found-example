import sqlite3

class database_operation:
    def __init__(self, dbname: str) -> None:
        self.mydb = sqlite3.connect(dbname)
        self.cursor = self.mydb.cursor()
    
    def check_connection(self):
        """
        Function to check connection.
        """
        if self.mydb.cursor:
            return True
        else:
            return False
      
    def execute_sql(self, sql: str):
        """
        Function to execute SQL query.
        """
        self.cursor.execute(sql)
        return True 

    def get_table_data(self, sql: str):
        """
        Function to get data from table.
        """
        result = self.cursor.execute(sql)
        return result



