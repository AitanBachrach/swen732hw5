import locations
import students


stu1 = students.swen_student("John Smith")
stu2 = students.english_student("Smith John")

locs = [locations.swen_class(),locations.english_class(),locations.physics_class(),locations.LAH(),locations.GOS(),locations.GOL()]


stu : students.student
loc : locations.location
for stu in [stu1,stu2]:
    for loc in locs:
        loc.acceptStudent(stu)