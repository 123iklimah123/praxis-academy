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