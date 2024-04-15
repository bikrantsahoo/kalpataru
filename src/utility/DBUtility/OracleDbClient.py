import cx_Oracle
from src.config.config import load_db_config


class OracleDBClient:

    def __init__(self, user):
        self.user = user
        self.connection = None

    def connect(self):
        try:
            db_config, user_config = load_db_config(self.user)

            dns_tns = cx_Oracle.makedsn(
                host=db_config.get('host'),
                port=db_config.get('port'),
                service_name=db_config.get('service_name')
            )
            self.connection = cx_Oracle.connect(
                user=user_config.get('username'),
                password=user_config.get('password'),
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
            #TODO: is commit required
            self.connection.commit()
            # cursor.close()
            return True
        except cx_Oracle.DatabaseError as e:
            print(f"Error executing query: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            # if self.connection:
            #     self.connection.close()

    def fetch_results(self, query):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            # cursor.close()
            return results
        except cx_Oracle.DatabaseError as e:
            print(f"Error fetching results: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            # if self.connection:
            #     self.connection.close()

    def insert(self, query):
        try:
            self.execute_query(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"insert failed: {e}")
            return False

    def update(self, query):
        try:
            self.execute_query(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"update failed: {e}")
            return False
