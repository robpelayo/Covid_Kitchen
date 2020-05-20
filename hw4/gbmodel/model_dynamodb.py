from .Model import Model
import boto3


class model(Model):
    def __init__(self):
        self.resource = boto3.resource("dynamodb")
        self.table = self.resource.Table('foodtrucks')
        try:
            self.table.load()
        except:
            self.resource.create_table(
                TableName="foodtrucks",
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
            ftentries = self.table.scan()

        except Exception as e:
            return ([['scan failed', '.', '.', '.']])

        return ([[f['name'], f['address'], f['city'], f['state'], f['zip'], f['hours'], f['phone'], f['rating'],
                  f['pricing'], f['parking'], f['review']] for f in ftentries['Items']])

    def insert(self, name, address, city, state, zip, hours, phone, rating, pricing, parking, review):
        """
        Inserts entry into database
        :param name: String
        :param address: String
        :param city: String
        :param state: String
        :param zip: Integer
        :param hours: String
        :param phone: String
        :param rating: String
        :param pricing: String
        :param parking: String
        :param review: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        ftitem = {'name': name,
                  'address': address,
                  'city': city,
                  'state': state,
                  'zip': zip,
                  'hours': hours,
                  'phone': phone,
                  'rating': rating,
                  'pricing': pricing,
                  'parking': parking,
                  'review': review}

        try:
            self.table.put_item(Item=ftitem)
        except:
            return False

        return True
