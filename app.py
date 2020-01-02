from flask import Flask

from routes import app_routes
import os


app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

app.register_blueprint(app_routes, root_path=app.instance_path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

