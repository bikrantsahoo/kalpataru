from src.utility.DBUtility.OracleDbClient import OracleDBClient
from src.services.load_sql_service import load_sql_query
from src.constants import constants


class DeServices:

    @staticmethod
    def disable_job(job_instance_id):
        db_client = OracleDBClient(user="DE_DEV")
        if db_client.connect():
            if DeServices.is_job_present(job_instance_id, db_client):
                params = {"job_instance_id": job_instance_id}
                query = load_sql_query(constants.UPDATE_DE_DISABLE_PATH, params)
                print(query)
                # TODO: after testing replace it with update query
                # db_client.execute_query(query)
                db_client.disconnect()
                return True
            else:
                db_client.disconnect()
                return False
        else:
            return False

    @staticmethod
    def is_job_present(job_instance_id, db_client):
        params = {"job_instance_id": job_instance_id}
        query = load_sql_query(constants.SELECT_DE_DISABLE_PATH, params)
        print(query)
        db_client.execute_query(query)
        count = db_client.fetch_results(query)
        return len(count) > 0
