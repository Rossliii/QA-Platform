import os

#you need define three environment variable: SECRET_KEY, PASSWORD, MAIL_USERNAME, MAIL_PASSWORD

# add your own POP3/SMTP/IMAP password in your terminal before run like this:
# export SECRET_KEY=mysecretkey
SECRET_KEY = os.environ['SECRET_KEY']

HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
# define your own password in your terminal before run like this:
# export PASSWORD=mypassword
PASSWORD = os.environ['PASSWORD']
DATABASE = "QA-web"
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI

#config email
#JRABLYQWUFOOXZAP

MAIL_SERVER = "smtp.163.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
# add your own email in your terminal before run like this:
# export MAIL_USERNAME=myemail
MAIL_USERNAME = os.environ['MAIL_USERNAME']
# add your own POP3/SMTP/IMAP password in your terminal before run like this:
# export MAIL_PASSWORD=myemailpassword
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
MAIL_DEFAULT_SENDER = MAIL_USERNAME