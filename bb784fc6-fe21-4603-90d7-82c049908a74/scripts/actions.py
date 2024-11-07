# ------------------------------------------------------------------------------
# Constant and Variables Values
# ------------------------------------------------------------------------------
import re
import itertools

shields = []
playerside = None
sideflip = None
diesides = 20
shieldMarker = ('Shield', 'a4ba770e-3a38-4494-b729-ef5c89f561b7')
waitingFunct = []  # Functions waiting for targets. Please replace this with FUNCTIONS waiting for targets later. If a card calls 2 functions both will happen again otherwise
evaluateNextFunction = True #For conditional evaluation of one function after the other, currently only implemented for bounce() in IVT
alreadyEvaluating = False
wscount = 0
arrow = {}
# Start of Automation code

cardScripts = {
	# ON PLAY EFFECTS

	'Alshia, Spirit of Novas': {'onPlay': ['search(me.piles["Graveyard"], 1, "Spell")']},
	'Angila, Electro-Mask': {'onPlay':['waveStriker(`search(me.piles["Graveyard"], 1, "Creature")`, card)']},
	'Aures, Spirit Knight': {'onPlay': ['mana(me.Deck)']},
	'Aqua Bouncer': {'onPlay': ['bounce()']},
	'Aqua Deformer': {'onPlay': ['fromMana(2, "ALL", "ALL", "ALL", True, False, True)']},
	'Aqua Hulcus': {'onPlay': ['draw(me.Deck, True)']},
	'Aqua Hulk': {'onPlay': ['draw(me.Deck, True)']},
	'Aqua Sniper': {'onPlay': ['bounce(2)']},
	'Aqua Surfer': {'onPlay': ['bounce()']},
	'Aqua Trickster': {'onPlay':['waveStriker("tapCreature()", card)']},
	'Armored Decimator Valkaizer': {'onPlay': [' kill(4000)']},
	'Artisan Picora': {'onPlay': ['fromMana(1,"ALL","ALL","ALL",False,True)']},
	'Astral Warper': {'onPlay': ['draw(me.Deck, True, 3)']},
	'Baban Ban Ban, Earth\'s Blessing': {'onPlay': ['massMana(me.Deck, True)']},
	'Ballom, Master of Death': {'onPlay': ['destroyAll(table, True, "ALL", "Darkness", True)']},
	'Bega, Vizier of Shadow': {'onPlay': ['shields(me.Deck)', 'targetDiscard(True)']},
	'Belix, the Explorer': {'onPlay': ['fromMana(1,"Spell")']},
	'Bonfire Lizard': {'onPlay':['waveStriker(\'kill(count=2, rulesFilter="{BLOCKER}")\', card)']},
	'Bronze-Arm Tribe': {'onPlay': ['mana(me.Deck)']},
	'Bronze Chain Sickle': {'onPlay': ['mana(me.Deck)']},
	'Bubble Lamp': {'onPlay': ['draw(me.Deck, True) if len([c for c in me.piles["Graveyard"] if re.search("Bubble Lamp", c.Name)]) > 0 else None']},
	'Buinbe, Airspace Guardian': {'onPlay': ['draw(me.Deck, True)']},
	'Carnival Totem': {'onPlay': ['carnivalTotem()']},
	'Chaos Worm': {'onPlay': [' kill()']},
	'Chief De Baula, Machine King of Mystic Light': {'onPlay': ['search(me.piles["Graveyard"], 1, "Spell")']},
	'Cobalt Hulcus, Aqua Savage': {'onPlay': ['draw(me.Deck, True)']},
	'Corile': {'onPlay': ['bounce(1, True, True)']},
	'Cranium Clamp': {'onPlay': ['craniumClamp()']},
	'Craze Valkyrie, the Drastic': {'onPlay': ['tapCreature(2)']},
	'Crimson Maru, the Untamed Flame': {'onPlay': [' kill(4000)']},
	'Cyber N World': {'onPlay': [' semiReset()']},
	'Dacity Dragoon, Explosive Beast': {'onPlay': ['kill(3000)']},
	'Dandy Eggplant': {'onPlay': ['fromDeck()']},
	'Dark Hydra, Evil Planet Lord': {'onPlay': ['fromGrave()']},
	'Death Mendosa, Death Dragonic Baron': {'onPlay': ['kill("ALL","Untap")']},
	'Dolmarks, the Shadow Warrior': {'onPlay': ['dolmarks()']},
	'Dorballom, Lord of Demons': {'onPlay': ['destroyAll(table, True, "ALL", "Darkness", True)', 'destroyAllMana(table, "Darkness", True)']},
	'Emperor Himiko': {'onPlay': ['draw(me.Deck, True)']},
	'Emeral': {'onPlay': ['emeral(card)']},
	'Emperor Marco': {'onPlay': ['draw(me.Deck, True, 3)']},
	'Estol, Vizier of Aqua': {'onPlay': ['shields(me.Deck)']},
	'Eviscerating Warrior Lumez': {'onPlay':['waveStriker("destroyAll(table, True, 2000)", card)']},
	'Evolution Totem': {'onPlay': [' search(me.Deck, 1, "Evolution Creature")']},
	'Explosive Fighter Ucarn':{'onPlay': ['fromMana(count=2, toGrave=True)']},
	'Factory Shell Q': {'onPlay': [' search(me.Deck, 1, "ALL", "ALL", "Survivor")']},
	'Fighter Dual Fang': {'onPlay': [' mana(me.Deck,2)']},
	'Fist Dragoon': {'onPlay': ['kill(2000)']},
	'Flame Trooper Goliac': {'onPlay':['waveStriker("kill(5000)", card)']},
	'Flameburn Dragon': {'onPlay': ['kill(4000)']},
	'Fonch, the Oracle': {'onPlay': [' tapCreature()']},
	'Forest Sword, Great Hero': {'onPlay': ['mana(me.Deck)']},
	'Fortress Shell': {'onPlay': [' destroyMana(2)']},
	'Forbos, Sanctum Guardian Q': {'onPlay': [' search(me.Deck, 1, "Spell")']},
	'Funky Wizard': {'onPlay': ['funkyWizard()']},
	'Gajirabute, Vile Centurion': {'onPlay': ['burnShieldKill(1)']},
	'Galek, the Shadow Warrior': {'onPlay': ['kill(count=1, rulesFilter="{BLOCKER}")', 'targetDiscard(True)']},
	'Galklife Dragon': {'onPlay': ['destroyAll(table, True, 4000, "Light")']},
	'Gardner, the Invoked': {'onPlay': ['gear("mana")']},
	'Gigargon': {'onPlay': [' search(me.piles["Graveyard"], 2, "Creature")']},
	'Gigabalza': {'onPlay': ['targetDiscard(True)']},
	'Grave Worm Q': {'onPlay': ['search(me.piles["Graveyard"], 1, "ALL", "ALL", "Survivor")']},
	'Gunes Valkyrie, Holy Vizier': {'onPlay': ['tapCreature()']},
	'Gylus, Larval Lord': {'onPlay': ['targetDiscard(True)']},
	'Gyulcas, Sage of the East Wind': {'onPlay': [' search(me.Deck, 1, "Cross Gear")']},
	'Hawkeye Lunatron': {'onPlay': ['search(me.Deck, 1, "ALL", "ALL", "ALL", False)']},
	'Hazaria, Duke of Thorns': {'onPlay': ['waveStriker("opponentSacrifice()", card)']},
	'Honenbe, Skeletal Guardian': {
		'onPlay': ['mill(me.Deck, 3, True)', 'search(me.piles["Graveyard"], 1, "Creature")']},
	'Hormone, Maxim Bronze': {'onPlay': ['mana(me.Deck)']},
	'Hot Spring Crimson Meow': {'onPlay': ['draw(me.Deck, True)']},
	'Hulk Crawler': {'onPlay': ['draw(me.Deck, True)']},
	'Hurlosaur': {'onPlay': [' kill(1000)']},
	'Iron Arm Tribe': {'onPlay': ['mana(me.Deck)']},
	'Izana Keeza': {'onPlay': [' kill(2000)']},
	'Jagila, the Hidden Pillager': {'onPlay':['waveStriker(\'targetDiscard(True, "grave", 3)\', card)']},
	'Jasmine, Mist Faerie': {'onPlay': ['suicide("Jasmine, Mist Faerie", mana, me.Deck)']},
	'Jelly, Dazzling Electro-Princess': {'onPlay': ['draw(me.Deck, True)']},
	'Jenny, the Dismantling Puppet': {'onPlay': [' targetDiscard()']},
	'Jenny, the Suicide Doll': {'onPlay': ['suicide("Jenny, the Suicide Doll", targetDiscard, True)']},
	'Jet R.E, Brave Vizier': {'onPlay': ['shields(me.Deck)']},
	'King Ripped-Hide': {'onPlay': ['draw(me.Deck, True, 2)']},
	'King Muu Q': {'onPlay':['bounce()']},
	'Klujadras': {'onPlay': ['waveStriker("klujadras()", card)']},
	'Kolon, the Oracle': {'onPlay': ['tapCreature()']},
	'Lena, Vizier of Brilliance': {'onPlay': ['fromMana(1,"Spell")']},
	'Lucky Ball': {'onPlay': ['luckyBall()']},
	'Lugias, The Explorer': {'onPlay': ['tapCreature()']},
	'Locomotiver': {'onPlay': ['targetDiscard(True)']},
	'Magris, Vizier of Magnetism': {'onPlay': ['draw(me.Deck, True)']},
	'Magmarex': {'onPlay': ['destroyAll(table, True, 1000,"ALL", False, True)']},
	'Masked Horror, Shadow of Scorn': {'onPlay': ['targetDiscard(True)']},
	'Mechadragon\'s Breath': {'onPlay':['mechadragonsBreath()']},
	'Meteosaur': {'onPlay': ['kill(2000)']},
	'Miele, Vizier of Lightning': {'onPlay': ['tapCreature()']},
	'Moors, the Dirty Digger Puppet': {'onPlay': [' search(me.piles["Graveyard"])']},
	'Muramasa\'s Socket': {'onPlay': [' kill(1000)']},
	'Murian': {'onPlay': ['suicide("Murian", draw, me.Deck)']},
	'Nam=Daeddo, Bronze Style': {'onPlay': ['mana(me.Deck, preCondition=manaArmsCheck("Nature",3))']},
	'Niofa, Horned Protector': {'onPlay': ['search(me.Deck, 1, "ALL", "Nature")']},
	'Ochappi, Pure Hearted Faerie': {'onPlay': ['fromGrave()']},
	'Onslaughter Triceps':{'onPlay': ['fromMana()']},
	'Pakurio': {'onPlay': [' targetDiscard(False,"shield")']},
	'Phal Eega, Dawn Guardian': {'onPlay': ['search(me.piles["Graveyard"], 1, "Spell")']},
	'Phal Pierro, Apocalyptic Guardian': {'onPlay': ['suicide("Phal Pierro, Apocalyptic Guardian", fromGrave, )']},
	'Phal Reeze, Apocalyptic Sage': {'onPlay': ['search(me.piles["Graveyard"], 1, "Spell")']},
	'Piara Heart': {'onPlay': [' kill(1000)']},
	'Pointa, the Aqua Shadow': {'onPlay': ['targetDiscard(True)']},
	'Prometheus, Splash Axe': {'onPlay': ['mana(me.Deck, 2, False, True)']},
	'Punch Trooper Bronks': {'onPlay': ['bronks()']},
	'Qurian': {'onPlay': ['draw(me.Deck, True)']},
	'Raiden, Lightfang Ninja': {'onPlay': ['tapCreature()']},
	'Rayla, Truth Enforcer': {'onPlay': ['search(me.Deck, 1, "Spell")']},
	'Ripple Lotus Q': {'onPlay': ['tapCreature()']},
	'Rom, Vizier of Tendrils': {'onPlay': ['tapCreature()']},
	'Rothus, the Traveler': {'onPlay': ['rothus()']},
	'Romanesk, the Dragon Wizard': {'onPlay': [' mana(me.Deck, 4)']},
	'Rumbling Terahorn': {'onPlay': ['search(me.Deck, 1, "Creature")']},
	'Ryokudou, the Principle Defender': {'onPlay': ['mana(me.Deck,2)', 'fromMana()']},
	'Sarvarti, Thunder Spirit Knight': {'onPlay': ['search(me.piles["Graveyard"], 1, "Spell")']},
	'Saucer-Head Shark':{'onPlay':['bounce(len([c for c in table if int(c.Power.strip("+"))<=2000))]']},
	'Scissor Scarab': {'onPlay': ['search(1,"ALL","ALL","Giant Insect")']},
	'Shtra': {'onPlay': [' fromMana(1, "ALL", "ALL", "ALL", True, False, True)']},
	'Self-Destructing Gil Poser': {'onPlay': ['suicide("Self-Destructing Gil Poser", kill, 2000)']},
	'Sir Navaal, Thunder Mecha Knight': {'onPlay': ['fromMana(1,"Spell")']},
	'Sir Virginia, Mystic Light Insect': {'onPlay': [' search(me.piles["Graveyard"], 1, "Creature")']},
	'Scarlet Skyterror': {'onPlay': ['destroyAll([c for c in table if re.search("\{BLOCKER\}", c.Rules)], True)']},
	'Skyscraper Shell': {'onPlay': ['waveStriker("sendToMana()", card)']},
	'Skysword, the Savage Vizier': {'onPlay': ['mana(me.Deck)', 'shields(me.deck)']},
	'Solidskin Fish': {'onPlay': ['fromMana()']},
	'Spiritual Star Dragon': {'onPlay': ['fromDeck()']},
	'Splash Zebrafish': {'onPlay': ['fromMana()']},
	'Storm Shell':{'onPlay':['stormShell()']},
	'Steamroller Mutant': {'onPlay': ['waveStriker("destroyAll(table, True)", card)']},
	'Syforce, Aurora Elemental': {'onPlay': ['fromMana(1,"Spell")']},
	'Terradragon Zalberg': {'onPlay': [' destroyMana(2)']},
	'Thorny Mandra': {'onPlay': [' fromGrave()']},
	'Thrash Crawler': {'onPlay': [' fromMana()']},
	'Titan Giant': {'onPlay': ['mana (me.Deck, 2, True)']},
	'Torpedo Cluster': {'onPlay': [' fromMana()']},
	'Triple Mouth, Decaying Savage': {'onPlay': ['mana(me.Deck)', 'targetDiscard(True)']},
	'Trombo, Fractured Doll': {'onPlay':['waveStriker(`search(me.piles["Graveyard"], 1, "Creature")`, card)']},
	'Uncanny Turnip': {'onPlay':['waveStriker(["mana(me.Deck)", "fromMana(1,\'Creature\')"], card)']},
	'Unicorn Fish': {'onPlay': ['bounce()']},
	'Vampire Silphy':{'onPlay': ['destroyAll(table, True, 3000)']},
	'Velyrika Dragon': {'onPlay': ['search(me.Deck, 1, "ALL", "ALL", "Armored Dragon")']},
	'Viblo Blade, Hulcus Range': {'onPlay': ['draw(me.Deck, True)']},
	'Walmiel, Electro-Sage': {'onPlay': ['tapCreature()']},
	'Whispering Totem': {'onPlay': ['fromDeck()']},
	'Wind Axe, the Warrior Savage': {'onPlay': ['kill(count=1, rulesFilter="{BLOCKER}")', 'mana(me.Deck)']},
	'Zardia, Spirit of Bloody Winds': {'onPlay': [' shields(me.Deck)']},
	'Zemechis, the Explorer': {'onPlay': [' gear("kill")']},
	
	# ON CAST EFFECTS

	'Abduction Charger': {'onPlay': [' bounce(2)']},
	'Apocalypse Day': {'onPlay': [' destroyAll(table, len([c for c in table if isCreature(c)])>5)']},
	'Apocalypse Vise': {'onPlay':['apocalypseVise()']},
	'Big Beast Cannon': {'onPlay': ['kill(7000)']},
	'Blizzard of Spears': {'onPlay': [' destroyAll(table, True, 4000)']},
	'Bomber Doll': {'onPlay': ['kill(2000)']},
	'Bonds of Justice': {'onPlay': ['tapCreature(1, True, True, filterFunction="not re.search(r\\"{BLOCKER}\\", c.Rules)")']},
	'Bone Dance Charger': {'onPlay': ['mill(me.Deck, 2)']},
	'Boomerang Comet': {'onPlay': ['fromMana()', 'toMana(card)']},
	'Brain Cyclone': {'onPlay': ['draw(me.Deck, False, 1)']},
	'Brain Serum': {'onPlay': [' draw(me.Deck, False, 2)']},
	'Burst Shot': {'onPlay': ['destroyAll(table, True, 2000)']},
	'Cannonball Sling': {'onPlay': ['kill(2000)'],
						 'onMetaMorph': ['kill(6000)']},
	'Chains of Sacrifice': {'onPlay': ['kill("ALL","ALL","ALL",2)', 'sacrifice()']},
	'Clone Factory': {'onPlay': [' fromMana(2)']},
	'Cloned Nightmare': {'onPlay': [' clonedDiscard()']},
	'Comet Missile': {'onPlay':['kill(powerFilter=6000, count=1, rulesFilter="{BLOCKER}")']},
	'Corpse Charger': {'onPlay': [' search(me.piles["Graveyard"], 1, "Creature")']},
	'Crimson Hammer': {'onPlay': ['kill(2000)']},
	'Critical Blade': {'onPlay':['kill(count=1, rulesFilter="{BLOCKER}")']},
	'Cyber Brain': {'onPlay': ['draw(me.Deck, True, 3)']},
	'Crystal Memory': {'onPlay': ['search(me.Deck, 1, "ALL", "ALL", "ALL", False)']},
	'Darkflame Drive': {'onPlay': ['kill("ALL","Untap")']},
	'Dark Reversal': {'onPlay': ['search(me.piles["Graveyard"], 1, "Creature")']},
	'Death Chaser': {'onPlay': ['kill("ALL","Untap")']},
	'Death Cruzer, the Annihilator': {'onPlay': ['destroyAll([c for c in table if c.controller == me and c != card], True)']},
	'Death Gate, Gate of Hell': {'onPlay': ['kill("ALL","Untap")', 'fromGrave()']},
	'Death Smoke': {'onPlay': ['kill("ALL","Untap")']},
	'Decopin Crash': {'onPlay': ['kill(4000)']},
	'Devil Hand': {'onPlay': ['kill()', 'mill(me.Deck, 3, True)']},
	'Devil Smoke': {'onPlay': ['kill("ALL","Untap")']},
	'Dimension Gate': {'onPlay': ['search(me.Deck, 1, "Creature")']},
	'Slash Charger': {'onPlay': ['fromDeckToGrave()']},
	'Dracobarrier': {'onPlay': ['tapCreature()']},
	'Drill Bowgun': {'onPlay': ['gear("kill")']},
	'Emergency Typhoon':{'onPlay':['draw(me.Deck, True, 2)','selfDiscard()'],},
	'Enchanted Soil': {'onPlay': ['fromGrave()']},
	'Energy Stream': {'onPlay': ['draw(me.Deck, False, 2)']},
	'Eureka Charger': {'onPlay': ['draw(me.Deck)']},
	'Eureka Program': {'onPlay': ['eurekaProgram(True)']},
	'Faerie Crystal': {'onPlay': ['mana(me.Deck, postAction="ManaIfCiv", postArgs=["Zero"] )']},
	'Faerie Life': {'onPlay': ['mana(me.Deck)']},
	'Faerie Miracle': {'onPlay': ['mana(me.Deck, postAction="mana(me.Deck)", postCondition="manaArmsCheck()")']},
	'Faerie Shower': {'onPlay': ['lookAtTopCards(2,"card","hand","mana", False)']},
	'Flame-Absorbing Palm': {'onPlay': ['kill(2000)']},
	'Fire Crystal Bomb': {'onPlay': ['kill(5000)']},
	'Flame Lance Trap': {'onPlay': ['kill(5000)']},
	'Flood Valve': {'onPlay': ['fromMana()']},
	'Gardening Drive': {'onPlay': ['mana(me.Deck)']},
	'Gatling Cyclone': {'onPlay': [' kill(2000)']},
	'Geo Bronze Magic': {'onPlay': ['mana(me.Deck, postAction="DrawIfCiv", postArgs=["Fire", "Light"])']},
	'Ghost Clutch': {'onPlay': ['targetDiscard(True)']},
	'Ghost Touch': {'onPlay': ['targetDiscard(True)']},
	'Goren Cannon': {'onPlay': ['kill(3000)']},
	'Goromaru Communication': {'onPlay': ['search(me.Deck, 1, "Creature")']},
	'Hell Chariot': {'onPlay': ['kill("ALL","Untap")']},
	'Hide and Seek': {'onPlay': ['bounce(1, True, condition = \'not re.search("Evolution", card.Type)\')', 'targetDiscard(True)']},
	'Hogan Blaster': {'onPlay': ['drama(True, "creature or spell", "battlezone", "top")']},
	'Holy Awe': {'onPlay': ['tapCreature(1,True)']},
	'Hopeless Vortex': {'onPlay': ['kill()']},
	'Hyperspatial Storm Hole': {'onPlay': ['kill(5000)']},
	'Hyperspatial Bolshack Hole': {'onPlay': ['kill(5000)']},
	'Hyperspatial Kutt Hole': {'onPlay': ['kill(5000)']},
	'Hyperspatial Guard Hole': {'onPlay': ['sendToShields()']},
	'Hyperspatial Vice Hole': {'onPlay': [' targetDiscard()']},
	'Hyperspatial Shiny Hole': {'onPlay': ['tapCreature()']},
	'Hyperspatial Energy Hole': {'onPlay': ['draw(me.Deck, False, 1)']},
	'Hyperspatial Faerie Hole': {'onPlay': ['mana(me.Deck)']},
	'Hyperspatial Revive Hole': {'onPlay': ['search(me.piles["Graveyard"], 1, "Creature")']},
	'Illusionary Merfolk': {'onPlay': ['draw(me.Deck, True, 3) if len([c for c in table if isCreature(c) and not isBait(c) and c.owner == me and re.search("Cyber Lord", c.Race)]) > 0 else None']},
	'Infernal Smash': {'onPlay': ['kill()']},
	'Intense Vacuuming Twist': {'onPlay': ['lookAtTopCards(5, "card", "hand", "bottom", True, "BOUNCE", ["Fire", "Nature"])', 'bounce(conditionalFromLastFunction=True)']},
	'Invincible Abyss': {'onPlay': ['destroyAll([c for c in table if c.owner != me], True)']},
	'Invincible Aura': {'onPlay': ['shields(me.Deck, 3, True)']},
	'Invincible Technology': {'onPlay': ['search(me.Deck, len(me.Deck))']},
	'Lifeplan Charger': {'onPlay': ['lookAtTopCards(5, "Creature")']},
	'Lightning Charger': {'onPlay': ['tapCreature()']},
	'Like a Rolling Storm': {'onPlay': ['mill(me.Deck, 3, True)', 'search(me.piles["Graveyard"], 1, "Creature")']},
	'Lionic Phantom Dragon\'s Flame': {'onPlay': [' kill(2000)']},
	'Living Lithograph': {'onPlay': ['mana(me.Deck)']},
	'Logic Cube': {'onPlay': ['search(me.Deck, 1, "Spell")']},
	'Logic Sphere': {'onPlay': ['fromMana(1, "Spell")']},
	'Lost Soul': {'onPlay': ['discardAll()']},
	'Mana Crisis': {'onPlay': ['destroyMana()']},
	'Martial Law': {'onPlay': ['gear("kill")']},
	'Magic Shot - Arcadia Egg': {'onPlay': ['kill("ALL","Untap")']},
	'Magic Shot - Chain Spark': {'onPlay': ['tapCreature()']},
	'Magic Shot - Open Brain': {'onPlay': ['draw(me.Deck, False, 2)']},
	'Magic Shot - Panda Full Life': {'onPlay': ['mana(me.Deck)']},
	'Magic Shot - Soul Catcher': {'onPlay': [' search(me.piles["Graveyard"], 1, "Creature")']},
	'Magic Shot - Sword Launcher': {'onPlay': [' kill(3000)']},
	'Mana Bonanza': {'onPlay': ['massMana(me.Deck, False)']},
	'Miraculous Plague': {'onPlay':['miraculousPlague()']},
	'Miraculous Rebirth': {'onPlay': ['miraculousRebirth()']},
	'Miraculous Snare': {'onPlay': ['sendToShields(1, False)']},
	'Moonlight Flash': {'onPlay': ['tapCreature(2)']},
	'Morbid Medicine': {'onPlay': ['search(me.piles["Graveyard"], 2, "Creature")']},
	'Mystery Cube': {'onPlay': ['drama()']},
	'Mystic Dreamscape': {'onPlay': ['fromMana(3)']},
	'Mystic Inscription': {'onPlay': ['shields(me.Deck)']},
	'Natural Snare': {'onPlay': ['sendToMana()']},
	'Persistent Prison of Gaia': {
		'onPlay': ['bounce(1, True, condition = \'not re.search("Evolution", card.Type)\')', 'targetDiscard(True)']},
	'Phantom Dragon\'s Flame': {'onPlay': [' kill(2000)']},
	'Phantasm Clutch': {'onPlay': ['kill("ALL","Tap")']},
	'Pixie Cocoon': {'onPlay': ['fromMana(1, "Creature")','toMana(card)']},
	'Pixie Life': {'onPlay': ['mana(me.Deck, 1, False, False)', 'fromMana(1, "ALL", "Zero")']},
	'Primal Scream': {'onPlay': ['mill(me.Deck, 4, True)', 'search(me.piles["Graveyard"], 1, "Creature")']},
	'Proclamation of Death': {'onPlay': ['opponentSacrifice()'] },
	'Punish Hold': {'onPlay': ['tapCreature(2)']},
	'Purgatory Force': {'onPlay': ['search(me.piles["Graveyard"], 2, "Creature")']},
	'Rain of Arrows': {'onPlay': ['lookAtHandAndDiscardAll(filterFunction="re.search(r\\"Darkness\\",c.Civilization) and re.search(r\\"Spell\\",c.Type)")']},
	'Reap and Sow': {'onPlay': ['destroyMana()', 'mana(me.Deck)']},
	'Reaper Hand': {'onPlay': ['kill()']},
	'Reflecting Ray': {'onPlay': ['tapCreature()']},
	'Reverse Cyclone': {'onPlay': ['tapCreature()']},
	'Riptide Charger': {'onPlay': [' bounce()']},
	'Scheming Hands': {'onPlay':['lookAtHandAndDiscard()']},
	'Skeleton Vice': {'onPlay': ['targetDiscard(True, "grave", 2)']},
	'Samurai Decapitation Sword': {'onPlay': [' kill(5000)']},
	'Screaming Sunburst': {'onPlay': ['tapCreature(1, True, True, filterFunction="not re.search(r\\"Light\\", c.Civilization)")']},
	'Screw Rocket': {'onPlay': ['gear("kill")']},
	'Seventh Tower': {'onPlay': ['mana(me.Deck)'],
					  'onMetamorph': ['mana(me.Deck,3)']},
	'Searing Wave': {'onPlay': ['burnShieldKill(1, True, 3000, "ALL", False)']},
	'Solar Grace': {'onPlay': ['tapCreature()']},
	'Solar Ray': {'onPlay': ['tapCreature()']},
	'Solar Trap': {'onPlay': ['tapCreature()']},
	'Soulswap': {'onPlay': ['soulSwap()']},
	'Spastic Missile': {'onPlay': [' kill(3000)']},
	'Spiral Drive': {'onPlay': ['bounce()']},
	'Spiral Gate': {'onPlay': ['bounce()']},
	'Spiral Lance': {'onPlay': ['gear("bounce")']},
	'Stronghold of Lightning and Flame': {'onPlay': ['kill(3000)', 'tapCreature()']},
	'Super Burst Shot': {'onPlay': [' destroyAll([c for c in table if c.owner != me], True, 2000)']},
	'Super Infernal Gate Smash': {'onPlay': ['kill()']},
	'Super Spark': {'onPlay': ['tapCreature(1,True)']},
	'Teleportation': {'onPlay': ['bounce(2)']},
	'Ten-Ton Crunch': {'onPlay': ['kill(3000)']},
	'Terror Pit': {'onPlay': ['kill("All")']},
	'The Strong Spiral': {'onPlay': ['bounce()']},
	'The Strong Breath': {'onPlay': ['kill("ALL","Untap")']},
	'Timeless Garden': {'onPlay': ['mana(me.Deck)']},
	'Tornado Flame': {'onPlay': [' kill(4000)']},
	'Transmogrify': {'onPlay': ['killAndSearch(True)']},
	'Triple Brain': {'onPlay': ['draw(me.Deck, False, 3)']},
	'Q-tronic Hypermind': {'onPlay':['draw(me.Deck, True, len(getSurvivorsOnYourTable(False)))']},
	'Ultimate Force': {'onPlay': [' mana(me.Deck, 2)']},
	'Vacuum Ray': {'onPlay': ['tapCreature()']},
	'Valiant Spark': {'onPlay': [' tapCreature()'],
					  'onMetamorph': ['tapCreature(1,True)']},
	'Virtual Tripwire': {'onPlay': ['tapCreature()']},
	'Volcanic Arrows': {'onPlay': ['burnShieldKill(1, True, 6000, 1, False)']},
	'Volcano Charger': {'onPlay': ['kill(2000)']},
	'Wave Rifle': {'onPlay': ['gear("bounce")']},
	'White Knight Spark': {'onPlay': ['tapCreature(1,True)']},
	'Wizard Resurrection': {'onPlay': ['mana(me.Deck)', 'fromMana(1,"Spell")']},
	'XENOM, the Reaper Fortress': {'onPlay': [' targetDiscard(True)']},
	'Zombie Carnival': {'onPlay': ['fromGrave()']},
	'Zombie Cyclone': {'onPlay': [' search(me.piles["Graveyard"], 1, "Creature")']},
	
	# ON DESTROY EFFECTS

	'Akashic First, Electro-Dragon': {'onDestroy': ['toHand(card)']},
	'Akashic Second, Electro-Spirit': {'onPlay': ['draw(me.Deck, True)'],
										'onDestroy': ['toMana(card)']},
	'Aqua Agent': {'onDestroy': ['toHand(card)']},
	'Aqua Knight': {'onDestroy': ['toHand(card)']},
	'Aqua Ranger': {'onDestroy': ['toHand(card)']},
	'Aqua Skydiver': {'onDestroy': [' toHand(card)']},
	'Aqua Soldier': {'onDestroy': ['toHand(card)']},
	'Aqua Warrior': {'onDestroy': [' draw(me.Deck, True, 2)']},
	'Asylum, the Dragon Paladin': {'onDestroy': [' toShields(card)']},
	'Balloonshroom Q': {'onDestroy': ['toMana(card)']},
	'Bat Doctor, Shadow of Undeath': {'onDestroy': [' search(me.piles["Graveyard"], 1, "Creature")']},
	'Bone Piercer': {'onDestroy': ['fromMana(1, "Creature")']},
	'Cetibols': {'onDestroy': [' draw(me.Deck, True)']},
	'Chilias, the Oracle': {'onDestroy': [' toHand(card)']},
	'Coiling Vines': {'onDestroy': ['toMana(card)']},
	'Crasher Burn': {'onDestroy': ['kill(3000)']},
	'Crystal Jouster': {'onDestroy': ['toHand(card)']},
	'Cubela, the Oracle': {'onDestroy': ['tapCreature()']},
	'Death Monarch, Lord of Demons': {'onDestroy': [
		'SummonFromGrave(len([c for c in me.piles["Graveyard"] if not re.search("Evolution",c.type)]),"Creature", "ALL", "Demon Command")']},
	'Dracodance Totem': {'onDestroy': ['fromMana(1,"ALL","ALL","Dragon")', 'toMana(card)']},
	'Fly Lab, Crafty Demonic Tree': {'onDestroy': ['targetDiscard(True)']},
	'Glider Man': {'onDestroy': ['targetDiscard()']},
	'Hammerhead Cluster': {'onDestroy': ['bounce()']},
	'Jewel Spider': {'onDestroy': ['bounceShield()']},
	'Jil Warka, Time Guardian': {'onDestroy': [' tapCreature(2)']},
	'Mighty Shouter': {'onDestroy': ['toMana(card)']},
	'Ouks, Vizier of Restoration': {'onDestroy': [' toShields(card)']},
	'Peace Lupia': {'onDestroy': ['tapCreature()']},
	'Peru Pere, Viral Guardian': {'onDestroy': ['toHand(card)']},
	'Pharzi, the Oracle': {'onDestroy': ['search(me.piles["Graveyard"], 1, "Spell")']},
	'Propeller Mutant': {'onDestroy': ['targetDiscard(True)']},
	'Proxion, the Oracle': {'onDestroy': ['toHand(card)']},
	'Shaman Broccoli': {'onDestroy': ['toMana(card)']},
	'Shout Corn': {'onDestroy': ['toMana(card)']},
	'Solid Horn': {'onDestroy': ['toMana(card)']},
	'Stallob the Lifequasher': {'onDestroy': ['destroyAll(table, True)']},
	'Stubborn Jasper': {'onDestroy': ['toHand(card)']},
	'Red-Eye Scorpion': {'onDestroy': ['toMana(card)']},
	'Revival Soldier': {'onDestroy': ['waveStriker("toHand(card)", card)']},
	'Worm Gowarski, Masked Insect': {'onDestroy': ['targetDiscard(True)']},

	#ON DISCARD FROM HAND 
	
	'Algo Bardiol, Devil Admiral':  {'onDiscard':['toPlayAfterDiscard(card)']},
	'Baiken, Blue Dragon of the Hidden Blade': {'onDiscard':['toPlayAfterDiscard(card)']},
	'Bingole, the Explorer': {'onDiscard':['toPlayAfterDiscard(card)']},
	'Dava Torey, Seeker of Clouds': {'onDiscard':['toPlayAfterDiscard(card)']},
	'Gauss Blazer, Flame Dragon Admiral': {'onDiscard':['toPlayAfterDiscard(card)']},
	'Lanerva Stratus, Poseidon\'s Admiral': {'onDiscard':['toPlayAfterDiscard(card)']},
	'Mecha Admiral Sound Shooter': {'onDiscard':['toPlayAfterDiscard(card)']},
	'Sanfist, the Savage Vizier': {'onDiscard':['toPlayAfterDiscard(card)']},
	'Sephia Parthenon, Spirit Admiral': {'onDiscard':['toPlayAfterDiscard(card)']},
	'Sir Matthias, Ice Fang Admiral': {'onDiscard':['toPlayAfterDiscard(card)']},
	'Terradragon Arque Delacerna': {'onDiscard':['toPlayAfterDiscard(card)']},
	'Yu Wandafor, Phantom Beast Admiral': {'onDiscard':['toPlayAfterDiscard(card)']},
	'Zack Pichi, Winged Dragon Admiral': {'onDiscard':['toPlayAfterDiscard(card)']},

	#ON TAP EFFECTS

	'Bliss Totem, Avatar of Luck': {'onTap': ['fromGrave()']},
	'Charmilia, the Enticer': {'onTap': ['search(me.Deck, TypeFilter="Creature")']},
	'Cosmogold, Spectral Knight': {'onTap': ['fromMana(1, "Spell")']},
	'Deklowaz, the Terminator': {'onTap': ['destroyAll(table, True, 3000)', 'deklowazDiscard()' ]},
	'Rikabu\'s Screwdriver': {'onTap': ['kill(count=1, rulesFilter="{BLOCKER}")']},
	'Rondobil, the Explorer': {'onTap': ['sendToShields(1, False, True)']},
	'Tanzanyte, the Awakener': {'onTap': ['tanzanyte()']},
	'Techno Totem': {'onTap': ['tapCreature()']},
	
	#ON YOUR TURN END EFFECTS

	'Aqua Officer': {'onTurnEnd': ['tapCreature(2, onlyOwn=True)'], 'onTurnStart': ['draw(me.Deck, True, 2)']},
	'Balesk Baj, the Timeburner': {'onTurnEnd': ['toHand(card)']},
	'Ballus, Dogfight Enforcer Q': {'onTurnEnd': ['untap(card, False)']},
	'Bazagazeal Dragon': {'onTurnEnd': ['toHand(card)']},
	'Cutthroat Skyterror': {'onTurnEnd': ['toHand(card)']},
	'Frei, Vizier of Air': {'onTurnEnd':['untap(card)']},
	'Pyrofighter Magnus': {'onTurnEnd': ['toHand(card)']},
	'Ruby Grass': {'onTurnEnd':['untap(card)']},
	'Toel, Vizier of Hope': {'untapAll()'},
	'Urth, Purifying Elemental':{'onTurnEnd':['untap(card)']},

	#ON YOUR TURN START EFFECTS
	'Aloro, War God': {'onTurnStart': ['fromMana(1,"ALL","ALL","ALL",True,True)']},
	'Cosmic Nebula': {'onTurnStart': ['draw(me.Deck, True)']},
	'Cosmoview Lunatron': {'onTurnStart': ['draw(me.Deck, True)']},
	'Wingeye Moth': {'onTurnStart': ['draw(me.Deck, True)']},

	#SILENT SKILL EFFECTS
	'Brad, Super Kickin\' Dynamo': {'silentSkill':['kill(count=1, rulesFilter="{BLOCKER}")']},
	'Flohdani, the Spydroid': {'silentSkill':['tapCreature(2)']},
	'Gazer Eyes, Shadow of Secrets': {'silentSkill':['lookAtHandAndDiscard()']},
	'Hustle Berry': {'silentSkill':['mana(me.Deck)']},
	'Soderlight, the Cold Blade': {'silentSkill':['opponentSacrifice()']},
	'Vorg\'s Engine': {'silentSkill':['destroyAll(table, True, 2000)']},

	# ON SHIELD TRIGGER CHECKS - condtion for a card to be shield trigger(functions used here should ALWAYS return a boolean)
	
	'Awesome! Hot Spring Gallows' : {'onTrigger': ['manaArmsCheck("Water", 3)']},
	'Soul Garde, Storage Dragon Elemental': {'onTrigger': ['manaArmsCheck("Light", 5)']},
	'Sg Spagelia, Dragment Symbol': {'onTrigger': ['manaArmsCheck("Water", 5)']},
	'Zanjides, Tragedy Demon Dragon': {'onTrigger': ['manaArmsCheck("Darkness", 5)']},
	'Mettagils, Passion Dragon': {'onTrigger': ['manaArmsCheck("Fire", 5)']},
	'Traptops, Green Trap Toxickind': {'onTrigger': ['manaArmsCheck("Nature", 5)']},
}

