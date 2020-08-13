
class Request:
    def __init__(self, id, first, last, message, admin=False):
        self.id = id
        self.name = first + last
        self.message = message
        self._admin = admin
        self.city = None


def cityChoice():


def answer(req):
    if