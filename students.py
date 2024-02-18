from defs import student




    
class swen_student(student):
    import locations
    def __init__(self, name : str) -> None:
        super().__init__(name)

    def visit_english_class(self, eng_class) -> None:
        print(self.name +" wonders why they have to go to english class "+ eng_class.get_course_english())

    def visit_LAH(self, lah) -> None:
        print(self.name +" loathes the " + lah.get_LAH_name())

    def visit_GOL(self, gol) -> None:
        print(self.name + " does most of their classes in " + gol.get_GOL_name())

    def visit_swen_class(self, swen_class) -> None:
        print(self.name + " thinks " + swen_class.get_course_swen() + " needs a rework")

    def visit_GOS(self,  gos) -> None:
        print(self.name + " takes a suprising amount of classes in " + gos.get_GOS_name())

    def visit_physics_class(self, phys_class) -> None:
        print(self.name + " mildly enjoys " + phys_class.get_course_physics())

class english_student(student):
    import locations
    def __init__(self, name : str) -> None:
        super().__init__(name)

    def visit_english_class(self, eng_class) -> None:
        print(self.name +" enjoys "+ eng_class.get_course_english())

    def visit_LAH(self, lah) -> None:
        print(self.name +" takes most of their classes in the " + lah.get_LAH_name())

    def visit_GOL(self, gol) -> None:
        print(self.name + " has had one class in the " + gol.get_GOL_name())

    def visit_swen_class(self, swen_class) -> None:
        print(self.name + " needs something from their friend in " + swen_class.get_course_swen())

    def visit_GOS(self,  gos) -> None:
        print(self.name + " has had a several classes in " + gos.get_GOS_name())

    def visit_physics_class(self, phys_class) -> None:
        print(self.name + " is indifferent to " + phys_class.get_course_physics())