######### Events ##################
def endTurn(args, x=0, y=0):
	mute()
	clearWaitingFuncts()
	nextPlayer = args.player
	if nextPlayer == None or "":
		# normally passed without green button
		currentPlayers = getPlayers()
		if len(currentPlayers) > 1:
			nextPlayer = currentPlayers[1]
		else:
			nextPlayer = me
	if turnNumber() > 0:
		if nextPlayer == me and len(getPlayers()) > 1:
			whisper("You shall not pass the turn to yourself!")
		elif getActivePlayer() != me:
			whisper("It's not your turn")
		else:
			processOnTurnEndEffects()
			notify("{} ends their turn.".format(me))
			remoteCall(nextPlayer, 'untapAll', [table, True])
			nextTurn(nextPlayer, True)
	else:
		# The first turn. Can be passed to anyone.
		nextTurn(nextPlayer, True)

def resetGame():
	mute()
	me.setGlobalVariable("shieldCount", "0")

def onTarget(args): #this is triggered by OCTGN events when any card is targeted or untargeted. Used to continue evaluating functions that are waiting for target
	numberOfTargets = len([c for c in table if c.targetedBy == me])
	if numberOfTargets == 0:
		return
	global alreadyEvaluating
	if waitingFunct and not alreadyEvaluating:
		alreadyEvaluating = True
		evaluateWaitingFunctions()
		alreadyEvaluating = False

