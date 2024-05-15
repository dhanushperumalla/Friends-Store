from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the app
db = SQLAlchemy(app)

# Import routes after db initialization to avoid circular imports
import routes

with app.app_context():
    db.create_all()
 

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)



    
#to run like nodemon
#flask run --reload