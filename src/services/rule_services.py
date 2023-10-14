from src.utility.DBUtility.OracleDbClient import OracleDBClient
from src.services.load_sql_service import load_sql_query
from src.constants import constants


class RuleServices:

    @staticmethod
    def disable_multiple_rule(rule_names):
        try:
            rule_names = rule_names.split(',')
            db_client = OracleDBClient(user="PROCESS_CONF")
            if db_client.connect():
                for rule_name in rule_names:
                    rule_name = rule_name.strip()
                    global query
                    params = {"rule_name": rule_name}
                    query = load_sql_query(constants.SELECT_RULE_PATH, params)
                    results = db_client.fetch_results(query)
                    print(results)

                    rule_ids = [str(result[0]) for result in results]
                    if rule_ids:
                        in_clause = ",".join(rule_ids)
                        query = load_sql_query(constants.UPDATE_RULE_PATH, params)
                        print(query)
                        db_client.update(query)
                        db_client.disconnect()

                        db_client = OracleDBClient(user="DE_DEV")
                        params = {"rule_ids": in_clause}
                        query = load_sql_query(constants.UPDATE_RULE_MASTER_PATH, params)
                        print(query)
                        db_client.connect()
                        db_client.update(query)
                    else:
                        return False

                db_client.disconnect()
                return True
            else:
                db_client.disconnect()
                return False
        except Exception as e:
            print(f"Error: {str(e)}")
            return False
