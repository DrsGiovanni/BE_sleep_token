from flask import Flask

app = Flask(__name__)

@app.route('/ciao')
def home():
    return 'Benvenuto nel server backend!'

if __name__ == '__main__':
    app.run()

