import json
import random

stuff = json.load(open('Rpgstuff.json'))
stuff2=json.load(open('loot.json'))
stuff3=json.load(open('grades.json'))
stuff4=json.load(open('quest.json'))
stuff5=json.load(open('npc.json'))
stuff6=json.load(open('items.json'))

def loot_generator(grade, quantity, quantity2):
	if grade == 'Bad':
		price=10
	if grade == 'Normal':
		price=25
	if grade == 'Good':
		price=40
	for x in range(quantity2):
		while True:
			h=quantity+random.randint(-2,2)
			if h < 1:
				h=quantity+random.randint(-2,2)
			else:
				break;
		while True:
			p = price+random.randint(-20,20)
			if p < 1:
				p = price+random.randint(-20,20)
			else:
				break;
		print(h, random.choice(list(stuff3[grade])), random.choice(stuff2)+':', p)

def shop_generator(Type):
	items = random.sample(list(stuff[Type]), random.randint(5,15))
	try:
		for item in items:
			while True:
				h=stuff[Type][item] + random.randint(-5, 5)
				if h < 1:
					h=stuff[Type][item] + random.randint(-5, 5)
				else:
					break;
		print('{} - {}: {}'.format(items.index(item) + 1, item, h))
	except KeyError:
		print('Not a valid shop type')

def quest_generator(Quest):
	if Quest == 'Battle':
		print(random.choice(list(stuff4['Intro']))+", "+random.choice(list(stuff4['Attention']))+". "+random.choice(list(stuff4['Problem'])), random.choice(list(stuff4['Adjective'])), random.choice(list(stuff4['Monster']))+'. '+random.choice(list(stuff4['Comewith'])), random.choice(list(stuff4['Careful']))+'. '+random.choice(list(stuff4['Kill'])), random.choice(list(stuff4['Reward'])), random.choice(list(stuff4['Final'])))
	elif Quest == 'Gather':
		print(random.choice(list(stuff4['Gatherintro']))+". "+random.choice(list(stuff4['Quest'])), random.choice(list(stuff4['Gatherreward'])), random.choice(list(stuff4['Gatherfinal'])))

class itemp:
	def __init__(self, Name, Description, Stat_bonuses, Edible, Equippable, Other_Stuff, lvl):
		self.Name = Name
		self.Description = Description
		self.Stat_bonuses = Stat_bonuses
		self.Edible = Edible
		self.Equippable= Equippable
		self.Other_Stuff = Other_Stuff
		self.lvl = lvl
		self.Quantity= 1

class player:
	def __init__(self,name, hp, strength, defense, speed, mana, dexterity):
		self.xp=0
		self.lvl=1
		self.hp = hp
		self.inventory = {}
		self.name=name
		self.coins=100
		self.weapon=None
		self.helmet=None
		self.chest=None
		self.legs=None
		self.boots=None
		self.strength=strength
		self.defense=defense
		self.speed=speed
		self.mana=mana
		self.dexterity=dexterity
		self.skills={'Charisma':1, 'Stealth':1, 'Knowledge':1, 'Wisdom':1, 'Luck':1}

def character_loader():
	Me2=json.load(open('character.json'))
	Me = player(Me2['name'], Me2['hp'], Me2['strength'], Me2['defense'], Me2['speed'], Me2['mana'], Me2['dexterity'])
	Me.inventory = Me2['inventory']
	Me.coins = Me2['coins']
	Me.xp = Me2['xp']
	Me.weapon = Me2['weapon']
	Me.helmet = Me2['helmet']
	Me.chest = Me2['chest']
	Me.legs = Me2['legs']
	Me.boots = Me2['boots']
	Me.skills=Me2['skills']
	return Me

def character_saver(Me=None):
	c=open('character.json', 'w');c.write(json.dumps(Me.__dict__, indent=4));c.close();

def npc_generator():
	print("NPC:\nRace: "+random.choice(list(stuff5['Race']))+"\nManners: "+random.choice(list(stuff5['Manners']))+"\nIntelligence: "+random.choice(list(stuff5['Intelligence']))+"\nPhysical Strength: "+random.choice(list(stuff5['Physical Strength']))+"\nInfluence: "+random.choice(list(stuff5['Influence']))+"\nReligious: "+random.choice(list(stuff5['Religious']))+"\nSocial Ranking: "+random.choice(list(stuff5['Social Ranking']))+"\nWealth: "+random.choice(list(stuff5['Wealth'])))