from flask import Blueprint, jsonify, request
from ..tables.user_table import Users
import pprint

# User endpoint

user = Blueprint('User', __name__)


@user.route('/', methods=["GET"])
def get_users(**path_variables):
    return jsonify({'users': 'Jim'}), 200


@user.route('/<string:id>', methods=['GET'])
def user_profile(id):
    error = None
    user_profile = Users.get(id)
    return jsonify({i: user_profile. for i in user_profile.__dict__})
