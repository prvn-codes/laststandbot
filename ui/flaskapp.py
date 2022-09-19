from flask import Flask, render_template
import api.challonge as ch

app = Flask("__name__", template_folder="./ui/template")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088, debug=True)
