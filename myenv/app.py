from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)
# dunder name - the name of the file you are writing

# ROUTE or VIEW FUNCTION
@app.route("/")         # @ - "decorator"
def homepage():
    lucky_num = randint(1, 100)
    # return "<html><body>oh hi</body></html>"
    return render_template("homepage.html", num=lucky_num)

@app.route("/madlibs")  # default is regular smegular get request
def ask_questions():
    return render_template("questions.html")

@app.route("/madlibs", methods=["POST"])
def tell_story():
    noun = request.form['noun']
    verb = request.form['verb']
    adj = request.form['adj']
    # return "this works!!!"
    # 1. Get noun, adj, and verb from the user form
    # 2. Render them on "story.html"

    return render_template(
        "story.html",
        noun=noun,
        verb=verb,
        adj=adj
    )


app.run(debug=True)
