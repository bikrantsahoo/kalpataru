from src.utility.DBUtility.OracleDbClient import OracleDBClient
from src.enums.DbUserEnums import DbUser
from src.services.load_sql_service import load_sql_query
from src.constants import constants


class AlertServices:

    @staticmethod
    def delete_alert(alert_names):
        try:
            print(alert_names)
            alert_names = alert_names.split(',')
            db_client = OracleDBClient(user="PROCESS_CONF")
            if db_client.connect():
                alert_results = []
                for alert_name in alert_names:
                    alert_name = alert_name.strip()
                    if is_alert_present(alert_name, db_client):
                        alert_results.append(alert_name)

                if alert_results:
                    print(alert_results)
                    in_clause = ",".join("'" + result + "'" for result in alert_results)
                    params = {"alert_name": in_clause}
                    query = load_sql_query(constants.UPDATE_ALERT_PATH, params)
                    print(query)
                    # TODO: after testing replace it with update query
                    db_client.execute_query(query)
                    db_client.disconnect()
                    return True
                else:
                    db_client.disconnect()
                    return False
            else:
                return False
        except Exception as e:
            print(f"Error: {str(e)}")
            return False


def is_alert_present(alert_name, db_client):
    global query
    params = {"alert_name": alert_name}
    query = load_sql_query(constants.SELECT_ALERT_PATH, params)
    print(query)
    db_client.execute_query(query)
    count = db_client.fetch_results(query)
    return len(count) > 0
