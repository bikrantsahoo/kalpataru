from src.utility.DBUtility.OracleDbClient import OracleDBClient
from src.enums.DbUserEnums import DbUser


class AlertServices:
    # def __init__(self, user):
    #     self.db_client = OracleDBClient(user=user)

    # def __int__(self):
    #     pass

    @staticmethod
    def delete_alert(alert_name):
        db_client = OracleDBClient(user=DbUser.HCMP_REPLICA1.value)
        if db_client.connect():
            query = f"DELETE FROM alerts WHERE name = '{alert_name}'"
            # query = "select * from HCMP_DE_DEV.HCMP_SUBS_MASTER"
            success = db_client.execute_query(query)
            db_client.disconnect()
            return success
        else:
            return False

    @staticmethod
    def get_alert(alert_name):
        db_client = OracleDBClient(user=DbUser.HCMP_PROCESS_CONF.value)
        if db_client.connect():
            query = f"SELECT * FROM alerts WHERE name = '{alert_name}'"
            result = db_client.fetch_results(query)
            db_client.disconnect()
            return result
        else:
            return None
