from src.utility.DBUtility.OracleDbClient import OracleDBClient
from src.enums.DbUserEnums import DbUser
from src.services.load_sql_service import load_sql_query
from src.constants import constants
import json


class CMDBServices:

    @staticmethod
    def ip_search(ip):
        try:
            db_client = OracleDBClient(user="REPLICA")
            if db_client.connect():
                params = {"ip": ip}
                query = load_sql_query(constants.SELECT_SEARCH_IP_PATH, params)
                print(query)
                db_client.execute_query(query)
                milestones_data = db_client.fetch_results(query)
                data = []
                if milestones_data:
                    data.append({"name": None})
                    for row in milestones_data:
                        IP_ADDRESS, STATUS, RESOURCE_TYPE_ID, CREATED_ON, UPDATED_ON, UPDATED_BY \
                            , NAME, ASSET_ID, PROJECT_ID, SOURCE, STATUS, ENABLED, HOSTNAME, ORDER_ID, PROVISIONED_BY, UPDATED_ON \
                            , NAME, PROJECT_DESC \
                            = row
                        data.append({
                            "ip_address": IP_ADDRESS,
                            "rn_status": STATUS,
                            "resource_type_id": RESOURCE_TYPE_ID,
                            "created_on": CREATED_ON.strftime("%Y-%m-%d %H:%M:%S"),
                            "updated_on": UPDATED_ON.strftime("%Y-%m-%d %H:%M:%S"),
                            "updated_by": UPDATED_BY,
                            "name": NAME,
                            "asset_id": ASSET_ID,
                            "project_id": PROJECT_ID,
                            "item_price": SOURCE,
                            "status": STATUS,
                            "enabled": ENABLED,
                            "hostname": HOSTNAME,
                            "order_id": ORDER_ID,
                            "provisioned_by": PROVISIONED_BY,
                            "hpm_updated_on": UPDATED_ON.strftime("%Y-%m-%d %H:%M:%S"),
                            "proj_name": NAME,
                            "project_desc": PROJECT_DESC,
                        })
                json_data = json.dumps(data)
                return json_data
        except (ConnectionError, Exception) as e:
            print(f"Error: {str(e)}")
            return False
