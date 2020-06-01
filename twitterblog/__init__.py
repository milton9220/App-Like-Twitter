from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'#eikhane login hosscce route er function name. ar eita use kora hoi jodi kew login na thake tahole kew login page access korte parbe na
login_manager.login_message_category='info'#eita use kora hoise jate kew login na kore account page access korte gele j message dibe oita te jate bootstrap info class r maddhome dei
app.config.update(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = '587',
    MAIL_USE_TLS = True,
    MAIL_USERNAME = "tayabarahaman779@gmail.com",
    MAIL_PASSWORD=  ""
)
mail = Mail(app)

from twitterblog import routes


