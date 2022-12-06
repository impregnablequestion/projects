from db.run_sql import run_sql
from models.staff_member import Staffmember

def save(staff_member):
    sql = "INSERT INTO staff (name, min_hours, max_hours, happy) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [staff_member.name, staff_member.min_hours, staff_member.max_hours, staff_member.happy]
    results = run_sql(sql, values)
    staff_member.id = results[0]['id']
    return staff_member

def update(staff_member):
    sql = "UPDATE staff SET (name, min_hours, max_hours) = (%s, %s, %s, %s) WHERE id = %s RETURNING *"
    values = [staff_member.name, staff_member.min_hours, staff_member.max_hours, staff_member.happy, staff_member.id]
    run_sql(sql, values)
    return staff_member


def select(id):
    staff_member = None
    
    sql = "SELECT * FROM staff WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    result = results[0]
    staff_member = Staffmember(result["name"], result["min_hours"], result["max_hours"], result['happy'], result["id"])
    return staff_member

def select_by_name(name):
    sql = "SELECT * FROM staff WHERE name = %s"
    values = [name]
    results = run_sql(sql, values)
    result = results[0]
    staff_member = Staffmember(result["name"], result["min_hours"], result["max_hours"], result['happy'], result["id"])
    return staff_member

def select_all():
    staff = []

    sql = "SELECT * FROM staff"
    results = run_sql(sql)
    for row in results:
        staff_member = Staffmember(row["name"], row["min_hours"], row["max_hours"], row['happy'], row["id"])
        staff.append(staff_member) 
    return staff

def delete(id):   
    sql = "DELETE FROM staff WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql)