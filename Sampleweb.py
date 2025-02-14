from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("bakedbliss.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":  # Corrected here
    app.run(debug=True)
