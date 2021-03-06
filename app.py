import os
import datetime
from flask import Flask, request, render_template
from pymongo import MongoClient


def create_app():
    app = Flask(__name__)
    # client = MongoClient("mongodb+srv://peramvs04:black@microblog.tqzdf.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE")
    # client = MongoClient("mongodb+srv://peramvs04:black@microblog.tqzdf.mongodb.net/test")
    # mongodb+srv://<username>:<password>@cluster0.zecj0.mongodb.net/test
    client = MongoClient("mongodb+srv://peramvs04:black@cluster0.zecj0.mongodb.net/test")

    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%y-%m-%d")
            print(entry_content)
            print(formatted_date)
            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

        for entry in app.db.entries.find({}):
            print(entry)
            print(entry["content"])
            print(entry["date"])
            entries_with_date = [
                (
                    entry["content"],
                    entry["date"],
                    datetime.datetime.strptime(entry["date"], "%y-%m-%d").strftime("%b %d")
                )

            ]

        return render_template("home.html", entries=entries_with_date)

    return app
