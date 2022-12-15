import json

from pathlib import Path

from flask import Flask, jsonify, render_template

config_folder = Path(__file__).parent / "config"
config_folder.mkdir(parents=True, exist_ok=True)

app = Flask(__name__)


@app.get('/')
def hello_world():
    return 'Hello, World!'


@app.get('/list_config')
def get_list_config():
    return render_template('list_config.html', configs=[x.stem for x in config_folder.iterdir() if x.is_file()])


@app.get('/config/<name>')
def get_config(name):
    return jsonify(json.loads(config_folder.joinpath(f"{name}.json").read_text()))


if __name__ == '__main__':
    app.run(debug=True)