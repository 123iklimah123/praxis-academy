from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:allah1@localhost:5432/contoh'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
@app.route("/")
def index():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        input = User(username=username, email=email)
        db.session.add(input)
        db.session.commit()
        print(username, email)
    data = User.query.all()
    print(data)
    return render_template("index.html", context=data)

if __name__ == "__main__":
    db.create_all()
    app.run()