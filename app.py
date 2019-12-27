from flask import Flask

from routes import app_routes



app = Flask(__name__)
app.register_blueprint(app_routes, root_path=app.instance_path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

