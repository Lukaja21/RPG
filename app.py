from flask import Flask, render_template, request
from generators import (loot_generator, shop_generator,
                        npc_generator, quest_generator, item_search, battle, town_generator)

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/quest_generator')
def quest_page():
    try:
        return render_template('quest_page.html', quest=quest_generator(request.args['quest_type']))
    except:
        return 'Error'


@app.route('/loot_generator')
def loot_page():
    try:
        return render_template('loot_page.html', loots=list(loot_generator(request.args['grade'], int(request.args['amount']), int(request.args['itemcount']))))

    except:
        return 'Error'


@app.route('/npc_generator')
def npc_page():
    try:
        return render_template('npc_page.html', npc=npc_generator())

    except:
        return 'Error'


@app.route('/shop_generator')
def shop_page():
    try:
        return render_template('shop_page.html', shops=list(shop_generator(request.args['type'])))

    except:
        return 'Error'

@app.route('/item_search')
def item_page():
    try:
        return render_template('items_page.html', items=list(item_search(request.args['answer'])))
    
    except:
        return 'Error'

@app.route('/battle')
def battle_page():
    try:
        return render_template('battle_page.html', battles=list(battle(int(request.args['enemy_health']), int(request.args['enemy_attack']), int(request.args['enemy_defense']), int(request.args['enemy_speed']), int(request.args['enemy_crit']), int(request.args['health']), int(request.args['attack']), int(request.args['defense']), int(request.args['speed']), int(request.args['crit']))))

    except:
        return 'Error'

@app.route('/town_generator')
def town_page():
    return render_template('town_page.html', towns=town_generator())

if __name__ == '__main__':
    app.run()
