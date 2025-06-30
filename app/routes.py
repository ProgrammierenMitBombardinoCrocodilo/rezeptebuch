from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def home():
    rezepte = [
        {
            "slug": "tomatensuppe",
            "titel": "Tomatensuppe",
            "bild": "suppe.jpg",
            "zubereitung": "Tomaten klein schneiden, mit Zwiebeln und Knoblauch andünsten, pürieren und mit Salz, Pfeffer und Basilikum würzen."
        },
        {
            "slug": "spaghetti-bolognese",
            "titel": "Spaghetti Bolognese",
            "bild": "spaghetti.jpg",
            "zubereitung": "Hackfleisch anbraten, Zwiebeln und Knoblauch dazugeben, Tomatensoße und Gewürze hinzufügen und köcheln lassen. Mit Spaghetti servieren."
        },
        {
            "slug": "pfannkuchen",
            "titel": "Pfannkuchen",
            "bild": "pfannkuchen.jpg",
            "zubereitung": "Mehl, Milch und Eier zu einem Teig verrühren, in der Pfanne goldgelb ausbacken. Mit Zucker, Marmelade oder Nutella servieren."
        },
    ]
    return render_template("index.html", rezepte=rezepte)
