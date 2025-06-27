from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    rezepte = [
        {"titel": "Tomatensuppe", "bild": "suppe.jpg"},
        {"titel": "Spaghetti Bolognese", "bild": "spaghetti.jpg"},
        {"titel": "Pfannkuchen", "bild": "pfannkuchen.jpg"},
    ]
    return render_template("index.html", rezepte=rezepte)
