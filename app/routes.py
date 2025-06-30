from flask import Flask, render_template, abort

app = Flask(__name__)

rezepte = [
    {
        "slug": "tomatensuppe",
        "titel": "Tomatensuppe",
        "bild": "suppe.jpg",
        "zubereitung": "Tomaten klein schneiden, mit Zwiebeln und Knoblauch andünsten, pürieren und würzen."
    },
    {
        "slug": "spaghetti-bolognese",
        "titel": "Spaghetti Bolognese",
        "bild": "spaghetti.jpg",
        "zubereitung": "Hackfleisch anbraten, mit Tomatensoße und Gewürzen köcheln lassen. Mit Spaghetti servieren."
    },
    {
        "slug": "pfannkuchen",
        "titel": "Pfannkuchen",
        "bild": "pfannkuchen.jpg",
        "zubereitung": "Mehl, Milch, Eier verrühren, in der Pfanne goldgelb ausbacken."
    },
]
@app.route("/rezept/<slug>")
def rezept_detail(slug):
    rezept = next((r for r in rezepte if r["slug"] == slug), None)
    if rezept is None:
        abort(404)
    return render_template("rezept_detail.html", rezept=rezept)
