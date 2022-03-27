from flask import Flask
from flask import render_template, redirect, request
from predict import predict


# create a flask app with a single post endpoint to handle the request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/topic', methods=['POST'])
def topic():
    if request.method == 'POST':
        email_from = request.form['email']
        org = request.form['organization']
        subject = request.form['subject']
        content = request.form['content']
        full_email = ' '.join([email_from, org, subject, content])
        prediction_string = predict(full_email)
        return render_template('topic.html', prediction_string=prediction_string)


if __name__ == "__main__":
    app.run(debug=True)
