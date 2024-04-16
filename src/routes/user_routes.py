from flask import Blueprint, render_template, request, flash, redirect, url_for
from src.routes.forms.mobile_form import ModifyMobileNumber
from src.routes.forms.search_form import SearchForm
from src.routes.forms.guest_form import GuestForm

from src.services.user_services import UserService
from src.constants import constants

user_bp = Blueprint("users", __name__)


@user_bp.route("/create_user")
def create_user():
    return render_template('users/create_user.html')


@user_bp.route("/modify_user", methods=["GET", "POST"])
def modify_user():
    if request.method == 'POST':
        selected_action = request.form['action']
        if selected_action == constants.MOBILE_NUMBER:
            form = ModifyMobileNumber()
            return render_template('users/modify_mobile_number.html',
                                   name=None, mobile_number=None, form=form)
        if selected_action == constants.DELETE_GUEST_USER:
            form = GuestForm()
            return render_template('users/delete_guest_user.html',
                                   name=None, form=form)
        if selected_action == constants.NAME:
            form = SearchForm()
            return render_template('users/modify_name.html',
                                   name=None, form=form)
        if selected_action == constants.ROLES:
            return render_template('users/modify_roles.html')
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


@user_bp.route("/delete_guest_user", methods=['GET', 'POST'])
def delete_guest_user():
    users_list = []
    form = GuestForm()
    # user_id = request.args.get('user_id')
    if form.validate_on_submit():
        user_id = form.name.data
        users_list = UserService.get_user_list(user_id=user_id)
        # users_list = [{'user_login_id': '200000235565', 'customer_id': 'SUSE 15.4 - M1 Small (2vCPU 4 GB RAM)',
        #                'status': 'bharat1.agarwal@ril.com', 'action_type_code': 'Provisioning',
        #                'error': 'Exception({\'message\': \'AssertionError\', \'output\': ["An error occurred while opening the clustered role \'testsusebh999\'.\\nScript Failed:- VM: testsusebh999 doesn\'t exist..Exception.InnerException.Message"]})',
        #                'created_on': '2023-10-20 18:48:08'}]
        # if status:
        #     flash(f"Deleted user {user_id} successfully", constants.SUCCESS)
        # else:
        #     flash(f"Failed to delete  {user_id} ", constants.ERROR)

    return render_template('users/delete_guest_user.html', form=form, users_list=users_list)


@user_bp.route("/delete_users", methods=["POST"])
def delete_users():
    # if request.method == "POST":
    for getid in request.form.getlist('mycheckbox'):
        print(getid)
        status = UserService.delete_guest_user(user_id=getid)
        # status = True
        if status:
            flash(f"Deleted {getid} successfully", constants.SUCCESS)
        else:
            flash(f"Failed to delete user {getid} ", constants.ERROR)
    # user_id = request.args.get('user_id')
    return redirect('/delete_guest_user')


@user_bp.route("/modify_name", methods=['GET', 'POST'])
def modify_name():
    users_list = []
    form = SearchForm()
    user_id = request.args.get('user_id')
    print(user_id)
    if form.validate_on_submit():
        user_id = form.name.data
        users_list = UserService.get_user_name(user_id=user_id)
        users_list = [{'user_log_id': '200000235565', 'customer_id': 'himanshu is a superman'}]
        # if status:
        #     flash(f"Deleted user {user_id} successfully", constants.SUCCESS)
        # else:
        #     flash(f"Failed to delete  {user_id} ", constants.ERROR)

    return render_template('users/modify_name.html', form=form, users_list=users_list)


@user_bp.route("/update_name", methods=["POST"])
def update_name():
    # if request.method == "POST":
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    middle_name = request.form['middle_name']
    customer_id = request.form['customer_id']
    print(first_name)
    print(middle_name)
    print(last_name)
    print(customer_id)
    status = UserService.update_name(customer_id=customer_id, first_name=first_name,middle_name=middle_name,
                                     last_name=last_name)
    #status = True
    if status:
        flash(f"Updated {customer_id} successfully", constants.SUCCESS)
    else:
        flash(f"Failed to update user {customer_id} ", constants.ERROR)
    return redirect('/modify_name')
