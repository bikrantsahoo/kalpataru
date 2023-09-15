# app_test/routes/user_routes.py
from flask import Blueprint, jsonify, request, render_template

user_bp = Blueprint("user", __name__)


@user_bp.route("/create_user")
def create_user():
    # Get users data from the request (JSON or form data)
    #user_data = request.json  # Assuming JSON data is sent

    # Perform users creation logic here
    # ...

    #return jsonify({"message": "User created successfully"})
    return render_template('users/create_user.html')


@user_bp.route("/modify_user/<int:user_id>", methods=["PUT"])
def modify_user(user_id):
    # Get users data from the request (JSON or form data)
    user_data = request.json  # Assuming JSON data is sent

    # Perform users modification logic here for the given user_id
    # ...

    return jsonify({"message": "User modified successfully"})


@user_bp.route("/delete_user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    # Perform users deletion logic here for the given user_id
    # ...

    return jsonify({"message": "User deleted successfully"})
