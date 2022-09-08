from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
            host="localhost",
            database="vaksin",  
            user="postgres",
            password="allah1")
    curs = conn.cursor()
    

    if request.method == "POST":
        nama = request.form.get("nama")
        umur = request.form.get("umur")
        jumlah_vaksin = request.form.get("jumlah_vaksin")
        keterangan = request.form.get("keterangan")
        query = f"insert into santri(nama, umur, jumlah_vaksin, keterangan) values('{nama}', '{umur}', '{jumlah_vaksin}', '{keterangan}')"
        curs.execute(query)
        conn.commit()
       
        print(request.method)
    query = f"select * from santri"
    curs.execute(query)
    data = curs.fetchall()
    return render_template("index.html", context=data)

@app.route("/detail/<santri_id>")
def detail (santri_id):
    conn = psycopg2.connect(
            host="localhost",
            database="vaksin",  
            user="postgres",
            password="allah1"
)

    curs = conn.cursor()
    query = f"select * from santri where id = {santri_id}"
    curs.execute(query)
    data = curs.fatchone()
    curs.close()
    conn.close()
    print(data)
    return render_template("index.html", context=data)

@app.route("/delete/<santri_id>")
def delete(santri_id):
    conn = psycopg2.connect(
            host="localhost",
            database="vaksin",  
            user="postgres",
            password="allah1"
)

    curs = conn.cursor()
    query = f"delete * from santri where id = {santri_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect ("/")

@app.route("/update/<santri_id>", methods=["GET", "POST"])
def update (santri_id):
    conn = psycopg2.connect(
            host="localhost",
            database="vaksin",  
            user="postgres",
            password="allah1"
)

    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        umur = request.form.get("umur")
        jumlah_vaksin = request.form.get("jumlah_vaksin")
        keterangan = request.form.get("keterangan")
        query = f"update santri set nama = '{nama}', umur = '{umur}', jumlah_vaksin = '{jumlah_vaksin}', keterangan = '{keterangan}' where id = {santri_id}"
        curs.execute(query)
        conn.commit()
        # print("data masuk")
        return redirect("/")
    query = f"select *  from santri where id = {santri_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    return render_template("update.html", context=data)

if __name__ == "__main__":
    app.run()