import os
from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SESSION_PERMANENT'] = False
@app.route('/')
def home():
    return render_template('index.html')
    



if __name__ == '__main__':
    app.run(debug=True)