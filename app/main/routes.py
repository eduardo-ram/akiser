import csv
import os
from flask import render_template, current_app, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
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

@main.route("/services")
def services():
    csv_path = current_app.config["CSV_PATH"]
    services = []
    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                services.append(row)
    except FileNotFoundError:
        pass
    return render_template("services.html", services=services)

@main.route("/add", methods=["POST"])
def add_service():
    csv_path = current_app.config["CSV_PATH"]
    nome = request.form.get("nome")
    servico = request.form.get("servico")
    descricao = request.form.get("descricao")
    contato = request.form.get("contato")
    valor = request.form.get("valor")
    file = request.files.get("imagem")

    if not all([nome, servico, descricao, contato, valor, file]):
        return redirect(url_for("main.index"))

    filename = secure_filename(file.filename)
    save_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    file.save(save_path)

    file_exists = os.path.isfile(csv_path)
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["nome", "servico", "descricao", "contato", "imagem", "valor"])
        writer.writerow([nome, servico, descricao, contato, filename, valor])

    return redirect(url_for("main.index"))

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

@main.app_errorhandler(500)
def internal_error(e):
    return render_template("error.html"), 500
