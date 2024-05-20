import json

from flask import Blueprint, render_template, request, flash, redirect
from src.routes.forms.ip_search_form import IPSearchForm

from src.services.cmdb_services import CMDBServices
from src.constants import constants
import json


cmdb_bp = Blueprint("cmdb", __name__)

@cmdb_bp.route('/ip_search', methods=['GET', 'POST'])
def ip_search():
    name = None
    json_data = {}
    form = IPSearchForm()
    if request.method == 'POST':
        form.name.data = ''
        ip = request.form.get("name")
        #json_data = CMDBServices.ip_search(ip)
        json_data = [{
            "ip_address": '1234',
            "rn_status": 'afaf',
            "resource_type_id": 'aef',
            "created_on": 'af',
            "updated_on": 'af',
            "updated_by": 'aef',
            "name": 'aef',
            "asset_id": 'aef',
            "project_id": 'aef',
            "item_price": 'aef',
            "status": 'aef',
            "enabled": 'aef',
            "hostname": 'None',
            "order_id": 'aef',
            "provisioned_by": 'aef',
            "hpm_updated_on": 'aef',
            "proj_name": 'aef',
            "project_desc": 'aef'
        }, {
            "ip_address": 'aef',
            "rn_status": 'aef',
            "resource_type_id": 'aef',
            "created_on": 'aef',
            "updated_on": 'aef',
            "updated_by": 'aef',
            "name": 'aef',
            "asset_id": 'aef',
            "project_id": 'aef',
            "item_price": 'aef',
            "status": 'aef',
            "enabled": 'aef',
            "hostname": None,
            "order_id": 'aef',
            "provisioned_by": 'aef',
            "hpm_updated_on": 'aef',
            "proj_name": 'aef',
            "project_desc": 'aef'}
        ]
        json_data = json.dumps(json_data)
        if json_data:
            json_data = json.loads(json_data)
        else:
            flash(f" IP {ip} not found ", constants.ERROR)
    return render_template('ip/ip_search.html', name=name, form=form,json_data=json_data, num_items=len(json_data))