def onArrow(args):
	player = args.player
	fromCard = args.fromCard
	toCard = args.toCard
	targeted = args.targeted
	scripted = args.scripted

	if player != me: return
	if isCreature(fromCard):
		global arrow
		if targeted:
			if fromCard in arrow:
				arrow[fromCard].append(toCard)
			else:
				arrow[fromCard] = [toCard]
		else:
			if fromCard in arrow:
					del arrow[fromCard]
				
############################################ Misc utility functions ####################################################################################

def askCard2(list, title="Select a card", buttonText="Select",numberToTake=1):  # askCard function was changed. So using the same name but with the new functionality
#this is for showing a dialog box with the cards in the incoming list. Careful, all cards will be visible, even if they're facedown.
	dlg = cardDlg(list)
	dlg.title = title

	if numberToTake == 0:
		# if this dialog is opened without any card to take, that means it's for rearranging cards.
		dlg.min, dlg.max = 0, 0
		dlg.text = "Card Order(drag to rearrange):"
		dlg.show()
		return dlg.list
	result = dlg.show()

	if result is None:
		return None
	return result[0]

def askYN(text="Proceed?", choices=["Yes", "No"], colorsList = ['#FF0000', '#FF0000', '#FF0000']):
	# this asks a simple Y N question, but Yes or No can be replaced by other words. Returns 1 if yes, 2 for No and 0 if the box is closed
	
	choice = askChoice(text, choices, colorsList)
	return choice

def askNumber(text="Enter a Number", defaultAnswer=1000):
	choice = askInteger(text, defaultAnswer)
	return choice

def getTargetPlayer(text="Pick a player:"):
		playerList = []
		currentPlayers = getPlayers()
		for player in currentPlayers:
			playerList.append(player.name)
		choicePlayer = askChoice(text, playerList)
		if choicePlayer < 1: return
		return currentPlayers[choicePlayer - 1]

def removeIfEvo(card):
	# Will remove passed card from the list of tracked evos/baits
	# returns a list of bait cards if evo was removed
	# returns empty list if not found or bait was removed

	evolveDict = eval(me.getGlobalVariable('evolution'))
	resultList = []
	for evo in evolveDict.keys():
		if evo == card._id:
			for cardID in evolveDict[evo]:
				resultList.append(Card(cardID))
			del evolveDict[evo]
			# notify("Evo removed from evo in dict")
			break
		baitList = evolveDict[evo]
		if card._id in baitList:
			baitList.remove(card._id)
			evolveDict[evo] = baitList
			# notify("Bait removed from evo in dict")
			break
	me.setGlobalVariable('evolution', str(evolveDict))
	return resultList

def antiDiscard(card, sourcePlayer):
	# sourcePlayer = the player trying play the discarding effect, not the target player
	# le anti-discard check. Still WIP.
	return False
	if card in antiDiscardDict:
		# do shit
		notify("Anti-Discard triggered")
	else:
		return False

def waitForTarget():
	whisper("Waiting for targets. Please (re)target...")
	whisper("[Esc to cancel]")
	global alreadyEvaluating 
	alreadyEvaluating = False
	#now wait for user to target - event trigger will run def onTarget
	return

def evaluateWaitingFunctions():
	while len(waitingFunct)>0:
			#notify("{}, {}".format(card,waitingFunct[0][1]))
			card = waitingFunct[0][0]
			waitingForTarget = eval(waitingFunct[0][1]) #stored in the form [card, function]
			if waitingForTarget:
				waitForTarget()
				break #stop evaluating further functions, will start again when target is triggered
			else:
				#notify("DEBUG: card, function deQueued: {}".format(waitingFunct[0]))
				cardBeingPlayed = waitingFunct[0][0]
				del waitingFunct[0] #deQueue
				if len(waitingFunct)==0:
					endOfFunctionality(cardBeingPlayed)
				elif cardBeingPlayed != waitingFunct[0][0]: #the next card is a different one
					endOfFunctionality(cardBeingPlayed)
				#notify("DEBUG: Waiting list is now: {}".format(str(waitingFunct)))

def clearWaitingFuncts():  # clears any pending plays for a card that's waiting to choose targets etc
	if waitingFunct:
		for funct in waitingFunct:
			cardBeingPlayed = waitingFunct[0][0]
			del waitingFunct[0]
			notify("Waiting for target/effect for {} cancelled.".format(cardBeingPlayed))
			if isSpellInBZ(cardBeingPlayed):
				endOfFunctionality(cardBeingPlayed)		
	alreadyEvaluating = False
	evaluateNextFunction = True #this should always be True, unless you're waiting for the next function to evaluate

def manaArmsCheck(civ='ALL5', num=0):
	if civ == 'ALL5':  # check if you have all 5 civs in mana zone
		manaCards = [card for card in table if isMana(card) and card.owner == me]
		civList = ["Fire", "Nature", "Water", "Light", "Darkness"]
		flags = [False] * 5  # one flag for each corresponding civ [False, False, False, False, False]
		for card in manaCards:
			for i in range(0, 5):
				if not flags[i] and re.search(civList[i], card.Civilization):
					flags[i] = True
			if flags[0] and flags[1] and flags[2] and flags[3] and flags[4]:
				return True
		return False
	else:
		manaCards = [card for card in table if isMana(card) and card.owner == me and re.search(civ, card.Civilization)]
		if len(manaCards) >= num:
			return True

def ifRaceInBattleZone(race):
	cardList = [card for card in table if card.owner == me and isCreature(card) and not isBait(card) and re.search(race, card.Race)]

def sort_cardList(cards, sortCiv=True, sortCost=True, sortName=True):
	def _civilization_rank(card_civilization):
		civilization_order = {
    	'Light': 0,
    	'Water': 1,
    	'Darkness': 2,
    	'Fire': 3,
    	'Nature': 4,
		'/': float('inf')
		}

		for civ_name, rank in civilization_order.items():
			if re.search(civ_name, card_civilization):
				return rank
		return float('inf') 

	sorted_list = sorted(cards,key=lambda card: (
		(_civilization_rank(card.Civilization) if sortCiv else float('inf')),
		(card.Cost if sortCost else float('inf')),
		(card.Name if sortName else float('inf')),
		
	))
	return sorted_list

def reverse_cardList(list):
    list.reverse()

def processEvolution(card, targets):
	targetList = [c._id for c in targets]
	evolveDict = eval(
		me.getGlobalVariable("evolution"))  ##evolveDict tracks all cards 'underneath' the evolution creature
	for evolveTarget in targets:  ##check to see if the evolution targets are also evolution creatures
		if evolveTarget._id in evolveDict:  ##if the card already has its own cards underneath it
			if isCreature(evolveTarget):
				targetList += evolveDict[evolveTarget._id]  ##add those cards to the new evolution creature
			del evolveDict[evolveTarget._id]
	evolveDict[card._id] = targetList
	me.setGlobalVariable("evolution", str(evolveDict))
################ Quick card attribute checks ####################

def isCreature(card):
	mute()
	if card in table and not isShield(card) and not card.orientation == Rot180 and not card.orientation == Rot270 and re.search("Creature", card.Type):
		return True
	#by default python functions will return None, which is more or less the same as False

def isSpellInBZ(card):
	mute()
	if card in table and not isShield(card) and not isMana(card) and re.search("Spell", card.Type):
		return True

def isGod(card):
	mute()
	if isCreature(card) and re.search("God", card.Race):
		return True

def isGear(card):
	mute()
	if card in table and not isShield(card) and not isMana(card) and re.search("Cross Gear", card.Type):
		return True

def isFortress(card):
	mute()
	if card in table and not isShield(card) and not isMana(card) and re.search("Fortress", card.Type) and not re.search("Dragheart", card.Type):
		return True

def isMana(card):
	mute()
	if card in table and not isShield(card) and not card.orientation == Rot90 and not card.orientation == Rot0:
		return True

def isShield(card):
	mute()
	if card in table and not card.isFaceUp:
		return True
	elif card in table and card.markers[shieldMarker] > 0:
		return True

def isPsychic(card):
	mute()
	if re.search("Psychic", card.Type) or re.search("Dragheart", card.Type):
		return True

def isBait(card):  # check if card is under and evo(needs to be ignored by most things) This is (probably)inefficient, maybe make a func to get all baits once
	evolveDict = eval(me.getGlobalVariable('evolution'))
	for evo in evolveDict.keys():
		baitList = evolveDict[evo]
		if card._id in baitList:
			return True

def metamorph():
	mute()
	cardList = [card for card in table if isMana(card) and card.owner == me]
	if len(cardList) >= 7:
		return True

def getWaveStrikerCount(player='ALL'):
	mute()
	cardList = []
	if player != 'ALL':
		cardList = [card for card in table if isCreature(card) and card.controller == player and re.search('wave striker', card.Rules, re.IGNORECASE) and not isBait(card)]
	else:
		cardList = [card for card in table if isCreature(card) and re.search('wave striker', card.Rules, re.IGNORECASE) and not isBait(card)]
	return len(cardList)

def getSurvivorsOnYourTable(searchForEffects=True):
	mute()
	if searchForEffects:
		return [card for card in table if isCreature(card) and card.controller == me and re.search('\{SURVIVOR\}', card.Rules) and not isBait(card)]
	else:	
		return [card for card in table if isCreature(card) and card.controller == me and re.search('Survivor', card.Race) and not isBait(card)]

################ Functions used in the Automation dictionaries.####################

