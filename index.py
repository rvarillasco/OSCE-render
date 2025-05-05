from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bienvenido a mi página</h1><p>Este es un ejemplo de un archivo HTML servido con Flask.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
