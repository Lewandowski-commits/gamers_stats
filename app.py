from flask import Flask, render_template, url_for, redirect, request, flash
from api import *

df = get_all_apps()

app = Flask(__name__)
app.secret_key = '125asf'

@app.route('/')
def hello_world():
    return render_template('searchbar.html')

@app.route('/find', methods=['POST', 'GET'])
def find():
    if request.method == 'POST':
        form_input = request.form['gameName']
        return redirect(url_for('game', game_name = form_input))
    else:
        form_input = request.args.get('gameName')
        return redirect(url_for('game', game_name=form_input))

@app.route('/search/<game_name>')
def game(game_name):
    game_name = game_name.lower()
    filtered_df = df[df['name_lower'].str.contains(game_name)]
    filtered_df = filtered_df.iloc[:,0:1].sort_values('name')

    if filtered_df.shape[0] == 0:
        flash(f'No games match your search: {game_name}')
        return redirect('/')
    else:
        return render_template('searchresults.html',
                               column_names=filtered_df.columns.values,
                               row_data=list(filtered_df.values.tolist()),
                               zip=zip
                               )

if __name__ == '__main__':
   app.run(debug=True)