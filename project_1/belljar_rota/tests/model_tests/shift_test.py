import unittest
from models.shift import Shift
from models.staff_member import Staffmember

class TestShift(unittest.TestCase):

    def setUp(self):
        self.dave = Staffmember("Dave", 3)
        self.thu_close = Shift("close", "5-12.30", 7.5, "Thu", self.dave, 4)
        
    def test_shift_has_type(self):
        self.assertEqual(self.thu_close.type, "close")

    def test_shift_has_times(self):
        self.assertEqual(self.thu_close.times, "5-12.30")

    def test_shift_has_hours(self):
        self.assertEqual(self.thu_close.hours, 7.5)

    def test_shift_has_day(self):
        self.assertEqual(self.thu_close.day, "Thu")

    def test_shift_has_staff_member(self):
        self.assertEqual(self.thu_close.staff_member.name, self.dave.name)

    def test_shift_has_id(self):
        self.assertEqual(self.thu_close.id, 4)



