# coding = utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', subject="안녕하세요. 반갑습니다.")

if __name__ == "__main__":
    app.run()
