import os
from flask import Flask, render_template
from flask_migrate import Migrate
from models import db
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SESSION_PERMANENT'] = False

db.init_app(app)
 
migrate = Migrate(app , db)


if __name__ == '__main__':
    app.run(debug=True)