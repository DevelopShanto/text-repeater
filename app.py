from flask import Flask, render_template, request

app = Flask(__name__)

# অক্ষরের শেপ ম্যাপ - বড় অক্ষরের ডিজাইন (বডি তৈরি করার জন্য)
CHARS = {
    'S': [" SSSSS ", "S      ", " SSSS  ", "     S ", "SSSSS  "],
    'H': ["H   H  ", "H   H  ", "HHHHH  ", "H   H  ", "H   H  "],
    'A': ["  A    ", " A A   ", "AAAAA  ", "A   A  ", "A   A  "],
    'N': ["N   N  ", "NN  N  ", "N N N  ", "N  NN  ", "N   N  "],
    'T': ["TTTTT  ", "  T    ", "  T    ", "  T    ", "  T    "],
    'O': [" OOO   ", "O   O  ", "O   O  ", "O   O  ", " OOO   "],
    'I': ["IIIII  ", "  I    ", "  I    ", "  I    ", "IIIII  "],
    'L': ["L      ", "L      ", "L      ", "L      ", "LLLLL  "],
    'V': ["V   V  ", "V   V  ", "V   V  ", " V V   ", "  V    "],
    'E': ["EEEEE  ", "E      ", "EEEEE  ", "E      ", "EEEEE  "],
    'U': ["U   U  ", "U   U  ", "U   U  ", "U   U  ", " UUU   "]
}

def generate_text_art(name, message):
    name = name.upper()
    lines = ["", "", "", "", ""]
    
    for char in name:
        if char in CHARS:
            for i in range(5):
                # অক্ষরের প্রতিটা অংশে মেসেজটি শত বার রিপিট হবে
                styled_line = ""
                for segment in CHARS[char][i]:
                    if segment != " ":
                        # যেখানে অক্ষরের দাগ আছে, সেখানে মেসেজটি বসবে
                        styled_line += message + " "
                    else:
                        # খালি জায়গায় মেসেজের সমান স্পেস (আরও ইউনিক করতে)
                        styled_line += " " * (len(message) + 1)
                
                # ৫টি লাইনে আর্টটি জমা হচ্ছে
                lines[i] += styled_line + "   "
                
    return "\n".join(lines)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        name = request.form.get("name", "")
        message = request.form.get("message", "love")
        # নাম ১-৫ অক্ষরের মধ্যে রাখলে মোবাইল স্ক্রিনে সুন্দর দেখাবে
        result = generate_text_art(name, message)
            
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
