from flask import Flask, render_template, request
from generators import (loot_generator, shop_generator,
                        npc_generator, quest_generator)

app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello World!'


@app.route('/quest_generator')
def quest_page():
    if request.args['quest_type'].lower() in ['gather', 'battle']:
        return render_template('quest_page.html', quest=quest_generator(request.args['quest_type']))

    else:
        return 'Error'


app.run()
