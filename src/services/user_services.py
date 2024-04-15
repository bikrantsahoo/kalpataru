from src.utility.DBUtility.OracleDbClient import OracleDBClient
from src.services.load_sql_service import load_sql_query
from src.constants import constants


class UserService:

    @staticmethod
    def modify_mobile_number(customer_id, mobile_number):
        db_client = OracleDBClient(user="REPLICA")
        if db_client.connect():
            if UserService.is_customer_present(db_client, customer_id):
                params = {"mobile_number": mobile_number, 'customer_id': customer_id}
                query = load_sql_query(constants.UPDATE_MOB_NUM_PATH, params)
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

    @staticmethod
    def is_customer_present(db_client, customer_id):
        params = {"customer_id": customer_id}
        query = load_sql_query(constants.SELECT_CUSTOMER_PATH, params)
        print(query)
        db_client.execute_query(query)
        count = db_client.fetch_results(query)
        return len(count) > 0

    def delete_guest_user(user_id):
        try:
            db_client = OracleDBClient(user="REPLICA")
            if db_client.connect():
                params = {"user_id": user_id}
                query = load_sql_query(constants.UPDATE_GUEST_USER, params)
                print(query)
                # TODO: after testing replace it with update query
                db_client.execute_query(query)
                db_client.disconnect()
                return True
            else:
                db_client.disconnect()
                return False
        except Exception as e:
            print(f"Error: {str(e)}")
            return False

    def get_user_list(user_id):
        try:
            db_client = OracleDBClient(user="REPLICA")
            query = ""
            if db_client.connect():
                params = {"user_id": user_id}
                query = load_sql_query(constants.SELECT_GUEST_USER, params)
                print(query)
                db_client.execute_query(query)
                users_list = db_client.fetch_results(query)
                users_list_data = []
                for user_list in users_list:
                    user_list_data = {
                        "user_log_id": user_list[0],
                        "customer_id": user_list[1],
                        "status": user_list[2],
                        "action_type_code": user_list[3]
                    }
                    users_list_data.append(user_list_data)
                db_client.disconnect()
                return users_list_data
            else:
                db_client.disconnect()
                return []
        except Exception as e:
            print(f"Error: {str(e)}")
            return False
