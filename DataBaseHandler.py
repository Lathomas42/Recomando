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
            self._setupdb()
        self.con = sqlite3.connect(path)
        self.cursor = self.con.cursor()
        self.table_list = {}

    def add_purchase(self, UserID, ItemID, PurchaseID):
        """
        Adds a purchase element to the purchases dable with values
        corresponding to the arguments.
        """
        exec_str = "INSERT INTO purchases\
                    VALUES ( {}, {}, {})".format(UserID, ItemID, PurchaseID)
        self.con.execute(exec_str)

    def add_purchase_list(self, purchase_list):
        """
        adds rows to the purchases table from a list.
        list elements should be [UserID, ItemID, PurchaseID]
        """
        self.cursor.executemany("INSERT INTO purchases \
                                 VALUES (?, ?, ?)", purchase_list)

    def _setupdb(self):
        print("Initializing Database...")
        # First setup the Purchases Database
        self.add_table("purchases", UserID=int, ItemID=int, PurchaseID=int)
        # Then the ratings Database
        self.add_table("ratings", UserID=int, ItemID=int, Rating=int)
        # then the Items Database
        self.add_table("items", Name=str, Price=float, CategoryID=int)
        # then finally the users
        self.add_table("users", UserID=int, Location=int)

    def add_table(self, table_name, **kwargs):
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

