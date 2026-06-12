from flask import Blueprint, request, jsonify
from services.user_service import get_users, create_user, get_user_by_id
from utils.validators import validate_user_data
from utils.response import success_response, error_response

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def fetch_users():
    search = request.args.get("search")
    page = request.args.get("page", default=1, type=int)
    limit = request.args.get("limit", default=10, type=int)

    result = get_users(search=search, page=page, limit=limit)

    return jsonify(
        success_response(
            data=result,
            message="Users retrieved successfully"
        )
    ), 200
 

@user_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    is_valid, error = validate_user_data(data)

    if not is_valid:
        return jsonify(error_response(error)), 400

    user, error = create_user(data)

    if error:
        return jsonify(error_response(error)), 409

    return jsonify(
        success_response(
            data=user,
            message="User created successfully"
        )
    ), 201


@user_bp.route("/users/<int:user_id>", methods=["GET"])
def fetch_user_by_id(user_id):
    user = get_user_by_id(user_id)

    if not user:
        return jsonify(error_response("User not found")), 404

    return jsonify(
        success_response(
            data=user,
            message="User retrieved successfully"
        )
    ), 200