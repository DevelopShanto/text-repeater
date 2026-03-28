from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    repeated_text = ""
    if request.method == "POST":
        text = request.form.get("text")
        try:
            count = int(request.form.get("count"))
        except:
            count = 1
        
        if count > 1000: count = 1000 # লিমিট ১০০০
        
        # টেক্সটটি সংখ্যা অনুযায়ী রিপিট করা
        repeated_text = (text + "\n") * count
        
    return render_template("index.html", repeated_text=repeated_text)

if __name__ == "__main__":
    app.run(debug=True)
