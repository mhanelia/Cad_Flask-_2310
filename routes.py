from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('home.html')


@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/cadastrar')
def cadastrar():

    return render_template('cadastrar.html')

@app.route('/lista')
def lista():
    parent = [{'Nome':'Murilo','Idade':'15','Email':'murilo.aippe@hotmail.com'}]
    return render_template('lista.html', parent_dict=parent)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
