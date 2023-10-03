from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

student = Student(name="Edward", surname="agle", is_active=False)
print(student)

student = Student(name="Edward", surname="agle", is_active=True)
print(student)

try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except Exception as e:
    print(f"{type(e).__name__}: {e}")
