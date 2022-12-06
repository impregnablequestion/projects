class Staffmember:

    def __init__(self, name, min_hours, max_hours, id=None):
        self.name = name
        self.id = id
        self.min_hours = min_hours
        self.max_hours = max_hours