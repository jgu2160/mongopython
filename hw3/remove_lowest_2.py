
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)


def remove_lowest_hw():
    
    db=connection.school
    students=db.students
    numOfStudents=db.students.count()
    i=0
    try:
        while i<numOfStudents:
            numOfGrades=students.find({'scores.type':'homework','_id':i})
            homeworkArray=numOfGrades[0]['scores'][2:4]
            print homeworkArray
            score1=homeworkArray[0]['score']
            score2=homeworkArray[1]['score']
            print "\n\nremoving all lowest hw"
            if score1<score2:
                students.update({"_id":i,"scores.score":score1},{"$pull":{"scores":{"score":score1}}})
            else:
                students.update({"_id":i,"scores.score":score2},{"$pull":{"scores":{"score":score2}}})
            i=i+1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    print "all lowest removed"  

remove_lowest_hw()
