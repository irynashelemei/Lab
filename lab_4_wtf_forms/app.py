import json

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, AnyOf

app = Flask(__name__)
app.config["SECRET_KEY"] = "some_key"
app.config["TESTING"] = True
file_path = "./data.json"


class ContactForm(FlaskForm):
    name = StringField(
        "name",
        validators=[
            InputRequired("A name is required!"),
            Length(min=3, max=10, message="Must be from 3 to 10 chars")
        ]
    )
    email = EmailField(
        "email",
        validators=[
            InputRequired("Email is required!"),
        ]
    )
    body = StringField(
        "body",
        validators=[
            InputRequired("A body is required!")
        ]
    )


@app.route("/form", methods=["GET", "POST"])
def form():
    contact_form = ContactForm()

    if contact_form.validate_on_submit():
        data_s = json.dumps(
                {
                    "name": contact_form.name.data,
                    "email": contact_form.email.data,
                    "body": contact_form.body.data
                }
            )
        with open(file_path, "a") as fp:
            fp.write(data_s + "\n")
        return data_s
    return render_template("form.html", form=contact_form)


if __name__ == '__main__':
    app.run(debug=True)
