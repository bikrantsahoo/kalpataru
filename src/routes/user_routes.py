from flask import Blueprint, render_template, request, flash, redirect, url_for
from src.routes.forms.search_form import SearchForm
from src.routes.forms.guest_form import GuestForm
from src.routes.forms.user_mail_form import UserMailForm
from src.routes.forms.pincode_form import PincodeForm

from src.services.user_services import UserService
from src.constants import constants
import subprocess

user_bp = Blueprint("users", __name__)


@user_bp.route("/create_user")
def create_user():
    return render_template('users/create_user.html')


@user_bp.route("/modify_user", methods=["GET", "POST"])
def modify_user():
    if request.method == 'POST':
        selected_action = request.form['action']
        if selected_action == constants.MOBILE_NUMBER:
            form = GuestForm()
            return render_template('users/modify_mobile_number.html',
                                   name=None, form=form)
        if selected_action == constants.DELETE_GUEST_USER:
            form = GuestForm()
            return render_template('users/delete_guest_user.html',
                                   name=None, form=form)
        if selected_action == constants.NAME:
            form = SearchForm()
            return render_template('users/modify_name.html',
                                   name=None, form=form)
        # if selected_action == constants.ROLES:
        #     return render_template('users/modify_roles.html')
        if selected_action == constants.EMAIL:
            form = GuestForm()
            return render_template('users/modify_email.html',
                                   name=None, form=form)
        # if selected_action == constants.DEPARTMENT:
        #     return render_template('users/modify_department.html')
    return render_template('users/modify_user.html')


@user_bp.route("/modify_mobile_number", methods=["POST", "GET"])
def modify_mobile_number():
    users_list = []
    form = GuestForm()
    if form.validate_on_submit():
        user_id = form.name.data
        #users_list = UserService.get_user_name(user_id=user_id)
        users_list = [{'user_log_id': 'somu@ril.com', 'customer_id': 'SUSE 15.4 - M1 Small (2vCPU 4 GB RAM)',
                       'status': 'bharat1.agarwal@ril.com', 'action_type_code': 'Provisioning',
                       'error': 'Exception({\'message\': \'AssertionError\', \'output\': ["An error occurred while opening the clustered role \'testsusebh999\'.\\nScript Failed:- VM: testsusebh999 doesn\'t exist..Exception.InnerException.Message"]})',
                       'created_on': '2023-10-20 18:48:08'}]
    return render_template('users/modify_mobile_number.html', form=form, users_list=users_list)

@user_bp.route("/update_mobile_number", methods=["POST"])
def update_mobile_number():
    # if request.method == "POST":
    new_mobile_number = request.form['new_mobile_number']
    customer_id = request.form['customer_id']
    print(len(new_mobile_number))
    print(len(new_mobile_number))

    if len(new_mobile_number) == 0:
        flash(f"Check mobile number", constants.WARNING)
        return redirect("/modify_mobile_number")
    status = UserService.update_mobile_number(customer_id=customer_id,new_mobile_number=new_mobile_number)
    status = True
    if status:
        flash(f"Updated email successfully", constants.SUCCESS)
    else:
        flash(f"Failed to update email  ", constants.ERROR)
    return redirect('/modify_mobile_number')

@user_bp.route("/delete_guest_user", methods=['GET', 'POST'])
def delete_guest_user():
    users_list = []
    form = GuestForm()
    # user_id = request.args.get('user_id')
    if form.validate_on_submit():
        user_id = form.name.data
        users_list = UserService.get_user_list(user_id=user_id)
        # users_list = [{'user_log_id': '200000235565', 'customer_id': 'SUSE 15.4 - M1 Small (2vCPU 4 GB RAM)',
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

@user_bp.route("/modify_email", methods=['GET', 'POST'])
def modify_email():
    users_list = []
    form = GuestForm()
    # user_id = request.args.get('user_id')
    if form.validate_on_submit():
        user_id = form.name.data
        users_list = UserService.get_user_name(user_id=user_id)
        # users_list = [{'user_log_id': 'somu@ril.com', 'customer_id': 'SUSE 15.4 - M1 Small (2vCPU 4 GB RAM)',
        #                'status': 'bharat1.agarwal@ril.com', 'action_type_code': 'Provisioning',
        #                'error': 'Exception({\'message\': \'AssertionError\', \'output\': ["An error occurred while opening the clustered role \'testsusebh999\'.\\nScript Failed:- VM: testsusebh999 doesn\'t exist..Exception.InnerException.Message"]})',
        #                'created_on': '2023-10-20 18:48:08'}]
    return render_template('users/modify_email.html', form=form, users_list=users_list)