def SummonFromGrave(count=1, TypeFilter="ALL", CivFilter="ALL", RaceFilter="ALL",noEvo=True):  # Temporary Fix for not allowing Evolutions
	mute()
	for i in range(0, count):
		if TypeFilter != "ALL" and noEvo:
			cardsInGroup_Type_Filtered = [card for card in me.piles["Graveyard"] if
										  re.search(TypeFilter, card.Type) and not re.search("Evolution", card.type)]
		else:
			cardsInGroup_Type_Filtered = [card for card in me.piles["Graveyard"]]
		if CivFilter != "ALL":
			cardsInGroup_CivandType_Filtered = [card for card in cardsInGroup_Type_Filtered if
												re.search(CivFilter, card.properties['Civilization'])]
		else:
			cardsInGroup_CivandType_Filtered = [card for card in cardsInGroup_Type_Filtered]
		if RaceFilter != "ALL":
			cardsInGroup_CivTypeandRace_Filtered = [card for card in cardsInGroup_CivandType_Filtered if
													re.search(RaceFilter, card.properties['Race'])]
		else:
			cardsInGroup_CivTypeandRace_Filtered = [card for card in cardsInGroup_CivandType_Filtered]
		if len(cardsInGroup_CivTypeandRace_Filtered) == 0: return
		choice = askCard2(cardsInGroup_CivTypeandRace_Filtered, 'Choose a Creature to Summon from the Graveyard',
						  'Graveyard')
		if type(choice) is not Card: break
		toPlay(choice)

def drama(shuffle=True, type='creature', targetZone='battlezone', failZone='mana', conditional=True):
	# drama = getting creatures from top of deck for free, eg. Mystery Cube, Balga Raiser, Hogan Blaster
	mute()
	if shuffle:
		me.Deck.shuffle()
		notify("{} shuffles their deck.".format(me))
	card = me.Deck.top()
	card.isFaceUp = True
	notify("Top card is {}".format(card))
	played = False  # Flag for resolving after shuffle, unused rn
	if type == 'creature':
		success = re.search("Creature", card.Type)
	elif type == 'creature or spell':
		success = re.search("Creature", card.Type) or re.search("Spell", card.Type)
	if success:
		if conditional:
			choice = askYN("Put {} into {}?\n\n {}".format(card.Name, targetZone, card.Rules))
			# more conditions for non-bz to be added?
			if choice == 1:
				toPlay(card)
				played = True
				return
			elif choice == 0: #player closes the window
				failzone = 'backOnTop'
		else:
			toPlay(card)
			played = True
			return
	if failZone == 'mana':
		toMana(card)
	elif failZone == 'hand':
		toHand(card)
	else:
		notify("{} puts {} back on top of deck".format(me, card))
		card.isFaceUp = False

def lookAtTopCards(num, cardType='card', targetZone='hand', remainingZone='bottom', reveal=True, specialaction='NONE', specialaction_civs = []):
	mute()
	notify("{} looks at the top {} Cards of their deck".format(me, num))
	cardList = [card for card in me.Deck.top(num)]
	choice = askCard2(cardList, 'Choose a Card to put into {}'.format(targetZone))
	if type(choice) is Card:
		if not 'NONE' in specialaction:
			card_for_special_action = choice
		if cardType == 'card' or re.search(cardType, choice.Type):
			# use switch instead, when more zones are added here
			if targetZone == 'mana':
				toMana(choice)
			else:
				# to hand is default rn
				toHand(choice, show=reveal)
		else:
			notify("Please select a {}! Action cancelled.".format(cardType))
			return
	else:
		notify("Nothing selected! Action cancelled.")
		return
	cardList = [card for card in me.Deck.top(num - 1)]
	# will it always be 1 card that goes into target zone? Account for more in later upgrades
	if len(cardList) > 1 and remainingZone == 'bottom':
		cardList = askCard2(cardList, 'Rearrange the remaining Cards to put to {}'.format(remainingZone), 'OK', 0)
	for card in cardList:
		if remainingZone == 'mana':
			toMana(card)
		else:
			card.moveToBottom(me.Deck)
			notify("{} moved a card to the bottom of their deck.".format(me))
	if specialaction == "BOUNCE":
		for civs in specialaction_civs:
			if not re.search(civs, card_for_special_action.properties['Civilization']):
				evaluateNextFunction = False

def targetDiscard(randomDiscard=False, targetZone='grave', count=1):
	mute()
	cardList = []
	targetPlayer = getTargetPlayer()
	if not targetPlayer: return
	for i in range(count):
		if randomDiscard:
			remoteCall(targetPlayer, 'randomDiscard', targetPlayer.hand)
			continue
		cardList = [card for card in targetPlayer.hand]
		if me.isInverted: reverse_cardList(cardList)
		cardChoice = askCard2(cardList, "Choose a Card to discard.")
		if type(cardChoice) is not Card:
			notify("Discard cancelled.")
			return
		cardList.remove(cardChoice)
		if targetZone == 'shield':
			whisper("Setting {} as shield.".format(cardChoice))
			remoteCall(targetPlayer, 'toShields', cardChoice)
		elif targetZone == 'grave':
			# do anti-discard check here
			if not remoteCall(targetPlayer, 'antiDiscard', [cardChoice, me]):
				# anti discard will return false if no antiDiscard is available. Remotecalling because...idk might do some things in antiDiscard later.
				# Maybe change it to normal call later, and remoteCall from only inside anti-disc.
				# still WIP
				remoteCall(targetPlayer, 'toDiscard', cardChoice)

def lookAtHandAndDiscard(count=1):
	targetPlayer = getTargetPlayer()
	if not targetPlayer: return
	choices=[]
	cardList = [card for card in targetPlayer.hand]
	if me.isInverted: reverse_cardList(cardList)
	for i in range(count):
		cardChoice = askCard2(cardList, "Choose a Card to discard.")
		if type(cardChoice) is not Card: 
			notify("Discard cancelled.")
			return
		choices.append(cardChoice)
		cardList.remove(cardChoice)
	for choice in choices:
		remoteCall(choice.owner, 'toDiscard', choice)

def lookAtHandAndDiscardAll(filterFunction):
	targetPlayer = getTargetPlayer()
	if not targetPlayer: return
	cardList = [card for card in targetPlayer.hand]
	if me.isInverted: reverse_cardList(cardList)
	askCard2(cardList, "Opponent's Hand. (Close to continue)", numberToTake=0)
	choices = [c for c in cardList if eval(filterFunction)]
	for choice in choices:
		remoteCall(choice.owner, 'toDiscard', choice)

def discardAll():
	mute()
	cardList = []
	targetPlayer = getTargetPlayer()
	if not targetPlayer: return
	cardList = [card for card in targetPlayer.hand]
	for card in cardList:
		remoteCall(targetPlayer, 'toDiscard', card)

def clonedDiscard():
	mute()
	targetPlayer = getTargetPlayer()
	if not targetPlayer: return
	cardList = [card for card in targetPlayer.hand]

	count = 1
	for player in currentPlayers:
		for card in player.piles["Graveyard"]:
			if re.search(card.Name, "Cloned Nightmare"):
				count += 1
	notify("Cloned Nightmares in graves:{}".format(count - 1))

	if remoteCall(targetPlayer, 'antiDiscard', ['GENERALCHECK', me]):
		return

	for i in range(0, count):
		remoteCall(targetPlayer, 'randomDiscard', targetPlayer.hand)

# do some anti-discard inside dat randomdisc function

def fromMana(count=1, TypeFilter="ALL", CivFilter="ALL", RaceFilter="ALL", show=True, toGrave=False, ApplyToAllPlayers=False):
	mute()
	if ApplyToAllPlayers == True:
		playerList = players
	else:
		playerList = [players[0]]  # players[0] is the player calling this function, me
	for player in playerList:
		if TypeFilter != "ALL":
			cardsInGroup_Type_Filtered = [card for card in table if
										  isMana(card) and card.owner == me and re.search(TypeFilter, card.Type)]
		else:
			cardsInGroup_Type_Filtered = [card for card in table if isMana(card) and card.owner == me]
		if CivFilter != "ALL":
			cardsInGroup_CivandType_Filtered = [card for card in cardsInGroup_Type_Filtered if
												re.search(CivFilter, card.properties['Civilization'])]
		else:
			cardsInGroup_CivandType_Filtered = [card for card in cardsInGroup_Type_Filtered]
		if RaceFilter != "ALL":
			cardsInGroup_CivTypeandRace_Filtered = [card for card in cardsInGroup_CivandType_Filtered if
													re.search(RaceFilter, card.properties['Race'])]
		else:
			cardsInGroup_CivTypeandRace_Filtered = [card for card in cardsInGroup_CivandType_Filtered]
		if len(cardsInGroup_CivTypeandRace_Filtered) == 0: return
		if me.isInverted: reverse_cardList(cardsInGroup_CivTypeandRace_Filtered)
		for i in range(0, count):
			choice = askCard2(cardsInGroup_CivTypeandRace_Filtered, 'Choose a Card from the Mana Zone', 'Mana Zone')
			if type(choice) is not Card: break
			cardsInGroup_CivTypeandRace_Filtered.remove(choice)
			if toGrave == True:
				remoteCall(player, "destroy", choice)
			else:
				remoteCall(player, "toHand", [choice, show])

def killAndSearch(play=False, singleSearch=False):
	# looks like this is only used for Transmogrify
	mute()
	cardList = [card for card in table if isCreature(card) and not isBait(card)]
	if len(cardList) == 0: return
	if me.isInverted: reverse_cardList(cardList)
	choice = askCard2(cardList, 'Choose a Creature to destroy')
	if type(choice) is not Card: return
	card = choice
	remoteCall(choice.owner, 'destroy', choice)
	if singleSearch:
		return
	else:
		remoteCall(choice.owner, 'loopThroughDeck', [card, play])

def loopThroughDeck(card, play=False):
	group = card.owner.Deck
	if len(group) == 0: return
	newCard = group[0]
	newCard.isFaceUp = True
	notify("{} reveals {}".format(card.owner, newCard.Name))

	if re.search("Creature", newCard.Type) and not re.search("Evolution Creature", newCard.Type):
		if play == True:
			remoteCall(newCard.owner, 'toPlay', newCard)
			return
		else:
			remoteCall(newCard.owner, 'moveTo', newCard.owner.hand)
			return
	else:
		remoteCall(newCard.owner, 'toDiscard', newCard)
		remoteCall(newCard.owner, 'loopThroughDeck', [card, play])

def eurekaProgram(ask=True):
	mute()
	cardList = [card for card in table if isCreature(card) and not isBait(card) and card.owner == me]
	cardList = [card for card in cardList if not re.search("Psychic", card.Type)]
	if len(cardList) == 0: return
	if me.isInverted: reverse_cardList(cardList)
	choice = askCard2(cardList, 'Choose a Creature to destroy')
	if type(choice) is not Card: return
	originalCost = int(choice.Cost)
	found = False
	destroy(choice)
	notify("Looking for a creature with cost {}...".format(originalCost + 1))

	for card in me.Deck:
		card = me.Deck[0]
		card.isFaceUp = True
		cost = int(card.Cost)
		notify("{} reveals {}".format(me, card))

		if (int(card.Cost) - originalCost) == 1:
			if re.search("Creature", card.Type):
				if not re.search("Evo", card.Type):
					if ask:
						yn = askYN("Put {} into the battle zone?\n\n {}".format(card.Name, card.Rules))
						if yn == 1:
							found = True
							toPlay(card, ignoreEffects=True)
							choice = card
					##add card to resolve list
					break
				else:
					if ask:
						yn = askYN("Put {} into the battle zone?\n\n {}".format(card.Name, card.Rules))
						if yn == 1:
							found = True
							toPlay(card, ignoreEffects=True)
							choice = card
							##add card to resolve list
							card.moveToTable(0, 0)
							align()
					break
		card.moveToBottom(me.Deck)
	for card in me.Deck:
		if card.isFaceUp:
			card.isFaceUp = False
	me.Deck.shuffle()
	notify("{} shuffles their deck.".format(me))
	if found:
		## Temporary fix without a proper resolve list
		toPlay(choice, notifymute=True)
	else:
		notify("No card with cost {} found or action cancelled.".format(originalCost + 1))

def search(group, count=1, TypeFilter="ALL", CivFilter="ALL", RaceFilter="ALL", show=True, x=0, y=0):
	mute()
	if len(group) == 0: return
	dialogText = 'Search a {} to take to hand (1 at a time)'
	for i in range(0, count):
		cardsInGroup = [card for card in group]
		if TypeFilter != "ALL":
			cardsInGroup_Type_Filtered = [card for card in group if re.search(TypeFilter, card.Type)]
			dialogText = dialogText.format(TypeFilter)
		else:
			cardsInGroup_Type_Filtered = [card for card in group]
		if CivFilter != "ALL":
			cardsInGroup_CivandType_Filtered = [card for card in cardsInGroup_Type_Filtered if
												re.search(CivFilter, card.properties['Civilization'])]
		else:
			cardsInGroup_CivandType_Filtered = [card for card in cardsInGroup_Type_Filtered]
		if RaceFilter != "ALL":
			cardsInGroup_CivTypeandRace_Filtered = [card for card in cardsInGroup_CivandType_Filtered if
													re.search(RaceFilter, card.properties['Race'])]
			dialogText = dialogText.format(RaceFilter)
		else:
			cardsInGroup_CivTypeandRace_Filtered = [card for card in cardsInGroup_CivandType_Filtered]
		dialogText = dialogText.format('Card')
		while (True):
			choice = askCard2(sort_cardList(cardsInGroup), dialogText)
			if type(choice) is not Card:
				group.shuffle()
				notify("{} finishes searching their {}.".format(me, group.name))
				return
			if choice in cardsInGroup_CivTypeandRace_Filtered:
				toHand(choice, show)
				break
	group.shuffle()
	notify("{} finishes searching their {}.".format(me, group.name))

def fromDeckToGrave(count=1):
	mute()
	group = []
	targetPlayer = getTargetPlayer()
	if not targetPlayer: return
	group = targetPlayer.deck
	if len(group) == 0: return
	for i in range(0, count):
		cardsInGroup = sort_cardList([card for card in group])
		while (True):
			choice = askCard2(cardsInGroup, 'Search a Card to put to Graveyard (1 at a time)')
			if type(choice) is not Card:
				remoteCall(targetPlayer,'shuffle',group)
				notify("{} finishes searching opponent's {}.".format(me, group.name))
				return
			remoteCall(targetPlayer,'toDiscard',choice)
			update()
			break
	remoteCall(targetPlayer,'shuffle',group)
	update()
	notify("{} finishes searching opponent's {}.".format(me, group.name))

def kill(powerFilter='ALL', tapFilter='ALL', civFilter='ALL', count=1, targetOwn=False, rulesFilter='ALL'):
	mute()
	if powerFilter == 'ALL':	powerFilter = float('inf')
	if targetOwn:
		cardList = [card for card in table if isCreature(card) and not isBait(card) and int(card.Power.strip('+')) <= powerFilter]
	else:
		cardList = [card for card in table if isCreature(card) and not isBait(card) and not card.owner == me and int(card.Power.strip('+')) <= powerFilter]
	if tapFilter != 'ALL':
		if tapFilter == 'Untap':
			cardList = [card for card in cardList if card.orientation == Rot0]
		if tapFilter == 'Tap':
			cardList = [card for card in cardList if card.orientation == Rot90]
	if civFilter != "ALL":
		cardList = [card for card in cardList if re.search(civFilter, card.Civilization)]
	if rulesFilter != 'ALL':
		cardList = [card for card in cardList if re.search(rulesFilter, card.Rules)]
	if len(cardList) == 0:
		whisper("No valid targets on the table.")
		return
	
	count = min(count, len(cardList))
	targets = [c for c in table if c.targetedBy == me and isCreature(c)]
	if len(targets) != count:
		whisper("Wrong number of targets!")
		return True  # return true activates the cardStack/waiting for targets mechanism
	killList = []
	for i in range(0, count):
		if (targets[i] in cardList):
			choice = targets[i]
			killList.append(choice)
		else:
			whisper("Invalid target(s)! Waiting for targets...")
			return True

	for card in killList:
		remoteCall(card.owner, "destroy", card)

