import pdb

from models.staff_member import Staffmember
from models.shift import Shift
import repositories.shift_repository as shifts_repo
import repositories.staff_repository as staff_repo

shifts_repo.delete_all()
staff_repo.delete_all()

cover = Staffmember("None", 0, 40)
dave = Staffmember("Dave", 30, 40)
lewis = Staffmember("Lewis", 35, 45)
sophie = Staffmember("Sophie", 35, 45)
hebe = Staffmember("Hebe", 15, 30)
megan = Staffmember("Megan", 20, 40)
seamus = Staffmember("Seanus", 6, 12)
lili = Staffmember("Lilî", 15, 30)
kirsty = Staffmember("Kirsty", 0, 20)

staff_repo.save(cover)
staff_repo.save(dave)
staff_repo.save(lewis)
staff_repo.save(sophie)
staff_repo.save(hebe)
staff_repo.save(megan)
staff_repo.save(seamus)
staff_repo.save(lili)
staff_repo.save(kirsty)

mon_open = Shift("open", "10-6", 8, "Mon", cover)
tue_open = Shift("open", "10-6", 8, "Tue", cover)
wed_open = Shift("open", "10-6", 8, "Wed", cover)
thu_open = Shift("open", "10-6", 8, "Thu", cover)
fri_open = Shift("open", "10-6", 8, "Fri", cover)
sat_open = Shift("open", "10-6", 8, "Sat", cover)
sun_open = Shift("open", "10-6", 8, "Sun", cover)

mon_cross = Shift("cross", "12-9", 9, "Mon", cover)
thu_cross = Shift("cross", "12-9", 9, "Thu", cover)
sat_cross = Shift("cross", "12-9", 9, "Sat", cover)
sun_cross = Shift("cross", "12-9", 9, "Sun", cover)

mon_close1 = Shift("close", "5-12.30", 7.5, "Mon", cover)
tue_close1 = Shift("close", "5-12.30", 7.5, "Tue", cover)
wed_close1 = Shift("close", "5-12.30", 7.5, "Wed", cover)
thu_close1 = Shift("close", "5-12.30", 7.5, "Thu", cover)
fri_close1 = Shift("close", "4-12.30", 7.5, "Fri", cover)
sat_close1 = Shift("close", "4-12.30", 7.5, "Sat", cover)
sun_close1 = Shift("close", "5-12.30", 7.5, "Sun", cover)

mon_close2 = Shift("close", "6-12.30", 7.5, "Mon", cover)
tue_close2 = Shift("close", "6-12.30", 7.5, "Tue", cover)
wed_close2 = Shift("close", "5-12.30", 7.5, "Wed", cover)
thu_close2 = Shift("close", "5-12.30", 7.5, "Thu", cover)
fri_close2 = Shift("close", "5-12.30", 7.5, "Fri", cover)
sat_close2 = Shift("close", "5-12.30", 7.5, "Sat", cover)
sun_close2 = Shift("close", "5-12.30", 7.5, "Sun", cover)

fri_close3 = Shift("close", "6-12.30", 7.5, "Fri", cover)
sat_close3 = Shift("close", "6-12.30", 7.5, "Sat", cover)

shifts_repo.save(mon_open)
shifts_repo.save(tue_open)
shifts_repo.save(wed_open)
shifts_repo.save(thu_open)
shifts_repo.save(fri_open)
shifts_repo.save(sat_open)
shifts_repo.save(sun_open)

shifts_repo.save(mon_cross)
shifts_repo.save(thu_cross)
shifts_repo.save(sat_cross)
shifts_repo.save(sun_cross)

shifts_repo.save(mon_close1)
shifts_repo.save(tue_close1)
shifts_repo.save(wed_close1)
shifts_repo.save(thu_close1)
shifts_repo.save(fri_close1)
shifts_repo.save(sat_close1)
shifts_repo.save(sun_close1)

shifts_repo.save(mon_close2)
shifts_repo.save(tue_close2)
shifts_repo.save(wed_close2)
shifts_repo.save(thu_close2)
shifts_repo.save(fri_close2)
shifts_repo.save(sat_close2)
shifts_repo.save(sun_close2)

shifts_repo.save(fri_close3)
shifts_repo.save(sat_close3)









pdb.set_trace()