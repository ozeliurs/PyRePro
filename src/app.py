import json

from pathlib import Path

from flask import Flask, jsonify, render_template

from pyrepro.site_conf import NginxConf

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


@app.get('/config/<name>/conf')
def get_config_conf(name):
    conf = NginxConf(config_folder.joinpath(f"{name}.conf"))
    conf.load(config_folder.joinpath(f"{name}.json"))
    return f"<pre>{conf.generate()}</pre>"


if __name__ == '__main__':
    app.run(debug=True)