from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

BACKEND_API_URL = 'http://localhost:8080/api/tasks'

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    tasks = requests.get(BACKEND_API_URL).json()
    emit('initial_tasks', tasks)

@socketio.on('add_task')
def handle_add_task(task_data):
    response = requests.post(BACKEND_API_URL, json=task_data)
    if response.status_code == 200:
        emit('task_added', response.json(), broadcast=True)

@socketio.on('update_task')
def handle_update_task(task_data):
    response = requests.put(f"{BACKEND_API_URL}/{task_data['id']}", json=task_data)
    if response.status_code == 200:
        emit('task_updated', response.json(), broadcast=True)

@socketio.on('delete_task')
def handle_delete_task(task_id):
    response = requests.delete(f"{BACKEND_API_URL}/{task_id}")
    if response.status_code == 200:
        emit('task_deleted', {'id': task_id}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
