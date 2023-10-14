from flask import Blueprint, render_template, request, flash, redirect
from src.routes.forms.de_disable_form import DisableForm

from src.services.de_job_services import DeServices
from src.constants import constants

de_bp = Blueprint("de_jobs", __name__)


@de_bp.route("/manage_job", methods=["GET", "POST"])
def manage_job():
    name = None
    form = DisableForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        if request.method == "POST":
            job_instance_id = request.form.get("name")
            toggle_switch = request.form.get("toggle_switch")
            print(toggle_switch)
            print(job_instance_id)
            # TODO: check and remove this condition check after few days
            # if len(job_instance_id) <= constants.ALERT_SIZE:
            #     flash("recheck the alert name", constants.WARNING)
            #     return redirect("/delete_alert")
            if toggle_switch == "on":
                status = DeServices.manage_job(job_instance_ids=job_instance_id, enable=True)
            else:
                status = DeServices.manage_job(job_instance_ids=job_instance_id, enable=False)

            if status:
                flash(f"Disable {job_instance_id} successfully", constants.SUCCESS)
            else:
                flash(f"Failed to disable job {job_instance_id} ", constants.ERROR)
    return render_template('de/disable.html', name=name, form=form)


@de_bp.route("/job_history", methods=["GET", "POST"])
def job_history():
    job_histories_data = []
    name = None
    form = DisableForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        if request.method == "POST":
            job_instance_id = request.form.get("name")
            print(job_instance_id)
            job_histories_data = DeServices.get_job_histories(job_instance_id=job_instance_id)
            # # job_histories = [(2023, 2024, 'success'), (2023, 2024, 'success'), (2023, 2024, 'success'),(2023, 2024, 'success')]
            # job_histories_data = []
            # for job_history in job_histories:
            #     job_history_data = {
            #         "start_time": job_history[0],
            #         "end_time": job_history[1],
            #         "status": job_history[2]
            #     }
            #     job_histories_data.append(job_history_data)
    form = DisableForm()
    return render_template('de/job_histories.html', name=name, form=form, job_histories_data=job_histories_data)
