from src.utility.DBUtility.OracleDbClient import OracleDBClient
from src.enums.DbUserEnums import DbUser


class AlertServices:
    # def __init__(self, user):
    #     self.db_client = OracleDBClient(user=user)

    # def __int__(self):
    #     pass

    @staticmethod
    def delete_alert(alert_name):
        db_client = OracleDBClient(user="DE_DEV")
        if db_client.connect():
            query = f"SELECT * FROM HCMP_SUBS_MASTER"
            #query = "select * from HCMP_DE_DEV.HCMP_SUBS_MASTER"
            db_client.execute_query(query)
            results = db_client.fetch_results(query)
            print(results)
            db_client.disconnect()
            return True
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