@user_bp.route("/update_email", methods=["POST"])
def update_email():
    # if request.method == "POST":
    new_email_id = request.form['new_email']
    old_mail_id = request.form['customer_id']
    print(new_email_id)
    print(old_mail_id)
    status = UserService.update_email(old_mail_id=old_mail_id, new_email_id=new_email_id)
    status = True
    if status:
        flash(f"Updated email successfully", constants.SUCCESS)
    else:
        flash(f"Failed to update email  ", constants.ERROR)
    return redirect('/modify_email')

@user_bp.route("/modify_name", methods=['GET', 'POST'])
def modify_name():
    users_list = []
    form = SearchForm()
    user_id = request.args.get('user_id')
    print(user_id)
    if form.validate_on_submit():
        user_id = form.name.data
        users_list = UserService.get_user_name(user_id=user_id)
        #users_list = [{'user_log_id': '200000235565', 'customer_id': 'himanshu is a superman'}]
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
    status = UserService.update_name(customer_id=customer_id, first_name=first_name, middle_name=middle_name,
                                     last_name=last_name)
    # status = True
    if status:
        flash(f"Updated {customer_id} successfully", constants.SUCCESS)
    else:
        flash(f"Failed to update user {customer_id} ", constants.ERROR)
    return redirect('/modify_name')

@user_bp.route("/add_pincode", methods=["GET", "POST"])
def add_pincode():
    name = None
    form = PincodeForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        if request.method == "POST":
            pincode = request.form.get("name")
            print(pincode)
            # TODO: check and remove this condition check after few days
            #status = UserService.add_pincode(pincode=pincode)
            status = False
            if status:
                flash(f"Inserted {pincode} successfully", constants.SUCCESS)
            else:
                flash(f"Failed to insert pincode {pincode} ", constants.ERROR)
    return render_template('alerts/delete.html', name=name, form=form)


