from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__, static_folder=".", static_url_path="")


@app.route("/")
def home():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.environ.get("MYSQL_PASSWORD"),
        database="portfolio_db"
    )

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM projects")

    projects = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("index.html", projects=projects)


if __name__ == "__main__":
    app.run(debug=True)