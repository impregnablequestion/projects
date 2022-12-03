import pdb

from models.staff_member import Staffmember
from models.shift import Shift
import repositories.shift_repository as shifts
import repositories.staff_repository as staff

shifts.delete_all()
staff.delete_all()


dave = Staffmember("Dave")
lewis = Staffmember("Lewis")
sophie = Staffmember("Sophie")
hebe = Staffmember("Hebe")

staff.save(dave)
staff.save(lewis)
staff.save(sophie)
staff.save(hebe)

thu_close = Shift("close", "5-cl", 7.5, "Thu", dave)
thu_open = Shift("open", "10-6", 8.0, "Thu", sophie)

shifts.save(thu_close)
shifts.save(thu_open)



pdb.set_trace()