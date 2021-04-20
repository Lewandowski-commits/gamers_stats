from flask import Flask, render_template, url_for, redirect, request, flash
from api import *

df = get_all_apps()

app = Flask(__name__)
app.secret_key = '125asf'

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/find', methods=['POST', 'GET'])
def find():
    if request.method == 'POST':
        form_input = request.form['gameName']
        return redirect(url_for('game', game_name = form_input))
    else:
        form_input = request.args.get('gameName')
        return redirect(url_for('game', game_name=form_input))

@app.route('/game/<game_name>')
def game(game_name):
    app_details_json = get_app_details(game_name)

    return render_template('appiddetails.html',
                           app_details_json=app_details_json)


if __name__ == '__main__':
   app.run(debug=False)