import pymongo

Client = pymongo.MongoClient(host='localhost', port=27017)
db = Client['NewMovie']
collection = db['new']
results = collection.find()
for result in results:
    print(result['MovieName'] + ' : ' + result['MovieUrl'])