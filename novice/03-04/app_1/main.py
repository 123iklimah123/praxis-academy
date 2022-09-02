from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()


if request.method == "POST":
        print(20*"=")
        print(request.form)
        print(request.form.get("nama"))
        print(request.form.get("detail"))
        print(20*"=")
