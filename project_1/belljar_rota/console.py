import pdb

from models.staff_member import Staffmember
from models.shift import Shift
import repositories.shift_repository as shifts
import repositories.staff_repository as staff

staff.delete_all()

dave = Staffmember("Dave")
found = staff.save(dave)

pdb.set_trace()