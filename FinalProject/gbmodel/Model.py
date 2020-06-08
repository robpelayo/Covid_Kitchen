class Model():
    def select(self):
        """
        Gets all entries from the database for states
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, state, confirmed, deaths, active):
        """
        Inserts state entry into database
        :param state: String
        :param cases: Integer
        :param deaths: Integer
        :param: active: Integer
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass

    def food_insert(self, name, calories, protein, fat, carbs, fiber):
        """
        Inserts entry into database
        :param name: String
        :param calories: Integer
        :param protein: Integer
        :param fat: Integer
        :param: carbs: Integer
        :return: fiber: Integer
        :raises: Database errors on connection and insertion
        """
        pass

    def food_select(self):
        """
        Gets all entries from the database for food
        :return: Tuple containing all rows of database
        """
        pass
