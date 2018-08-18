import json
import random


with open('./data/grades.json') as grades_file:
    grades = json.load(grades_file)

with open('./data/loot.json') as loot_file:
    loot = json.load(loot_file)

with open('./data/npc.json') as npc_file:
    npc = json.load(npc_file)

with open('./data/quest.json') as quest_file:
    quest = json.load(quest_file)

with open('./data/shop.json') as shop_file:
    shop = json.load(shop_file)

with open('./data/items.json') as items_file:
    items = json.load(items_file)

with open('./data/town.json') as items_file:
    town = json.load(items_file)

with open('./data/dungeon.json') as dungeon_file:
    dungeon = json.load(dungeon_file)

def dungeon_generator(length):
    h = 0
    for x in range(int(length)):
        h = h + 1
        yield 'Room {}: {}'.format(h, random.choice(list(dungeon['dungeons'])))

def loot_generator(grade, amount, itemcount):
    if grade.lower() == 'bad':
        price = 10

    elif grade.lower() == 'normal':
        price = 25

    elif grade.lower() == 'good':
        price = 40

    for x in range(itemcount):
        quant_adjustment = random.randint(-2, 2)
        adjusted_quantity = amount + quant_adjustment if amount + \
            quant_adjustment > 0 else amount

        price_adjustment = random.randint(-20, 20)
        adjusted_price = price + price_adjustment if price + price_adjustment > 0 else price

        item = random.choice(loot)
        item_grade = random.choice(grades[grade.lower().capitalize()])

        yield '{} {} {} - {} Coins'.format(adjusted_quantity, item_grade, item, adjusted_price * adjusted_quantity)


def shop_generator(type_):
    Traits = str(random.choice(list(npc['Traits'])) + ', ' + random.choice(list(npc['Traits'])) + ', ' + random.choice(list(npc['Traits'])))
    yield 'Shop Keeper:'
    yield 'Name: {}'.format(random.choice(list(npc['Names'])))
    yield 'Race: {}'.format(random.choice(list(npc['Race'])))
    yield 'Manners: {}'.format(random.choice(list(npc['Manners'])))
    yield 'Intelligence: {}'.format(random.choice(list(npc['Intelligence'])))
    yield 'Physical Strength: {}'.format(random.choice(list(npc['Physical_Strength'])))
    yield 'Influence: {}'.format(random.choice(list(npc['Influence'])))
    yield 'Religious: {}'.format(random.choice(list(npc['Religious'])))
    yield 'Social Ranking: {}'.format(random.choice(list(npc['Social_Ranking'])))
    yield 'Wealth: {}'.format(random.choice(list(npc['Wealth'])))
    yield 'Dominant Traits: {}'.format(Traits)
    yield 'Profession: {}'.format(random.choice(list(npc['Profession'])))
    yield ''
    yield 'Shop Inventory:'
    for item in random.sample(list(shop[type_.lower().capitalize()]), random.randint(20, 30)):
        price_adjustment = random.randint(-5, 5)
        yield '{} - {} Coins'.format(item, shop[type_.lower().capitalize()][item] + price_adjustment if shop[type_.lower().capitalize()][item] + price_adjustment > 0 else shop[type_.lower().capitalize()][item])

def quest_generator(quest_type):
    if quest_type.lower() == 'battle':
        return '{}, {}. {} {} {} {} {}. {} {}'.format(random.choice(list(quest['Intro'])), random.choice(list(quest['Attention'])), random.choice(list(quest['Problem'])), random.choice(list(quest['Adjective'])), random.choice(list(quest['Monster'])
                                                                                                                                                                                                                                  ), random.choice(list(quest['Comewith'])), random.choice(list(quest['Careful'])), random.choice(list(quest['Kill'])), random.choice(list(quest['Reward'])), random.choice(list(quest['Final'])))
    elif quest_type.lower() == 'gather':
        return '{}. {} {} {}'.format(random.choice(list(quest['Gatherintro'])), random.choice(list(quest['Quest'])), random.choice(list(quest['Gatherreward'])), random.choice(list(quest['Gatherfinal'])))


def npc_generator():
    Traits = str(random.choice(list(npc['Traits'])) + ', ' + random.choice(list(npc['Traits'])) + ', ' + random.choice(list(npc['Traits'])))
    return {'Name': random.choice(list(npc['Names'])),
            'Race': random.choice(list(npc['Race'])),
            'Manners': random.choice(list(npc['Manners'])),
            'Intelligence': random.choice(list(npc['Intelligence'])),
            'Physical_Strength': random.choice(list(npc['Physical_Strength'])),
            'Influence': random.choice(list(npc['Influence'])),
            'Religious': random.choice(list(npc['Religious'])),
            'Social_Ranking': random.choice(list(npc['Social_Ranking'])),
            'Wealth': random.choice(list(npc['Wealth'])),
            'Dominant_Traits': Traits, 
            'Profession': random.choice(list(npc['Profession']))}

def item_search(term):
    for item in items:
        if term.lower() in item.lower():
            yield items[item]

