from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
            host="localhost",
            database="bendahara",  
            user="postgres",
            password="allah1")
    curs = conn.cursor()
    

    if request.method == "POST":
        tanggal = request.form.get("tanggal")
        keterangan = request.form.get("keterangan")
        pemasukan = request.form.get("pemasukan")
        pengeluaran = request.form.get("pengeluaran")
        saldo = request.form.get("saldo")
        query = f"insert into kas(tanggal, keterangan, pemasukan, pengeluaran, saldo) values('{tanggal}', '{keterangan}', '{pemasukan}', '{pengeluaran}', '{saldo}')"
        curs.execute(query)
        conn.commit()
       
        print(request.method)
    query = f"select * from kas"
    curs.execute(query)
    data = curs.fetchall()
    return render_template("index.html", context=data)

@app.route("/detail/<kas_id>")
def detail (kas_id):
    conn = psycopg2.connect(
            host="localhost",
            database="bendahara",  
            user="postgres",
            password="allah1"
)

    curs = conn.cursor()
    query = f"select * from kas where id = {kas_id}"
    curs.execute(query)
    data = curs.fatchone()
    curs.close()
    conn.close()
    print(data)
    return render_template("index.html", context=data)

@app.route("/delete/<kas_id>")
def delete(kas_id):
    conn = psycopg2.connect(
            host="localhost",
            database="bendahara",  
            user="postgres",
            password="allah1"
)

    curs = conn.cursor()
    query = f"delete * from kas where id = {kas_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect ("/")

@app.route("/update/<kas_id>", methods=["GET", "POST"])
def update (kas_id):
    conn = psycopg2.connect(
            host="localhost",
            database="bendahara",  
            user="postgres",
            password="allah1"
)

    curs = conn.cursor()
    if request.method == "POST":
        tanggal = request.form.get("tanggal")
        keterangan = request.form.get("keterangan")
        pemasukan= request.form.get("pemasukan")
        pengeluaran= request.form.get("pengeluaran")
        saldo = request.form.get("saldo")
        query = f"update kas set tanggal = '{tanggal}',keterangan = '{keterangan}', pemasukan = '{pemasukan}', pengeluaran = '{pengeluaran}', saldo = '{saldo}' where id = {kas_id}"
        curs.execute(query)
        conn.commit()
        # print("data masuk")
        return redirect("/")
    query = f"select *  from kas where id = {kas_id}", 
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    return render_template("update.html", context=data)

if __name__ == "__main__":
    app.run()