from src.services.notitification_service import send_email
from src.utility.DBUtility.OracleDbClient import OracleDBClient
from src.enums.DbUserEnums import DbUser
from src.services.load_sql_service import load_sql_query
from src.constants import constants
from flask import render_template


class AlertServices:
    # def __init__(self, user):
    #     self.db_client = OracleDBClient(user=user)

    # def __int__(self):
    #     pass

    # @staticmethod
    # def load_sql_query(file_path, params=None):
    #     with open(file_path, 'r') as file:
    #         query = file.read()
    #         if params:
    #             query = query.format(**params)
    #         return query

    # @staticmethod
    # def load_sql_query(file_path, params=None):
    #     with open(file_path, 'r') as file:
    #         query = file.read()
    #         if params:
    #             template = Template(query)
    #             query = template.safe_substitute(params)
    #             # TODO: instead of template try to work on below
    #             # query = query.format(**params)
    #         return query

    @staticmethod
    def delete_alert(alert_name):
        db_client = OracleDBClient(user="PROCESS_CONF")
        if db_client.connect():
            if AlertServices.is_alert_present(alert_name, db_client):
                params = {"alert_name": alert_name}
                query = load_sql_query(constants.UPDATE_ALERT_PATH, params)
                print(query)
                # TODO: after testing replace it with update query
                db_client.execute_query(query)
                db_client.disconnect()
                email_message_template = render_template('email/simple_email_template.html',
                                                         subject=constants.ALERT_MAIL_SUBJECT.format(alert_name),
                                                         message=alert_name)

                send_email(constants.RECIPIENT_MAIL,
                           constants.ALERT_MAIL_SUBJECT.format(alert_name), email_message_template)

                return True
            else:
                db_client.disconnect()
                return False
        else:
            return False

    @staticmethod
    def get_alert(alert_name):
        db_client = OracleDBClient(user=DbUser.HCMP_PROCESS_CONF.value)
        if db_client.connect():
            query = f"testing  '{alert_name}'"
            result = db_client.fetch_results(query)
            db_client.disconnect()
            return result
        else:
            return None

    @staticmethod
    def is_alert_present(alert_name, db_client):
        params = {"alert_name": alert_name}
        query = load_sql_query(constants.SELECT_ALERT_PATH, params)
        print(query)
        db_client.execute_query(query)
        count = db_client.fetch_results(query)
        return len(count) > 0
