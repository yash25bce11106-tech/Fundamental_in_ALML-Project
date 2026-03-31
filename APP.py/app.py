from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
# MESSAGE CHECKER
@app.route('/checker', methods=['GET', 'POST'])
def checker():
    result = ""
    if request.method == 'POST':
        msg = request.form['message'].lower()
        scam_words = ["otp", "win", "prize", "urgent", "bank", "link", "click"]
        if any(word in msg for word in scam_words):
            result = "⚠️ Scam Detected!"
        else:
            result = "✅ Looks Safe"
    return render_template('checker.html', result=result)
# URL CHECKER
@app.route('/url', methods=['GET', 'POST'])
def url_checker():
    result = ""
    if request.method == 'POST':
        url = request.form['url']
        if "http" not in url or "@" in url or "bit.ly" in url:
            result = "⚠️ Suspicious URL"
        else:
            result = "✅ Safe URL"
    return render_template('url.html', result=result)
# REPORT SCAM
@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        scam = request.form['scam']
        with open("reports.txt", "a") as f:
            f.write(scam + "\n")
        return "✅ Report Submitted!"
    return render_template('report.html')
# QUIZ
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    result = ""
    if request.method == 'POST':
        answer = request.form['q1']
        if answer == "scam":
            result = "✅ Correct!"
        else:
            result = "❌ Wrong! It was a scam."
    return render_template('quiz.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)
