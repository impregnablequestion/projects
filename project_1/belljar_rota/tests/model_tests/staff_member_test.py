import unittest
from models.staff_member import Staffmember

class TestStaffMember(unittest.TestCase):

    def setUp(self):
        self.dave = Staffmember("Dave", 10, 40, False, 5)

    def test_staff_member_has_name(self):
        self.assertEqual(self.dave.name, "Dave")
    
    def test_staff_member_has_id(self):
        self.assertEqual(self.dave.id, 5)

    def test_staff_member_has_min_hours(self):
        self.assertEqual(self.dave.min_hours, 10)

    def test_staff_member_has_max_hours(self):
        self.assertEqual(self.dave.max_hours, 40)

    def test_staff_member_happy_with_hours(self):
        hours = 20
        self.dave.check_happy_with(hours)
        output = self.dave.happy
        self.assertEqual(output, True)
