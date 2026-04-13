from flask import Flask
import psycopg2

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        dbname="testww",
        user="joachim1",
        password="DatabaseJoachim",
        host="localhost"
    )

@app.route("/")
def index():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("INSERT INTO testww DEFAULT VALUES;")
    conn.commit()

    cur.execute("SELECT COUNT(*) FROM testww;")
    count = cur.fetchone()[0]

    cur.close()
    conn.close()

    return f"Antall rader i testww: {count}"

if __name__ == "__main__":
    app.run(debug=True)