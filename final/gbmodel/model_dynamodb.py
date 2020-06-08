from .Model import Model
import boto3

class model(Model):
    def __init__(self):
        self.resource = boto3.resource("dynamodb")
        self.table = self.resource.Table('covidkitchen')

        try:
            self.table.load()
        except:
            self.resource.create_table(
                TableName="covidkitchen",
                KeySchema=[
                    {
                        "AttributeName": "state",
                        "KeyType": "HASH"
                    }
                ],
                AttributeDefinitions=[
                    {
                        "AttributeName": "state",
                        "AttributeType": "S"
                    }
                ],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1
                }
            )
        self.resource2 = boto3.resource("dynamodb")
        self.table2 = self.resource2.Table('caloriecounter')
        try:
            self.table2.load()
        except:
            self.resource2.create_table(
                TableName="covidkitchen",
                KeySchema=[
                    {
                        "AttributeName": "name",
                        "KeyType": "HASH"
                    }
                ],
                AttributeDefinitions=[
                    {
                        "AttributeName": "name",
                        "AttributeType": "S"
                    }
                ],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1
                }
            )

    def select(self):
        try:
            ckentries = self.table.scan()
        except Exception as e:
            return([['scan failed', '.', '.', '.']])

        return([ [f['state'], f['confirmed'], f['deaths'], f['active']] for f in ckentries['Items']])

    def insert(self, state, confirmed, deaths, active):
        """
        Inserts entry into database
        :param state: String
        :param confirmed: Integer
        :param deaths: Integer
        :param active: Integer
        :return: none
        :raises: Database errors on connection and insertion
        """
        ckitem = {'state': state,
                  'confirmed': confirmed,
                  'deaths': deaths,
                  'active': active}

        try:
            self.table.put_item(Item=ckitem)
        except:
            return False

        return True

    def delete(self, state):
        ckitem = {'state': state}
        try:
            response = self.table.delete_item(Key=ckitem)
            print(response)
        except:
            return False
        return True

    def food_select(self):
        try:
            fientries = self.table2.scan()
        except Exception as e:
            return([['scan failed', '.', '.', '.', '.', '.','.']])

        return([ [f['name'], f['calories'], f['protein'], f['fat'], f['carbs'], f['fiber']] for f in fientries['Items']])

    def food_insert(self, name, calories, protein, fat, carbs, fiber):
        """
        Inserts entry into database
        :param name: String
        :param calories: Integer
        :param protein: Integer
        :param fat: Integer
        :param: carbs: Integer
        :return: fiber: Integer
        :param: image: String
        :raises: Database errors on connection and insertion
        """
        fitem = {'name': name,
                  'calories': calories,
                  'protein': protein,
                  'fat': fat,
                  'carbs': carbs,
                  'fiber': fiber}

        try:
            self.table2.put_item(Item=fitem)
        except:
            return False

        return True

    def food_delete(self, name):
        fitem = {'name': name}

        try:
            print(fitem)
            self.table2.delete_item(Key=fitem)
        except:
            return False
        return True