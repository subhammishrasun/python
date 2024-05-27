
import pymongo
 
# Connect to the database
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['e-com']
 
# Get the 'users' collection
products = db['products']
 
# Insert a single document
'''mylist = [
   { 'name': 'fog',
    'brand':'axe',
    'price':4200,
    'categorey':'porfume'},
    {
        'name':'akash gupta',
        'brand':'guchi',
        'price':5000,
        'categorey':'wallet'
    }   
]
result=products.insert_many(mylist)
 
print(result.inserted_ids)'''

'''#find function is use
for x in products.find():
    print(x)'''