def destroyAll(group, condition=False, powerFilter='ALL', civFilter="ALL", AllExceptFiltered=False, exactPower=False, dontAsk=False):
	mute()

	if powerFilter == 'ALL':
		powerfilter = float('inf')
	cardlist = []
	if condition == True:
		if civFilter == "ALL":
			cardList = [card for card in group if isCreature(card) and (int(card.Power.strip('+')) == powerFilter if exactPower else int(card.Power.strip('+')) <= powerFilter)]
		else:
			if AllExceptFiltered:
				cardList = [card for card in group if isCreature(card) and (int(card.Power.strip('+')) == powerFilter if exactPower else int(card.Power.strip('+')) <= powerFilter) 
				and not re.search(civFilter, card.properties['Civilization'])]
			else:
				cardList = [card for card in group if
						isCreature(card) (int(card.Power.strip('+')) == powerFilter if exactPower else int(card.Power.strip('+')) <= powerFilter) 
						and re.search(civFilter, card.properties['Civilization'])]
	else:
		cardList = group
	
	if len(cardList) == 0:
		return
	
	if not dontAsk and condition:
		if askYN('Destroy automatically?') != 1: return
	global wscount
	if not wscount:
		wscount = getWaveStrikerCount()
	
	# We do this to handle survivor/wavestriker effects properly.
	myCardList = [card for card in cardList if card.owner == me and not isBait(card)]
	opponentList = [card for card in cardList if card.owner != me]

	survivors = []
	if any(re.search("Survivor", card.Race) for card in myCardList):
		survivors = getSurvivorsOnYourTable()

	for card in myCardList:
		cardToBeSaved = card
		possibleSavers = [card for card in table if
		cardToBeSaved != card and isCreature(card) and card.owner == me and re.search("Saver",card.rules) and (
			re.search(cardToBeSaved.properties['Race'], card.rules) or re.search(
			"Saver: All Races", card.rules))]
		if len(possibleSavers) > 0:
			if confirm("Prevent {}'s destruction by using a Saver on your side of the field?\n\n".format(
					cardToBeSaved.Name)):
				if me.isInverted: reverse_cardList(possibleSavers)
				choice = askCard2(possibleSavers, 'Choose Saver to destroy')
				if type(choice) is Card:
					toDiscard(choice)
					cardList.remove(choice)
					cardList = [card for card in cardList]
					notify(
						"{} destroys {} to prevent {}'s destruction.".format(me, choice.name, cardToBeSaved.name))
					continue

		toDiscard(cardToBeSaved)
		card = cardToBeSaved  # fix for onDestroy effect, as toDiscard somehow changes card
		
		functionList=[]
		if cardScripts.get(card.Name, {}).get('onDestroy', {}):
			notify('Added {} to {}'.format(cardScripts.get(card.Name).get('onDestroy'), card.Name))
			functionList = cardScripts.get(card.Name).get('onDestroy')
		if re.search("Survivor", card.Race):
			for surv in survivors:
				if surv != card and cardScripts.get(surv.name, {}).get('onDestroy', []):
					notify('Added {} to {}'.format(cardScripts.get(surv.name).get('onDestroy'), card.Name))
					functionList.extend(cardScripts.get(surv.name).get('onDestroy'))
		for function in functionList:
			waitingFunct.append([card, function])
	global alreadyEvaluating
	if not alreadyEvaluating:
		alreadyEvaluating = True
		evaluateWaitingFunctions()
		alreadyEvaluating = False
	if len(opponentList):
		remoteCall(opponentList[0].owner, "destroyAll", [opponentList, False])

def destroyMana(count=1):
	mute()
	for i in range(0, count):
		cardList = [card for card in table if isMana(card) and not card.owner == me]
		if len(cardList) == 0:
			return
		if me.isInverted: reverse_cardList(cardList)
		choice = askCard2(cardList, 'Choose a Mana Card to destroy')
		if type(choice) is not Card:
			return
		remoteCall(choice.owner, "destroy", choice)

def destroyAllMana(group, civFilter="ALL", AllExceptFiltered=False):
	mute()
	cardList = []
	if(civFilter != "ALL"):
			cardList = [card for card in group if isMana(card) and (re.search(civFilter, card.Civilization) != AllExceptFiltered)]
	else: 
		cardList = [card for card in group if isMana(card)]
	if len(cardList) == 0: return
	for card in cardList:
		remoteCall(card.owner, "destroy", card)

def burnShieldKill(count=1, targetOwnSh=False, powerFilter='ALL', killCount=0,
				   targetOwnCr=False):  # Mainly for destroying shields. Kill is optional.
	mute()
	targets = [c for c in table if c.targetedBy == me]
	targetSh = []
	targetCr = []
	for c in targets:
		if isShield(c):
			targetSh.append(c)
		elif isCreature(c):
			targetCr.append(c)

	if killCount == "ALL" or killCount > 0:
		if powerFilter == 'ALL': powerFilter = float('inf')
		validKillTargets = [c for c in table if isCreature(c) and not isBait(card) and int(c.Power.strip(' +')) <= powerFilter]
		if not targetOwnCr:
			validKillTargets = [c for c in validKillTargets if not c.owner == me]
			targetCr = [c for c in targetCr if not c.owner == me]
		if killCount == "ALL":
			targetCr = validKillTargets
			killCount = len(targetCr)
		else:
			killCount = min(killCount, len(validKillTargets))

	myShields = len([c for c in table if isShield(c) and c.owner == me])
	oppShields = len([c for c in table if isShield(c) and c.owner != me])

	if targetOwnSh:
		targetSh = [c for c in targetSh if c.owner == me]
		count = min(count, myShields)
	else:
		targetSh = [c for c in targetSh if c.owner != me]
		count = min(count, oppShields)

	if count == 0 and killCount == 0:  # No shields left to burn, nothing to kill
		whisper("No valid targets.")
		return

	if len(targetSh) != count or len(targetCr) != killCount:
		whisper("Invalid shields and/or creatures targeted.")
		return True  # =>will wait for target

	for shield in targetSh:
		remoteCall(shield.owner, "destroy", [shield, 0, 0, True])
	for card in targetCr:
		remoteCall(card.owner, "destroy", card)

def fromDeck():
	mute()
	notify("{} looks at their Deck.".format(me))
	me.Deck.lookAt(-1)

def fromGrave():
	mute()
	notify("{} looks at their Graveyard.".format(me))
	me.piles['Graveyard'].lookAt(-1)

def lookAtCards(count=1, isTop=True):
	mute()
	if isTop == False:
		notify("{} looks at {} cards from bottom of their deck.".format(me, count))
	notify("{} looks at {} cards from top of their deck.".format(me, count))
	me.Deck.lookAt(count, isTop)

def sacrifice(power=float('inf'), count=1):
	mute()
	for i in range(0, count):
		cardList = [card for card in table if
					isCreature(card) and card.owner == me and re.search("Creature", card.Type)]
		cardList = [card for card in cardList if int(card.Power.strip('+')) <= power]
		if len(cardList) == 0:
			return
		if me.isInverted: reverse_cardList(cardList)
		choice = askCard2(cardList, 'Choose a Creature to destroy')
		if type(choice) is not Card:
			return
		destroy(choice)

def bounce(count=1, opponentOnly=False, toDeckTop=False, condition='True', conditionalFromLastFunction=False):
	mute()
	if count == 0: return
	global evaluateNextFunction
	if conditionalFromLastFunction: #for example in case of Intense Vacuuming Twist
		if not evaluateNextFunction:
			evaluateNextFunction = True
			return
	if opponentOnly:
		cardList = [card for card in table if
					isCreature(card) and card.owner != me and not isBait(card) and eval(condition)]
	else:
		cardList = [card for card in table if
					isCreature(card) and not isBait(card) and eval(condition)]
	if len(cardList) < 1:
		whisper("No valid targets on the table.")
		return
	
	count = min(count, len(cardList))
	targets = [c for c in table if c.targetedBy == me]
	if len(targets) != count:
		return True #forcing octgn to go to targets function and wait

	bounceList = []
	for i in range(0, count):
		if (targets[i] in cardList):
			choice = targets[i]
			bounceList.append(choice)
			whisper("{}.".format(choice))
		else:
			whisper("Wrong target(s)!")
			return True #true return forces wait. The same function is called again when targets change.

	for card in bounceList:
		if toDeckTop:
			remoteCall(card.owner, "toDeck", card)
		else:
			remoteCall(card.owner, "toHand", card)

#for Effects that return shield and don't trigger shield triggers
def bounceShield(count = 1, selfOnly=True):
	mute()
	cardList = []
	if selfOnly:
		cardList = [card for card in table if isShield(card) and card.controller == me]
	else:
		cardList = [card for card in table if isShield(card)]
	if len(cardList) == 0: return
	
	count = min(count, len(cardList))
	targets = [c for c in table if c.targetedBy == me]
	if len(targets) != count:
		return True #forcing octgn to go to targets function and wait

	bounceList = []
	for i in range(0, count):
		if (targets[i] in cardList):
			choice = targets[i]
			bounceList.append(choice)
			whisper("{}.".format(choice))
		else:
			whisper("Wrong target(s)!")
			return True #true return forces wait. The same function is called again when targets change.
		
	for card in bounceList:
		remoteCall(card.owner, "toHand", [card, False])

def gear(str):
	mute()
	if str == 'kill':
		cardList = [card for card in table if isGear(card)
					and not card.owner == me]
		if len(cardList) == 0:
			return
		if me.isInverted: reverse_cardList(cardList)
		choice = askCard2(cardList, 'Choose a Cross Gear to send to Graveyard')
		if type(choice) is not Card:
			return
		remoteCall(choice.owner, 'destroy', choice)
	elif str == 'bounce':
		cardList = [card for card in table if isGear(card)]
		if len(cardList) == 0:
			return
		if me.isInverted: reverse_cardList(cardList)
		choice = askCard2(cardList, 'Choose a Cross Gear to send to Hand')
		if type(choice) is not Card:
			return
		if choice.owner == me:
			toHand(choice)
		else:
			remoteCall(choice.owner, 'toHand', choice)
	elif str == 'mana':
		cardList = [card for card in table if isGear(card)]
		if len(cardList) == 0:
			return
		if me.isInverted: reverse_cardList(cardList)
		choice = askCard2(cardList, 'Choose a Cross Gear to send to Mana')
		if type(choice) is not Card:
			return
		if choice.owner == me:
			toHand(choice)
		else:
			remoteCall(choice.owner, 'toMana', choice)

#Called for Creatures by tapMultiple, which is the same as Ctrl+G or "Tap / Untap"
def processTapUntapCreature(card, processTapEffects = True):
	mute()
	card.orientation ^= Rot90
	if card.orientation & Rot90 == Rot90:
		notify('{} taps {}.'.format(me, card))
		global arrow
		#Tap Effects can only activate during active Player's turn.
		if processTapEffects and getActivePlayer() == me and not isBait(card) and cardScripts.get(card.name, {}).get('onTap', []) and not card in arrow:
			choice = askYN("Activate Tap Effect(s) for {}?\n\n{}".format(card.Name, card.Rules), ["Yes", "No"])
			if choice != 1: return

			notify('{} uses Tap Effect of {}'.format(me, card))
			functionList = cardScripts.get(card.Name).get('onTap')
			# THERE ARE CURRENTLY NO SURVIVORS THAT HAVE TAP ABILITIES.
			for function in functionList:
				waitingFunct.append([card, function])
			global alreadyEvaluating
			if not alreadyEvaluating:
				alreadyEvaluating = True
				evaluateWaitingFunctions()
				alreadyEvaluating = False

				
	else:
		notify('{} untaps {}.'.format(me, card))

def processOnTurnEndEffects():
	cardList = [card for card in table if card.controller == me and isCreature(card) and not isBait(card)]
	survivors = getSurvivorsOnYourTable(False)
	for card in cardList:
		functions = cardScripts.get(card.name, {}).get('onTurnEnd', [])
		if functions:
			functionList = []
			notify('{} acitvates at the end of {}\'s turn'.format(card.Name, me))
			for function in functions:
				functionList.append([card, function])
			#Share your onTurnEnd effect with other survivors.
			if re.search("Survivor", card.Race):
				for surv in survivors:
					if surv != card:
						for function in functions:
							functionList.append([surv, function])
			for function in functionList:
				waitingFunct.append(function)	
	global alreadyEvaluating
	if not alreadyEvaluating:
		alreadyEvaluating = True
		evaluateWaitingFunctions()
		alreadyEvaluating = False

def processOnTurnStartEffects():
	cardList = [card for card in table if card.controller == me and isCreature(card) and not isBait(card)]
	survivors = getSurvivorsOnYourTable(False)
	for card in cardList:
		functions = cardScripts.get(card.name, {}).get('onTurnStart', [])
		if functions:
			functionList = []
			notify('{} acitvates at the start of {}\'s turn'.format(card.Name, me))
			for function in functions:
				functionList.append([card, function])
			#Share your onTurnStart effect with other survivors.
			if re.search("Survivor", card.Race):
				for surv in survivors:
					if surv != card:
						for function in functions:
							functionList.append([surv, function])
			for function in functionList:
				waitingFunct.append(function)	
	global alreadyEvaluating
	if not alreadyEvaluating:
		alreadyEvaluating = True
		evaluateWaitingFunctions()
		alreadyEvaluating = False

def sendToShields(count=1, opponentOnly=True, selfOnly = False):
	mute()
	for i in range(0, count):
		cardList = [card for card in table if isCreature(card) and (
			(opponentOnly and card["owner"] != me) or 
        	(selfOnly and card["owner"] == me) or 
        	(not opponentOnly and not selfOnly))]
		if len(cardList) == 0: return
		if me.isInverted: reverse_cardList(cardList)
		choice = askCard2(cardList, 'Choose a Creature to send to Shields')
		if type(choice) is not Card: return
		remoteCall(choice.owner, "toShields", choice)

def sendToMana(count=1):
	mute()
	for i in range(0, count):
		cardList = [card for card in table if isCreature(card) and card.owner != me]
		if len(cardList) == 0: return
		if me.isInverted: reverse_cardList(cardList)
		choice = askCard2(cardList, 'Choose a Creature to send to Mana Zone')
		if type(choice) is not Card: return
		remoteCall(choice.owner, "toMana", choice)

def sendSelfToMana(count=1):
	mute()
	for i in range(0, count):
		cardList = [card for card in table if isCreature(card) and card.owner == me]
		if len(cardList) == 0: return
		choice = askCard2(cardList, 'Choose a Creature to send to Mana Zone')
		if type(choice) is not Card: return
		remoteCall(choice.owner, "toMana", choice)


def selfDiscard(count=1):
	mute()
	for i in range(count):
		cardList = [card for card in me.hand]
		if me.isInverted: reverse_cardList(cardList)
		cardChoice = askCard2(cardList, "Choose a Card to discard")
		if type(cardChoice) is not Card:
			notify("Discard cancelled.")
			return
			# do anti-discard check here
		toDiscard(cardChoice)
		update()

def toPlayAfterDiscard(card, onlyOnOpponentTurn = True):
	if not onlyOnOpponentTurn or getActivePlayer() != me:
		choice = askYN("Summon {} because it was discarded during opponent's turn?\n\n{}".format(card.Name, card.Rules), ["Yes", "No"])
		if choice == 1:
			toPlay(card) 

def suicide(name, action, arg):
	mute()
	choiceList = ['Yes', 'No']
	colorsList = ['#FF0000', '#FF0000']
	choice = askChoice("Destroy the card to activate effect?", choiceList, colorsList)
	if choice == 0 or choice == 2:
		return
	cardList = [card for card in table if card.name == name and card.owner == me and isCreature(card) ]
	toDiscard(cardList[-1])
	action(arg)

def opponentSacrifice(sacrificeArgs=[]):
	targetPlayer = getTargetPlayer()
	if not targetPlayer: return
	remoteCall(targetPlayer, 'sacrifice', sacrificeArgs)

def tapCreature(count=1, targetALL=False, includeOwn=False, onlyOwn=False, filterFunction="True"):
	mute()
	if targetALL:
		cardList = []
		if onlyOwn:
			cardList = [card for card in table if
						isCreature(card) and card.orientation == Rot0 and card.owner == me and re.search("Creature", card.Type)]
		elif includeOwn == True:
			cardList = [card for card in table if
						isCreature(card) and card.orientation == Rot0 and re.search("Creature", card.Type)]
		else:
			cardList = [card for card in table if
						isCreature(card) and card.orientation == Rot0 and not card.owner == me and re.search("Creature",
																											 card.Type)]
		cardList = [c for c in cardList if eval(filterFunction)]
		if len(cardList) == 0:
			return
		for card in cardList:
			remoteCall(card.owner, "processTapUntapCreature", [card, False])
	else:
		for i in range(0, count):
			cardList=[]
			if onlyOwn:
				cardList = [card for card in table if
							isCreature(card) and card.orientation == Rot0 and card.owner == me and re.search("Creature", card.Type)]
			elif includeOwn == True:
				cardList = [card for card in table if
							isCreature(card) and card.orientation == Rot0 and re.search("Creature", card.Type)]
			else:
				cardList = [card for card in table if
							isCreature(card) and card.orientation == Rot0 and not card.owner == me and re.search(
								"Creature", card.Type)]
			cardList = [c for c in cardList if eval(filterFunction)]
			if len(cardList) == 0:
				return
			if me.isInverted: reverse_cardList(cardList)
			choice = askCard2(cardList, 'Choose a Creature to tap')
			if type(choice) is not Card:
				return
			remoteCall(choice.owner, "processTapUntapCreature", [choice, False])

