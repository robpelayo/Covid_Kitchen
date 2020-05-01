from .model_sqlite3 import model

# Create the instance of the model
appmodel = model()


def get_model():
    return appmodel
