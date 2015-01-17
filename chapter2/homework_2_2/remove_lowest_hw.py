
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)


def remove_lowest_hw():
    print "\n\nremoving all lowest hw"
    db=connection.students
    grades = db.grades
    try:
        numOfGrades=grades.find({'type':'homework'},{'_id':0}).count()
        print numOfGrades
        i=0
        while i<200:
            query={'type':'homework','student_id':i}
            lowestStudentGrade=grades.find(query).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)]).limit(1)
            for doc in lowestStudentGrade:
                number=doc['score']
                print number
                print "removing lowest grade\n\n"
                newquery={'type':'homework','student_id':i,'score':number}
                grades.remove(newquery)
            i=i+1


    except:
        print "Unexpected error:", sys.exc_info()[0]
       
remove_lowest_hw()