def semiReset():
	mute()
	if confirm("Are you sure you want to continue?"):
		currentPlayers = getPlayers()
		for player in currentPlayers:
			cardsInHand = [c for c in player.hand]
			cardsInGrave = [c for c in player.piles['Graveyard']]
			if cardsInHand or cardsInGrave:
				for card in cardsInHand:
					remoteCall(player, 'toDeck', card)
				for card in cardsInGrave:
					remoteCall(player, 'toDeck', card)
			remoteCall(player, 'shuffle', player.deck)
			remoteCall(player, 'draw', [player.deck, False, 5])

# Special Card Group Automatization

def waveStriker(functionArray, card):
	if isinstance(functionArray, str):
		functionArray=[functionArray]
	global wscount
	wscount = getWaveStrikerCount()
	if functionArray and wscount >= 3:
		for funct in functionArray:
				waitingFunct.append([card, funct.replace('wscount', repr(wscount))])

#Special Card Automatization

def apocalypseVise():
	powerLeft=8000
	creaturesToDestroy=[]
	creatureList = [card for card in table if isCreature(card) and card.owner!=me and int(card.Power.strip('+'))<=powerLeft]
	if me.isInverted: reverse_cardList(creatureList)
	while powerLeft>0 and len(creatureList)>0:
		creatureChoice = askCard2(creatureList, 'Choose a Creature to destroy.')
		if type(creatureChoice) is not Card: break
		powerLeft = powerLeft-int(creatureChoice.Power.strip('+'))
		creatureChoice.target()
		creaturesToDestroy.append(creatureChoice)
		creatureList.remove(creatureChoice)
		notify("Apocalypse Vise - Power Spent: {}".format(8000-powerLeft))
		creatureList = [card for card in creatureList if int(card.Power.strip('+'))<=powerLeft]

	destroyAll(creaturesToDestroy, False)

def bronks():
	creatureList = [c for c in table if isCreature(c) and not isBait(c)]
	minPower = min(int(c.Power.strip('+')) for c in creatureList)
	notify("Lowest Power found: {}".format(minPower))
	leastPowerCreatureList = [c for c in creatureList if int(c.Power.strip('+')) == minPower]
	opponentCreatures = [card for card in creatureList if card.owner != me]
	myCreatures = [card for card in creatureList if card.owner == me]
	leastPowerCreatureList = sorted(leastPowerCreatureList, key=lambda x: (
       	int(me.isInverted) if x in opponentCreatures else int(not me.isInverted),
        (opponentCreatures + myCreatures).index(x)))
	if me.isInverted: reverse_cardList(leastPowerCreatureList)
	else: 
		leastPowerCreatureList = sorted(leastPowerCreatureList, key=lambda x: (
       	 	0 if x in opponentCreatures else 1,
        	(opponentCreatures + myCreatures).index(x)))
	choice = askCard2(leastPowerCreatureList, "Select a card to destroy (Opponent's are shown first).")
	if type(choice) is not Card: return
	remoteCall(choice.owner,'destroy',choice)

def carnivalTotem():
	manaZoneList = [card for card in table if isMana(card) and card.controller == me]
	handList = [card for card in me.hand]
	for manaCard in manaZoneList:
		toHand(manaCard)
	for handCard in handList:
		toMana(handCard)
		handCard.orientation = Rot270

def deklowazDiscard():
	mute()
	targetPlayer = getTargetPlayer()
	cardList = [card for card in targetPlayer.hand]
	if me.isInverted: reverse_cardList(cardList)
	cardChoice = askCard2(cardList, "Look at opponent's hand. (close pop-up or select any card to finish.)")
	for card in cardList:
		if re.search("Creature", card.Type) and int(card.Power.strip('+')) <= 3000:
			remoteCall(targetPlayer, 'toDiscard', cardChoice)

def dolmarks():
	sacrifice()
	fromMana(1,"ALL","ALL","ALL",True,True)
	targetPlayer = getTargetPlayer()
	if not targetPlayer: return
	remoteCall(targetPlayer,'sacrifice',[])
	remoteCall(targetPlayer,'fromMana',[1,"ALL","ALL","ALL",True,True])

def emeral(card):
	if len([c for c in table if isShield(c) and c.owner == me]) == 0: return
	choice = askYN("Use Emeral's effect?")
	if choice != 1: return
	handList = [c for c in me.hand]
	if me.isInverted: reverse_cardList(handList)
	cardFromHand = askCard2(handList)
	if type(cardFromHand) is not Card: return
	toShields(cardFromHand)
	waitingFunct.append([card,'bounceShield()'])

def funkyWizard():
	for player in players:
		remoteCall(player, "draw", [player.Deck, True]) 

def klujadras():
	for player in players:
		count = getWaveStrikerCount(player)
		if count:
			remoteCall(player, "draw", [player.Deck, False, count]) 

def luckyBall():
	shieldList = [c for c in table if isShield(c) and c.controller != me]
	if len(shieldList)<=3:
		draw(me.Deck,True,2)

def miraculousPlague():
	mute()
	creatureList = [card for card in table if isCreature(card) and card.owner != me]
	if len(creatureList) != 0:
		if len(creatureList) == 1:
			remoteCall(creatureList[0].owner, "toHand", creatureList[0])
		else:
			if me.isInverted: reverse_cardList(creatureList)
			creatureChoices = []
			creatureChoice = askCard2(creatureList, 'Choose Creatures for your opponent (one at a time).')
			if type(creatureChoice) is not Card: return
			creatureChoices.append(creatureChoice)
			creatureChoice.target()
			creatureList.remove(creatureChoice)
			creatureChoice2 = askCard2(creatureList, 'Choose Creatures for your opponent (one at a time).')
			if type(creatureChoice2) is not Card: return
			creatureChoice2.target()
			creatureChoices.append(creatureChoice2)
			#sort the choices to reflect the table state.
			creatureChoices = sorted(creatureChoices, key= lambda x: [card for card in table if isCreature(card) and card.owner != me].index(x))

			remoteCall(creatureChoice.owner,"_miraculousPlagueChooseToHand", [creatureChoices])

	manaList = [card for card in table if isMana(card) and card.owner != me]
	if len(manaList) != 0:
		if len(manaList) == 1:
			remoteCall(manaList[0].owner, "toHand", manaList[0])
		else:
			if me.isInverted: reverse_cardList(manaList)
			manaChoices = []
			manaChoice = askCard2(manaList, 'Choose Mana Cards for your opponent (one at a time).')
			if type(manaChoice) is not Card: return
			manaChoice.target()
			manaChoices.append(manaChoice)
			manaList.remove(manaChoice)
			manaChoice2 = askCard2(manaList, 'Choose Mana Cards for your opponent (one at a time).')
			if type(manaChoice2) is not Card: return
			manaChoice2.target()
			manaChoices.append(manaChoice2)
			#sort the choices to reflect the table state.
			sorted(manaChoices, key=lambda x: [card for card in table if isMana(card) and card.owner != me].index(x))

			remoteCall(manaChoice.owner,"_miraculousPlagueChooseToHand", [manaChoices])

def _miraculousPlagueChooseToHand(cardList):
	if me.isInverted: reverse_cardList(cardList)
	cardToHand = askCard2(cardList, 'Choose a Card to return to Hand.')
	if type(cardToHand) is not Card: return
	cardList.remove(cardToHand)
	toHand(cardToHand)
	destroy(cardList[0])

def miraculousRebirth():
	mute()
	cardList = [card for card in table if
				isCreature(card) 
				and not isBait(card)
				and not card.owner == me 
				and int(card.Power.strip('+')) <= 5000]
	if len(cardList) == 0:
		whisper("No valid targets on the table.")
		return
	targetCard = [c for c in table if c.targetedBy == me and c in cardList]
	if len(targetCard) != 1:
		whisper("Wrong number of targets!")
		return True
	remoteCall(targetCard[0].owner, "destroy", targetCard[0])
	targetCost = int(targetCard[0].Cost)
	notify('Miraculous Rebirth destroys a Creature that costs {} Mana.'.format(targetCost))

	group = me.deck
	if len(group) == 0: return
	cardsInGroup = sort_cardList([card for card in group])
	validChoice = None
	while (True):
		choice = askCard2(cardsInGroup, 'Search a Creature with {} Cost to put to Play'.format(targetCost))
		if type(choice) is not Card:
			group.shuffle()
			notify("{} finishes searching their {}.".format(me, group.name))
			return
		if int(choice.Cost) == targetCost:
			validChoice = choice
			break
	group.shuffle()
	notify("{} finishes searching their {}.".format(me, group.name))
	toPlay(validChoice)

def rothus():
	sacrifice()
	opponentSacrifice()

def soulSwap():
	mute()
	targetPlayer = getTargetPlayer()
	if not targetPlayer: return
	#list of creatures in battlezone
	creatureList = [card for card in table if isCreature(card) and card.controller == targetPlayer]
	if me.isInverted: reverse_cardList(creatureList)
	creatureChoice = askCard2(creatureList, 'Choose a Creature to send to Mana')
	if type(creatureChoice) is not Card: return
	remoteCall(creatureChoice.owner, "toMana", creatureChoice)
	update()
	remoteCall(me,"_fromManaToField", targetPlayer)

def tanzanyte():
	cardList = [card for card in me.piles['Graveyard'] if re.search('Creature', card.Type)]
	choice = askCard2(sort_cardList(cardList), 'Select a Creature to return all copies of from Graveyard.')
	if type(choice) is not Card: return
	for card in cardList:
		if card.Name == choice.Name:
			toHand(card, True)	

def craniumClamp():
	mute()

	targetPlayer = getTargetPlayer()
	if not targetPlayer: return
	remoteCall(targetPlayer,'selfDiscard', 2)

def stormShell():
	mute()

	targetPlayer = getTargetPlayer()
	if not targetPlayer: return
	remoteCall(targetPlayer,'sendSelfToMana',1)

def mechadragonsBreath():
	power = askNumber()
	
	if(power>6000):
		notify("{} chose incorrect Power ({}).".format(me, power))
		return
	notify("{} chose {} Power.".format(me, power))
	destroyAll(table,True,power,"ALL",False,True)

def _fromManaToField(targetPlayer):
	mute()
	update()
	#Count the number of cards in mana zone for the one that will be added.
	count = len([card for card in table if isMana(card) and card.controller == targetPlayer])
	#get valid targets from mana
	manaList = [card for card in table if isMana(card) and card.controller == targetPlayer and re.search("Creature", card.Type) and not re.search("Evolution Creature", card.Type) and int(card.Cost)<=count]
	if me.isInverted: reverse_cardList(manaList)
	manaChoice = askCard2(manaList, 'Choose a Creature to play from Mana')

	if type(manaChoice) is not Card: 
		return
	update()
	remoteCall(targetPlayer, "toPlay", manaChoice)

# End of Automation Code

# MENU OPTIONS
# Battlezone Options
def flip(card, x=0, y=0):
	mute()
	if (re.search("Psychic", card.Type)):
		altName = card.alternateProperty('awakening', 'name')
		if card.alternate is '':
			card.alternate = 'awakening'
			notify("{}'s' {} awakens to {}.".format(me, altName, card))
			align()
			return
		else:
			card.alternate = ''
			notify("{}'s {} reverts to {}.".format(me, altName, card))
			align()
			return
	elif (re.search("Dragheart", card.Type)):
		# draghearts
		old = card.Name
		forms = card.alternates
		if card.alternate is forms[0]:
			card.alternate = forms[1]
			notify("{}'s' {} dragonsolutions to {}.".format(me, old, card))
		elif card.alternate is forms[1]:
			# Is in 2nd form
			if len(forms) == 2:
				# Not 3 sided
				card.alternate = forms[0]
				notify("{}'s {} reverts to {}.".format(me, old, card))
			else:
				# 3 sided card
				card.alternate = forms[2]
				notify("{}'s {} 3D dragonsolutions to {}.".format(me, old, card))
		elif card.alternate is forms[2]:
			card.alternate = forms[0]
			notify("{}'s {} reverts to {}.".format(me, old, card))
		align()
		return

	else:
		if card.isFaceUp:
			notify("{} flips {} face down.".format(me, card))
			card.isFaceUp = False
		else:
			card.isFaceUp = True
			notify("{} flips {} face up.".format(me, card))

def toHyperspatial(card, x=0, y=0, notifymute=False):
	mute()
	removeIfEvo(card)
	if card.alternate is not '' and re.search("{RELEASE}", card.Rules):
		flip(card)
		return
	else:
		card.moveTo(me.Hyperspatial)
		align()
		if notifymute == False:
			notify("{}'s {} returns to the Hyperspatial Zone.".format(me, card))

def moveCards(args): #this is triggered every time a card is moved
	mute()
	clearWaitingFuncts()  # clear the waitingCard if ANY CARD moved
	player = args.player

	fromGroup = args.fromGroups[0]
	toGroup = args.toGroups[0]
	## Old vars are: player, card, fromGroup, toGroup, oldIndex, index, oldX, oldY, x, y, highlights, markers, faceup
	for card in args.cards:
		if player != me:  ##Ignore for cards you don't control
			return
		##When a player moves top card of deck to bottom of deck
		if fromGroup == me.Deck and toGroup == me.Deck:
			if card == me.Deck.bottom():
				notify("{} moves a card in their deck to bottom".format(me))
			elif card == me.Deck.top():
				notify("{} moves a card in their deck to top".format(me))
			else:
				notify("{} moves a card around in their deck".format(me))
			return

		## This updates the evolution dictionary in the event one of the cards involved in an evolution leaves the battlezone.
		if table not in args.fromGroups:  ## we only want cases where a card is being moved from table to another group
			##notify("Ignored")
			return
		evolveDict = eval(me.getGlobalVariable("evolution"))
		for evo in evolveDict.keys():
			if Card(evo) not in table:
				del evolveDict[evo]
			else:
				evolvedList = evolveDict[evo]
				for evolvedCard in evolvedList:
					if Card(evolvedCard) not in table:
						evolvedList.remove(evolvedCard)
				if len(evolvedList) == 0:
					del evolveDict[evo]
				else:
					evolveDict[evo] = evolvedList
		if evolveDict != eval(me.getGlobalVariable("evolution")):
			me.setGlobalVariable("evolution", str(evolveDict))

