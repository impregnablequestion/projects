from flask import Blueprint, render_template, request, redirect
import repositories.staff_repository as staff_repo
import repositories.shift_repository as shift_repo
from models.staff_member import Staffmember

staff_blueprint = Blueprint("staff", __name__)

@staff_blueprint.route('/staff/')
def staff_index():
    staff = staff_repo.select_all()
    return render_template("staff/staff.html", staff=staff)

@staff_blueprint.route('/staff/create')
def show_create_staff():
    return render_template("staff/create_staff.html")

@staff_blueprint.route('/staff/', methods=['POST'])
def create_staff_member():
    result = request.form
    name = result['name']
    new_staff = Staffmember(name)
    staff_repo.save(new_staff)
    return redirect('/staff')

@staff_blueprint.route('/staff/<id>')
def show_staff_member(id):
    staff_member = staff_repo.select(id)
    return render_template("staff/staff_member.html", staff_member=staff_member)

@staff_blueprint.route('/staff/<id>/delete', methods=['POST'])
def delete_staff_member(id):
    staff_repo.delete(id)
    return redirect('/staff')

# add an "are you sure" intermediate page to make it less easy to just delete members of staff

@staff_blueprint.route("/staff/<id>/edit")
def show_edit_screen(id):
    staff_member = staff_repo.select(id)
    return render_template("staff/edit.html", staff_member=staff_member)

@staff_blueprint.route("/staff/edit/<id>", methods=["POST"])
def edit_staff_member(id):
    result=request.form
    updated_sm = Staffmember(result['name'], id)
    staff_repo.update(updated_sm)
    return redirect('/staff')

@staff_blueprint.route("/staff/<id>/shifts")
def show_shifts_by_staff(id):
    staff_member = staff_repo.select(id)
    shifts = shift_repo.shifts_by_staff_member(id)
    return render_template(
        "staff/shifts_by_staff.html", staff_member = staff_member, shifts = shifts
        )
