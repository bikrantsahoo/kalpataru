from src.utility.DBUtility.OracleDbClient import OracleDBClient


class RuleServices:
    # def __init__(self, user):
    #     self.db_client = OracleDBClient(user=user)

    # def __int__(self):
    #     pass

    @staticmethod
    def disable_multiple_rule(user, alert_name):
        db_client = OracleDBClient(user=user)
        if db_client.connect():
            query = f"DELETE FROM alerts WHERE name = '{alert_name}'"
            success = db_client.execute_query(query)
            db_client.disconnect()
            return success
        else:
            return False
