from flask import Blueprint, request

responses_bp = Blueprint('responses', __name__, url_prefix='/responses')


@responses_bp.route('/', methods=['GET'])
def get_responses():
    return 'Get all responses'


@responses_bp.route('/', methods=['POST'])
def add_response():
    return 'Add a response'
