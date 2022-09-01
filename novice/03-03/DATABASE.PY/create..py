try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="riyan")

except Exception as e:
    print(e)

curs = conn.cursor()
query = f"insert into siswa(nama, umur) values('anggu', 21)"
curs.execute(query)
conn.commit()
print("data masuk")
except Exception as e:
    print(e)


    try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="hda182526")

except Exception as e:
    print(e)

curs = conn.cursor()

nama = 'chenle'
umur = 22
query = f"insert into siswa(nama, umur) values('{nama}', {umur})"
curs.execute(query)
conn.commit()
