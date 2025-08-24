import csv
from flask import render_template, current_app
from . import main

@main.route("/")
def index():
    csv_path = current_app.config["CSV_PATH"]
    services = []
    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                services.append(row)
    except FileNotFoundError:
        pass
    return render_template("index.html", services=services)