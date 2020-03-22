from os import environ

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    try:
        dato = environ["DATABASE_URL"]
    except:
         return "hola Wachin"
    else:
        return dato


if __name__ == '__main__':
  app.run()