def town_generator():   
    yield "Located {}, {} is a {} {} town that specializes in {}. It's houses are generally built of {} and {}, although some are built of more valuable materials.".format(random.choice(list(town['location'])), random.choice(list(town['names'])), random.choice(list(town['size'])), random.choice(list(town['adjective'])), random.choice(list(town['description'])), random.choice(list(town['material2'])), random.choice(list(town['material'])))
    yield "The town's attractions include a {} {} and a {} {}, both were made under the current ruler {} {} who was elected {}.".format(random.choice(list(town['adjective2'])), random.choice(list(town['attractions'])), random.choice(list(town['adjective2'])), random.choice(list(town['attractions2'])), random.choice(list(town['titles'])), random.choice(list(town['names2'])), random.choice(list(town['elect'])))
    yield "The town's economy is {} and is predicted to {} in the next few years under the current ruler. Meanwhile the political climate is outright {} and studies report the government will soon {} when the opposition party lead by {} {} {}.".format(random.choice(list(town['size'])), random.choice(list(town['growth'])), random.choice(list(town['politics'])), random.choice(list(town['politics2'])), random.choice(list(town['titles'])), random.choice(list(town['names2'])), random.choice(list(town['politics3'])))
    yield 'Population: {}'.format(random.randint(100, 10000))
    yield 'Military Strength: {}'.format(random.choice(list(town['military'])))
    yield 'Crime Rate: {}'.format(random.choice(list(town['crime'])))
    yield ''
    yield 'Local Tavern:'
    yield 'Name: {} {}'.format(random.choice(list(town['Tavern'])), random.choice(list(town['Tavern2'])))
    yield 'Patron(s) 1: {}'.format(random.choice(list(town['patrons'])))
    yield 'Patron(s) 2: {}'.format(random.choice(list(town['patrons'])))
    yield 'Patron(s) 3: {}'.format(random.choice(list(town['patrons'])))
    yield 'Rooms Available: {}.'.format(random.randint(0, 7))
    yield 'Menu:'
    yield '1. {} {}'.format(random.choice(list(town['cook'])), random.choice(list(town['dish'])))
    yield '2. {} {}'.format(random.choice(list(town['cook'])), random.choice(list(town['dish'])))
    yield '3. {} {}'.format(random.choice(list(town['cook'])), random.choice(list(town['dish'])))
    yield '4. {} {}'.format(random.choice(list(town['cook'])), random.choice(list(town['dish'])))
    yield '5. {} {}'.format(random.choice(list(town['cook'])), random.choice(list(town['dish'])))
    yield '6. {} {}'.format(random.choice(list(town['cook'])), random.choice(list(town['dish'])))
    yield '7. {} {}'.format(random.choice(list(town['cook'])), random.choice(list(town['dish'])))
    yield '8. {} {}'.format(random.choice(list(town['cook'])), random.choice(list(town['dish'])))
    yield '9. {} {}'.format(random.choice(list(town['cook'])), random.choice(list(town['dish'])))
    yield '10. {} {}'.format(random.choice(list(town['cook'])), random.choice(list(town['dish'])))
    h = 0
    yield 'Interesting NPCs:'
    for x in range(0,3):
        Traits = str(random.choice(list(npc['Traits'])) + ', ' + random.choice(list(npc['Traits'])) + ', ' + random.choice(list(npc['Traits'])))
        h =  h + 1
        yield ''
        yield 'NPC {}:'.format(h)
        yield 'Name: {}'.format(random.choice(list(npc['Names'])))
        yield 'Race: {}'.format(random.choice(list(npc['Race'])))
        yield 'Manners: {}'.format(random.choice(list(npc['Manners'])))
        yield 'Intelligence: {}'.format(random.choice(list(npc['Intelligence'])))
        yield 'Physical Strength: {}'.format(random.choice(list(npc['Physical_Strength'])))
        yield 'Influence: {}'.format(random.choice(list(npc['Influence'])))
        yield 'Religious: {}'.format(random.choice(list(npc['Religious'])))
        yield 'Social Ranking: {}'.format(random.choice(list(npc['Social_Ranking'])))
        yield 'Wealth: {}'.format(random.choice(list(npc['Wealth'])))
        yield 'Dominant Traits: {}'.format(Traits)
        yield 'Profession: {}'.format(random.choice(list(npc['Profession'])))

