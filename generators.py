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
    for item in random.sample(list(shop[type_.lower().capitalize()]), random.randint(5, 15)):
        price_adjustment = random.randint(-5, 5)
        yield '{} - {} Coins'.format(item, shop[type_.lower().capitalize()][item] + price_adjustment if shop[type_.lower().capitalize()][item] + price_adjustment > 0 else shop[type_.lower().capitalize()][item])


def quest_generator(quest_type):
    if quest_type.lower() == 'battle':
        return '{}, {}. {} {} {} {} {}. {} {}'.format(random.choice(list(quest['Intro'])), random.choice(list(quest['Attention'])), random.choice(list(quest['Problem'])), random.choice(list(quest['Adjective'])), random.choice(list(quest['Monster'])
                                                                                                                                                                                                                                  ), random.choice(list(quest['Comewith'])), random.choice(list(quest['Careful'])), random.choice(list(quest['Kill'])), random.choice(list(quest['Reward'])), random.choice(list(quest['Final'])))
    elif quest_type.lower() == 'gather':
        return '{}. {} {} {}'.format(random.choice(list(quest['Gatherintro'])), random.choice(list(quest['Quest'])), random.choice(list(quest['Gatherreward'])), random.choice(list(quest['Gatherfinal'])))


def npc_generator():
    return {'race': random.choice(list(npc['Race'])),
            'manners': random.choice(list(npc['Manners'])),
            'intelligence': random.choice(list(npc['Intelligence'])),
            'physical_strength': random.choice(list(npc['Physical Strength'])),
            'influence': random.choice(list(npc['Influence'])),
            'religious': random.choice(list(npc['Religious'])),
            'social_ranking': random.choice(list(npc['Social Ranking'])),
            'wealth': random.choice(list(npc['Wealth']))}
