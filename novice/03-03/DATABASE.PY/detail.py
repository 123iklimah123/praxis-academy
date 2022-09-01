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
query = f"select * from siswa where nama='naah'"
curs.execute(query)
data = curs.fetchone()
if not data:
    print("egk ad")
else:
    print("nama:", data[0], "umur:", data[1])