from app import app


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_login_success():
    res = client().post("/login", data={"email": "sato@example.com", "password": "password123"})
    assert res.status_code == 302


def test_login_wrong_password():
    res = client().post("/login", data={"email": "sato@example.com", "password": "wrong"})
    assert "パスワードが違います" in res.get_data(as_text=True)
