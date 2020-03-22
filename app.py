from os import environ

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    try:
        dato = environ["HOME"]
    except:
         return "hola VE no encontrado"
    else:
        return dato


if __name__ == '__main__':
  app.run()
