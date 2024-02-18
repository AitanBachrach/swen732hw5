from defs import location





class english_class(location):
    def __init__(self):
        pass

    def acceptStudent(self, student) -> None:
        student.visit_english_class(self)

    def get_course_english(self) -> str:
        return "UWRT-150"

class physics_class(location):
    def __init__(self):
        pass
    
    def acceptStudent(self, student) -> None:
        student.visit_physics_class(self)

    def get_course_physics(self) -> str:
        return "PHYS-211"

class swen_class(location):
    def __init__(self):
        pass

    def acceptStudent(self, student) -> None:
        student.visit_swen_class(self)

    def get_course_swen(self) -> str:
        return "SWEN-261"

class LAH(location):
    def __init__(self):
        pass

    def acceptStudent(self, student) -> None:
        student.visit_LAH(self)

    def get_LAH_name(self) -> str:
        return "Liberal Arts Hall"

class GOS(location):
    def __init__(self):
        pass

    def acceptStudent(self, student) -> None:
        student.visit_GOS(self)
    
    def get_GOS_name(self) -> str:
        return "Gosnell Hall"

class GOL(location):
    def __init__(self):
        pass

    def acceptStudent(self, student) -> None:
        student.visit_GOL(self)
    
    def get_GOL_name(self) -> str:
        return "Golisano Hall"