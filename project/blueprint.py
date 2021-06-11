from flask import Blueprint, jsonify, request
from http import HTTPStatus

from project.models import Teacher

v1 = Blueprint('v1', __name__, template_folder='templates')

teacher_data = {
    "last_name": "Пупкін",
    "first_name": "Василь",
    "middle_name": "Васильович",
    "position": "Доцент",
    "chair": "Математики та інформатики",
    "date_start": "2021/01/01",
    "phone": "0666123666",
}


@v1.route('/', methods=["GET"])
def teachers_list():
    # teachers = get_all_teachers()
    return jsonify({"result": [teacher_data], "count": len([teacher_data])}), HTTPStatus.OK


@v1.route('/', methods=["POST"])
def teachers_create():
    Teacher.create(**request.json)
    return "", HTTPStatus.CREATED


@v1.route('/<teacher_id>', methods=["GET"])
def teacher_get(teacher_id):
    teacher_data = Teacher.get(int(teacher_id))
    return jsonify(teacher_data), HTTPStatus.OK


@v1.route('/<teacher_id>', methods=["DELETE"])
def teacher_delete(teacher_id):
    # teacher_data = delete_teacher(teacher_id)
    return jsonify(teacher_data), HTTPStatus.OK


@v1.route('/<teacher_id>', methods=["PUT"])
def teacher_update(teacher_id):
    # teacher_data = update_teacher(teacher_id)
    return jsonify(teacher_data), HTTPStatus.OK
