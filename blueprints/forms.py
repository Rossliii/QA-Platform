import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired
from models import UserModel, EmailCaptchaModel
from exts import db


class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Invalid email")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="Invalid Vertification Code")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="Invalid username")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Invalid Password")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="Different password")])

    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="The email has been used")

    # 2. 验证码是否正确
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email, captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="Invalid email or vertification code！")
        # else:
        #     db.session.delete(captcha_model)
        #     db.session.commit()


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Invalid email form")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Invalid Password form")])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="Invalid title: should between 3 and 100")])
    content = wtforms.StringField(validators=[Length(min=3,message="Invalid content: should at least 3 characters")])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message="Invalid content: should at least 3 characters")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="Must add question id")])