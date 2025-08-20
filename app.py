from flask import Flask, render_template

#CONTROLLER
app = Flask(__name__)


@app.route('/')
def calculadora():
    return render_template('calculadora.html')


if __name__ == '__main__':
    app.run()
