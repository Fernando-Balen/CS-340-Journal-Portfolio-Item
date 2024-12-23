from pymongo import MongoClient
from bson.objectid import ObjectId
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, USER,PASS):
        # Connection Variables
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32057
        DB = 'aac'
        COL = 'animals'
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d'% (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % DB]
        self.collection = self.database['%s' % COL]
    def create(self, data):
        """Create a new document in the animals collection."""
        try:
            if data:
                self.database.animals.insert_one(data)
                return True
            else:
                raise ValueError("The 'data' parameter is empty.")
        except Exception as e:
            print(f"An error occurred while creating the document: {str(e)}")
            return False
    def read(self, search_criteria=None):
        """Read documents from the animals collection based on search criteria."""
        try:
            if search_criteria is None:
            	search_criteria = {}
            return list(self.database.animals.find(search_criteria))
        except Exception as e:
            print(f"An error occurred while reading documents: {str(e)}")
            return []
    def update(self, search_criteria, update_data):
        """Update document(s) in the animals collection based on search criteria."""
        try:
            if search_criteria and update_data:
                result = self.database.animals.update_many(search_criteria, {'$set': update_data})
                return result.modified_count
            else:
                raise ValueError("Both 'search_criteria' and 'update_data' are required.")
        except Exception as e:
            print(f"An error occurred while updating documents: {str(e)}")
            return 0
    def delete(self, search_criteria):
        """Delete document from the animals collection based on search criteria."""
        try:
            if search_criteria:
                result = self.database.animals.delete_many(search_criteria)
                return result.deleted_count
            else:
                raise ValueError("Search criteria are required to delete documents.")
        except Exception as e:
            print(f"An error occurred while deleting documents: {str(e)}")
            return 0