def battle(enemy_health, enemy_attack, enemy_defense, enemy_speed, enemy_crit, health, attack, defense, speed, crit):
    while True:
        if enemy_health > 0 and health > 0:
            if enemy_speed > speed:
                
                if defense > enemy_attack:
                    if random.randint(1, 100) > enemy_crit:
                        defense = defense - enemy_attack
                        damage = 0
                        yield 'Enemy attacks for {} damage. Players defense is now {}.'.format(enemy_attack, defense)
                    else:
                        if defense > enemy_attack * 3:
                            defense = defense - enemy_attack * 3
                            yield 'Enemy attacks for {} damage. Players defense is now {}.'.format(enemy_attack * 3, defense)
                        else:
                            damage = enemy_attack * 3 - defense
                            defense = 0
                            yield 'Players defense is broken. Attacking Player...'
                            health = health - damage
                            yield 'Enemy attacks for {} damage and crits, dealing {} damage to Player. Players health is now {}.'.format(enemy_attack * 3, damage, health)
                            if health < 1:
                                yield 'Player dies.'
                                break
                
                else:
                    if random.randint(1, 100) > enemy_crit:
                        damage = enemy_attack - defense
                    else:
                        damage = enemy_attack * 3 - defense
                    defense = 0
                    yield 'Players defense is broken. Attacking Player...'
                    health = health - damage
                    yield 'Enemy attacks for {} damage, dealing {} damage to Player. Players health is now {}.'.format(enemy_attack, damage, health)
                    if health < 1:
                        yield 'Player dies.'
                        break
                
                if enemy_defense > attack:
                    if random.randint(1, 100) > crit:
                        enemy_defense = enemy_defense - attack
                        damage = 0
                        yield "Player attacks for {} damage. Enemy's defense is now {}.".format(attack, enemy_defense)
                    else:
                        if enemy_defense > attack * 3:
                            enemy_defense = enemy_defense - attack * 3
                            yield "Player attacks for {} damage. Enemy's defense is now {}.".format(attack * 3, enemy_defense)
                        else:
                            damage = attack * 3 - enemy_defense
                            enemy_defense = 0
                            yield "Enemy's defense is broken. Attacking Enemy..."
                            enemy_health = enemy_health - damage
                            yield "Player attacks for {} damage and crits, dealing {} damage to Enemy. Enemy's health is now {}.".format(attack * 3, damage, enemy_health)
                            if enemy_health < 1:
                                yield "Enemy dies"
                                break
                
                else:
                    if random.randint(1, 100) > crit:
                        damage = attack - enemy_defense
                    else:
                        damage = attack * 3 - enemy_defense
                    enemy_defense= 0
                    yield "Enemy's defense is broken. Attacking Enemy..."
                    enemy_health = enemy_health - damage
                    yield "Player attacks for {} damage, dealing {} damage to Enemy. Enemy's health is now {}.".format(attack, damage, enemy_health)
                    if enemy_health < 1:
                        yield "Enemy dies"
                        break
            else:
                
                if enemy_defense > attack:
                    if random.randint(1, 100) > crit:
                        enemy_defense = enemy_defense - attack
                        damage = 0
                        yield "Player attacks for {} damage. Enemy's defense is now {}.".format(attack, enemy_defense)
                    else:
                        if enemy_defense > attack * 3:
                            enemy_defense = enemy_defense - attack * 3
                            "Player attacks for {} damage. Enemy's defense is now {}.".format(attack * 3, enemy_defense)
                        else:
                            damage = attack * 3 - enemy_defense
                            enemy_defense = 0
                            yield "Enemy's defense is broken. Attacking Enemy..."
                            enemy_health = enemy_health - damage
                            yield "Player attacks for {} damage and crits, dealing {} damage to Enemy. Enemy's health is now {}.".format(attack * 3, damage, enemy_health)
                            if enemy_health < 1:
                                yield "Enemy dies"
                                break
                
                else:
                    if random.randint(1, 100) > crit:
                        damage = attack - enemy_defense
                    else:
                        damage = attack * 3 - enemy_defense
                    enemy_defense= 0
                    yield "Enemy's defense is broken. Attacking Enemy..."
                    enemy_health = enemy_health - damage
                    yield "Player attacks for {} damage, dealing {} damage to Enemy. Enemy's health is now {}.".format(attack, damage, enemy_health)
                    if enemy_health < 1:
                        yield "Enemy dies"
                        break
                
                if defense > enemy_attack:
                    if random.randint(1, 100) > enemy_crit:
                        defense = defense - enemy_attack
                        damage = 0
                        yield 'Enemy attacks for {} damage. Players defense is now {}.'.format(enemy_attack, defense)
                    else:
                        if defense > enemy_attack * 3:
                            defense = defense - enemy_attack * 3
                            yield 'Enemy attacks for {} damage. Players defense is now {}.'.format(enemy_attack * 3, defense)
                        else:
                            damage = enemy_attack * 3 - defense
                            defense = 0
                            yield 'Players defense is broken. Attacking Player...'
                            health = health - damage
                            yield 'Enemy attacks for {} damage and crits, dealing {} damage to Player. Players health is now {}.'.format(enemy_attack * 3, damage, health)
                            if health < 1:
                                yield 'Player dies.'
                                break
                
                else:
                    if random.randint(1, 100) > enemy_crit:
                        damage = enemy_attack - defense
                    else:
                        damage = enemy_attack * 3 - defense
                    defense = 0
                    yield 'Players defense is broken. Attacking Player...'
                    health = health - damage
                    yield 'Enemy attacks for {} damage, dealing {} damage to Player. Players health is now {}.'.format(enemy_attack, damage, health)
                    if health < 1:
                        yield 'Player dies.'
                        break
        else:
            break