def align():
	mute()
	global playerside  ##Stores the Y-axis multiplier to determine which side of the table to align to
	global sideflip  ##Stores the X-axis multiplier to determine if cards align on the left or right half
	if sideflip == 0:  ##the 'disabled' state for alignment so the alignment positioning doesn't have to process each time
		return "BREAK"
	if Table.isTwoSided():
		if playerside == None:  ##script skips this if playerside has already been determined
			if me.isInverted:
				playerside = -1  # inverted (negative) side of the table
			else:
				playerside = 1
		if sideflip == None:  ##script skips this if sideflip has already been determined
			playersort = sorted(getPlayers(), key=lambda
				player: player._id)  ##makes a sorted players list so its consistent between all players
			playercount = [p for p in playersort if
						   me.isInverted == p.isInverted]  ##counts the number of players on your side of the table
			if len(playercount) > 2:  ##since alignment only works with a maximum of two players on each side
				whisper("Cannot align: Too many players on your side of the table.")
				sideflip = 0  ##disables alignment for the rest of the play session
				return "BREAK"
			if playercount[0] == me:  ##if you're the 'first' player on this side, you go on the positive (right) side
				sideflip = 1
			else:
				sideflip = -1
	else:  ##the case where two-sided table is disabled
		whisper("Cannot align: Two-sided table is required for card alignment.")
		sideflip = 0  ##disables alignment for the rest of the play session
		return "BREAK"

	cardorder = [[], [], []]
	evolveDict = eval(me.getGlobalVariable("evolution"))

	for card in table:
		if card.controller == me and not isFortress(card) and not card.anchor and not card._id in list(
				itertools.chain.from_iterable(evolveDict.values())):
			if isShield(card):
				cardorder[1].append(card)
			elif isMana(card):
				cardorder[2].append(card)
			else:  ##collect all creatures
				cardorder[0].append(card)

	temp = []
	bigCards = []
	for card in cardorder[0]:
		if card.size == "tall":
			bigCards.append(card)
		else:
			temp.append(card)
	cardorder[0] = temp
	# remove all big cards from normal aligned ones
	xpos = 80
	ypos = 5 + 10 * (max([len(evolveDict[x]) for x in evolveDict]) if len(evolveDict) > 0 else 1)
	for cardtype in cardorder:
		if cardorder.index(cardtype) == 1:
			xpos = 80
			ypos += 93
		elif cardorder.index(cardtype) == 2:
			xpos = 80
			ypos += 93
		for c in cardtype:
			x = sideflip * xpos
			y = playerside * ypos + (44 * playerside - 44)
			if c.position != (x, y):
				c.moveToTable(x, y)
			xpos += 79
	for evolution in evolveDict:
		count = 0
		for evolvedCard in evolveDict[evolution]:
			x, y = Card(evolution).position
			count += 1
			Card(evolvedCard).moveToTable(x, y - 10 * count * playerside)
			Card(evolvedCard).sendToBack()
	# for landscape or large cards
	xpos = 15
	if playerside==1:
		xpos -= 93
	ypos = 5 + 10 * (max([len(evolveDict[x]) for x in evolveDict]) if len(evolveDict) > 0 else 1)
	for c in bigCards:
		if playerside==1:
			xpos += max(c.width, c.height) + 10
		x = -1 * sideflip * xpos
		y = playerside * ypos + (c.height/2 * playerside - c.height/2)
		if c.position != (x, y):
			c.moveToTable(x, y)
		if playerside==-1:
			xpos += max(c.width, c.height) + 10

#Clear Targets/Arrows
def clear(group, x=0, y=0):
	mute()
	clearWaitingFuncts()
	for card in group:
		card.target(False)

#Set Up Battlezone
def setup(group, x=0, y=0):
	mute()
	clearWaitingFuncts()

	cardsInTable = [c for c in table if c.controller == me and c.owner == me and not isPsychic(c)]
	cardsInHand = [c for c in me.hand if not isPsychic(c)]
	cardsInGrave = [c for c in me.piles['Graveyard'] if not isPsychic(c)]

	psychicsInTable = [c for c in table if c.controller == me and c.owner == me and isPsychic(c)]
	psychicsInHand = [c for c in me.hand if isPsychic(c)]
	psychicsInGrave = [c for c in me.piles['Graveyard'] if isPsychic(c)]

	if cardsInTable or cardsInHand or cardsInGrave or psychicsInTable or psychicsInGrave or psychicsInHand:
		if confirm("Are you sure you want to setup battlezone? Current setup will be lost"):

			for card in cardsInTable:
				card.moveTo(me.Deck)
			for card in cardsInHand:
				card.moveTo(me.Deck)
			for card in cardsInGrave:
				card.moveTo(me.Deck)

			for card in psychicsInTable:
				card.moveTo(me.Hyperspatial)
			for card in psychicsInHand:
				card.moveTo(me.Hyperspatial)
			for card in psychicsInGrave:
				card.moveTo(me.Hyperspatial)
		else:
			return
	if len(me.Deck) < 10:  # We need at least 10 cards to properly setup the game
		whisper("Not enough cards in deck")
		return

	cardsInDeck = [c for c in me.Deck]
	for card in cardsInDeck:
		if isPsychic(card):
			whisper("You cannot have Psychic creatures in your main deck")
			return

	me.setGlobalVariable("shieldCount", "0")
	me.setGlobalVariable("evolution", "{}")
	me.Deck.shuffle()

	for card in me.Deck.top(5): toShields(card, notifymute=True)
	for card in me.Deck.top(5): card.moveTo(card.owner.hand)
	align()
	notify("{} sets up their battle zone.".format(me))

def rollDie(group, x=0, y=0):
	mute()
	global diesides
	n = rnd(1, diesides)
	notify("{} rolls {} on a {}-sided die.".format(me, n, diesides))

def untapAll(group=table, isNewTurn=False, x=0, y=0):
	mute()
	clearWaitingFuncts()
	for card in group:
		if not card.owner == me:
			continue
		# Untap Creatures
		if card.orientation == Rot90:
			if not isNewTurn:
				card.orientation = Rot0
			elif not isCreature(card) or isBait(card) or not cardScripts.get(card.name, {}).get('silentSkill', []):
				card.orientation = Rot0
			#Silent Skill Check
			else:
					card.target()
					choice = askYN("Activate Silent Skill for {}?\n\n{}".format(card.Name, card.Rules), ["Yes", "No"])
					if choice != 1: 
						card.orientation = Rot0
						card.target(False)
						return
					notify('{} uses Silent Skill of {}'.format(me, card))
					card.target(False)
					functionList = cardScripts.get(card.Name).get('silentSkill')
					# THERE ARE CURRENTLY NO SURVIVORS THAT HAVE SILENT SKILL
					for function in functionList:
						waitingFunct.append([card, function])
					global alreadyEvaluating
					if not alreadyEvaluating:
						alreadyEvaluating = True
						evaluateWaitingFunctions()
						alreadyEvaluating = False

		# Untap Mana
		if card.orientation == Rot270:
			card.orientation = Rot180

	if isNewTurn:
		processOnTurnStartEffects()
	notify("{} untaps all their cards.".format(me))

#Default call for Destroy (del key), handles mass creature destruction effects
def destroyMultiple(cards, x=0, y=0):
	if len(cards) == 1:
		destroy(cards[0])
	else: 
		creatureList = [c for c in cards if isCreature(c)]
		otherList = [c for c in cards if c not in creatureList]
		for c in otherList:
			destroy(c)
		destroyAll(creatureList, dontAsk=True)
		
def tapMultiple(cards, x=0, y=0, clearFunctions = True): #batchExecuted for multiple cards tapped at once(manually)
	mute()
	if clearFunctions:
		clearWaitingFuncts()
	mana = [card for card in cards if isMana(card)]
	creatures = [card for card in cards if isCreature(card)]
	tappedMana = 0
	for card in creatures:
		processTapUntapCreature(card)
			
	for card in mana:
		card.orientation ^= Rot90
		if card.orientation & Rot90 == Rot90:
			tappedMana+=1
	untappedMana = len(mana) - tappedMana

	if len(mana)==1:
		notify('{} taps {} in mana.'.format(me, mana[0])) if mana[0].orientation & Rot90 == Rot90 else notify('{} untaps {} in mana.'.format(me,  mana[0]))
			
	elif len(mana)>1:
		if tappedMana>0 and untappedMana>0:
			notify('{} taps mana {} and untaps {} mana.'.format(me, tappedMana, untappedMana))
		elif tappedMana>0:
			notify('{} taps {} mana.'.format(me, tappedMana))
		else:
			notify('{} untaps {} mana.'.format(me, untappedMana))

def destroy(card, x=0, y=0, dest=False, ignoreEffects=False):
	mute()
	if isShield(card):
		if dest == True:
			toDiscard(card)
			return
		card.peek()

		#Magical bugfix to remove Peek symbol in hand
		rnd(1,1)
		#check conditional trigger for cards like Awesome! Hot Spring Gallows or Traptops
		conditionalTrigger = True
		if cardScripts.get(card.Name, {}).get('onTrigger'):
			trigFunctions = cardScripts.get(card.Name).get('onTrigger')
			notify("On trig list is".format(trigFunctions[0]))
			for function in trigFunctions:
				conditionalTrigger = conditionalTrigger and eval(trigFunctions[0])
		if conditionalTrigger and re.search("{SHIELD TRIGGER}", card.Rules):
			choice = askYN("Activate Shield Trigger for {}?\n\n{}".format(card.Name, card.Rules), ["Yes", "No", "Wait"])
			if choice==1:

				notify("{} uses {}'s Shield Trigger.".format(me, card.Name))
				card.isFaceUp = True
				toPlay(card, notifymute=True)
				return
			elif choice==3 or choice==0:
				notify("{} peeks at shield#{}".format(me, card.markers[shieldMarker]))
				return

		shieldCard = card
		cardsInHandWithStrikeBackAbility = [c for c in me.hand if re.search("Strike Back", c.rules)]
		if len(cardsInHandWithStrikeBackAbility) > 0:
			cardsInHandWithStrikeBackAbilityThatCanBeUsed = []
			for cardInHandWithStrikeBackAbility in cardsInHandWithStrikeBackAbility:
				if re.search("Super Strike Back", cardInHandWithStrikeBackAbility.rules):  # special case for Deadbrachio
					if manaArmsCheck():
						cardsInHandWithStrikeBackAbilityThatCanBeUsed.append(cardInHandWithStrikeBackAbility)
				elif re.search("Strike Back.*Hunter", cardInHandWithStrikeBackAbility.rules):
					if re.search("Hunter", shieldCard.Race):  # special case for Aqua Advisor
						cardsInHandWithStrikeBackAbilityThatCanBeUsed.append(cardInHandWithStrikeBackAbility)
				elif re.search("Strike Back", cardInHandWithStrikeBackAbility.rules) and re.search(cardInHandWithStrikeBackAbility.Civilization, shieldCard.Civilization):
					cardsInHandWithStrikeBackAbilityThatCanBeUsed.append(cardInHandWithStrikeBackAbility)
			if len(cardsInHandWithStrikeBackAbilityThatCanBeUsed) > 0:
				if confirm("Activate Strike Back by sending {} to the graveyard?\n\n{}".format(shieldCard.Name,
																							   shieldCard.Rules)):
					if me.isInverted: reverse_cardList(cardsInHandWithStrikeBackAbilityThatCanBeUsed)
					choice = askCard2(cardsInHandWithStrikeBackAbilityThatCanBeUsed, 'Choose Strike Back to activate')
					if type(choice) is Card:
						shieldCard.isFaceUp = True

						toPlay(choice, notifymute=True)
						toDiscard(shieldCard)
						notify("{} destroys {} to use {}'s Strike Back.".format(me, shieldCard.name, choice.name))
						return
		notify("{}'s shield #{} is broken.".format(me, shieldCard.markers[shieldMarker]))
		shieldCard.moveTo(shieldCard.owner.hand)
	elif isMana(card) or ignoreEffects:
		toDiscard(card)
	else:
		cardToBeSaved = card
		possibleSavers = [c for c in table if
						  cardToBeSaved != c and isCreature(c) and c.owner == me and re.search("Saver",c.rules) 
						  and (re.search(cardToBeSaved.properties['Race'], c.rules) or re.search("Saver: All Races", c.rules))]
		if len(possibleSavers) > 0:
			if confirm("Prevent {}'s destruction by using a Saver on your side of the field?\n\n".format(
					cardToBeSaved.Name)):
				if me.isInverted: reverse_cardList(possibleSavers)
				choice = askCard2(possibleSavers, 'Choose Saver to destroy')
				if type(choice) is Card:
					toDiscard(choice)
					notify("{} destroys {} to prevent {}'s destruction.".format(me, choice.name, cardToBeSaved.name))
					return
		global wscount
		wscount = getWaveStrikerCount()
		toDiscard(cardToBeSaved)
		card = cardToBeSaved 

		functionList=[]
		if cardScripts.get(card.Name, {}).get('onDestroy', {}):
			functionList = cardScripts.get(card.Name).get('onDestroy')
		if re.search("Survivor", card.Race):
			survivors = getSurvivorsOnYourTable()
			for surv in survivors:
				if cardScripts.get(surv.name, {}).get('onDestroy', []):
					functionList.extend(cardScripts.get(surv.name).get('onDestroy'))
		for function in functionList:
			waitingFunct.append([card, function])
		global alreadyEvaluating
		if not alreadyEvaluating:
			alreadyEvaluating = True
			evaluateWaitingFunctions()
			alreadyEvaluating = False

def untap(card, ask = True):
	if card.orientation == Rot90:
		if ask:
			card.target()
			choice = askYN("Would you like to Untap {}?".format(card.name))
			card.target(False)
			if choice != 1: return
		tapMultiple([card], clearFunctions=False)

#Deck Menu Options
def shuffle(group, x=0, y=0):
	mute()
	if len(group) == 0: return
	for card in group:
		if card.isFaceUp:
			card.isFaceUp = False
	group.shuffle()
	notify("{} shuffled their {}".format(me, group.name))

def draw(group, conditional=False, count=1, x=0, y=0):
	mute()
	for i in range(0, count):
		if len(group) == 0:
			return
		if conditional == True:
			choiceList = ['Yes', 'No']
			colorsList = ['#FF0000', '#FF0000']
			choice = askChoice("Draw a card?", choiceList, colorsList)
			if choice == 0 or choice == 2:
				return
		card = group[0]
		card.moveTo(card.owner.hand)
		notify("{} draws a card.".format(me))

def drawX(group, x=0, y=0):
	if len(group) == 0: return
	mute()
	count = askInteger("Draw how many cards?", 7)
	if count == None: return
	for card in group.top(count): card.moveTo(card.owner.hand)
	notify("{} draws {} cards.".format(me, count))

#Discard top card
def mill(group, count=1, conditional=False, x=0, y=0):
	mute()
	if len(group) == 0:
		notify("No cards left in Deck!")
		return
	if conditional:
		choiceList = ['Yes', 'No']
		colorsList = ['#FF0000', '#FF0000']
		choice = askChoice("Discard top {} cards?".format(count), choiceList, colorsList)
		if choice == 0 or choice == 2:
			return
	if len(group) < count: count = len(group)
	for card in group.top(count):
		toDiscard(card, notifymute=True)
		notify("{} discards {} from top of Deck.".format(me, card))

#Discard top X cards
def millX(group, x=0, y=0):
	mute()
	if len(group) == 0: return
	count = askInteger("Discard how many cards?", 1)
	if count == None: return
	for card in group.top(count): toDiscard(card, notifymute=True)
	notify("{} discards top {} cards of Deck.".format(me, count))

#Random discard function (from hand)
def randomDiscard(group, x=0, y=0):
	mute()
	if len(group) == 0: return
	card = group.random()
	toDiscard(card, notifymute=True)
	notify("{} randomly discards {}.".format(me, card))

#Charge Top Card as Mana
def mana(group, count=1, ask=False, tapped=False, postAction="NONE", postArgs=[], postCondition='True', preCondition=True):
	mute()
	if not preCondition:
		return
	if ask:
		choice = askYN("Charge top {} cards as mana?".format(count))
		if choice == 0 or choice == 2:
			return
	for i in range(0, count):
		if len(group) == 0: return
		card = group[0]
		toMana(card, notifymute=True)
		if tapped and card.orientation & Rot90 != Rot90:
			card.orientation ^= Rot90
		notify("{} charges {} from top of {} as mana.".format(me, card, group.name))
	doPostAction(card, postAction, postArgs, postCondition)

def doPostAction(card, postAction, postArgs, postCondition):
	# does something more in the effect, might be based on what the first card was; eg: Geo Bronze Magic or simple stuff like Skysword(shield comes after mana)
	# implement BounceIfCiv for Intense Vacuuming Twist? Maybe make a whole different function for ifCiv or ifRace just to evaluate the conditon based on args
	# For example, if there is "IfCiv" in postAction, check args for the civ, if there's "ifRace"(eg Eco Aini) etc. -> This can be done in a separate function instead of here
	if postAction == "NONE":
		return
	if postAction == "DrawIfCiv":  # eg Geo Bronze Magic
		for civs in postArgs:
			if re.search(civs, card.properties['Civilization']):
				draw(me.Deck, True)
				break
		return
	if postAction == "ManaIfCiv":  # eg Faerie Crystal
		for civs in postArgs:
			if re.search(civs, card.properties['Civilization']):
				mana(me.Deck)
				break
		return
	if eval(postCondition):  # eg. Faerie Miracle
		eval(postAction)  # simple eval of a function, if postCondition is satisfied(is true by default)

#Charge top X cards as mana (not yet used)
def massMana(group, conditional=False, x=0, y=0):
	mute()
	cardList = [card for card in table if isMana(card) and card.owner == me]
	count = len(cardList)
	if conditional == True:
		choiceList = ['Yes', 'No']
		colorsList = ['#FF0000', '#FF0000']
		choice = askChoice("Charge top {} cards to mana?".format(count), choiceList, colorsList)
		if choice == 0 or choice == 2: return
	for i in range(0, count):
		if len(group) == 0: return
		card = group[0]
		toMana(card, notifymute=True)
		if card.orientation & Rot90 != Rot90:
			card.orientation ^= Rot90
	notify("{} charges top {} cards of {} as mana.".format(me, count, group.name))

