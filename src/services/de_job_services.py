from src.utility.DBUtility.OracleDbClient import OracleDBClient
from src.services.load_sql_service import load_sql_query
from src.constants import constants


class DeServices:

    @staticmethod
    def manage_job(job_instance_ids, enable):
        try:
            job_ids = job_instance_ids.split(',')
            db_client = OracleDBClient(user="DE_DEV")
            if db_client.connect():
                job_result_ids = []
                for job_id in job_ids:
                    job_id = job_id.strip()
                    if DeServices.is_job_present(job_id, db_client):
                        job_result_ids.append(job_id)
                if job_result_ids:
                    print(job_result_ids)
                    in_clause = ",".join("'" + str(result) + "'" for result in job_result_ids)
                    if enable:
                        params = {"job_instance_id": in_clause, "status1": "A", "status2": "I"}
                    else:
                        params = {"job_instance_id": in_clause, "status1": "I", "status2": "A"}
                    query = load_sql_query(constants.UPDATE_DE_DISABLE_PATH, params)
                    print(query)
                    # TODO: after testing replace it with update query
                    db_client.execute_query(query)
                    db_client.disconnect()
                    return True
                else:
                    return False
            else:
                db_client.disconnect()
                return False
        except Exception as e:
            print(f"Error: {str(e)}")
            return False

    def is_job_present(job_instance_id, db_client):
        params = {"job_instance_id": job_instance_id}
        query = load_sql_query(constants.SELECT_DE_DISABLE_PATH, params)
        print(query)
        db_client.execute_query(query)
        count = db_client.fetch_results(query)
        return len(count) > 0

    @staticmethod
    def get_job_histories(job_instance_id):
        db_client = OracleDBClient(user="DE_DEV")
        query = ""
        if db_client.connect():
            print("i am here")
            params = {"job_instance_id": job_instance_id}
            try:
                query = load_sql_query(constants.SELECT_JOB_HISTORY_PATH, params)
                print(query)
                db_client.execute_query(query)
                job_histories = db_client.fetch_results(query)
                job_histories_data = []
                for job_history in job_histories:
                    if job_history[0] is not None:
                        formatted_start_time = job_history[0].strftime("%Y-%m-%d %H:%M:%S"),
                    else:
                        formatted_start_time = None
                    if job_history[1] is not None:
                        formatted_end_time = job_history[1].strftime("%Y-%m-%d %H:%M:%S"),
                    else:
                        formatted_end_time = None

                    job_history_data = {
                        "start_time": formatted_start_time,
                        "end_time": formatted_end_time,
                        "status": job_history[2]
                    }
                    job_histories_data.append(job_history_data)
                print(job_histories_data)
                return job_histories_data
            except Exception as e:
                print(f"Error: {str(e)}")
                return []
            finally:
                db_client.disconnect()

        else:
            return []
