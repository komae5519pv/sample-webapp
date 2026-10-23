"""ログイン機能だけを持つ、小さな Web アプリ。"""
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "dev-only-secret"

# デモ用のユーザー（本番ではデータベースに置く）
USERS = {
    "sato@example.com": {"name": "サトウ", "password_hash": generate_password_hash("password123")},
}


@app.route("/")
def index():
    if "email" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", name=USERS[session["email"]]["name"])


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        user = USERS.get(email)
        if user and check_password_hash(user["password_hash"], password):
            session["email"] = email
            return redirect(url_for("index"))
        error = "メールアドレスかパスワードが違います"
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
