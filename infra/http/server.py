# Import all Dependences
from flask import Flask
import config
import os
from dotenv import load_dotenv

# Initialize Flask Global in config
config.app = Flask(__name__)
config.app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER")

# Import api modules (Set import always add a new api service)
import infra.http.api.echo


def run():
    # Load dotenv
    load_dotenv()

    #Start http server
    config.app.run(debug=os.getenv("SYSTEM_DEBUG"), host='0.0.0.0', port=os.getenv("SYSTEM_PORT"))