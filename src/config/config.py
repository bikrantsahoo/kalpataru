import json
import os
from src.constants import constants


# TODO: better add class for  more configs
def load_db_config(user):
    # current_dir = os.path.dirname("/config/db_config.json")
    # json_file_path = os.path.join(current_dir, '..', 'db_config.json')
    print(os.getcwd())
    config_data = None
    try:
        if os.path.exists(constants.DB_CONFIG_PATH):
            with open(constants.DB_CONFIG_PATH, 'r') as config_file:
                config_data = json.load(config_file)

        # Retrieve the common database configuration
        db_config = config_data.get("database", {})

        # Retrieve the user-specific configuration based on the provided user
        user_config = config_data.get(user, {})
        # TODO: remove once app is working fine
        print("Loaded db_config:", db_config)
        print("Loaded user_config for user", user, ":", user_config)
        return db_config, user_config
    except FileNotFoundError:
        print("db_config.json file not found.")
        return None, None
    except json.JSONDecodeError:
        print("Invalid JSON format in db_config.json file.")
        return None, None
