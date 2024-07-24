from fastapi import FastAPI
from pydantic import BaseModel
# إنشاء تطبيق FastAPI
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # يسمح بالوصول من أي مصدر. قم بتقييد هذا في الإنتاج
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)
# تعريف نموذج البيانات باستخدام Pydantic
class Student(BaseModel):
  id: int
  name: str
  grade: int
# قائمة لتخزين البيانات في الذاكرة
students = [
  Student(id=1,name="karim ali",grade=5),
  Student(id=2,name="khadija ahmed",grade=3),
]
# قراءة جميع العناصر
@app.get("/students/")
def read_students():
  return students
# إنشاء عنصر جديد
@app.post("/students/")
def create_student(New_Student: Student):
  students.append(New_Student)
  return New_Student
# تحديث عنصر معين بناءً على معرفه (ID) باستخدام PUT method
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
  for index, student in enumerate(students):
      if student.id == student_id:
          students[index] = updated_student
          return updated_student
  return {"error": "Student not found"}
# حذف عنصر معين بناءً على معرفه (ID) باستخدام DELETE method
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
  for index, student in enumerate(students):
      if student.id == student_id:
          del students[index]
          return {"message": "Student deleted"}
  return {"error": "Student not found"}
