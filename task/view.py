from flask import jsonify

from main import app
from task.model import Task


@app.route('/api/task/<int:user_id>')
def index(user_id: int):
    query = Task.query.filter(id=user_id)

    return jsonify(query)
