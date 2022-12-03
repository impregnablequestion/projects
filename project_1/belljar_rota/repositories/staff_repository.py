from db.run_sql import run_sql
from models.staff_member import Staffmember

def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql)

def save(staff_member):
    sql = "INSERT INTO staff ( name ) VALUES ( %s ) RETURNING *"
    values = [staff_member.name]
    results = run_sql(sql, values)
    staff_member.id = results[0]['id']
    return staff_member