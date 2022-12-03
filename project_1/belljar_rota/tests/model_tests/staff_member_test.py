import unittest
from models.staff_member import Staffmember

class TestStaffMember(unittest.TestCase):

    def setUp(self):
        self.dave = Staffmember("Dave", 5)

    def test_staff_member_has_name(self):
        self.assertEqual(self.dave.name, "Dave")
    
    def test_staff_member_has_id(self):
        self.assertEqual(self.dave.id, 5)