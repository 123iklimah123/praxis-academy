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
query = f"select * from siswa"
curs.execute(query)
data = curs.fetchall()

for d in data:
    print("nama:", d[0], "umur:", d[1])


try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="hda182526")


    curs = conn.cursor()

    namaLama = ''

    namaBaru = 'mark'
    umurBaru = 24
    query = f"update siswa set nama='{namaBaru}', umur='{umurBaru}' where nama='{namaLama}'"
    curs.execute(query)
    conn.commit()
    print("data msuk")
except Exception as e:
    print(e)