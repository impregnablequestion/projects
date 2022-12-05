from flask import Blueprint, render_template, redirect, request
import repositories.shift_repository as shift_repo
import repositories.staff_repository as staff_repo
from models.shift import Shift

shift_blueprint = Blueprint("shifts", __name__)

@shift_blueprint.route('/shifts/')
def show_rota():
    shifts = shift_repo.select_all()
    return render_template("shifts/rota.html", shifts = shifts)

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
    shifts = shift_repo.select_all()
    staff = staff_repo.select_all()
    return render_template("shifts/create_rota.html", shifts = shifts, staff = staff)

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

