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
