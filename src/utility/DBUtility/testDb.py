import cx_Oracle
from src.config.ConfigUtility.config import load_db_config

class OracleDBClient:
    def __init__(self, user):
        self.user = user
        self.connection = None
    def connect(self):
        try:
            db_config, user_config = load_db_config(self.user)
            dns_tns = cx_Oracle.makedsn(
                host='10.193.18.70',
                port='1535',
                service_name='HCMPREPL'
            )
            self.connection = cx_Oracle.connect(
                user='HCMP_DE_DEV',
                password='Gdn9Ef$2K23',
                dsn=dns_tns
            )
            return True
        except cx_Oracle.DatabaseError as e:
            print(f"Failed to connect to the database: {e}")
            return False
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
    def execute_query(self, query):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
            return True
        except cx_Oracle.DatabaseError as e:
            print(f"Error executing query: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            if self.connection:
                self.connection.close()
    def fetch_results(self, query):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except cx_Oracle.DatabaseError as e:
            print(f"Error fetching results: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if self.connection:
                self.connection.close()
