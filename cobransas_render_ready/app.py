from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/agregar', methods=['POST'])
def agregar():
    monto = request.form.get("monto")
    metodo = request.form.get("metodo")
    return f"Agregado: {monto} Gs - Método: {metodo}"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
