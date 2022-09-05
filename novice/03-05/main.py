from flask import Flask, render_template, request
import psycopg2
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
            host="localhost",
            database="contoh",  
            user="postgres",
            password="allah1")

    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        detail = request.form.get("detail")
        query = f"insert into buah(nama, detail) values ('{nama}','{detail}')"
        curs.execute(query)
        conn.commit()
        curs.close()
        conn.close()

        # print(20*"=")
        # print(nama)
        # print(detail)
        # print(20*"=")
    
    
    print(request.method)
    query = f"select * from buah"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    data = ["apel", "pear", "anggur", "jeruk", "belimbing", "kelengkeng"]
    return render_template("index.html", context=data)

@app.route("/detail/<buah_id>")
def detail(buah_id):
    conn = psycopg2.connect(
            host="localhost",
            database="contoh",  
            user="postgres",
            password="allah1"
)
    curs = conn.cursor()
    query = f"select * from buah where id = {buah_id}"
    curs.execute(query)
    data = curs.fechthone()
    conn.commit()
    curs.close()
    conn.close()
    print(data)
    return render_template("detail.html", context=data)

    @app.route("/detail/<buah_id>")
def detail(buah_id):
    conn = psycopg2.connect(
            host="localhost",
            database="contoh",  
            user="postgres",
            password="allah1"
)
    curs = conn.cursor()
    query = f"select * from buah where id = {buah_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    print(data)
    return redirect("/")

if __name__ == "__main__":
    app.run()
