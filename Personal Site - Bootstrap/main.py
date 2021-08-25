import smtplib
import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import datetime

EMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
PASSWORD = os.getenv("PASSWORD")

app = Flask(__name__)
Bootstrap(app)

current_year = datetime.datetime.now().year

@app.route('/')
def home():
    return render_template("index.html", year=current_year)


@app.route('/education')
def education():
    return render_template("education.html", year=current_year)


@app.route('/professional-experience')
def professional():
    return render_template("professional-experience.html", year=current_year)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
#         data = request.form
        data = request.form
        send_email(data["name"], data["company"], data["email"], data["message"])
        return render_template("contact.html", year=current_year, msg_sent=True)
    return render_template("contact.html", year=current_year, msg_sent=False)

def send_email(name, company, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nCompany: {company}\nEmail: {email}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, PASSWORD)
        connection.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, email_message)


if __name__ == "__main__":
    app.run(debug=True)
