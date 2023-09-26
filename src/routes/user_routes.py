from flask import Blueprint, render_template, request, flash
from src.routes.forms.mobile_form import ModifyMobileNumber

from src.services.user_services import UserService
from src.constants import constants

user_bp = Blueprint("users", __name__)


@user_bp.route("/create_user")
def create_user():
    return render_template('users/create_user.html')


@user_bp.route("/modify_user", methods=["GET", "POST"])
def modify_user():
    if request.method == 'POST':
        selected_action = request.form['users']
        if selected_action == constants.MOBILE_NUMBER:
            form = ModifyMobileNumber()
            return render_template('users/modify_mobile_number.html',
                                   name=None, mobile_number=None, form=form)
        if selected_action == constants.EMAIL:
            return render_template('users/modify_email.html')
        if selected_action == constants.DEPARTMENT:
            return render_template('users/modify_department.html')
    return render_template('users/modify_user.html')


@user_bp.route("/modify_mobile_number", methods=["POST"])
def modify_mobile_number():
    customer_id = None
    mobile_number = None
    form = ModifyMobileNumber()
    if form.validate_on_submit():
        customer_id = form.name.data
        mobile_number = form.mobile_number.data
        form.name.data = ''
        form.mobile_number.data = ''
        status = UserService.modify_mobile_number(customer_id, mobile_number)
        if status:
            flash(f"Updated  mobile number successfully", constants.SUCCESS)
        else:
            flash(f"Failed to updated number for user  {customer_id} ", constants.ERROR)
    return render_template('users/modify_mobile_number.html',
                           name=customer_id, mobile_number=mobile_number, form=form)
