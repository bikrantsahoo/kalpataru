from flask import Blueprint, render_template, request, flash, redirect
from src.routes.forms.date_form import DateForm

from src.services.report_services import ReportServices
from src.constants import constants

reports_bp = Blueprint("reports", __name__)


@reports_bp.route("/order_milestone", methods=["GET", "POST"])
def order_milestone():
    milestones_data = []
    name = None
    form = DateForm()
    if form.validate_on_submit():
        start_date = form.startdate.data
        end_date = form.enddate.data
        print(start_date)
        print(end_date)
        date_difference = (end_date - start_date).days
        if date_difference < 0:
            flash('End date must be after the start date.', constants.WARNING)
        elif date_difference > 10:
            flash('Date range should not exceed 10 days.', constants.WARNING)
        else:
            milestones_data = ReportServices.order_milestone(start_date, end_date)

    return render_template('reports/date.html', name=name, form=form, milestones_data=milestones_data)
