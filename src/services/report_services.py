from src.utility.DBUtility.OracleDbClient import OracleDBClient
from src.services.load_sql_service import load_sql_query
from src.constants import constants


class ReportServices:

    def order_milestone(start_date, end_date):
        db_client = OracleDBClient(user="REPLICA")
        if db_client.connect():
            global query
            params = {"start_date": start_date, "end_date": end_date}
            try:
                query = load_sql_query(constants.SELECT_ORDER_MILESTONE_PATH, params)
                print(query)
                db_client.execute_query(query)
                milestones_data = db_client.fetch_results(query)
                order_milestones_data = []
                for milestone_data in milestones_data:
                    order_milestone_data = {
                        "order_number": milestone_data[0],
                        "product_name": milestone_data[1],
                        "created_by": milestone_data[2],
                        "milestone": milestone_data[3],
                        "error": milestone_data[4],
                        "created_on": milestone_data[5].strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    order_milestones_data.append(order_milestone_data)
                print(order_milestones_data)
                return order_milestones_data
            except Exception as e:
                print(f"Error: {str(e)}")
                return []
            finally:
                db_client.disconnect()

        else:
            return []
