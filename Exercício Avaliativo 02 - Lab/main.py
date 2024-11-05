from database import Database
from teacher_crud import TeacherCRUD

db = Database("bolt://98.84.114.137", "neo4j", "rest-lesson-stopper")
#db.drop_all()

teacher_crud = TeacherCRUD(db)

#teacher_crud.create(1956, "Chris Lima",  '189.052.396-66')

#print(teacher_crud.read("Chris Lima"))

teacher_crud.update("Chris Lima","162.052.777-77")