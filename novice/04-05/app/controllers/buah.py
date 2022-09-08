import psycopg2
from flask import request, render_template
def index():
    conn = psycopg2.connect(
            host="localhost",
            database="contoh",  
            user="postgres",
            password="allah1"
    )

    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        detail = request.form.get("detail")
        query = f"insert into buah(nama, detail) values ('{nama}','{detail}')"
        curs.execute(query)
        conn.commit()
       
        # print(20*"=")
        # print(nama)
        # print(detail)
        # print(20*"=")
    
    
    print(request.method)
    query = f"select * from buah"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    # data = ["apel", "pear", "anggur", "jeruk", "belimbing", "kelengkeng"]
    return render_template("index.html", context=data)
