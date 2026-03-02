# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # This method implements the C in CRUD. 
    def create(self, createQuery):
        if createQuery is not None: 
            insert_result = self.database.animals.insert_one(createQuery)  # createQuery should be dictionary             
            return f"Document created: {insert_result.acknowledged}" # Returns True if document successfully saved
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # This method implements the R in CRUD. 
    def read(self, readQuery):
        if readQuery is not None:
            result = list(self.database.animals.find(readQuery)) # readQuery should be dictionary             
            return result # Return the list of document results if found
        else:
            raise Exception("Nothing to find, because data parameter is empty")
            
            
    # This method implements the U in CRUD. 
    def update(self, findQuery, updateQuery):
        if findQuery and updateQuery is not None:
            result = self.database.animals.update_many(findQuery, updateQuery) # findQuery and updateQuery should be dictionaries             
            return f"Successfully updated {result.modified_count} documents." # Return the number of documents updated successfully
        else:
            raise Exception("Nothing to update, because findQuery and/or updateQuery parameters are empty")
            
            
    # This method implements the D in CRUD. 
    def delete(self, deleteQuery):
        if deleteQuery is not None:
            result = self.database.animals.delete_one(deleteQuery) # deleteQuery should be dictionary             
            return f"Successfully deleted {result.deleted_count} documents." # Return the number of documents deleted successfully
        else:
            raise Exception("Nothing to delete, because deleteQuery parameter is empty")