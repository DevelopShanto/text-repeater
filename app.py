from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form.get("text", "")
        count = int(request.form.get("count", 1000))
        # Text 1000 bar repeat hobe niche niche
        result = (text + "\n") * count
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
