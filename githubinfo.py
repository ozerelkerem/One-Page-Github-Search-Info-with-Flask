from flask import Flask,render_template,request

import requests

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        url = "https://api.github.com/users/"
        githubname = request.form.get("githubname")
        githubinfo = requests.get(url + githubname).json()
        reposinfo = 0
        if not "message" in githubinfo:
            reposinfo = requests.get(githubinfo["repos_url"]).json()
        return render_template("index.html",info = githubinfo, repos = reposinfo)
    else:
        return render_template("index.html")

if(__name__ == "__main__"):
    app.run()