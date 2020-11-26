import pymongo

client = None
db = None

# TODO: Throw error when connecting failed
def connect(host, database):
    global client, db
    client = pymongo.MongoClient("mongodb+srv://user:notuser@cluster0.7hhoe.mongodb.net/telegram_messages?retryWrites=true&w=majority")
    db = client[database]

def insert(message, collection):
    global db
    col = db[collection]
    col.insert_one(message)

# Print function for testing
def printAll(collection):
    col = db[collection]
    for x in col.find():
        print(x)