#Set Top Card as Shield
def shields(group, count=1, conditional=False, x=0, y=0):
	mute()
	if conditional == True:
		maxCount = count
		count = askInteger("Set how many cards as shields? (Max = {})".format(maxCount), maxCount)
		if count == 0 or count > maxCount: return
	for card in group.top(count):
		if len(group) == 0: return
		card = group[0]
		toShields(card, notifymute=True)
		notify("{} sets top card of {} as shield.".format(me, group.name))

#Charge as Mana menu option / Ctrl+C
def toMana(card, x=0, y=0, notifymute=False, checkEvo=True, alignCheck=True):
	mute()
	if isMana(card):
		whisper("This is already mana")
		return
	if isPsychic(card):
		toHyperspatial(card)
		return
	##notify("Removing from tracked evos if its bait or an evolved creature")
	if checkEvo:
		baitList = removeIfEvo(card)
		for baitCard in baitList:
			toMana(baitCard, checkEvo=False, alignCheck=False)
	if isShield(card):
		card.moveTo(me.hand)  # in case it is charged from shields
	card.moveToTable(0, 0)
	card.orientation = Rot180

	if re.search("/", card.Civilization):  # multi civ card
		card.orientation = Rot270
	if alignCheck:
		align()
	if notifymute == False:
		notify("{} charges {} as mana.".format(me, card))

#Set as shield menu option / Ctrl+H (both from hand and battlezone)
def toShields(card, x=0, y=0, notifymute=False, alignCheck=True, checkEvo=True):
	mute()
	if isShield(card):
		whisper("This is already a shield.")
		return
	if isPsychic(card):
		toHyperspatial(card)
		return
	count = int(me.getGlobalVariable("shieldCount")) + 1
	me.setGlobalVariable("shieldCount", convertToString(count))
	if notifymute == False:
		if isCreature(card) or isMana(
				card):  ##If a visible card in play is turning into a shield, we want to record its name in the notify
			notify("{} sets {} as shield #{}.".format(me, card, count))
		else:
			notify("{} sets a card in {} as shield #{}.".format(me, card.group.name, count))

	card.moveToTable(0, 0, True)
	if card.isFaceUp:
		card.isFaceUp = False
	if card.orientation != Rot0:
		card.orientation = Rot0
	card.markers[shieldMarker] = count
	if checkEvo:
		baitList = removeIfEvo(card)
		for baitCard in baitList:
			toShields(baitCard, checkEvo=False, alignCheck=False)
	if alignCheck:
		align()

#Play Card menu option (both from hand and battlezone)
def toPlay(card, x=0, y=0, notifymute=False, evolveText='', ignoreEffects=False, isEvoMaterial = False):
	mute()
	global alreadyEvaluating #is true when already evaluating some functions of the last card played, or when continuing after wait for Target
	#notify("DEBUG: AlreadyEvaluating is "+str(alreadyEvaluating))
	if card.group == card.owner.hand:
		clearWaitingFuncts() # this ensures that waiting for targers is cancelled when a new card is played from hand(not when through a function).

	if re.search("Evolution", card.Type) and not isEvoMaterial:
		targets= []
		textBox = 'Select Creature to put under Evolution{}'
		#Deck Evolutions
		if re.search("Deck Evolution", card.Rules, re.IGNORECASE):
			if len(me.Deck) == 0: return
			if re.search("Mad Deck Evolution", card.Rules, re.IGNORECASE):
				notify("{} uses Deck Evolution of {}".format(me, card))
				topCards = []
				cardCount = min(3,len(me.Deck))
				for i in range(0, cardCount):
					c = me.Deck[i]
					topCards.append(c)
					c.isFaceUp = True
					notify("{} reveals {} from the top of the Deck".format(me, c))
				topCreatures = [c for c in topCards if re.search("Creature", c.Type)]
				if len(topCreatures) == 0:
					notify("No Creatures revealed.")
					for c in topCards:
						toDiscard(c)
					return
				choice = askCard2(topCreatures,textBox.format(''))
				if type(choice) is not Card:
					return
				topCards.remove(choice)
				for c in topCards:
					toDiscard(c)
				toPlay(choice, 0, 0, True, ' for Deck Evolution of {}'.format(card),True, True)
				targets = [choice]		
			else:
				topC = me.Deck[0]
				topC.isFaceUp = True
				notify("{} uses Deck Evolution of {}".format(me, card))
				notify("{} reveals {} from the top of the Deck".format(me, topC.Name))
				if re.search("Creature", topC.Type):
					choice = askYN()
					if choice != 1: 
						return
					toPlay(topC, 0, 0, True, ' for Deck Evolution of {}'.format(card),True, True)
					targets=[topC]
				else:
					notify("{} is not a Creature".format(topC.Name))
					topC.isFaceUp = False
					return
		#Graveyard Evolutions
		elif re.search(r"Graveyard(?:\s+Galaxy)?(?:\s+Vortex)?\s+evolution", card.Rules, re.IGNORECASE):
			materialList = [c for c in me.piles['Graveyard'] if re.search("Creature",c.Type)]
			isMultiMaterial = False
			if re.search("Super Infinite Graveyard evolution", card.Rules, re.IGNORECASE) or re.search(r"Graveyard(?:\s+Galaxy)?(?:\s+Vortex)\s+evolution", card.Rules, re.IGNORECASE):
				isMultiMaterial = True
			targets = []
			if(isMultiMaterial): textBox = textBox.format(' from Graveyard(1 at a time, close pop-up to finish).')
			while len(materialList)>0 and (isMultiMaterial or len(targets) < 1):
				choice = askCard2(materialList,textBox.format(' from Graveyard'))
				if type(choice) is not Card: break
				targets.append(choice)
				materialList.remove(choice)
			for target in targets:
				toPlay(target,0, 0,True,' for Graveyard Evolution of {}'.format(card),True, True)
		#Mana Evolutions
		elif re.search(r"Mana(?:\s+Galaxy)?(?:\s+Vortex)?\s+evolution", card.Rules, re.IGNORECASE):
			materialList = [c for c in table if isMana(c) and c.owner == me and re.search("Creature", c.Type)]
			if me.isInverted: reverse_cardList(materialList)
			isMultiMaterial = False
			if re.search(r"Mana(?:\s+Galaxy)?(?:\s+Vortex)\s+evolution", card.Rules, re.IGNORECASE):
				isMultiMaterial = True
			targets = []
			if len(materialList)==0: 
					whisper("Cannot play {}, you don't have any Creatures in Mana Zone for it.".format(card))
					return
			while len(materialList)>0 and (isMultiMaterial or len(targets)<1):
				textBox = textBox.format(' from Mana(1 at a time, close pop-up to finish).')
				choice = askCard2(materialList,textBox.format(''))
				if type(choice) is not Card: break
				targets.append(choice)
				materialList.remove(choice)
			for target in targets:
				toPlay(target,0, 0,True,' for Vortex Mana Evolution of {}'.format(card),True, True)
		#Hand Evolutions
		elif re.search("Hand Evolution", card.Rules, re.IGNORECASE):
			materialList = [c for c in me.hand if re.search("Creature", c.Type) and c != card]
			if me.isInverted: reverse_cardList(materialList)
			if len(materialList)==0:
					whisper("Cannot play {}, you don't have any Other Creatures in Hand for it.".format(card))
					return
			choice = askCard2(materialList,textBox.format(' from Hand'))
			if type(choice) is not Card: return
			toPlay(choice,0, 0,True,' for Hand Evolution of {}'.format(card),True, True)
			targets=[choice]
		#Omega Evolutions
		elif re.search("Super Infinite evolution Omega", card.Rules, re.IGNORECASE) or re.search("Galaxy Vortex Evolution Omega", card.Rules, re.IGNORECASE):
			evoTypeText = 'Super Infinite evolution Omega'
			isGalaxy = False
			if re.search("Galaxy Vortex Evolution Omega", card.Rules, re.IGNORECASE):
				isGalaxy = True
				evoTypeText = 'Galaxy Vortex Evolution Omega'
			materialListGY = [c for c in me.piles['Graveyard'] if re.search("Creature",c.Type)]
			materialListMana = [c for c in table if isMana(c) and c.owner == me and re.search("Creature", c.Type)]
			materialListBZ = [c for c in table if (isCreature(c) or isGear(c)) and c.owner == me and not isBait(c)]
			if me.isInverted:
				reverse_cardList(materialListMana)
				reverse_cardList(materialListBZ)
			targetsGY = []
			targetsMana = []
			targetsBZ = []
			textBox = textBox.format(' (1 at a time, close pop-up to finish).')
			whisper("Pick cards from Graveyard, Mana and Battle Zone in that order. Close the Pop-Up to proceed to the next selection.")
			while len(materialListGY)>0 and (not isGalaxy or len(targetsGY) < 1):
				choice = askCard2(materialListGY,textBox.format(' from Graveyard'))
				if type(choice) is not Card: break
				targetsGY.append(choice)
				materialListGY.remove(choice)
			while len(materialListMana)>0 and (not isGalaxy or len(targetsMana) < 1):
				choice = askCard2(materialListMana,textBox.format(' from Mana'))
				if type(choice) is not Card: break
				targetsMana.append(choice)
				materialListMana.remove(choice)
			while len(materialListBZ)>0 and (not isGalaxy or len(targetsBZ) < 1):
				choice = askCard2(materialListBZ,textBox.format(' from Battle Zone'))
				if type(choice) is not Card: break
				targetsBZ.append(choice)
				materialListBZ.remove(choice)
			targets = targetsGY + targetsMana + targetsBZ
			if len(targets) < 1:
				whisper('No targets selected!')
				return
			for target in targetsGY:
				toPlay(target,0, 0,True,' for {} of {}'.format(evoTypeText, card),True, True)
			for target in targetsMana:
				toPlay(target,0, 0,True,' for {} of {}'.format(evoTypeText,card),True, True)
		#Default or Vortex Evolution
		else: 
			targets = [c for c in table
					   if c.controller == me
					   and c.targetedBy == me 
					   and (isCreature(c) or isGear(c))
					   and not isBait(c)]
			for c in targets:
				c.target(False)
			if len(targets) == 0:
				materialList = [c for c in table if ((re.search("Evolution Creature",card.Type) and isCreature(c)) or (re.search("Evolution Cross Gear", card.Type) and isGear(c))) and c.controller == me and not isBait(c)]
				if me.isInverted: reverse_cardList(materialList)
				if len(materialList) == 0:
					whisper("Cannot play {}, you don't have any Cards in Battle Zone for it.".format(card))
					whisper("Hint: Play a Creature or Gear first to evolve this card onto.")
					return
				targets = []
				isMultiMaterial = False
				if re.search(r"(?:Galaxy\s+)?Vortex Evolution",card.Rules, re.IGNORECASE) or re.search('Super Infinite Evolution', card.Rules, re.IGNORECASE):
					isMultiMaterial = True
				while len(materialList)>0 and (isMultiMaterial or len(targets)<1):
					choice = askCard2(materialList,'Select Card(s) to use as Material for Evolution.')
					if type(choice) is not Card: break
					targets.append(choice)
					materialList.remove(choice)
		
		if len(targets) == 0:
			whisper("No targets for {}'s Evolution selected. Aborting...".format(card))
			return
		evolveText = ", evolving {}".format(", ".join([c.name for c in targets]))
		processEvolution(card, targets)	
	if isMana(card) or isShield(card):
		card.moveTo(me.hand)
	card.moveToTable(0, 0)
	if shieldMarker in card.markers:
		card.markers[shieldMarker] = 0
	align()
	if notifymute == False:
		notify("{} plays {}{}.".format(me, card, evolveText))
	
	if not ignoreEffects:
		functionList = []
		if metamorph() and cardScripts.get(card.name, {}).get('onMetamorph', []):
			functionList = cardScripts.get(card.name).get('onMetamorph')
			notify("Metamorph for {} activated!".format(card))
		elif re.search('Survivor', card.Race):
			survivors = getSurvivorsOnYourTable()
			
			#for non-sharing survivors
			if card not in survivors:
				survivors.insert(0, card)
			for surv in survivors:
				if cardScripts.get(surv.name, {}).get('onPlay', []):
					functionList.extend(cardScripts.get(surv.name).get('onPlay'))
		elif cardScripts.get(card.name, {}).get('onPlay', []):
			functionList = cardScripts.get(card.name).get('onPlay')
		
		for function in functionList:
			waitingFunct.append([card, function])  # This fuction will be queued(along with the card that called it). RN it's waiting.
			#notify("DEBUG: Function added to waiting list: "+str(function))
		if not alreadyEvaluating: #this check is needed when a card is played with another card, for example Hogan Blaster
			alreadyEvaluating = True
			evaluateWaitingFunctions() #evaluate all the waiting functions. This thing stop evaluation if a function returns true(ie. its waiting for target)
			alreadyEvaluating = False #evaluation is done (or waiting, but the card has finished).
	if not waitingFunct: #Don't put card in grave if it's waiting for some effect.
		#BUG: This check will always be reached first by a spell without any automation being played with Hogan Blaster. And since HB is still in waitingFunct...the spell never goes to grave automatically
		#Soulution: Instead of this simple chcek make an intermediate function that checks if this card is in waitingFunct. If not, then do endOfFunctionality.
		endOfFunctionality(card)

def endOfFunctionality(card):
	if card.Type == "Spell" and not isMana(card):
		if re.search("Charger", card.name) and re.search("Charger", card.rules):
			toMana(card)
			align()
		else:
			card.moveTo(card.owner.piles['Graveyard'])
			align()

#Discard Card menu option
def toDiscard(card, x=0, y=0, notifymute=False, alignCheck=True, checkEvo=True):
	mute()
	src = card.group
	if src == table and checkEvo:
		baitList = removeIfEvo(card)
		for baitCard in baitList:
			toDiscard(baitCard, checkEvo=False, alignCheck=False)

	if isPsychic(card):
		toHyperspatial(card)
		return

	cardWasMana = isMana(card)
	card.moveTo(card.owner.piles['Graveyard'])
	if notifymute == False:
		if src == table:
			if cardWasMana:
				notify("{} destroys {} from mana.".format(me, card))
			else:
				notify("{} destroys {}.".format(me, card))
			if alignCheck:
				align()
		else:
			notify("{} discards {} from {}.".format(me, card, src.name))

	#Handle onDiscard effects
	if src.name=="Hand":
		functionList=[]
		if cardScripts.get(card.Name, {}).get('onDiscard', {}):
			functionList = cardScripts.get(card.Name).get('onDiscard')
			for function in functionList:
				eval(function)

#Move To Hand (from battlezone)
def toHand(card, show=True, x=0, y=0, alignCheck=True, checkEvo=True):
	mute()
	src = card.group
	if isPsychic(card):
		toHyperspatial(card)
		return
	if show:
		card.isFaceUp = True
		# need to use just card instead of card.Name for link to card
		# but it won't show as card name if card is not visible to a player, so turning it face up first
		notify("{} moved {} to hand from {}.".format(me, card, src.name))
		# card.isFaceUp = False
		card.moveTo(card.owner.hand)
	else:
		# here, move the card to hand first so it will only show card link to only the player who can see the hand
		# if you show first then move to hand 'card' won't show card name to the owner in the notify message
		card.moveTo(card.owner.hand)
		notify("{} moved {} to hand from {}.".format(me, card, src.name))

	if checkEvo:
		baitList = removeIfEvo(card)
		for baitCard in baitList:
			toHand(baitCard, checkEvo=False, alignCheck=False)

	if alignCheck:
		align()

#Move to Bottom (from battlezone)
def toDeckBottom(card, x=0, y=0):
	mute()
	toDeck(card, bottom=True)

#Move to Topdeck (from battlezone)
def toDeck(card, bottom=False):
	mute()
	if isPsychic(card):
		toHyperspatial(card)
		return
	cardList = removeIfEvo(card)  # baits
	cardList.append(card)  # top card as well
	while len(cardList) > 0:
		if len(cardList) == 1:
			choice = 1
		else:
			choice = askChoice("Choose a card to place it on top of your deck.", [c.name for c in cardList])
		if choice > 0:
			c = cardList.pop(choice - 1)
			if bottom == True:
				notify("{} moves {} to bottom of Deck.".format(me, c))
				c.moveToBottom(c.owner.Deck)
			else:
				notify("{} moves {} to top of Deck.".format(me, c))
				c.moveTo(c.owner.Deck)
	align()

