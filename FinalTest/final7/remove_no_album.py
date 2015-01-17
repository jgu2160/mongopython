
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

def removeNoAlbum():
    db=connection.photosharing
    db.albums.create_index([("images",pymongo.ASCENDING)])
    albums=db.albums
    images=db.images
    i = 0
    try:
        while i<images.count():
        	target_image = albums.find_one({"images":i})
        	if target_image == None:
        		images.remove({"_id":i})
        	i = i+1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    print "all orphans removed"  

removeNoAlbum()