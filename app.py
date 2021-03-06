from flask import Flask, render_template, request
from generators import (loot_generator, shop_generator, quest_generator, item_search, battle, town_generator, dungeon_generator, npc_generator)

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/quest_generator')
def quest_page():
    try:
        return render_template('quest_page.html', quest=quest_generator(request.args['quest_type']), npc=npc_generator())
    
    except Exception:
        return 'Error'


@app.route('/loot_generator')
def loot_page():
    return render_template('loot_page.html', loots=list(loot_generator(request.args['grade'], int(request.args['amount']), int(request.args['itemcount']), request.args['kind'])))

@app.route('/shop_generator')
def shop_page():
    try:
        return render_template('shop_page.html', shops=list(shop_generator(request.args['type'])))

    except Exception:
        return 'Error'

@app.route('/item_search')
def item_page():
    try:
        return render_template('items_page.html', items=list(item_search(request.args['answer'])))
    
    except Exception:
        return 'Error'

@app.route('/battle')
def battle_page():
    try:
        return render_template('battle_page.html', battles=list(battle(int(request.args['enemy_health']), int(request.args['enemy_attack']), int(request.args['enemy_defense']), int(request.args['enemy_speed']), int(request.args['enemy_crit']), int(request.args['health']), int(request.args['attack']), int(request.args['defense']), int(request.args['speed']), int(request.args['crit']))))

    except Exception:
        return 'Error'

@app.route('/town_generator')
def town_page():
    return render_template('town_page.html', towns=town_generator())

@app.route('/dungeon_generator')
def dungeon_page():
    try:
        return render_template('dungeon_page.html', dungeons=list(dungeon_generator(request.args['length'])))
    except Exception:
        return 'Error'

@app.route('/npc_generator')
def npc_page():
    return render_template('npc_page.html', npc=npc_generator())

if __name__ == '__main__':
    app.run(host='192.168.1.25')
