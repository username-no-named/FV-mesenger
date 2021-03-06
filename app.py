from flask import Flask, render_template, request
import json
import os


app = Flask(__name__, template_folder=os.getcwd())

@app.route("/", methods=['GET', 'POST'])
def index():
    log = ""
    if request.method == 'POST':
        if request.form.get("register_name"):  # мне кажется странным такой способ определения, но в основном я вижу такое
            login, password, confirm = request.form.values()
            if password != confirm:
                return "Пароли не совпадают!"
            with open("database.json", "r") as file:
                data = json.load(file)
                if data.get(login):
                    return "Такой аккаунт уже существует"
            data[login] = password
            with open("database.json", "w") as file:
                json.dump(data, file)
            return "Успех"
        elif request.form.get("login"):
            login, password = request.form.values()
            with open("database.json", "r") as file:  # вообще файлы можно открыть один раз в начале кода и потом использовать
                data = json.load(file)
            if not data.get(login):
                return "Не зарегистрирован"
            if data.get(login) != password:
                return render_template("index.html",log='password_incorrect!')
            return ("Успех")
    return render_template("index.html")

#app.run()
if __name__ == "__main__":
   from waitress import serve
    serve(app, host="https://fv-mesenger.herokuapp.com/", port=int(os.environ.get('PORT', 8080)))