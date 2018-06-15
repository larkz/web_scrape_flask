from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql123@localhost/t1'
db = SQLAlchemy(app)

from app import routes, models
# from app import db

# admin = models.User(username='admin', email='admin@example.com')
# db.session.add(admin)
db.create_all()
db.session.commit()

if __name__ == '__main__':
    
    # db.create_all()
    # print("Test1")
    '''
    print("Test")
    admin = web_url(web_url = 'larkin.com')
    db.session.add()
    db.session.commit()
    app.run(debug=True)
    '''


'''
app.config.from_object(Config)
# MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql123'
    app.config['MYSQL_DATABASE_DB'] = 'BucketList'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    MySQL(app)
mysql = MySQL(app)

'''


