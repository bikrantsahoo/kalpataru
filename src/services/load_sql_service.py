from string import Template
import os


def load_sql_query(file_path, params=None):
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                query = file.read()
                if params:
                    template = Template(query)
                    query = template.safe_substitute(params)
                    # TODO: instead of template try to work on below
                    # query = query.format(**params)
        return query
    except FileNotFoundError:
        print("sql file path not found ")