@user_bp.route("/approver_dump", methods=["GET", "POST"])
def approver_hierarchy_mapping():
    name = None
    form = UserMailForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        if request.method == "POST":
            email_string_list = request.form.get("name")
            # emails = [f"{email.strip()}" for email in email_string_list.split(',')]
            # # print(email_list)
            # emails_str = ', '.join(emails)
            # print(email_string_list)
            # print(emails_str)
            result = subprocess.run(["python3", constants.ETL, constants.APPROVER_HIERARCHY_MAPPING_PATH,
                                     constants.AHM_SUBJECT, email_string_list], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            flash(f"mail sent to {email_string_list} successfully", constants.SUCCESS)
    return render_template('users/user_mail.html', name=name, form=form)


# this code used for select date range and include all
# def order_milestone():
#     milestones_data = []
#     name = None
#     form = UserDateForm()
#     print(request.method)
#     if request.method == "POST":
#         # if form.validate_on_submit():
#             if not form.include_all_dates.data:
#                 start_date = form.startdate.data
#                 end_date = form.enddate.data
#                 date_difference = (end_date - start_date).days
#                 if date_difference < 0:
#                     flash('End date must be after the start date.', constants.WARNING)
#                 elif date_difference > 10:
#                     flash('Date range should not exceed 10 days.', constants.WARNING)
#                 else:
#                     milestones_data = [{'order_number': '200000235565', 'product_name': 'SUSE 15.4 - M1 Small (2vCPU 4 GB RAM)', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Provisioning', 'error': 'Exception({\'message\': \'AssertionError\', \'output\': ["An error occurred while opening the clustered role \'testsusebh999\'.\\nScript Failed:- VM: testsusebh999 doesn\'t exist..Exception.InnerException.Message"]})', 'created_on': '2023-10-20 18:48:08'}, {'order_number': '200000235584', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-20 17:52:53'}, {'order_number': '200000235583', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Out object is missing in the callback Response', 'created_on': '2023-10-20 17:34:08'}, {'order_number': '200000235563', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Out object is missing in the callback Response', 'created_on': '2023-10-20 17:23:14'}, {'order_number': '200000235582', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-20 16:56:53'}, {'order_number': '200000235581', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-20 16:48:49'}, {'order_number': '200000235562', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Out object is missing in the callback Response', 'created_on': '2023-10-20 16:24:32'}, {'order_number': '200000235561', 'product_name': 'Radware LoadBalancer', 'created_by': 'achintya.gupta@nic.in', 'milestone': 'CMDB_SYNC', 'error': 'Operation failed for externalResourceId: confonet2', 'created_on': '2023-10-20 15:47:18'}, {'order_number': '200000235560', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Provisioning', 'error': "Exception({'message': 'AssertionError', 'output': ['Script Failed:- You cannot call a method on a null-valued expression..Exception.InnerException.Message']})", 'created_on': '2023-10-20 14:50:02'}, {'order_number': '200000235558', 'product_name': 'Radware LoadBalancer', 'created_by': 'achintya.gupta@nic.in', 'milestone': 'Provisioning', 'error': 'CUENET exception[Exception({\'message\': "Unable to route task beacuse of exception[Exception(\'No platform mapped to target[https://10.166.70.76] for custid[636] and subid[5165]\')]"})] occurred while processing request!', 'created_on': '2023-10-20 11:20:04'}, {'order_number': '200000235558', 'product_name': 'Radware LoadBalancer', 'created_by': 'achintya.gupta@nic.in', 'milestone': 'Provisioning', 'error': 'CUENET exception[Exception({\'message\': "Unable to route task beacuse of exception[Exception(\'No platform mapped to target[https://10.166.70.76] for custid[636] and subid[5165]\')]"})] occurred while processing request!', 'created_on': '2023-10-20 12:50:51'}, {'order_number': '200000235571', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 4vCPU 16 GB and 1 W-4vCPU 16 GB)', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'K8PostProvisioningAction', 'error': 'com.jio.ngo.common.exception.ServiceException: please check the Template. could not replace all template fields\n\tat com.jio.hcmp.workflow.delegate.nodeworkflow.BuildRequest.validateRequest(BuildRequest.java:169)\n\tat com.jio.hcmp.workflow.delegate.nodeworkflow.BuildRequest.execute(BuildRequest.java:138)\n\tat org.camunda.bpm.engine.impl.bpmn.delegate.JavaDelegateInvocation.invoke(JavaDelegateInvocation.java:40)\n\tat org.camunda.bpm.engine.impl.delegate.DelegateInvocation.proceed(DelegateInvocation.java:58)\n\tat org.camunda.bpm.engine.impl.delegate.DefaultDelegateInterceptor.handleInvocationInContext(DefaultDelegateInterceptor.java:92)\n\tat org.camunda.bpm.engine.impl.delegate.DefaultDelegateInterceptor.handleInvocation(DefaultDelegateInterceptor.java:63)\n\tat org.camunda.bpm.engine.impl.bpmn.behavior.ServiceTaskJavaDelegateActivityBehavior.execute(ServiceTaskJavaDelegateActivityBehavior.java:55)\n\tat org.camunda.bpm.engine.impl.bpmn.behavior.ServiceTaskJavaDelegateActivityBehavior.performEx...', 'created_on': '2023-10-19 21:20:06'}, {'order_number': '200000235570', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Out object is missing in the callback Response', 'created_on': '2023-10-19 20:49:35'}, {'order_number': '200000235555', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 4vCPU 16 GB and 1 W-4vCPU 16 GB)', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Provisioning', 'error': "Exception({'message': 'AssertionError', 'output': ['Script Failed:- You cannot call a method on a null-valued expression..Exception.InnerException.Message']})", 'created_on': '2023-10-19 20:34:44'}, {'order_number': '200000235549', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-19 20:26:44'}, {'order_number': '200000235547', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 4vCPU 16 GB and 1 W-4vCPU 16 GB)', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Provisioning', 'error': 'Exception(\'Exception({\\\'message\\\': "== \\\'True\\\'", \\\'output\\\': [\\\'\\\\nAn error occurred: timed out\\\\nAn error occurred: timed out\\\\nAn error occurred: timed out\\\\nAn error occurred: timed out\\\']})\')', 'created_on': '2023-10-19 19:02:12'}, {'order_number': '200000235546', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Security_Agent', 'error': 'Out object is missing in the callback Response', 'created_on': '2023-10-19 18:44:15'}, {'order_number': '200000235545', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Security_Agent', 'error': 'Out object is missing in the callback Response', 'created_on': '2023-10-19 18:22:36'}, {'order_number': '200000235544', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-19 18:12:07'}, {'order_number': '200000235553', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-19 17:22:02'}, {'order_number': '200000235552', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-19 16:57:50'}, {'order_number': '200000235551', 'product_name': 'RHEL 7.9 – single master/worker (1 M- 4vCPU 8 GB and 1 W-4vCPU 8 GB)', 'created_by': 'adarsh.rai@nic.in', 'milestone': 'Provisioning', 'error': "SystemExit(b'Quota exceeded for cores: Requested 4, but already used 100 of 100 cores (HTTP 403) (Request-ID: req-addbfade-170b-4d42-a939-eee4c6bc4618)\\n')", 'created_on': '2023-10-19 14:48:48'}, {'order_number': '200000235550', 'product_name': 'SUSE 15.4 - M1 Small (2vCPU 4 GB RAM)', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Provisioning', 'error': 'Exception({\'message\': \'AssertionError\', \'output\': ["An error occurred while opening the clustered role \'CPecourttest\'.\\nScript Failed:- VM: CPecourttest doesn\'t exist..Exception.InnerException.Message"]})', 'created_on': '2023-10-19 13:38:47'}, {'order_number': '200000235541', 'product_name': 'SUSE 15.4 - M1 Small (2vCPU 4 GB RAM)', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Provisioning', 'error': 'Exception({\'message\': \'AssertionError\', \'output\': ["An error occurred while opening the clustered role \'CPTest19100131\'.\\nScript Failed:- VM: CPTest19100131 doesn\'t exist..Exception.InnerException.Message"]})', 'created_on': '2023-10-19 13:33:28'}, {'order_number': '200000235529', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-19 13:26:28'}, {'order_number': '200000235527', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 16vCPU 64 GB and 1 W-16vCPU 64 GB)', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'K8PostProvisioningAction', 'error': 'com.jio.ngo.common.exception.ServiceException: please check the Template. could not replace all template fields\n\tat com.jio.hcmp.workflow.delegate.nodeworkflow.BuildRequest.validateRequest(BuildRequest.java:169)\n\tat com.jio.hcmp.workflow.delegate.nodeworkflow.BuildRequest.execute(BuildRequest.java:138)\n\tat org.camunda.bpm.engine.impl.bpmn.delegate.JavaDelegateInvocation.invoke(JavaDelegateInvocation.java:40)\n\tat org.camunda.bpm.engine.impl.delegate.DelegateInvocation.proceed(DelegateInvocation.java:58)\n\tat org.camunda.bpm.engine.impl.delegate.DefaultDelegateInterceptor.handleInvocationInContext(DefaultDelegateInterceptor.java:92)\n\tat org.camunda.bpm.engine.impl.delegate.DefaultDelegateInterceptor.handleInvocation(DefaultDelegateInterceptor.java:63)\n\tat org.camunda.bpm.engine.impl.bpmn.behavior.ServiceTaskJavaDelegateActivityBehavior.execute(ServiceTaskJavaDelegateActivityBehavior.java:55)\n\tat org.camunda.bpm.engine.impl.bpmn.behavior.ServiceTaskJavaDelegateActivityBehavior.performEx...', 'created_on': '2023-10-19 12:35:18'}, {'order_number': '200000235526', 'product_name': 'Ubuntu Debian11 (OpenSource) (22.04 LTS) - 8 vCPU, 32 GB RAM, 100 GB OS Disk', 'created_by': 'rc.chebolu@nic.in', 'milestone': 'Provisioning', 'error': "SystemExit(b'Quota exceeded for cores: Requested 8, but already used 100 of 100 cores (HTTP 403) (Request-ID: req-2ae2d2c5-ff74-4c3c-bc30-05e6060d1d93)\\n')", 'created_on': '2023-10-19 12:16:03'}, {'order_number': '200000235525', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 16vCPU 64 GB and 1 W-16vCPU 64 GB)', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Provisioning', 'error': 'Exception({\'stdout\': "Transaction directory created.\\n### True\\nCluster execution failed with error: Docker installation failed on 10.192.70.198 server with error: http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nError: Package: docker-ce-rootless-extras-20.10.2-3.el7.x86_64 (DOCKERRPM)\\n           Requires: fuse-overlayfs >= 0.7\\nError: Package: 3:docker-ce-20.10.2-3.el7.x86_64 (DOCKERRPM)\\n           Requires: container-sel', 'created_on': '2023-10-19 12:03:30'}, {'order_number': '200000235539', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 16vCPU 64 GB and 1 W-16vCPU 64 GB)', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Provisioning', 'error': 'ConnectionError(MaxRetryError(\'HTTPConnectionPool(host=\\\'jio-hcmp-cuenet-gateway.jio-hcmp-cloudorch\\\', port=8084): Max retries exceeded with url: /v1/blueprint/?bid=235457&identifier=1 (Caused by NameResolutionError("<urllib3.connection.HTTPConnection object at 0x7fa2921e6730>: Failed to resolve \\\'jio-hcmp-cuenet-gateway.jio-hcmp-cloudorch\\\' ([Errno -2] Name or service not known)"))\'))', 'created_on': '2023-10-19 11:30:38'}, {'order_number': '200000235524', 'product_name': 'Ubuntu Debian11 (OpenSource) (22.04 LTS) - 8 vCPU, 32 GB RAM, 100 GB OS Disk', 'created_by': 'rc.chebolu@nic.in', 'milestone': 'Provisioning', 'error': "SystemExit(b'Quota exceeded for cores: Requested 8, but already used 100 of 100 cores (HTTP 403) (Request-ID: req-09d621af-ca8f-4fdf-b749-feaf9127babe)\\n')", 'created_on': '2023-10-19 11:10:27'}, {'order_number': '200000235537', 'product_name': 'Ubuntu Debian11 (OpenSource) (22.04 LTS) - 8 vCPU, 32 GB RAM, 100 GB OS Disk', 'created_by': 'rc.chebolu@nic.in', 'milestone': 'Provisioning', 'error': "SystemExit(b'Quota exceeded for cores: Requested 8, but already used 100 of 100 cores (HTTP 403) (Request-ID: req-418dada1-f01b-450e-8e1f-e9e4d51d618f)\\n')", 'created_on': '2023-10-19 11:06:08'}, {'order_number': '200000235536', 'product_name': 'Debian11-postgresql-15.2.0 - 32 vCPU, 128 GB RAM', 'created_by': 'adarsh.rai@nic.in', 'milestone': 'Provisioning', 'error': "SystemExit(b'Quota exceeded for cores: Requested 32, but already used 100 of 100 cores (HTTP 403) (Request-ID: req-464342b5-6486-4059-995e-d371e4292352)\\n')", 'created_on': '2023-10-19 10:03:45'}, {'order_number': '200000235535', 'product_name': 'Debian11-mysql-8.0.32 - 32 vCPU, 128 GB RAM', 'created_by': 'adarsh.rai@nic.in', 'milestone': 'Provisioning', 'error': "SystemExit(b'Quota exceeded for cores: Requested 32, but already used 100 of 100 cores (HTTP 403) (Request-ID: req-0cfea24a-22ce-4261-8f19-7f821b03aacd)\\n')", 'created_on': '2023-10-19 10:03:51'}, {'order_number': '200000235533', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 4vCPU 16 GB and 1 W-4vCPU 16 GB)', 'created_by': 'amar7.yadav@ril.com', 'milestone': 'Provisioning', 'error': "CUENET exception[Exception('unable to complete task[951d2054fec247c3a927a32029ef599c] requested timeline!')] occurred while processing request!", 'created_on': '2023-10-19 00:21:55'}]
#             else:
#                 # If include_all checkbox is checked, fetch all data
#                 milestones_data = [{'order_number': '200000235565', 'product_name': 'SUSE 15.4 - M1 Small (2vCPU 4 GB RAM)', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Provisioning', 'error': 'Exception({\'message\': \'AssertionError\', \'output\': ["An error occurred while opening the clustered role \'testsusebh999\'.\\nScript Failed:- VM: testsusebh999 doesn\'t exist..Exception.InnerException.Message"]})', 'created_on': '2023-10-20 18:48:08'}, {'order_number': '200000235584', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-20 17:52:53'}, {'order_number': '200000235583', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Out object is missing in the callback Response', 'created_on': '2023-10-20 17:34:08'}, {'order_number': '200000235563', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Out object is missing in the callback Response', 'created_on': '2023-10-20 17:23:14'}, {'order_number': '200000235582', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-20 16:56:53'}, {'order_number': '200000235581', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-20 16:48:49'}, {'order_number': '200000235562', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Out object is missing in the callback Response', 'created_on': '2023-10-20 16:24:32'}, {'order_number': '200000235561', 'product_name': 'Radware LoadBalancer', 'created_by': 'achintya.gupta@nic.in', 'milestone': 'CMDB_SYNC', 'error': 'Operation failed for externalResourceId: confonet2', 'created_on': '2023-10-20 15:47:18'}, {'order_number': '200000235560', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Provisioning', 'error': "Exception({'message': 'AssertionError', 'output': ['Script Failed:- You cannot call a method on a null-valued expression..Exception.InnerException.Message']})", 'created_on': '2023-10-20 14:50:02'}, {'order_number': '200000235558', 'product_name': 'Radware LoadBalancer', 'created_by': 'achintya.gupta@nic.in', 'milestone': 'Provisioning', 'error': 'CUENET exception[Exception({\'message\': "Unable to route task beacuse of exception[Exception(\'No platform mapped to target[https://10.166.70.76] for custid[636] and subid[5165]\')]"})] occurred while processing request!', 'created_on': '2023-10-20 11:20:04'}, {'order_number': '200000235558', 'product_name': 'Radware LoadBalancer', 'created_by': 'achintya.gupta@nic.in', 'milestone': 'Provisioning', 'error': 'CUENET exception[Exception({\'message\': "Unable to route task beacuse of exception[Exception(\'No platform mapped to target[https://10.166.70.76] for custid[636] and subid[5165]\')]"})] occurred while processing request!', 'created_on': '2023-10-20 12:50:51'}, {'order_number': '200000235571', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 4vCPU 16 GB and 1 W-4vCPU 16 GB)', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'K8PostProvisioningAction', 'error': 'com.jio.ngo.common.exception.ServiceException: please check the Template. could not replace all template fields\n\tat com.jio.hcmp.workflow.delegate.nodeworkflow.BuildRequest.validateRequest(BuildRequest.java:169)\n\tat com.jio.hcmp.workflow.delegate.nodeworkflow.BuildRequest.execute(BuildRequest.java:138)\n\tat org.camunda.bpm.engine.impl.bpmn.delegate.JavaDelegateInvocation.invoke(JavaDelegateInvocation.java:40)\n\tat org.camunda.bpm.engine.impl.delegate.DelegateInvocation.proceed(DelegateInvocation.java:58)\n\tat org.camunda.bpm.engine.impl.delegate.DefaultDelegateInterceptor.handleInvocationInContext(DefaultDelegateInterceptor.java:92)\n\tat org.camunda.bpm.engine.impl.delegate.DefaultDelegateInterceptor.handleInvocation(DefaultDelegateInterceptor.java:63)\n\tat org.camunda.bpm.engine.impl.bpmn.behavior.ServiceTaskJavaDelegateActivityBehavior.execute(ServiceTaskJavaDelegateActivityBehavior.java:55)\n\tat org.camunda.bpm.engine.impl.bpmn.behavior.ServiceTaskJavaDelegateActivityBehavior.performEx...', 'created_on': '2023-10-19 21:20:06'}, {'order_number': '200000235570', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Out object is missing in the callback Response', 'created_on': '2023-10-19 20:49:35'}, {'order_number': '200000235555', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 4vCPU 16 GB and 1 W-4vCPU 16 GB)', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Provisioning', 'error': "Exception({'message': 'AssertionError', 'output': ['Script Failed:- You cannot call a method on a null-valued expression..Exception.InnerException.Message']})", 'created_on': '2023-10-19 20:34:44'}, {'order_number': '200000235549', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'bharat1.agarwal@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-19 20:26:44'}, {'order_number': '200000235547', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 4vCPU 16 GB and 1 W-4vCPU 16 GB)', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Provisioning', 'error': 'Exception(\'Exception({\\\'message\\\': "== \\\'True\\\'", \\\'output\\\': [\\\'\\\\nAn error occurred: timed out\\\\nAn error occurred: timed out\\\\nAn error occurred: timed out\\\\nAn error occurred: timed out\\\']})\')', 'created_on': '2023-10-19 19:02:12'}, {'order_number': '200000235546', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Security_Agent', 'error': 'Out object is missing in the callback Response', 'created_on': '2023-10-19 18:44:15'}, {'order_number': '200000235545', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Security_Agent', 'error': 'Out object is missing in the callback Response', 'created_on': '2023-10-19 18:22:36'}, {'order_number': '200000235544', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-19 18:12:07'}, {'order_number': '200000235553', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-19 17:22:02'}, {'order_number': '200000235552', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-19 16:57:50'}, {'order_number': '200000235551', 'product_name': 'RHEL 7.9 – single master/worker (1 M- 4vCPU 8 GB and 1 W-4vCPU 8 GB)', 'created_by': 'adarsh.rai@nic.in', 'milestone': 'Provisioning', 'error': "SystemExit(b'Quota exceeded for cores: Requested 4, but already used 100 of 100 cores (HTTP 403) (Request-ID: req-addbfade-170b-4d42-a939-eee4c6bc4618)\\n')", 'created_on': '2023-10-19 14:48:48'}, {'order_number': '200000235550', 'product_name': 'SUSE 15.4 - M1 Small (2vCPU 4 GB RAM)', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Provisioning', 'error': 'Exception({\'message\': \'AssertionError\', \'output\': ["An error occurred while opening the clustered role \'CPecourttest\'.\\nScript Failed:- VM: CPecourttest doesn\'t exist..Exception.InnerException.Message"]})', 'created_on': '2023-10-19 13:38:47'}, {'order_number': '200000235541', 'product_name': 'SUSE 15.4 - M1 Small (2vCPU 4 GB RAM)', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Provisioning', 'error': 'Exception({\'message\': \'AssertionError\', \'output\': ["An error occurred while opening the clustered role \'CPTest19100131\'.\\nScript Failed:- VM: CPTest19100131 doesn\'t exist..Exception.InnerException.Message"]})', 'created_on': '2023-10-19 13:33:28'}, {'order_number': '200000235529', 'product_name': 'Ubuntu 22.04 LTS - 2 vCPU- 4 GB Ram, 100 GB OS Disk', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Security_Agent', 'error': 'Some task in seqence failed', 'created_on': '2023-10-19 13:26:28'}, {'order_number': '200000235527', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 16vCPU 64 GB and 1 W-16vCPU 64 GB)', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'K8PostProvisioningAction', 'error': 'com.jio.ngo.common.exception.ServiceException: please check the Template. could not replace all template fields\n\tat com.jio.hcmp.workflow.delegate.nodeworkflow.BuildRequest.validateRequest(BuildRequest.java:169)\n\tat com.jio.hcmp.workflow.delegate.nodeworkflow.BuildRequest.execute(BuildRequest.java:138)\n\tat org.camunda.bpm.engine.impl.bpmn.delegate.JavaDelegateInvocation.invoke(JavaDelegateInvocation.java:40)\n\tat org.camunda.bpm.engine.impl.delegate.DelegateInvocation.proceed(DelegateInvocation.java:58)\n\tat org.camunda.bpm.engine.impl.delegate.DefaultDelegateInterceptor.handleInvocationInContext(DefaultDelegateInterceptor.java:92)\n\tat org.camunda.bpm.engine.impl.delegate.DefaultDelegateInterceptor.handleInvocation(DefaultDelegateInterceptor.java:63)\n\tat org.camunda.bpm.engine.impl.bpmn.behavior.ServiceTaskJavaDelegateActivityBehavior.execute(ServiceTaskJavaDelegateActivityBehavior.java:55)\n\tat org.camunda.bpm.engine.impl.bpmn.behavior.ServiceTaskJavaDelegateActivityBehavior.performEx...', 'created_on': '2023-10-19 12:35:18'}, {'order_number': '200000235526', 'product_name': 'Ubuntu Debian11 (OpenSource) (22.04 LTS) - 8 vCPU, 32 GB RAM, 100 GB OS Disk', 'created_by': 'rc.chebolu@nic.in', 'milestone': 'Provisioning', 'error': "SystemExit(b'Quota exceeded for cores: Requested 8, but already used 100 of 100 cores (HTTP 403) (Request-ID: req-2ae2d2c5-ff74-4c3c-bc30-05e6060d1d93)\\n')", 'created_on': '2023-10-19 12:16:03'}, {'order_number': '200000235525', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 16vCPU 64 GB and 1 W-16vCPU 64 GB)', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Provisioning', 'error': 'Exception({\'stdout\': "Transaction directory created.\\n### True\\nCluster execution failed with error: Docker installation failed on 10.192.70.198 server with error: http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nhttp://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: [Errno 12] Timeout on http://repouser:repouser123@10.193.18.214:8081/repo/repository/rhel79/repodata/repomd.xml: (28, \'Operation too slow. Less than 1000 bytes/sec transferred the last 30 seconds\')\\nTrying other mirror.\\nError: Package: docker-ce-rootless-extras-20.10.2-3.el7.x86_64 (DOCKERRPM)\\n           Requires: fuse-overlayfs >= 0.7\\nError: Package: 3:docker-ce-20.10.2-3.el7.x86_64 (DOCKERRPM)\\n           Requires: container-sel', 'created_on': '2023-10-19 12:03:30'}, {'order_number': '200000235539', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 16vCPU 64 GB and 1 W-16vCPU 64 GB)', 'created_by': 'chetan.pinjarkar@ril.com', 'milestone': 'Provisioning', 'error': 'ConnectionError(MaxRetryError(\'HTTPConnectionPool(host=\\\'jio-hcmp-cuenet-gateway.jio-hcmp-cloudorch\\\', port=8084): Max retries exceeded with url: /v1/blueprint/?bid=235457&identifier=1 (Caused by NameResolutionError("<urllib3.connection.HTTPConnection object at 0x7fa2921e6730>: Failed to resolve \\\'jio-hcmp-cuenet-gateway.jio-hcmp-cloudorch\\\' ([Errno -2] Name or service not known)"))\'))', 'created_on': '2023-10-19 11:30:38'}, {'order_number': '200000235524', 'product_name': 'Ubuntu Debian11 (OpenSource) (22.04 LTS) - 8 vCPU, 32 GB RAM, 100 GB OS Disk', 'created_by': 'rc.chebolu@nic.in', 'milestone': 'Provisioning', 'error': "SystemExit(b'Quota exceeded for cores: Requested 8, but already used 100 of 100 cores (HTTP 403) (Request-ID: req-09d621af-ca8f-4fdf-b749-feaf9127babe)\\n')", 'created_on': '2023-10-19 11:10:27'}, {'order_number': '200000235537', 'product_name': 'Ubuntu Debian11 (OpenSource) (22.04 LTS) - 8 vCPU, 32 GB RAM, 100 GB OS Disk', 'created_by': 'rc.chebolu@nic.in', 'milestone': 'Provisioning', 'error': "SystemExit(b'Quota exceeded for cores: Requested 8, but already used 100 of 100 cores (HTTP 403) (Request-ID: req-418dada1-f01b-450e-8e1f-e9e4d51d618f)\\n')", 'created_on': '2023-10-19 11:06:08'}, {'order_number': '200000235536', 'product_name': 'Debian11-postgresql-15.2.0 - 32 vCPU, 128 GB RAM', 'created_by': 'adarsh.rai@nic.in', 'milestone': 'Provisioning', 'error': "SystemExit(b'Quota exceeded for cores: Requested 32, but already used 100 of 100 cores (HTTP 403) (Request-ID: req-464342b5-6486-4059-995e-d371e4292352)\\n')", 'created_on': '2023-10-19 10:03:45'}, {'order_number': '200000235535', 'product_name': 'Debian11-mysql-8.0.32 - 32 vCPU, 128 GB RAM', 'created_by': 'adarsh.rai@nic.in', 'milestone': 'Provisioning', 'error': "SystemExit(b'Quota exceeded for cores: Requested 32, but already used 100 of 100 cores (HTTP 403) (Request-ID: req-0cfea24a-22ce-4261-8f19-7f821b03aacd)\\n')", 'created_on': '2023-10-19 10:03:51'}, {'order_number': '200000235533', 'product_name': 'RHEL 7.9 – single master /worker (1 M- 4vCPU 16 GB and 1 W-4vCPU 16 GB)', 'created_by': 'amar7.yadav@ril.com', 'milestone': 'Provisioning', 'error': "CUENET exception[Exception('unable to complete task[951d2054fec247c3a927a32029ef599c] requested timeline!')] occurred while processing request!", 'created_on': '2023-10-19 00:21:55'}]
#         # else:
#         #     # If form validation fails, re-render the form with error messages
#         #     flash('Please correct the errors in the form.', 'error')
#     else:
#         # If it's a GET request, render the form without processing it
#         form.startdate.data = None
#         form.enddate.data = None
#
#     return render_template('users/date.html', name=name, form=form, milestones_data=milestones_data)


@user_bp.route("/complete_hierarchy", methods=["GET", "POST"])
def complete_hierarchy_mapping():
    name = None
    form = UserMailForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        if request.method == "POST":
            email_string_list = request.form.get("name")
            # print(email_string_list)
            # emails = [f"{email.strip()}" for email in email_string_list.split(',')]
            # # print(email_list)
            # emails_str = ', '.join(emails)
            # print(email_string_list)
            # print(emails_str)
            # print(emails)
            result = subprocess.run(["python3", constants.ETL, constants.COMPLETE_HIERARCHY_MAPPING_PATH
                                        ,constants.CHM_SUBJECT, email_string_list, ], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            # result = subprocess.run(["python3", "/Users/somashekhar/Downloads/scripts/my_script.py",constants.CHM_SUBJECT,email_list ],
            #                         capture_output=True, text=True)

            flash(f"mail sent to {email_string_list} successfully", constants.SUCCESS)

    return render_template('users/user_mail.html', name=name, form=form)
