from db.run_sql import run_sql
from models.shift import Shift
from models.staff_member import Staffmember
import repositories.staff_repository as staff_repo

def save(shift):
    sql = """INSERT INTO shifts (type, times, hours, day, staff_id) 
    VALUES (%s, %s, %s, %s, %s) RETURNING *"""

    values = [shift.type, shift.times, shift.hours, shift.day, shift.staff_member.id]
    results = run_sql(sql, values)
    shift.id = results[0]['id']
    return shift

def update(shift):
    sql = "UPDATE shifts SET (type, times, hours, day, staff_id) = (%s, %s, %s, %s, %s) WHERE id=%s RETURNING *"
    values = [shift.type, shift.times, shift.hours, shift.day, shift.staff_member.id, shift.id]
    results = run_sql(sql, values)
    result = results[0]
    staff_member = staff_repo.select(result['staff_id'])
    shift = Shift(result['type'], result['times'], result['hours'], result['day'], staff_member, result['id'])
    return shift

def delete(id):
    sql = "DELETE FROM shifts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM shifts"
    run_sql(sql)

def select(id):
    shift = None

    sql = "SELECT * FROM shifts WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    result = results[0]
    staff_member = staff_repo.select(result['staff_id'])
    shift = Shift(result['type'], result['times'], result['hours'], result['day'], staff_member, result['id'])
    return shift

def select_all():
    shifts = []

    sql = "SELECT * FROM shifts"
    results = run_sql(sql)

    for row in results:
        staff_member = staff_repo.select(row['staff_id'])
        shift = Shift(row['type'], row['times'], row['hours'], row['day'], staff_member, row['id'])
        shifts.append(shift)
    return shifts