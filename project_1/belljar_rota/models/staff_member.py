class Staffmember:

    def __init__(self, name, min_hours, max_hours, happy=False, id=None):
        self.name = name
        self.id = id
        self.min_hours = min_hours
        self.max_hours = max_hours
        self.happy = happy

    def check_happy_with(self, hours):
        if hours < self.max_hours and hours > self.min_hours:
            self.happy = True
        else:
            self.happy = False