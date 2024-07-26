from flask import Blueprint, request, jsonify, make_response

from app.models import Question, db

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    questions_data = [{'id': q.id, 'text': q.text} for q in questions]
    return jsonify(questions_data)


@questions_bp.route('/', methods=['POST'])
def create_question():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing data'}), 400

    question = Question(text=data['text'])
    db.session.add(question)
    db.session.commit()

    return jsonify({'message': 'Question created', 'id': question.id}), 201


@questions_bp.route('/<int:question_id>', methods=['GET'])
def get_question(question_id):
    return f'Detailed question: {question_id}'


@questions_bp.route('/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    return f'Question {question_id} was updated'


@questions_bp.route('/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    return f'Question {question_id} was deleted'
