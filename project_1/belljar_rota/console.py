import pdb

from models.staff_member import Staffmember
from models.shift import Shift
import repositories.shift_repository as shifts_repo
import repositories.staff_repository as staff_repo

shifts_repo.delete_all()
staff_repo.delete_all()


dave = Staffmember("Dave")
lewis = Staffmember("Lewis")
sophie = Staffmember("Sophie")
hebe = Staffmember("Hebe")

staff_repo.save(dave)
staff_repo.save(lewis)
staff_repo.save(sophie)
staff_repo.save(hebe)

found = staff_repo.select(dave.id)

thu_close = Shift("close", "5-cl", 7.5, "Thu", dave)
thu_open = Shift("open", "10-6", 8.0, "Thu", sophie)
wed_open = Shift("open", "10-6", 8, "Wed", sophie)

shifts_repo.save(thu_close)
shifts_repo.save(thu_open)
shifts_repo.save(wed_open)

# found = shifts_repo.shifts_by_staff_member(sophie.id)
# found.sort(key=lambda p: p.day)

found = shifts_repo.shifts_by_day("Thu")

pdb.set_trace()