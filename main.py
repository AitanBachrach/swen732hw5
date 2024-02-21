
# location interface defining the accept student function
class location:
    def __init__(self) -> None:
        pass

    def acceptStudent(self, student : 'student') -> None:
        pass

# location implementations responsible for implementaion of accept and any additional functions
class english_class(location):
    def __init__(self):
        pass

    def acceptStudent(self, student : 'student') -> None:
        student.visit_english_class(self)

    def get_course_english(self) -> str:
        return "UWRT-150"

class physics_class(location):
    def __init__(self):
        pass
    
    def acceptStudent(self, student : 'student') -> None:
        student.visit_physics_class(self)

    def get_course_physics(self) -> str:
        return "PHYS-211"

class swen_class(location):
    def __init__(self):
        pass

    def acceptStudent(self, student : 'student') -> None:
        student.visit_swen_class(self)

    def get_course_swen(self) -> str:
        return "SWEN-261"

class LAH(location):
    def __init__(self):
        pass

    def acceptStudent(self, student : 'student') -> None:
        student.visit_LAH(self)

    def get_LAH_name(self) -> str:
        return "Liberal Arts Hall"

class GOS(location):
    def __init__(self):
        pass

    def acceptStudent(self, student : 'student') -> None:
        student.visit_GOS(self)
    
    def get_GOS_name(self) -> str:
        return "Gosnell Hall"

class GOL(location):
    def __init__(self):
        pass

    def acceptStudent(self, student : 'student') -> None:
        student.visit_GOL(self)
    
    def get_GOL_name(self) -> str:
        return "Golisano Hall"

# Student Interface responsible for defining the possible visits a student might need to possess
class student:
    def __init__(self, name : str) -> None:
        self.name = name
        pass

    def visit_english_class(self, loc : english_class) -> None:
        pass

    def visit_LAH(self, loc : LAH) -> None:
        pass

    def visit_GOL(self, loc : GOL) -> None:
        pass

    def visit_swen_class(self, loc : swen_class) -> None:
        pass

    def visit_GOS(self, loc : GOS) -> None:
        pass

    def visit_physics_class(self, loc : physics_class) -> None:
        pass

# Student Implentations responsible for implementing the visits and calling the individual locations
class swen_student(student):
    def __init__(self, name : str) -> None:
        super().__init__(name)

    def visit_english_class(self, eng_class : english_class) -> None:
        print(self.name +" wonders why they have to go to english class "+ eng_class.get_course_english())

    def visit_LAH(self, lah : LAH) -> None:
        print(self.name +" loathes the " + lah.get_LAH_name())

    def visit_GOL(self, gol : GOL) -> None:
        print(self.name + " does most of their classes in " + gol.get_GOL_name())

    def visit_swen_class(self, swen_class : swen_class) -> None:
        print(self.name + " thinks " + swen_class.get_course_swen() + " needs a rework")

    def visit_GOS(self,  gos : GOS) -> None:
        print(self.name + " takes a suprising amount of classes in " + gos.get_GOS_name())

    def visit_physics_class(self, phys_class : physics_class) -> None:
        print(self.name + " mildly enjoys " + phys_class.get_course_physics())

class english_student(student):
    def __init__(self, name : str) -> None:
        super().__init__(name)

    def visit_english_class(self, eng_class : english_class) -> None:
        print(self.name +" enjoys "+ eng_class.get_course_english())

    def visit_LAH(self, lah : LAH) -> None:
        print(self.name +" takes most of their classes in the " + lah.get_LAH_name())

    def visit_GOL(self, gol : GOL) -> None:
        print(self.name + " has had one class in the " + gol.get_GOL_name())

    def visit_swen_class(self, swen_class : swen_class) -> None:
        print(self.name + " needs something from their friend in " + swen_class.get_course_swen())

    def visit_GOS(self,  gos : GOS) -> None:
        print(self.name + " has had a several classes in " + gos.get_GOS_name())

    def visit_physics_class(self, phys_class : physics_class) -> None:
        print(self.name + " is indifferent to " + phys_class.get_course_physics())

#Runs through the possible combinations of student and location showing off the different functionality
if __name__ == '__main__':
    stu1 = swen_student("John Smith")
    stu2 = english_student("Smith John")

    locs = [swen_class(),english_class(),physics_class(),LAH(),GOS(),GOL()]


    stu : student
    loc : location
    for stu in [stu1,stu2]:
        for loc in locs:
            loc.acceptStudent(stu)