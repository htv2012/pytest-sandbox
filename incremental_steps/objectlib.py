class MyObject:
    def __init__(self):
        self.id = 1
        self.status = "created"

    def delete(self):
        self.status = "deleted"


def create_object():
    global OBJ
    OBJ = MyObject()
    return OBJ


def get_object(object_id):
    return OBJ
