class Student:
    def __init__(self, name="", id_student="", point=0):
        self.name = name
        self.id_student = id_student
        self.point = point

    def set_name(self, name):
        self.name = name

    def set_id_student(self, id_student):
        self.id_student = id_student

    def set_point(self, point):
        self.point = point

    def get_name(self):
        return self.name

    def get_id_student(self):
        return self.id_student

    def get_point(self):
        return self.point
