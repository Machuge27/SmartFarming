from flask import Flask
from flask_socketio import SocketIO
from .views import views  # Assuming your views are in a separate file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

# Register blueprints
app.register_blueprint(views)

if __name__ == '__main__':
    socketio.run(app, debug=True)
