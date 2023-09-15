import json


# TODO: better add class for  more configs
def load_db_config(user):
    try:
        with open('db_config.json', 'r') as config_file:
            config_data = json.load(config_file)

        # Retrieve the common database configuration
        db_config = config_data.get("database", {})

        # Retrieve the user-specific configuration based on the provided user
        user_config = config_data.get(user, {})

        return db_config, user_config
    except FileNotFoundError:
        print("db_config.json file not found.")
        return None, None
    except json.JSONDecodeError:
        print("Invalid JSON format in db_config.json file.")
        return None, None
