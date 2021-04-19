from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/game/<game_name>')
def game(game_name):
    return 'You picked %s' % game_name

if __name__ == '__main__':
   app.run(debug=True)