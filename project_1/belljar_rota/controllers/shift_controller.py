from flask import Blueprint, render_template, redirect, request
import repositories.shift_repository as shift_repo
import repositories.staff_repository as staff_repo
from models.shift import Shift

shift_blueprint = Blueprint("shifts", __name__)

@shift_blueprint.route('/shifts/')
def show_rota_table_test():
    mon_shifts = shift_repo.shifts_by_day("Mon")
    tue_shifts = shift_repo.shifts_by_day("Tue")
    wed_shifts = shift_repo.shifts_by_day("Wed")
    thu_shifts = shift_repo.shifts_by_day("Thu")
    fri_shifts = shift_repo.shifts_by_day("Fri")
    sat_shifts = shift_repo.shifts_by_day("Sat")
    sun_shifts = shift_repo.shifts_by_day("Sun")

    return render_template(
        "shifts/rota.html",
        mon_shifts=mon_shifts,
        tue_shifts=tue_shifts,
        wed_shifts=wed_shifts,
        thu_shifts=thu_shifts,
        fri_shifts=fri_shifts,
        sat_shifts=sat_shifts,
        sun_shifts=sun_shifts
        )

@shift_blueprint.route('/shifts/shift/<id>')
def show_shift(id):
    shift = shift_repo.select(id)
    return render_template("shifts/shift.html", shift=shift)

@shift_blueprint.route('/shifts//<id>/edit')
def show_edit_shift(id):
    shift = shift_repo.select(id)
    staff = staff_repo.select_all()
    return render_template("shifts/edit_shift.html", shift=shift, staff=staff)

@shift_blueprint.route('/shifts/shift/<id>/edit', methods=["POST"])
def edit_shift(id):
    result = request.form
    type = result['type']
    times = result['times']
    hours = float(result['hours'])
    day = result['day']
    staff_id = result['staff_id']
    staff_member = staff_repo.select(staff_id)
    updated_shift = Shift(type, times, hours, day, staff_member, id)
    shift_repo.update(updated_shift)
    return redirect('/shifts/')

@shift_blueprint.route('/shifts/shift/<id>/delete', methods=["POST"])
def delete_shift(id):
    shift_repo.delete(id)
    return redirect('/shifts/')

@shift_blueprint.route("/shifts/create")
def show_create_shift():
    mon_shifts = shift_repo.shifts_by_day("Mon")
    tue_shifts = shift_repo.shifts_by_day("Tue")
    wed_shifts = shift_repo.shifts_by_day("Wed")
    thu_shifts = shift_repo.shifts_by_day("Thu")
    fri_shifts = shift_repo.shifts_by_day("Fri")
    sat_shifts = shift_repo.shifts_by_day("Sat")
    sun_shifts = shift_repo.shifts_by_day("Sun")
    staff = staff_repo.select_all()
    return render_template("shifts/create_rota.html",
    mon_shifts=mon_shifts,
    tue_shifts=tue_shifts,
    wed_shifts=wed_shifts,
    thu_shifts=thu_shifts,
    fri_shifts=fri_shifts,
    sat_shifts=sat_shifts,
    sun_shifts=sun_shifts,
    staff = staff)

@shift_blueprint.route("/shifts/create/post", methods = ["POST"])
def create_shift():
    result = request.form
    type = result['type']
    times = result['times']
    hours = float(result['hours'])
    day = result['day']
    staff_id = result['staff_id']
    staff_member = staff_repo.select(staff_id)
    shift = Shift(type, times, hours, day, staff_member)
    shift_repo.save(shift)
    return redirect("/shifts/create")

@shift_blueprint.route("/shifts/<day>")
def shifts_by_day(day):
    shifts = shift_repo.shifts_by_day(day)
    return render_template("shifts/shifts_by_day.html", shifts = shifts, day=day)
