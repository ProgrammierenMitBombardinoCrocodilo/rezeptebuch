from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

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

@app.route("/")
def home():
    return render_template("index.html", rezepte=rezepte)

@app.route("/neu", methods=["GET", "POST"])
def neues_rezept():
    if request.method == "POST":
        titel = request.form["titel"]
        bild = request.form["bild"]
        zubereitung = request.form["zubereitung"]
        slug = titel.lower().replace(" ", "-")

        neues = {
            "slug": slug,
            "titel": titel,
            "bild": bild,
            "zubereitung": zubereitung
        }

        rezepte.append(neues)
        return redirect(url_for("home"))

    return render_template("neu.html")
