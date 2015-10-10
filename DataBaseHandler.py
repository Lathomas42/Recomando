import sqlite3
import os.path


type_dict = {int: "Integer",
             float: "Float",
             str: "String"}


class DataBaseHandler(object):
    """
    Calss DataBaseHandler:
    -Controls sql database creation, management, and querying from python
    """
    def __init__(self, path="/DataBases/RecomandoDB.db"):
        if(not os.path.isfile(path)):
            self.table_list = []
            self.con = sqlite3.connect(path)
            self.cursor = self.con.cursor()
            self._setupdb()
        else:
            self.con = sqlite3.connect(path)
            self.cursor = self.con.cursor()

    # ------------------Purchase Handling-------------------------------
    def add_purchase(self, UserID, ItemID, PurchaseID):
        """
        Adds a purchase element to the purchases dable with values
        corresponding to the arguments.
        """
        self._add_rows("purchases", [UserID, ItemID, PurchaseID])

    def add_purchase_list(self, purchase_list):
        """
        adds rows to the purchases table from a list.
        list elements should be [UserID, ItemID, PurchaseID]
        """
        self._add_rows("purchases", purchase_list)

    # ------------------Ratings Handling-------------------------------
    def add_rating(self, UserID, ItemID, Rating):
        """
        Adds a purchase element to the purchases dable with values
        corresponding to the arguments.
        """
        self._add_rows("ratings", [UserID, ItemID, Rating])

    def add_rating_list(self, rating_list):
        """
        adds rows to the purchases table from a list.
        list elements should be [UserID, ItemID, PurchaseID]
        """
        self._add_rows("ratings", rating_list)

    # ------------------Ratings Handling-------------------------------
    def add_item(self, ItemID, Name, Price, CategoryID):
        """
        Adds a purchase element to the purchases dable with values
        corresponding to the arguments.
        """
        self._add_rows("items", [ItemID, Name, Price, CategoryID])

    def add_item_list(self, item_list):
        """
        adds rows to the purchases table from a list.
        list elements should be [UserID, ItemID, PurchaseID]
        """
        self._add_rows("items", item_list)

    # ------------------Private Functions------------------------------
    def _setupdb(self):
        print("Initializing Database...")
        # First setup the Purchases Database
        self._add_table("purchases", UserID=int, ItemID=int, PurchaseID=int)
        # Then the ratings Database
        self._add_table("ratings", UserID=int, ItemID=int, Rating=int)
        # then the Items Database
        self._add_table("items", ItemID=int, Name=str,
                        Price=float, CategoryID=int)
        # then finally the users
        self._add_table("users", UserID=int, Location=int)

    def _add_table(self, table_name, **kwargs):
        """
        Initializes a table in the database with name table_name
        and value fields corresponding to kwargs.
        eg:
        >add_table("myfriends",name=str, age=int, money=float)

        this makes a new table "myfriends" with 3 columns 1 string,
        1 int and 1 float

        the python types available are: str, int, float
        """
        assert(type(table_name) == str)
        # begin to create the SQL execution string to make the table
        exec_str = "CREATE TABLE {} (".format(table_name.lower())
        # go through kwargs and add columns
        for k in kwargs.keys():
            exec_str += " {} {},".format(k, type_dict[kwargs[k]])
        # remove final comma add a closing paren and execute the string
        exec_str = exec_str[:-1] + ")"
        self.con.execute(exec_str)
        self.table_list.append(table_name.lower())

    def _add_rows(self, table_name, rows):
        """
        adds rows to the specified table from a list.
        list elements should be [UserID, ItemID, PurchaseID]
        """
        exec_str = "INSERT INTO {} VALUES (".format(table_name)
        if(type(rows[0]) != list):
            # first make a string of one ? for each element
            values_str = (", ?"*len(rows))[2:]
            # this means you are dealing with a single row
            self.cursor.execute(exec_str + values_str + ")", rows)
        else:
            values_str = (", ?"*len(rows[0]))[2:]
            # this means you are dealing with multiple rows
            self.cursor.executemany(exec_str + values_str + ")", rows)

    def _update(self):
        """
        updates the tables to include the items added to other tables
        """
        return True
