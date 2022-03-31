from database import init_db
from flask import Flask
from routes import urls_blueprint, login_manager

app = Flask(__name__)
# register routes from urls
app.register_blueprint(urls_blueprint)

app.config["SECRET_KEY"] = "SECRETKEYOMG"

init_db()

login_manager.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
