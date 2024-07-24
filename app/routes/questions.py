from flask import Blueprint, request

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    return '<h1>Questions</h1>'


@questions_bp.route('/', methods=['POST'])
def create_question():
    return 'Question was created'


@questions_bp.route('/<int:question_id>', methods=['GET'])
def get_question(question_id):
    return f'Detailed question: {question_id}'


@questions_bp.route('/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    return f'Question {question_id} was updated'


@questions_bp.route('/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    return f'Question {question_id} was deleted'
