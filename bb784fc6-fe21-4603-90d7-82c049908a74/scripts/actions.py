# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Constant and Variables Values
# ------------------------------------------------------------------------------
import re
import itertools
import time
import operator

shields = []
playerside = None
sideflip = None
diesides = 20
civ_order = ['Light', 'Water', 'Darkness', 'Fire', 'Nature']
shieldMarker = ('Shield', 'a4ba770e-3a38-4494-b729-ef5c89f561b7')
waitingFunct = []  # Functions waiting for targets. Please replace this with FUNCTIONS waiting for targets later. If a card calls 2 functions both will happen again otherwise
evaluateNextFunction = True #For conditional evaluation of one function after the other, currently only implemented for bounce() in IVT
alreadyEvaluating = False
wscount = 0
arrow = {}
lastExecutionTime = 0
lastTappedCards = []
DEBOUNCE_DELAY = 0.5
my_challenge=None
validated = False
global_timer = None
start_time = None

# Start of Automation code

cardScripts = {
	# ON PLAY EFFECTS

	'Alshia, Spirit of Novas': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Spell")]},
	'Angila, Electro-Mask': {'onPlay':[lambda card: waveStriker(lambda card:search(me.piles["Graveyard"], 1, "Creature"), card)]},
	'Aures, Spirit Knight': {'onPlay': [lambda card: mana(me.Deck)]},
	'Aqua Bouncer': {'onPlay': [lambda card: bounce()]},
	'Aqua Deformer': {'onPlay': [lambda card: bothPlayersFromMana(2)]},
	'Aqua Hulcus': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Aqua Hulk': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Aqua Sniper': {'onPlay': [lambda card: bounce(2)]},
	'Aqua Surfer': {'onPlay': [lambda card: bounce()]},
	'Aqua Trickster': {'onPlay':[lambda card: waveStriker(lambda card: tapCreature(), card)]},
	'Armored Decimator Valkaizer': {'onPlay': [lambda card: kill(4000)]},
	'Artisan Picora': {'onPlay': [lambda card: fromMana(1,"ALL","ALL","ALL",False,True)]},
	'Astral Warper': {'onPlay': [lambda card: draw(me.Deck, True, 3)]},
	'Baban Ban Ban, Earth\'s Blessing': {'onPlay': [lambda card: massMana(me.Deck, True)]},
	'Ballom, Master of Death': {'onPlay': [lambda card: destroyAll(table, True, "ALL", "Darkness", True)]},
	'Baraga, Blade of Gloom': {'onPlay':[lambda card: bounceShield()]},
	'Bega, Vizier of Shadow': {'onPlay': [lambda card: shields(me.Deck), lambda card:targetDiscard(True)]},
	'Belix, the Explorer': {'onPlay': [lambda card: fromMana(1,"Spell")]},
	'Bombazar, Dragon of Destiny': {'onPlay': [lambda card: destroyAll([c for c in table if c != card], True, 6000, "ALL", False, True)]},
	'Bonfire Lizard': {'onPlay':[lambda card: waveStriker(lambda card: kill(count=2, rulesFilter="{BLOCKER}"), card)]},
	'Bronze-Arm Tribe': {'onPlay': [lambda card: mana(me.Deck)]},
	'Bronze Chain Sickle': {'onPlay': [lambda card: mana(me.Deck)]},
	'Bubble Lamp': {'onPlay': [lambda card: draw(me.Deck, True) if len([c for c in me.piles["Graveyard"] if re.search("Bubble Lamp", c.Name)]) > 0 else None]},
	'Buinbe, Airspace Guardian': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Carnival Totem': {'onPlay': [lambda card: swapManaAndHand()]},
	'Chaos Worm': {'onPlay': [lambda card: kill()]},
	'Chief De Baula, Machine King of Mystic Light': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Spell")]},
	'Cobalt Hulcus, Aqua Savage': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Corile': {'onPlay': [lambda card: bounce(1, True, True)]},
	'Cranium Clamp': {'onPlay': [lambda card: opponentToDiscard(2)]},
	'Craze Valkyrie, the Drastic': {'onPlay': [lambda card: tapCreature(2)]},
	'Crimson Maru, the Untamed Flame': {'onPlay': [lambda card: kill(4000)]},
	'Crystal Paladin': {'onPlay': [lambda card: bounceAll(table,True,True, filterFunction='re.search(r"{BLOCKER}", c.Rules)')]},
	'Cyber N World': {'onPlay': [lambda card: semiReset()]},
	'Dacity Dragoon, Explosive Beast': {'onPlay': [lambda card: kill(3000)]},
	'Dandy Eggplant': {'onPlay': [lambda card: fromDeckToMana(),lambda card: fromMana(count=1, toGrave=True)]},
	'Dandy Nasuo': {'onPlay': [lambda card: fromDeckToMana(),lambda card: fromMana(count=1, toGrave=True)]},
	'Dark Hydra, Evil Planet Lord': {'onPlay': [lambda card: fromGrave()]},
	'Death Mendosa, Death Dragonic Baron': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Dimension Splitter':{'onPlay':[lambda card: fromGraveyardAll("re.search(r'Dragon\\b', c.Race, re.I)", False, True, True)]},
	'Doboulgyser, Giant Rock Beast':{'onPlay': [lambda card: kill(3000)]},
	'Dolmarks, the Shadow Warrior': {'onPlay': [lambda card: dolmarks()]},
	'Dorballom, Lord of Demons': {'onPlay': [lambda card: destroyAll(table, True, "ALL", "Darkness", True), lambda card: destroyAllMana(table, "Darkness", True)]},
	'Emperor Himiko': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Emeral': {'onPlay': [lambda card: shieldswap(card)]},
	'Emperor Marco': {'onPlay': [lambda card: draw(me.Deck, True, 3)]},
	'Estol, Vizier of Aqua': {'onPlay': [lambda card: shields(me.Deck), lambda card: peekShield(1, True)]},
	'Eviscerating Warrior Lumez': {'onPlay':[lambda card: waveStriker(lambda card: destroyAll(table, True, 2000), card)]},
	'Evolution Totem': {'onPlay': [lambda card: search(me.Deck, 1, "Evolution Creature")]},
	'Explosive Fighter Ucarn':{'onPlay': [lambda card: fromMana(count=2, toGrave=True)]},
	'Factory Shell Q': {'onPlay': [lambda card: search(me.Deck, 1, "ALL", "ALL", "Survivor")]},
	'Fighter Dual Fang': {'onPlay': [lambda card: mana(me.Deck,2)]},
	'Fist Dragoon': {'onPlay': [lambda card: kill(2000)]},
	'Flame Trooper Goliac': {'onPlay':[lambda card: waveStriker(lambda card: kill(5000), card)]},
	'Flameburn Dragon': {'onPlay': [lambda card: kill(4000)]},
	'Fonch, the Oracle': {'onPlay': [lambda card: tapCreature()]},
	'Forest Sword, Great Hero': {'onPlay': [lambda card: mana(me.Deck)]},
	'Fortress Shell': {'onPlay': [lambda card: destroyMana(2)]},
	'Forbos, Sanctum Guardian Q': {'onPlay': [lambda card: search(me.Deck, 1, "Spell")]},
	'Funky Wizard': {'onPlay': [lambda card: funkyWizard()]},
	'Gajirabute, Vile Centurion': {'onPlay': [lambda card: burnShieldKill(1)]},
	'Galek, the Shadow Warrior': {'onPlay': [lambda card: kill(count=1, rulesFilter="{BLOCKER}"), lambda card: targetDiscard(True)]},
	'Galklife Dragon': {'onPlay': [lambda card: destroyAll(table, True, 4000, "Light")]},
	'Gardner, the Invoked': {'onPlay': [lambda card: gear("mana")]},
	'Gigabalza': {'onPlay': [lambda card: targetDiscard(True)]},
	'Gigabuster':{'onPlay':[lambda card: bounceShield()]},
	'Gigandura':{'onPlay': [lambda card: gigandura(card)]},
	'Gigargon': {'onPlay': [lambda card: search(me.piles["Graveyard"], 2, "Creature")]},
	'Grape Globbo':{'onPlay':[lambda card: lookAtOpponentHand()]},
	'Grave Worm Q': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "ALL", "ALL", "Survivor")]},
	'Gunes Valkyrie, Holy Vizier': {'onPlay': [lambda card: tapCreature()]},
	'Gylus, Larval Lord': {'onPlay': [lambda card: targetDiscard(True)], 'onLeaveBZ':[lambda card: opponentSearch([targetPlayer.piles["Graveyard"]])]},
	'Gyulcas, Sage of the East Wind': {'onPlay': [lambda card: search(me.Deck, 1, "Cross Gear")]},
	'Hawkeye Lunatron': {'onPlay': [lambda card: search(me.Deck, 1, "ALL", "ALL", "ALL", False)]},
	'Hazaria, Duke of Thorns': {'onPlay': [lambda card: waveStriker(lambda card:opponentSacrifice(), card)]},
	'Honenbe, Skeletal Guardian': {'onPlay': [lambda card: mill(me.Deck, 3, True), lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Hormone, Maxim Bronze': {'onPlay': [lambda card: mana(me.Deck)]},
	'Hot Spring Crimson Meow': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Hulk Crawler': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Hurlosaur': {'onPlay': [lambda card: kill(1000)]},
	'Iron Arm Tribe': {'onPlay': [lambda card: mana(me.Deck)]},
	'Izana Keeza': {'onPlay': [lambda card: kill(2000)]},
	'Jagila, the Hidden Pillager': {'onPlay':[lambda card: waveStriker(lambda card: targetDiscard(True, "grave", 3), card)]},
	'Jasmine, Mist Faerie': {'onPlay': [lambda card: suicide(card, mana, [me.Deck])]},
	'Jelly, Dazzling Electro-Princess': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Jenny, the Dismantling Puppet': {'onPlay': [lambda card: targetDiscard()]},
	'Jenny, the Suicide Doll': {'onPlay': [lambda card: suicide(card, targetDiscard, [True])]},
	'Jet R.E, Brave Vizier': {'onPlay': [lambda card: shields(me.Deck)]},
	'Katta Kirifuda & Katsuking -Story of Passion-': {'onPlay': [lambda card: lookAtTopCards(5, "card", "hand", "bottom", True, "BOUNCE", ["Fire", "Nature"]), lambda card: bounce(conditionalFromLastFunction=True)]},
	'King Aquakamui': {'onPlay': [lambda card: kingAquakamui(card)]},
	'King Mazelan': {'onPlay': [lambda card: bounce()]},
	'King Ripped-Hide': {'onPlay': [lambda card: draw(me.Deck, True, 2)]},
	'King Muu Q': {'onPlay': [lambda card: bounce()]},
	'King Tsunami':{'onPlay': [lambda card: bounceAll(group = [c for c in table if c!=card])]},
	'Klujadras': {'onPlay': [lambda card: waveStriker(lambda card: klujadras(), card)]},
	'Kolon, the Oracle': {'onPlay': [lambda card: tapCreature()]},
	'Kulus, Soulshine Enforcer':{'onPlay': [lambda card: manaCompare(1,True)]},
	'Larba Geer, the Immaculate':{'onPlay': [lambda card: tapCreature(1, True, filterFunction='re.search(r"{BLOCKER}", c.Rules)')]},
	'Lena, Vizier of Brilliance': {'onPlay': [lambda card: fromMana(1,"Spell")]},
	'Lucky Ball': {'onPlay': [lambda card: draw(me.Deck,True, 2) if len([c for c in table if isShield(c) and c.controller != me])<=3 else None]},
	'Lugias, The Explorer': {'onPlay': [lambda card: tapCreature()]},
	'Locomotiver': {'onPlay': [lambda card: targetDiscard(True)]},
	'Magris, Vizier of Magnetism': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Magmarex': {'onPlay': [lambda card: destroyAll(table, True, 1000,"ALL", False, True)]},
	'Masked Horror, Shadow of Scorn': {'onPlay': [lambda card: targetDiscard(True)]},
	'Mechadragon\'s Breath': {'onPlay':[lambda card: mechadragonsBreath()]},
	'Meteosaur': {'onPlay': [lambda card: kill(2000)]},
	'Miele, Vizier of Lightning': {'onPlay': [lambda card: tapCreature()]},
	'Midnight Crawler': {'onPlay': [lambda card: opponentManaToHand()]},
	'Moors, the Dirty Digger Puppet': {'onPlay': [lambda card: search(me.piles["Graveyard"])]},
	'Muramasa\'s Socket': {'onPlay': [lambda card: kill(1000)]},
	'Murian': {'onPlay': [lambda card: suicide(card, draw, [me.Deck])]},
	'Nam=Daeddo, Bronze Style': {'onPlay': [lambda card: mana(me.Deck, preCondition=manaArmsCheck("Nature",3))]},
	'Necrodragon Bryzenaga': {'onPlay': [lambda card: peekShields([c for c in table if isShield(c) and c.owner == me])]},
	'Niofa, Horned Protector': {'onPlay': [lambda card: search(me.Deck, 1, "ALL", "Nature")]},
	'Ochappi, Pure Hearted Faerie': {'onPlay': [lambda card: fromGrave()]},
	'Onslaughter Triceps':{'onPlay': [lambda card: fromMana(toGrave=True)]},
	'Pakurio': {'onPlay': [lambda card: targetDiscard(False,"shield")]},
	'Phal Eega, Dawn Guardian': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Spell")]},
	'Phal Pierro, Apocalyptic Guardian': {'onPlay': [lambda card: suicide(card, search, [me.piles["Graveyard"], 1, "Spell"])]},
	'Phal Reeze, Apocalyptic Sage': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Spell")]},
	'Piara Heart': {'onPlay': [lambda card: kill(1000)]},
	'Pointa, the Aqua Shadow': {'onPlay': [lambda card: peekShield(1, True),lambda card: targetDiscard(True)]},
	'Poison Worm':{'onPlay':[lambda card: kill(3000, 1, targetOwn=True)]},
	'Prometheus, Splash Axe': {'onPlay': [lambda card: mana(me.Deck, 2, False, True)]},
	'Punch Trooper Bronks': {'onPlay': [lambda card: bronks()]},
	'Q-tronic Hypermind': {'onPlay': [lambda card: draw(me.Deck, True, len(getSurvivorsOnYourTable(False)))]},
	'Qurian': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Raiden, Lightfang Ninja': {'onPlay': [lambda card: tapCreature()]},
	'Rayla, Truth Enforcer': {'onPlay': [lambda card: search(me.Deck, 1, "Spell")]},
	'Raptor Fish':{'onPlay': [lambda card: raptorFish()]},
	'Rimuel, Cloudbreak Elemental':{'onPlay': [lambda card: tapCreature(len([c for c in table if isMana(c) and c.owner==me and re.search("Light", c.Civilization) and c.orientation == Rot180]))]},
	'Ripple Lotus Q': {'onPlay': [lambda card: tapCreature()]},
	'Rom, Vizier of Tendrils': {'onPlay': [lambda card: tapCreature()]},
	'Rothus, the Traveler': {'onPlay': [lambda card: rothus()]},
	'Romanesk, the Dragon Wizard': {'onPlay': [lambda card: mana(me.Deck, 4)]},
	'Rumbling Terahorn': {'onPlay': [lambda card: search(me.Deck, 1, "Creature")]},
	'Ryokudou, the Principle Defender': {'onPlay': [lambda card: mana(me.Deck,2), lambda card: fromMana()]},
	'Sarvarti, Thunder Spirit Knight': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Spell")]},
	'Saucer-Head Shark':{'onPlay': [lambda card: bounceAll(filterFunction="int(c.Power.strip('+'))<=2000")]},
	'Scissor Scarab': {'onPlay': [lambda card: search(1,"ALL","ALL","Giant Insect")]},
	'Shtra': {'onPlay': [lambda card: bothPlayersFromMana()]},
	'Self-Destructing Gil Poser': {'onPlay': [lambda card: suicide(card, kill, [2000])]},
	'Sir Navaal, Thunder Mecha Knight': {'onPlay': [lambda card: fromMana(1,"Spell")]},
	'Sir Virginia, Mystic Light Insect': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Scarlet Skyterror': {'onPlay': [lambda card: destroyAll([c for c in table if re.search("\{BLOCKER\}", c.Rules)], True)]},
	'Skeleton Thief, the Revealer':{'onPlay': [lambda card: search(me.piles["Graveyard"], RaceFilter="Living Dead")]},
	'Skyscraper Shell': {'onPlay': [lambda card: waveStriker(lambda card: opponentSendToMana(), card)]},
	'Skysword, the Savage Vizier': {'onPlay': [lambda card: mana(me.Deck), lambda card: shields(me.deck)]},
	'Solidskin Fish': {'onPlay': [lambda card: fromMana()]},
	'Spiritual Star Dragon': {'onPlay': [lambda card: fromDeck()]},
	'Splash Zebrafish': {'onPlay': [lambda card: fromMana()]},
	'Storm Shell':{'onPlay': [lambda card: opponentSendToMana()]},
	'Steamroller Mutant': {'onPlay': [lambda card: waveStriker(lambda card: destroyAll(table, True), card)]},
	'Swamp Worm': {'onPlay': [lambda card: opponentSacrifice()]},
	'Syforce, Aurora Elemental': {'onPlay': [lambda card: fromMana(1,"Spell")]},
	'Telitol, the Explorer': {'onPlay': [lambda card: peekShields([c for c in table if isShield(c) and c.owner == me])]},
	'Tekorax': {'onPlay': [lambda card: peekShield(len([c for c in table if isShield(c) and c.owner != me]),True)]},
	'Terradragon Zalberg': {'onPlay': [lambda card: destroyMana(2)]},
	'Thorny Mandra': {'onPlay': [lambda card: fromGrave()]},
	'Thrash Crawler': {'onPlay': [lambda card: fromMana()]},
	'Three-Faced Ashura Fang':{'onPlay': [lambda card: bounceShield()]},
	'Titan Giant': {'onPlay': [lambda card: mana (me.Deck, 2, True)]},
	'Torpedo Cluster': {'onPlay': [lambda card: fromMana()]},
	'Trenchdive Shark': {'onPlay': [lambda card: shieldswap(card,2)]},
	'Triple Mouth, Decaying Savage': {'onPlay': [lambda card: mana(me.Deck), lambda card: targetDiscard(True)]},
	'Trombo, Fractured Doll': {'onPlay': [lambda card: waveStriker(lambda card: sercah(me.piles["Graveyard"], 1, "Creature"), card)]},
	'Trox, General of Destruction':{'onPlay': [lambda card: targetDiscard(randomDiscard=True, count=len([c for c in table if isCreature(c) and not isBait(c) and c.owner==me and re.search("Darkness", c.Civilization) and c._id!=card._id]))]},
	'Uncanny Turnip': {'onPlay': [lambda card: waveStriker([lambda card: mana(me.Deck), lambda card: fromMana(1,'Creature')], card)]},
	'Unicorn Fish': {'onPlay': [lambda card: bounce()]},
	'Vampire Silphy':{'onPlay': [lambda card: destroyAll(table, True, 3000)]},
	'Velyrika Dragon': {'onPlay': [lambda card: search(me.Deck, 1, "ALL", "ALL", "Armored Dragon")]},
	'Viblo Blade, Hulcus Range': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Walmiel, Electro-Sage': {'onPlay': [lambda card: tapCreature()]},
	'Whispering Totem': {'onPlay': [lambda card: fromDeck()]},
	'Wind Axe, the Warrior Savage': {'onPlay': [lambda card: kill(count=1, rulesFilter="{BLOCKER}"), lambda card: mana(me.Deck)]},
	'Zardia, Spirit of Bloody Winds': {'onPlay': [lambda card: shields(me.Deck)]},
	'Zemechis, the Explorer': {'onPlay': [lambda card: gear("kill")]},

	# ON CAST EFFECTS

	'Abduction Charger': {'onPlay': [lambda card: bounce(2)]},
	'Apocalypse Day': {'onPlay': [lambda card: destroyAll(table, len([c for c in table if isCreature(c) and not isBait(c)])>5)]},
	'Apocalypse Vise': {'onPlay': [lambda card: apocalypseVise()]},
	'Big Beast Cannon': {'onPlay': [lambda card: kill(7000)]},
	'Blizzard of Spears': {'onPlay': [lambda card: destroyAll(table, True, 4000)]},
	'Bomber Doll': {'onPlay': [lambda card: kill(2000)]},
	'Bonds of Justice': {'onPlay': [lambda card: tapCreature(1, True, True, filterFunction='not re.search(r"{BLOCKER}", c.Rules)')]},
	'Bone Dance Charger': {'onPlay': [lambda card: mill(me.Deck, 2)]},
	'Boomerang Comet': {'onPlay': [lambda card: fromMana(), lambda card: toMana(card)]},
	'Brain Cyclone': {'onPlay': [lambda card: draw(me.Deck, False, 1)]},
	'Brain Serum': {'onPlay': [lambda card: draw(me.Deck, False, 2)]},
	'Burst Shot': {'onPlay': [lambda card: destroyAll(table, True, 2000)]},
	'Cannonball Sling': {'onPlay': [lambda card: kill(2000)],
						 'onMetaMorph': [lambda card: kill(6000)]},
	'Cataclysmic Eruption':{'onPlay': [lambda card: destroyMana(len([c for c in table if isCreature(c) and not isBait(c) and c.owner==me and re.search(r'Nature',c.Civilization)]))]},
	'Chains of Sacrifice': {'onPlay': [lambda card: kill("ALL","ALL","ALL",2), lambda card:sacrifice()]},
	'Clone Factory': {'onPlay': [lambda card: fromMana(2)]},
	'Cloned Nightmare': {'onPlay': [lambda card: clonedDiscard()]},
	'Comet Missile': {'onPlay': [lambda card: kill(powerFilter=6000, count=1, rulesFilter="{BLOCKER}")]},
	'Corpse Charger': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Crimson Hammer': {'onPlay': [lambda card: kill(2000)]},
	'Crisis Boulder': {'onPlay': [lambda card: crisisBoulder(card)]},
	'Critical Blade': {'onPlay': [lambda card: kill(count=1, rulesFilter="{BLOCKER}")]},
	'Crystal Memory': {'onPlay': [lambda card: search(me.Deck, 1, "ALL", "ALL", "ALL", False)]},
	'Cyber Brain': {'onPlay': [lambda card: draw(me.Deck, True, 3)]},
	'Cyclone Panic': {'onPlay': [lambda card: cyclonePanic()]},
	'Dance of the Sproutlings': {'onPlay': [lambda card: declareRace(card)]},
	'Darkflame Drive': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Darkpact': {'onPlay': [lambda card: darkpact(card)]},
	'Dark Reversal': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Death Chaser': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Death Cruzer, the Annihilator': {'onPlay': [lambda card: destroyAll([c for c in table if c.controller == me and c != card], True)]},
	'Death Gate, Gate of Hell': {'onPlay': [lambda card: kill("ALL","Untap"), lambda card: fromGrave()]},
	'Death Smoke': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Decopin Crash': {'onPlay': [lambda card: kill(4000)]},
	'Devil Hand': {'onPlay': [lambda card: kill(), lambda card: mill(me.Deck, 3, True)]},
	'Devil Smoke': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Dimension Gate': {'onPlay': [lambda card: search(me.Deck, 1, "Creature")]},
	'Divine Riptide':{'onPlay': [lambda card: divineRiptide()]},
	'Slash Charger': {'onPlay': [lambda card: fromDeckToGrave()]},
	'Dracobarrier': {'onPlay': [lambda card: dracobarrier()]},
	'Drill Bowgun': {'onPlay': [lambda card: gear("kill")]},
	'Emergency Typhoon':{'onPlay': [lambda card: draw(me.Deck, True, 2), lambda card: selfDiscard()]},
	'Enchanted Soil': {'onPlay': [lambda card: fromGrave()]},
	'Energy Stream': {'onPlay': [lambda card: draw(me.Deck, False, 2)]},
	'Eureka Charger': {'onPlay': [lambda card: draw(me.Deck)]},
	'Eureka Program': {'onPlay': [lambda card: eurekaProgram(True)]},
	'Faerie Crystal': {'onPlay': [lambda card: mana(me.Deck, postAction="ManaIfCiv", postArgs=["Zero"])]},
	'Faerie Life': {'onPlay': [lambda card: mana(me.Deck)]},
	'Faerie Miracle': {'onPlay': [lambda card: mana(me.Deck, postAction="mana(me.Deck)", postCondition="manaArmsCheck()")]},
	'Faerie Shower': {'onPlay': [lambda card: lookAtTopCards(2,"card","hand","mana", False)]},
	'Flame-Absorbing Palm': {'onPlay': [lambda card: kill(2000)]},
	'Fire Crystal Bomb': {'onPlay': [lambda card: kill(5000)]},
	'Flame Lance Trap': {'onPlay': [lambda card: kill(5000)]},
	'Flood Valve': {'onPlay': [lambda card: fromMana()]},
	'Freezing Icehammer':{'onPlay': [lambda card: sendToMana(filterFunction = "re.search(r'Water', c.Civilization) or re.search(r'Darkness', c.Civilization)")]},
	'Future Slash':{'onPlay': [lambda card: fromDeckToGrave(2,True)]},
	'Gardening Drive': {'onPlay': [lambda card: mana(me.Deck)]},
	'Gatling Cyclone': {'onPlay': [lambda card: kill(2000)]},
	'Geo Bronze Magic': {'onPlay': [lambda card: mana(me.Deck, postAction="DrawIfCiv", postArgs=["Fire", "Light"])]},
	'Ghastly Drain':{'onPlay': [lambda card: ghastlyDrain(card)]},
	'Ghost Clutch': {'onPlay': [lambda card: targetDiscard(True)]},
	'Ghost Touch': {'onPlay': [lambda card: targetDiscard(True)]},
	'Glory Snow':{'onPlay': [lambda card: manaCompare(2,True)]},
	'Goren Cannon': {'onPlay': [lambda card: kill(3000)]},
	'Grinning Hunger': {'onPlay': [lambda card: grinningHunger(card)]},
	'Goromaru Communication': {'onPlay': [lambda card: search(me.Deck, 1, "Creature")]},
	'Hell Chariot': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Hide and Seek': {'onPlay': [lambda card: bounce(1, True, filterFunction='not re.search("Evolution", c.Type)'), lambda card: targetDiscard(True)]},
	'Hirameki Program': {'onPlay': [lambda card: eurekaProgram(True)]},
	'Hogan Blaster': {'onPlay': [lambda card: drama(True, "creature or spell", "battlezone", "top")]},
	'Holy Awe': {'onPlay': [lambda card: tapCreature(1, True)]},
	'Hopeless Vortex': {'onPlay': [lambda card: kill()]},
	'Hydro Hurricane':{'onPlay': [lambda card: hydroHurricane(card)]},
	'Hyperspatial Storm Hole': {'onPlay': [lambda card: kill(5000)]},
	'Hyperspatial Bolshack Hole': {'onPlay': [lambda card: kill(5000)]},
	'Hyperspatial Kutt Hole': {'onPlay': [lambda card: kill(5000)]},
	'Hyperspatial Guard Hole': {'onPlay': [lambda card: sendToShields(1, True, True, True, False, 'not re.search(r"Evolution", c.Type)')]},
	'Hyperspatial Vice Hole': {'onPlay': [lambda card: targetDiscard()]},
	'Hyperspatial Shiny Hole': {'onPlay': [lambda card: tapCreature()]},
	'Hyperspatial Energy Hole': {'onPlay': [lambda card: draw(me.Deck, False, 1)]},
	'Hyperspatial Faerie Hole': {'onPlay': [lambda card: mana(me.Deck)]},
	'Hyperspatial Revive Hole': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Illusionary Merfolk': {'onPlay': [lambda card: draw(me.Deck, True, 3) if len([c for c in table if isCreature(c) and not isBait(c) and c.owner == me and re.search("Cyber Lord", c.Race)]) > 0 else None]},
	'Impossible Tunnel': {'onPlay': [lambda card: declareRace(card)]},
	'Infernal Smash': {'onPlay': [lambda card: kill()]},
	'Intense Evil':{'onPlay': [lambda card: intenseEvil()]},
	'Dondon Vacuuming Now': {'onPlay': [lambda card: lookAtTopCards(5, "card", "hand", "bottom", True, "BOUNCE", ["Fire", "Nature"]), lambda card: bounce(conditionalFromLastFunction=True)]},
	'Invincible Abyss': {'onPlay': [lambda card: destroyAll([c for c in table if c.owner != me], True)]},
	'Invincible Aura': {'onPlay': [lambda card: shields(me.Deck, 3, True)]},
	'Invincible Cataclysm':{'onPlay': [lambda card: burnShieldKill(3)]},
	'Invincible Technology': {'onPlay': [lambda card: search(me.Deck, len(me.Deck))]},
	'Justice Jamming':{'onPlay': [lambda card: mode([lambda card: tapCreature(targetALL=True, includeOwn=True, filterFunction='re.search(r"Darkness",c.Civilization)'), lambda card: tapCreature(targetALL=True, includeOwn=True, filterFunction='re.search(r"Fire",c.Civilization)')], card, ["Tap all Darkness Creatures","Tap all Fire Creatures"])]},
	'Laser Whip':{'onPlay':[lambda card: tapCreature()]},
	'Lifeplan Charger': {'onPlay': [lambda card: lookAtTopCards(5, "Creature")]},
	'Lightning Charger': {'onPlay': [lambda card: tapCreature()]},
	'Like a Rolling Storm': {'onPlay': [lambda card: mill(me.Deck, 3, True), lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Lionic Phantom Dragon\'s Flame': {'onPlay': [lambda card: kill(2000)]},
	'Liquid Scope': {'onPlay': [lambda card: lookAtOpponentHand(),lambda card: peekShield(len([c for c in table if isShield(c) and c.owner != me]),True)]},
	'Living Lithograph': {'onPlay': [lambda card: mana(me.Deck)]},
	'Logic Cube': {'onPlay': [lambda card: search(me.Deck, 1, "Spell")]},
	'Logic Sphere': {'onPlay': [lambda card: fromMana(1, "Spell")]},
	'Lost Soul': {'onPlay': [lambda card: discardAll()]},
	'Mana Crisis': {'onPlay': [lambda card: destroyMana()]},
	'Mana Nexus': {'onPlay': [lambda card: sendToShields(1, False, True, False, True)]},
	'Martial Law': {'onPlay': [lambda card: gear("kill")]},
	'Magic Shot - Arcadia Egg': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Magic Shot - Chain Spark': {'onPlay': [lambda card: tapCreature()]},
	'Magic Shot - Open Brain': {'onPlay': [lambda card: draw(me.Deck, False, 2)]},
	'Magic Shot - Panda Full Life': {'onPlay': [lambda card: mana(me.Deck)]},
	'Magic Shot - Soul Catcher': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Magic Shot - Sword Launcher': {'onPlay': [lambda card: kill(3000)]},
	'Mana Bonanza': {'onPlay': [lambda card: massMana(me.Deck, False)]},
	'Miraculous Meltdown': {'onPlay': [lambda card: miraculousMeltdown(card)]},
	'Miraculous Plague': {'onPlay': [lambda card: miraculousPlague()]},
	'Miraculous Rebirth': {'onPlay': [lambda card: miraculousRebirth()]},
	'Miraculous Snare': {'onPlay': [lambda card: sendToShields(1, True, True, True, False, 'not re.search(r"Evolution", c.Type)')]},
	'Moonlight Flash': {'onPlay': [lambda card: tapCreature(2)]},
	'Morbid Medicine': {'onPlay': [lambda card: search(me.piles["Graveyard"], 2, "Creature")]},
	'Mulch Charger': {'onPlay': [lambda card: sendToMana(opponentCards = False,myCards = True)]},
	'Mystery Cube': {'onPlay': [lambda card: drama()]},
	'Mystic Dreamscape': {'onPlay': [lambda card: fromMana(3)]},
	'Mystic Inscription': {'onPlay': [lambda card: shields(me.Deck)]},
	'Mystic Treasure Chest':{'onPlay': [lambda card: fromDeckToMana(1,"not re.search(r\'Nature\', c.Civilization)")]},
	'Natural Snare': {'onPlay': [lambda card: sendToMana()]},
	'Persistent Prison of Gaia': {'onPlay': [lambda card: bounce(1, True, filterFunction = 'not re.search("Evolution", c.Type)'), lambda card: targetDiscard(True)]},
	'Phantom Dragon\'s Flame': {'onPlay': [lambda card: kill(2000)]},
	'Phantasm Clutch': {'onPlay': [lambda card: kill("ALL","Tap")]},
	'Pixie Cocoon': {'onPlay': [lambda card: fromMana(1, "Creature"), lambda card: toMana(card)]},
	'Pixie Life': {'onPlay': [lambda card: mana(me.Deck, 1, False, False), lambda card: fromMana(1, "ALL", "Zero")]},
	'Primal Scream': {'onPlay': [lambda card: mill(me.Deck, 4, True), lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Proclamation of Death': {'onPlay': [lambda card: opponentSacrifice()] },
	'Punish Hold': {'onPlay': [lambda card: tapCreature(2)]},
	'Purgatory Force': {'onPlay': [lambda card: search(me.piles["Graveyard"], 2, "Creature")]},
	'Rain of Arrows': {'onPlay': [lambda card: lookAtHandAndDiscardAll(filterFunction='re.search(r"Darkness",c.Civilization) and re.search(r"Spell",c.Type)')]},
	'Reap and Sow': {'onPlay': [lambda card: destroyMana(), lambda card: mana(me.Deck)]},
	'Reaper Hand': {'onPlay': [lambda card: kill()]},
	'Recon Operation': {'onPlay': [lambda card: peekShield(3, True)]},
	'Reflecting Ray': {'onPlay': [lambda card: tapCreature()]},
	'Relentless Blitz': {'onPlay': [lambda card: declareRace(card)]},
	'Reverse Cyclone': {'onPlay': [lambda card: tapCreature()]},
	'Riptide Charger': {'onPlay': [lambda card: bounce()]},
	'Roar of the Earth': {'onPlay': [lambda card: fromMana(1,"Creature",filterFunction="cardCostComparator(c,6,'>=', typeFilter='Creature')")]},
	'Samurai Decapitation Sword': {'onPlay': [lambda card: kill(5000)]},
	'Scheming Hands': {'onPlay': [lambda card: targetDiscard()]},
	'Screaming Sunburst': {'onPlay': [lambda card: tapCreature(1, True, True, filterFunction='not re.search(r"Light", c.Civilization)')]},
	'Screw Rocket': {'onPlay': [lambda card: gear("kill")]},
	'Seventh Tower': {'onPlay': [lambda card: mana(me.Deck)],
				   'onMetamorph': [lambda card: mana(me.Deck,3)]},
	'Searing Wave': {'onPlay': [lambda card: destroyAll([c for c in table if c.owner != me], True, 3000), lambda card: burnShieldKill(1, True)]},
	'Shock Hurricane':{'onPlay': [lambda card: shockHurricane(card)]},
	'Skeleton Vice': {'onPlay': [lambda card: targetDiscard(True, "grave", 2)]},
	'Snake Attack':{'onPlay': [lambda card: burnShieldKill(1,True)]},
	'Solar Grace': {'onPlay': [lambda card: tapCreature()]},
	'Solar Ray': {'onPlay': [lambda card: tapCreature()]},
	'Solar Trap': {'onPlay': [lambda card: tapCreature()]},
	'Soulswap': {'onPlay': [lambda card: soulSwap()]},
	'Soul Gulp':{'onPlay': [lambda card: opponentToDiscard(len([c for c in table if isCreature(c) and not isBait(c) and c.owner!=me and re.search("Light", c.Civilization)]))]},
	'Spastic Missile': {'onPlay': [lambda card: kill(3000)]},
	'Sphere of Wonder':{'onPlay': [lambda card: manaCompare(1,shield=True)]},
	'Spiral Drive': {'onPlay': [lambda card: bounce()]},
	'Spiral Gate': {'onPlay': [lambda card: bounce()]},
	'Spiral Lance': {'onPlay': [lambda card: gear("bounce")]},
	'Stronghold of Lightning and Flame': {'onPlay': [lambda card: kill(3000), lambda card: tapCreature()]},
	'Submarine Project': {'onPlay': [lambda card: lookAtTopCards(4)]},
	'Super Burst Shot': {'onPlay': [lambda card: destroyAll([c for c in table if c.owner != me], True, 2000)]},
	'Super Infernal Gate Smash': {'onPlay': [lambda card: kill()]},
	'Super Spark': {'onPlay': [lambda card: tapCreature(1,True)]},
	'Teleportation': {'onPlay': [lambda card: bounce(2)]},
	'Ten-Ton Crunch': {'onPlay': [lambda card: kill(3000)]},
	'Terror Pit': {'onPlay': [lambda card: kill("All")]},
	'Thunder Net': {'onPlay': [lambda card: tapCreature(count=len([c for c in table if isCreature(c) and not isBait(c) and c.owner==me and re.search(r'Water',c.Civilization)]))]},
	'The Strong Spiral': {'onPlay': [lambda card: bounce()]},
	'The Strong Breath': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Timeless Garden': {'onPlay': [lambda card: mana(me.Deck)]},
	'Tornado Flame': {'onPlay': [lambda card: kill(4000)]},
	'Transmogrify': {'onPlay': [lambda card: killAndSearch(True)]},
	'Triple Brain': {'onPlay': [lambda card: draw(me.Deck, False, 3)]},
	'Ultimate Force': {'onPlay': [lambda card: mana(me.Deck, 2)]},
	'Unified Resistance': {'onPlay': [lambda card: declareRace(card)]},
	'Upheaval': {'onPlay': [lambda card: upheaval()]},
	'Vacuum Gel': {'onPlay': [lambda card: kill(filterFunction="re.search(r'Light',c.Civilization) or re.search(r'Nature',c.Civilization)")]},
	'Vacuum Ray': {'onPlay': [lambda card: tapCreature()]},
	'Valiant Spark': {'onPlay': [lambda card: tapCreature()],
					  'onMetamorph': [lambda card: tapCreature(1,True)]},
	'Vine Charger': {'onPlay': [lambda card: opponentSendToMana()]},
	'Virtual Tripwire': {'onPlay': [lambda card: tapCreature()]},
	'Volcanic Arrows': {'onPlay': [lambda card: burnShieldKill(1, True, 6000, 1, True)]},
	'Volcano Charger': {'onPlay': [lambda card: kill(2000)]},
	'Wave Lance':{'onPlay':[lambda card: waveLance()]},
	'Wave Rifle': {'onPlay': [lambda card: gear("bounce")]},
	'White Knight Spark': {'onPlay': [lambda card: tapCreature(1,True)]},
	'Wizard Resurrection': {'onPlay': [lambda card: mana(me.Deck), lambda card: fromMana(1,"Spell")]},
	'XENOM, the Reaper Fortress': {'onPlay': [lambda card: targetDiscard(True)]},
	'Zombie Carnival': {'onPlay': [lambda card: declareRace(card), lambda card: search(me.piles["Graveyard"], 3, "Creature")]},
	'Zombie Cyclone': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},

	# ON DESTROY EFFECTS

	'Akashic First, Electro-Dragon': {'onDestroy': [lambda card: toHand(card)]},
	'Akashic Second, Electro-Spirit': {'onPlay': [lambda card: draw(me.Deck, True)],
									'onDestroy': [lambda card: toMana(card)]},
	'Aless, the Oracle':{'onDestroy': [lambda card: toShields(card)]},
	'Aqua Agent': {'onDestroy': [lambda card: toHand(card)]},
	'Aqua Knight': {'onDestroy': [lambda card: toHand(card)]},
	'Aqua Ranger': {'onDestroy': [lambda card: toHand(card)]},
	'Aqua Skydiver': {'onDestroy': [lambda card: toHand(card)]},
	'Aqua Soldier': {'onDestroy': [lambda card: toHand(card)]},
	'Aqua Warrior': {'onDestroy': [lambda card: draw(me.Deck, True, 2)]},
	'Asylum, the Dragon Paladin': {'onDestroy': [lambda card: toShields(card)]},
	'Balloonshroom Q': {'onDestroy': [lambda card: toMana(card)]},
	'Bat Doctor, Shadow of Undeath': {'onDestroy': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Bombersaur':{'onDestroy': [lambda card: bothPlayersFromMana(2,True)]},
	'Bone Piercer': {'onDestroy': [lambda card: fromMana(1, "Creature")]},
	'Bruiser Dragon':{'onDestroy':[lambda card: burnShieldKill(1,True)]},
	'Cetibols': {'onDestroy': [lambda card: draw(me.Deck, True)]},
	'Chilias, the Oracle': {'onDestroy': [lambda card: toHand(card)]},
	'Coiling Vines': {'onDestroy': [lambda card: toMana(card)]},
	'Crasher Burn': {'onDestroy': [lambda card: kill(3000)]},
	'Crystal Jouster': {'onDestroy': [lambda card: toHand(card)]},
	'Cubela, the Oracle': {'onDestroy': [lambda card: tapCreature()]},
	'Death Monarch, Lord of Demons': {'onDestroy': [lambda card: SummonFromGrave(len([c for c in me.piles["Graveyard"] if not re.search("Evolution",c.type)]),"Creature", "ALL", "Demon Command")]},
	'Dracodance Totem': {'onDestroy': [lambda card: dracodanceTotem(card)]},
	'Engineer Kipo':{'onDestroy': [lambda card: bothPlayersFromMana(1,True)]},
	'Fly Lab, Crafty Demonic Tree': {'onDestroy': [lambda card: targetDiscard(True)]},
	'Gigastand':{'onDestroy': [lambda card: returnAndDiscard(card)]},
	'Glider Man': {'onDestroy': [lambda card: targetDiscard()]},
	'Hammerhead Cluster': {'onDestroy': [lambda card: bounce()]},
	'Jewel Spider': {'onDestroy': [lambda card: bounceShield()]},
	'Jil Warka, Time Guardian': {'onDestroy': [lambda card: tapCreature(2)]},
	'Kalute, Vizier of Eternity': {'onDestroy': [lambda card: toHand(card) if any(c for c in table if c.owner == me and c.Name == card.Name) else None]},
	'Mighty Shouter': {'onDestroy': [lambda card: toMana(card)]},
	'Ouks, Vizier of Restoration': {'onDestroy': [lambda card: toShields(card)]},
	'Peace Lupia': {'onDestroy': [lambda card: tapCreature()]},
	'Peru Pere, Viral Guardian': {'onDestroy': [lambda card: toHand(card)]},
	'Pharzi, the Oracle': {'onDestroy': [lambda card: search(me.piles["Graveyard"], 1, "Spell")]},
	'Dream Pirate, Shadow of Theft':{'onDestroy': [lambda card: returnAndDiscard(card)]},
	'Propeller Mutant': {'onDestroy': [lambda card: targetDiscard(True)]},
	'Proxion, the Oracle': {'onDestroy': [lambda card: toHand(card)]},
	'Raza Vega, Thunder Guardian':{'onDestroy': [lambda card: toShields(card)]},
	'Schuka, Duke of Amnesia':{'onDestroy': [lambda card: discardAll(onlySelf=True), lambda card: discardAll()]},
	'Shaman Broccoli': {'onDestroy': [lambda card: toMana(card)]},
	'Shout Corn': {'onDestroy': [lambda card: toMana(card)]},
	'Sinister General Damudo': {'onDestroy': [lambda card: destroyAll(table, True, 3000)]},
	'Solid Horn': {'onDestroy': [lambda card: toMana(card)]},
	'Stallob, the Lifequasher': {'onDestroy': [lambda card: destroyAll(table, True)]},
	'Stubborn Jasper': {'onDestroy': [lambda card: toHand(card)]},
	'Red-Eye Scorpion': {'onDestroy': [lambda card: toMana(card)]},
	'Revival Soldier': {'onDestroy': [lambda card: waveStriker(lambda card: toHand(card), card)]},
	'Worm Gowarski, Masked Insect': {'onDestroy': [lambda card: targetDiscard(True)]},

	#ON REMOVE FROM BATTLE ZONE
	'Cruel Naga, Avatar of Fate': {'onLeaveBZ': [lambda card: destroyAll(table, True)]},

	#ON DISCARD FROM HAND
	'Algo Bardiol, Devil Admiral':  {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},
	'Baiken, Blue Dragon of the Hidden Blade': {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},
	'Bingole, the Explorer': {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},
	'Dava Torey, Seeker of Clouds': {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},
	'Gauss Blazer, Flame Dragon Admiral': {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},
	'Lanerva Stratus, Poseidon\'s Admiral': {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},
	'Mecha Admiral Sound Shooter': {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},
	'Sanfist, the Savage Vizier': {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},
	'Sephia Parthenon, Spirit Admiral': {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},
	'Sir Matthias, Ice Fang Admiral': {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},
	'Terradragon Arque Delacerna': {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},
	'Yu Wandafor, Phantom Beast Admiral': {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},
	'Zack Pichi, Winged Dragon Admiral': {'onDiscard': [lambda card: toPlayAfterDiscard(card)]},

	#ON TAP EFFECTS
	'Adomis, the Oracle':{'onTap': [lambda card: peekShield(1)]},
	'Aeropica':{'onTap': [lambda card: bounce()]},
	'Aqua Fencer':{'onTap': [lambda card: opponentManaToHand()]},
	'Bliss Totem, Avatar of Luck': {'onTap': [lambda card: fromGrave()]},
	'Brood Shell':{'onTap': [lambda card: fromMana(TypeFilter="Creature")]},
	'Charmilia, the Enticer': {'onTap': [lambda card: search(me.Deck, TypeFilter="Creature")]},
	'Chen Treg, Vizier of Blades':{'onTap': [lambda card: tapCreature()]},
	'Cosmogold, Spectral Knight': {'onTap': [lambda card: fromMana(1, "Spell")]},
	'Crath Lade, Merciless King':{'onTap': [lambda card: targetDiscard(randomDiscard=True, count=2)]},
	'Deklowaz, the Terminator': {'onTap': [lambda card: destroyAll(table, True, 3000), lambda card: deklowazDiscard()]},
	'Gigio\'s Hammer': {'onTap': [lambda card: declareRace(card)]},
	'Grim Soul, Shadow of Reversal': {'onTap': [lambda card: search(me.piles["Graveyard"],1,"Creature","Darkness")]},
	'Kachua, Keeper of the Icegate': {'onTap':[lambda card: fromDeckToField("re.search(r'Dragon\\b', c.Race, re.I)")]},
	'Hokira': {'onTap': [lambda card: declareRace(card)]},
	'Kipo\'s Contraption': {'onTap': [lambda card: kill(2000)]},
	'Neon Cluster': {'onTap': [lambda card: draw(me.Deck,False,2)]},
	'Popple, Flowerpetal Dancer':{'onTap': [lambda card: mana(me.Deck)]},
	'Rikabu\'s Screwdriver': {'onTap': [lambda card: kill(count=1, rulesFilter="{BLOCKER}")]},
	'Rondobil, the Explorer': {'onTap': [lambda card: sendToShields(1, False, True)]},
	'Silvermoon Trailblazer': {'onTap': [lambda card: declareRace(card)]},
	'Sky Crusher, the Agitator': {'onTap': [lambda card: bothPlayersFromMana(toGrave=True)]},
	'Tanzanyte, the Awakener': {'onTap': [lambda card: tanzanyte()]},
	'Tank Mutant':{'onTap': [lambda card: opponentSacrifice()]},
	'Techno Totem': {'onTap': [lambda card: tapCreature()]},
	'Tra Rion, Penumbra Guardian': {'onTap': [lambda card: declareRace(card)]},
	'Venom Worm': {'onTap': [lambda card: declareRace(card)]},

	#ON ALLY TAP EFFECTS (Effects that give their on Tap Effect to other creatures)
	#########IMPORTANT DIFFERENCE vvvvvvvvvvvv ################
	# Pass an array like this one: [['Condition Function to filter who gets the effect',['ACTUAL EFFECT]]]
	# 'c' is the variable of card to check with condition before allowing the Tap Effect.
	#########IMPORTANT DIFFERENCE ^^^^^^^^^^^^ ################

	'Arc Bine, the Astounding': {'onAllyTap':[['re.search("Light", c.Civilization)', [lambda card:tapCreature()]]]},
	'Fort Megacluster': {'onAllyTap':[['re.search("Water", c.Civilization)', [lambda card: draw(me.Deck)]]]},
	'Living Citadel Vosh': {'onAllyTap':[['re.search("Nature", c.Civilization)', [lambda card: mana(me.Deck)]]]},
	'Phantasmal Horror Gigazald': {'onAllyTap':[['re.search("Darkness", c.Civilization)', [lambda card: targetDiscard(True)]]]},

	#ON YOUR TURN END EFFECTS

	'Aqua Officer': {'onTurnEnd': [lambda card: tapCreature(2, onlyOwn=True)], 'onTurnStart': [lambda card: draw(me.Deck, True, 2)]},
	'Balesk Baj, the Timeburner': {'onTurnEnd': [lambda card: toHand(card)]},
	'Ballus, Dogfight Enforcer Q': {'onTurnEnd': [lambda card: untapCreature(card, False)]},
	'Bazagazeal Dragon': {'onTurnEnd': [lambda card: toHand(card)]},
	'Betrale, the Explorer': {'onTurnEnd': [lambda card: untapCreature(card, True)]},
	'Cutthroat Skyterror': {'onTurnEnd': [lambda card: toHand(card)]},
	'Frei, Vizier of Air': {'onTurnEnd': [lambda card: untapCreature(card)]},
	'Gnarvash, Merchant of Blood':{'onTurnEnd': [lambda card: lonely(card)]},
	'Laveil, Seeker of Catastrophe': {'onTurnEnd': [lambda card: untapCreature(card)]},
	'Lone Tear, Shadow of Solitude': {'onTurnEnd': {lambda card: lonely(card)}},
	'Pyrofighter Magnus': {'onTurnEnd': [lambda card: toHand(card)]},
	'Ruby Grass': {'onTurnEnd': [lambda card: untapCreature(card)]},
	'Skullcutter, Swarm Leader': {'onTurnEnd': {lambda card: lonely(card)}},
	'Toel, Vizier of Hope': {'onTurnEnd': [lambda card: untapCreatureAll()]},
	'Urth, Purifying Elemental': {'onTurnEnd': [lambda card: untapCreature(card)]},

	#ON YOUR TURN START EFFECTS
	'Aloro, War God': {'onTurnStart': [lambda card: fromMana(1,"ALL","ALL","ALL",True,True)]},
	'Cosmic Nebula': {'onTurnStart': [lambda card: draw(me.Deck, True)]},
	'Cosmoview Lunatron': {'onTurnStart': [lambda card: draw(me.Deck, True)]},
	'Wingeye Moth': {'onTurnStart': [lambda card: draw(me.Deck, True)]},

	#SILENT SKILL EFFECTS
	'Brad, Super Kickin\' Dynamo': {'silentSkill': [lambda card: kill(count=1, rulesFilter="{BLOCKER}")]},
	'Flohdani, the Spydroid': {'silentSkill': [lambda card: tapCreature(2)]},
	'Gazer Eyes, Shadow of Secrets': {'silentSkill': [lambda card: targetDiscard()]},
	'Hustle Berry': {'silentSkill': [lambda card: mana(me.Deck)]},
	'Minelord Skyterror': {'silentSkill': [lambda card: destroyAll(table, True, 3000)]},
	'Soderlight, the Cold Blade': {'silentSkill': [lambda card: opponentSacrifice()]},
	'Vorg\'s Engine': {'silentSkill': [lambda card: destroyAll(table, True, 2000)]},

	#ON ATTACK EFFECTS
	'Amber Piercer':{'onAttack': [lambda card: search(me.piles["Graveyard"], TypeFilter="Creature")]},
	'Armored Warrior Quelos':{'onAttack': [lambda card: bothPlayersFromMana(1,True,"not re.search(r'Fire',c.Civilization)")]},
	'Aqua Grappler': {'onAttack': [lambda card: draw(me.Deck,True,len([c for c in table if c!=card and isCreature(c) and not isBait(c) and c.owner==me and c.orientation==Rot90]))]},
	'Bloodwing Mantis':{'onAttack': [lambda card: fromMana(2,"Creature")]},
	'Bolzard Dragon':{'onAttack': [lambda card: destroyMana()]},
	'Cavern Raider': {'onAttack': [lambda card: search(me.Deck, 1, "Creature")]},
	'Chaos Fish':{'onAttack': [lambda card: draw(group=me.Deck,count=len([c for c in table if isCreature(c) and not isBait(c) and c.owner==me and re.search("Water", c.Civilization) and c._id!=card._id]),ask=True)]},
	'Curious Eye':{'onAttack': [lambda card: peekShield(1, True)]},
	'Cyclolink, Spectral Knight': {'onAttack': [lambda card: search(me.Deck, 1, "Spell")]},
	'Daidalos, General of Fury':{'onAttack': [lambda card: kill(targetOwn=True)]},
	'Dark Titan Maginn':{'onAttack': [lambda card: targetDiscard(True)]},
	'Earthstomp Giant':{'onAttack': [lambda card: fromManaAll("re.search(r'Creature',c.Type)")]},
	'Flametropus':{'onAttack': [lambda card: fromMana(toGrave=True,ask=True)]},
	'Gamil, Knight of Hatred':{'onAttack': [lambda card: search(me.piles["Graveyard"], CivFilter="Darkness")]},
	'General Dark Fiend':{'onAttack': [lambda card: burnShieldKill(1,True)]},
	'Geoshine, Spectral Knight': {'onAttack': [lambda card: tapCreature(includeOwn=True, filterFunction="re.search(r'Fire',c.Civilization) or re.search(r'Darkness',c.Civilization)")]},
	'Headlong Giant':{'onAttack': [lambda card: selfDiscard()]},
	'Horrid Worm': {'onAttack': [lambda card: targetDiscard(True)]},
	'Hypersquid Walter':{'onAttack': [lambda card: draw(me.Deck, True)]},
	'King Neptas':{'onAttack': [lambda card: bounce(1,filterFunction="int(c.Power.strip('+'))<=2000")]},
	'King Ponitas':{'onAttack': [lambda card: search(me.Deck, CivFilter="Water")]},
	'Lalicious':{'onAttack':[lambda card: lookAtOpponentHand(),lambda card: lookAtCards(opponent=True) ]},
	'Laguna, Lightning Enforcer':{'onAttack': [lambda card: search(me.Deck, TypeFilter="Spell")]},
	'Le Quist, the Oracle':{'onAttack': [lambda card: tapCreature(1,filterFunction="re.search(r'Fire',c.Civilization) or re.search(r'Darkness',c.Civilization)")]},
	'Metalwing Skyterror':{'onAttack': [lambda card: kill(rulesFilter="{BLOCKER}")]},
	'Muramasa, Duke of Blades':{'onAttack': [lambda card: kill(2000)]},
	'Necrodragon Galbazeek':{'onAttack': [lambda card: burnShieldKill(1,True)]},
	'Plasma Chaser':{'onAttack': [lambda card: draw(me.Deck, ask=True, count=len([c for c in table if isCreature(c) and not isBait(c) and c.owner!=me]))]},
	'Psyshroom':{'onAttack': [lambda card: fromGraveyardToMana(filterFunction="re.search(r'Nature',c.Civilization)",ask=True)]},
	'Ra Vu, Seeker of Lightning': {'onAttack': [lambda card: search(me.piles["Graveyard"], 1, "Spell","Light")]},
	'Shock Trooper Mykee': {'onAttack': [lambda card: kill(3000)]},
	'Silver Axe':{'onAttack': [lambda card: mana(me.Deck,ask=True)]},
	'Skullsweeper Q':{'onAttack': [lambda card: opponentToDiscard()]},
	'Smile Angler':{'onAttack': [lambda card: opponentManaToHand()]},
	'Sniper Mosquito':{'onAttack': [lambda card: fromMana()]},
	'Stained Glass':{'onAttack': [lambda card: bounce(opponentOnly=True, filterFunction="re.search(r'Fire',c.Civilization) or re.search(r'Nature',c.Civilization)")]},
	'Steam Rumbler Kain': {'onAttack': [lambda card: burnShieldKill(1, True)]},
	'Stinger Ball':{'onAttack': [lambda card: peekShield(1, True)]},
	'Split-Head Hydroturtle Q':{'onAttack': [lambda card: draw(me.Deck,True)]},
	'Supernova Jupiter King Empire': {'onAttack': [lambda card: meteorburn([lambda card, baitList: toPlay(baitList[0])],card, 1, 1)]},
	'Tentacle Cluster': {'onAttack': [lambda card: bounce()]},
	'Trixo, Wicked Doll': {'onAttack': [lambda card: opponentSacrifice()]},
	'Quakesaur': {'onAttack': [lambda card: oppponentFromMana()]},
	'Windmill Mutant': {'onAttack': [lambda card: targetDiscard(True)]},
	'Wyn, the Oracle': {'onAttack': [lambda card: peekShield(1,True)]},
	'Überdragon Bajula':{'onAttack': [lambda card: destroyMana(2)]},

	# ON SHIELD TRIGGER CHECKS - condtion for a card to be shield trigger(functions used here should ALWAYS return a boolean)

	'Awesome! Hot Spring Gallows': {'onTrigger': [lambda card: manaArmsCheck("Water", 3)]},
	'Mettagils, Passion Dragon': {'onTrigger': [lambda card: manaArmsCheck("Fire", 5)]},
	'Sg Spagelia, Dragment Symbol': {'onTrigger': [lambda card: manaArmsCheck("Water", 5)]},
	'Soul Garde, Storage Dragon Elemental': {'onTrigger': [lambda card: manaArmsCheck("Light", 5)]},
	'Traptops, Green Trap Toxickind': {'onTrigger': [lambda card: manaArmsCheck("Nature", 5)]},
	'Zanjides, Tragedy Demon Dragon': {'onTrigger': [lambda card: manaArmsCheck("Darkness", 5)]},

	# Untargettable Cards
	'Petrova, Channeler of Suns':{'untargettable':True,
							   'onPlay': [lambda card: declareRace(card, "Mecha Del Sol")]},
	'Warlord Ailzonius':{'untargettable':True},
	'Yuliana, Channeler of Suns':{'untargettable':True},
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
			remoteCall(nextPlayer, 'untapAll', [convertGroupIntoGroupNameList(table),0,0,True])
			nextTurn(nextPlayer, True)
	else:
		# The first turn. Can be passed to anyone.
		nextTurn(nextPlayer, True)

def resetGame():
	mute()
	me.setGlobalVariable("shieldCount", "0")
	clearFunctionsAndTargets(table)
	for player in players:
		if player != me:
			initiate_handshake(player)

def onTarget(args): #this is triggered by OCTGN events when any card is targeted or untargeted. Used to continue evaluating functions that are waiting for target
	numberOfTargets = len([c for c in table if c.targetedBy == me])
	if numberOfTargets == 0:
		return
	if waitingFunct:
		evaluateWaitingFunctions()

def onArrow(args):
	player = args.player
	fromCard = args.fromCard
	toCard = args.toCard
	targeted = args.targeted
	scripted = args.scripted
	if player != me: return
	if not isMana(fromCard) and not isShield(fromCard):
		global arrow
		if targeted:
			if fromCard._id in arrow:
				arrow[fromCard._id].append(toCard._id)
			else:
				arrow[fromCard._id] = [toCard._id]
		else:
			if fromCard in arrow:
					del arrow[fromCard._id]

def clearArrowOnMove(args):
	cardsMoved = args.cards
	cardsIdMoved = [card._id for card in cardsMoved]
	global arrow
	if not arrow or table not in args.fromGroups:
		return
	keys_to_remove = []
	for key, array in arrow.items():
		arrow[key] = [card for card in array if not card or card not in cardsIdMoved]
		if not arrow[key]:
			keys_to_remove.append(key)
	for key in keys_to_remove:
		del arrow[key]

######### Network Related functions #########
def getPlayerById(playerId):
	for player in players:
		if player._id == playerId:
			return player
	return None

def findCardByIdAndGroup(cardId, playerId, groupName):
	# Check if we need to search in the global table
	if groupName == "Table":
		# Search in the shared table pile
		for card in table:
			if card._id == cardId:
				return card
	else:
		# Retrieve the specific player by controller ID and search in their group
		controller = getPlayerById(playerId)  # Assume getPlayerById retrieves a player by their ID
		if controller:
			pile = controller.piles.get(groupName)
			if pile:
				for card in pile:
					if card._id == cardId:
						return card
	return None

def retrieveCardsFromData(cardDataList):
	cards = []
	for cardData in cardDataList:
		card = findCardByIdAndGroup(cardData["id"], cardData["playerId"], cardData["groupName"])
		if card:
			cards.append(card)
	return cards
###Handles both a single Card object and a list
def ensureCardObjects(cardInput, keepAsList = False):
	if not isinstance(cardInput, list):
		cardInput = [cardInput]
	if all(isinstance(card, Card) for card in cardInput):
		cards = cardInput
	elif all(isinstance(card, dict) and "id" in card for card in cardInput):
		cards = retrieveCardsFromData(cardInput)
	if keepAsList:
		return cards
	return cards[0] if len(cards)==1 else cards

def findGroupByNameAndPlayer(groupName, playerId):
	if groupName == "Table":
		return table

	player = getPlayerById(playerId)
	return player.piles[groupName]

def ensureGroupObject(group):
	if isinstance(group, Group):
		return group
	if isinstance(group, list):
		return ensureCardObjects(group, True)
	if isinstance(group, dict):
		return findGroupByNameAndPlayer(group['name'], group['playerId'])

### IMPORTANT: Send this object instead of Card/CardList for remoteCall!
def convertCardListIntoCardIDsList(cardList):
	if not isinstance(cardList,list):
		cardList=[cardList]
	return [{"id": card._id,"playerId": card.controller._id,"groupName": card.group.name} for card in cardList]
### IMPORTANT: Send this object instead of Group for remoteCall!
def convertGroupIntoGroupNameList(group):
	return {"name":group.name, "playerId":group.player._id if group.player else None}

############################################ Misc utility functions ####################################################################################

def askCard2(list, title="Select a card", buttonText="Select", minimumToTake=1, maximumToTake=1, returnAsArray=False):  # askCard function was changed. So using the same name but with the new functionalit
#this is for showing a dialog box with the cards in the incoming list. Careful, all cards will be visible, even if they're facedown.
	dlg = cardDlg(list)
	dlg.title = title

	if minimumToTake == 0 and not returnAsArray:
		# if this dialog is opened without any card to take, that means it's for rearranging cards.
		dlg.min, dlg.max = 0, 0
		dlg.text = "Card Order (drag to rearrange):"
		dlg.show()
		return dlg.list
	else:
		dlg.min, dlg.max = minimumToTake, maximumToTake
		result = dlg.show()

	if minimumToTake == 0 and maximumToTake == 0 and returnAsArray:
		return dlg.list
	if result is None:
		return None
	if len(result)==1 and not returnAsArray:
		return result[0]
	else:
		return result

def askYN(text="Proceed?", choices=["Yes", "No"], colorsList = ['#FF0000', '#FF0000', '#FF0000']):
	# this asks a simple Y N question, but Yes or No can be replaced by other words. Returns 1 if yes, 2 for No and 0 if the box is closed

	choice = askChoice(text, choices, colorsList)
	return choice

def askNumber(text="Enter a Number", defaultAnswer=1000):
	choice = askInteger(text, defaultAnswer)
	return choice

def getTargetPlayer(text="Pick a player:", onlyOpponent = False):
		playerList = []
		currentPlayers = getPlayers()
		for player in currentPlayers:
			playerList.append(player.name)
		if onlyOpponent and len(playerList) == 2:
			return currentPlayers[1]
		choicePlayer = askChoice(text, playerList)
		if choicePlayer < 1: return
		return currentPlayers[choicePlayer - 1]

def removeIfEvo(card):
	# Will remove passed card from the list of tracked evos/baits
	# returns a list of bait cards if evo was removed
	# returns empty list if not found or bait was removed

	evolveDict = eval(me.getGlobalVariable("evolution"), allowed_globals)
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
	me.setGlobalVariable("evolution", str(evolveDict))
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
	#now wait for user to target - event trigger will run def onTarget
	return

def evaluateWaitingFunctions():
	global alreadyEvaluating
	iterations = 0
	if alreadyEvaluating:
		return
	alreadyEvaluating = True
	while len(waitingFunct)>0:
			card = waitingFunct[0][0]
			iterations+=1
			if(iterations>100):
				notify('Report This to Developer!\nInfinite loop detected - card(s): {}'.format(', '.join(card.name for card, _ in waitingFunct)))
				clearWaitingFuncts()
				break
			#notify("{}, {}".format(card,waitingFunct[0][1]))
			if waitingFunct[0][1](card):
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
	alreadyEvaluating = False

def clearWaitingFuncts():  # clears any pending plays for a card that's waiting to choose targets etc
	if waitingFunct:
		for funct in waitingFunct:
			cardBeingPlayed = waitingFunct[0][0]
			del waitingFunct[0]
			notify("Waiting for target/effect for {} cancelled.".format(cardBeingPlayed))
			if cardBeingPlayed and isSpellInBZ(cardBeingPlayed):
				endOfFunctionality(cardBeingPlayed)
	global alreadyEvaluating, evaluateNextFunction
	alreadyEvaluating = False
	evaluateNextFunction = True #this should always be True, unless you're waiting for the next function to evaluate

def orderEvaluatingFunctions():
	global alreadyEvaluating, waitingFunct
	if waitingFunct:
		waitingFunctions = list(waitingFunct)
		effectAlreadyProcessing = None
		if alreadyEvaluating and waitingFunctions:
			effectAlreadyProcessing = waitingFunctions.pop(0)

		cardList = []
		for card, _ in waitingFunctions:
			if card not in cardList:
				cardList.append(card)
		if len(cardList)>1:
			if me.isInverted: reverseCardList(cardList)
			cardOrder = askCard2(cardList,'Choose the order of effects to activate (from left to right)', minimumToTake=0, maximumToTake=0, returnAsArray=True)
			if not cardOrder: return
			cardOrderMap = {card: index for index, card in enumerate(cardOrder)}
			waitingFunctions = sorted(waitingFunctions, key=lambda x: cardOrderMap.get(x[0]))
			if(effectAlreadyProcessing):
				waitingFunctions.insert(0, effectAlreadyProcessing)
			waitingFunct = waitingFunctions

def manaArmsCheck(civ='ALL5', num=0):
	if civ == 'ALL5':  # check if you have all 5 civs in mana zone
		manaCards = [card for card in table if isMana(card) and card.owner == me]
		civList = ['Light', 'Water', 'Darkness', 'Fire', 'Nature']
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

def reverseCardList(list):
	list.reverse()

def processEvolution(card, targets):
	if any(c.orientation == Rot90 for c in targets):
		card.orientation = Rot90
	if card.orientation == Rot90:
		for c in targets:
			c.orientation = Rot90
	targetList = [c._id for c in targets]
	evolveDict = eval(me.getGlobalVariable("evolution"), allowed_globals)  ##evolveDict tracks all cards 'underneath' the evolution creature
	for evolveTarget in targets:  ##check to see if the evolution targets are also evolution creatures
		if evolveTarget._id in evolveDict:  ##if the card already has its own cards underneath it
			if isCreature(evolveTarget):
				targetList += evolveDict[evolveTarget._id]  ##add those cards to the new evolution creature
			del evolveDict[evolveTarget._id]
	evolveDict[card._id] = targetList
	me.setGlobalVariable("evolution", str(evolveDict))

#Useful to handle Twinpacts
def cardCostComparator(card, value, comparisonOperator='==', typeFilter="ALL"):
	comparisons = {
		'==': operator.eq,
		'!=': operator.ne,
		'<': operator.lt,
		'<=': operator.le,
		'>': operator.gt,
		'>=': operator.ge
	}

	# If the card is a Twinpact (has both Cost1 and Cost2)
	if card.hasProperty("Cost1") and card.hasProperty("Cost2"):
		cost1 = int(card.Cost1)
		cost2 = int(card.Cost2)

		if typeFilter == "ALL":
			if comparisons[comparisonOperator](cost1, value) or comparisons[comparisonOperator](cost2, value):
				return True

		else:
			if re.search(typeFilter,card.Type1) and comparisons[comparisonOperator](cost1, value):
				return True
			if re.search(typeFilter,card.Type2) and comparisons[comparisonOperator](cost2, value):
				return True

	# If it's not a Twinpact card, just compare the single cost
	elif card.hasProperty("Cost"):
		cost = int(card.Cost)
		if typeFilter == "ALL":
			return comparisons[comparisonOperator](cost, value)

		if re.search(typeFilter,card.Type) and comparisons[comparisonOperator](cost, value):
			return True

	return False


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

def isCastle(card):
	mute()
	if card in table and not isShield(card) and not isMana(card) and re.search("Castle", card.Type) and not re.search("Dragheart", card.Type):
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

def isGacharange(card):
	mute()
	if re.search("Gacharange", card.Type):
		return True

def isBait(card):  # check if card is under and evo(needs to be ignored by most things) This is (probably)inefficient, maybe make a func to get all baits once
	evolveDict = eval(card.owner.getGlobalVariable("evolution"), allowed_globals)
	for evo in evolveDict.keys():
		baitList = evolveDict[evo]
		if card._id in baitList:
			return True

#Get a list of bait materials under Evo
def getEvoBaits(card):
	evolveDict = eval(card.owner.getGlobalVariable("evolution"), allowed_globals)
	if card._id in evolveDict:
		baitList = []
		for cardId in evolveDict[card._id]:
			baitList.append(Card(cardId))
		return baitList
	return []

def isEvo(cards, x=0, y=0):
	if len(cards)==0: return
	card = cards[len(cards)-1]
	if card in table and re.search("Evolution", card.Type):
		return True

def isUntargettable(card):
	mute()
	if card in table and card.owner != me and cardScripts.get(card.name, {}).get('untargettable', False):
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
	count = min(count, len(cardsInGroup_CivTypeandRace_Filtered))
	choices = askCard2(cardsInGroup_CivTypeandRace_Filtered, 'Choose {} Creature(s) to Summon from the Graveyard'.format(count),
					  'Graveyard', maximumToTake=count, returnAsArray=True)
	if not isinstance(choices, list): return
	for choice in choices:
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

def lookAtTopCards(num, cardType='card', targetZone='hand', remainingZone='bottom', reveal=True, specialaction='NONE', specialaction_civs = [], count = 1):
	mute()
	notify("{} looks at the top {} Cards of their deck".format(me, num))
	cardList = [card for card in me.Deck.top(num)]
	choices = askCard2(cardList, 'Choose up to {} Card(s) to put into {}'.format(count, targetZone),maximumToTake=count, returnAsArray=True)
	cards_for_special_action = []
	if isinstance(choices, list):
		for choice in choices:
			if not 'NONE' in specialaction:
				cards_for_special_action.append(choice)
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
	cardList = [card for card in me.Deck.top(num-len(choices))]
	# will it always be 1 card that goes into target zone? Account for more in later upgrades
	if len(cardList) > 1 and remainingZone == 'bottom':
		cardList = askCard2(cardList, 'Rearrange the remaining Cards to put to {}'.format(remainingZone), 'OK', 0)
	for card in cardList:
		if remainingZone == 'mana':
			toMana(card)
		else:
			card.resetProperties()
			card.moveToBottom(me.Deck)
			notify("{} moved a card to the bottom of their deck.".format(me))
	if specialaction == "BOUNCE":
		if not any(re.search(civs, card.properties['Civilization']) for civs in specialaction_civs for card in cards_for_special_action):
			global evaluateNextFunction
			evaluateNextFunction = False

#Random discard or look at hand and select discard FOR OPPONENT, also setting cards as shield from hand for some reason?!
#TODO:Split discarding and setting shield
def targetDiscard(randomDiscard=False, targetZone='grave', count=1):
	mute()
	targetPlayer = getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	if randomDiscard:
		for i in range(count):
			remoteCall(targetPlayer, 'randomDiscard', convertGroupIntoGroupNameList(targetPlayer.hand))
		return
	cardList = [card for card in targetPlayer.hand]
	#Both players see the opponent's hand reversed
	reverseCardList(cardList)
	count = min(count, len(cardList))
	if len(cardList) == count:
		cardChoices = cardList
	else:
		cardChoices = askCard2(cardList, "Choose {} Card(s) to discard.".format(count),minimumToTake=count, maximumToTake=count, returnAsArray=True)
	if not isinstance(cardChoices,list):
		notify("Discard cancelled.")
		return
	for cardChoice in cardChoices:
		if targetZone == 'mana':
			whisper("Putting {} as Mana.".format(cardChoice))
			remoteCall(targetPlayer, 'toMana', convertCardListIntoCardIDsList(cardChoice))
		if targetZone == 'shield':
			whisper("Setting {} as shield.".format(cardChoice))
			remoteCall(targetPlayer, 'toShields', convertCardListIntoCardIDsList(cardChoice))
		elif targetZone == 'grave':
			# do anti-discard check here
			#if not remoteCall(targetPlayer, 'antiDiscard', [cardChoice, me]):
				# anti discard will return false if no antiDiscard is available. Remotecalling because...idk might do some things in antiDiscard later.
				# Maybe change it to normal call later, and remoteCall from only inside anti-disc.
				# still WIP
			remoteCall(targetPlayer, 'toDiscard', convertCardListIntoCardIDsList(cardChoice))

def lookAtOpponentHand():
	targetPlayer = getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	cardList = [card for card in targetPlayer.hand]
	#Both players see their opponent's hand reversed
	reverseCardList(cardList)
	notify("{} looks at {} Hand.".format(me,targetPlayer))
	askCard2(cardList, "Opponent's Hand. (Close to continue)", minimumToTake=0)

#Look at selected player's hand and discard all cards matching filterFunction
def lookAtHandAndDiscardAll(filterFunction="True"):
	targetPlayer = getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	cardList = [card for card in targetPlayer.hand]
	#Both players see their opponent's hand reversed
	reverseCardList(cardList)
	askCard2(cardList, "Opponent's Hand. (Close to continue)", minimumToTake=0)
	choices = [c for c in cardList if eval(filterFunction, allowed_globals, {'c': c})]
	for choice in choices:
		remoteCall(choice.owner, 'toDiscard', convertCardListIntoCardIDsList(choice))

def discardAll(onlyOpponent=True, onlySelf=False):
	mute()
	cardList = []
	targetPlayer=me
	if onlySelf == False: targetPlayer = getTargetPlayer(onlyOpponent=onlyOpponent)
	if not targetPlayer: return
	cardList = [card for card in targetPlayer.hand]
	for card in cardList:
		remoteCall(targetPlayer, 'toDiscard', convertCardListIntoCardIDsList(card))

#Cloned Nightmares
def clonedDiscard():
	mute()
	targetPlayer = getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	cardList = [card for card in targetPlayer.hand]

	count = 1
	for player in currentPlayers:
		for card in player.piles["Graveyard"]:
			if re.search(card.Name, "Cloned Nightmare"):
				count += 1
	notify("Cloned Nightmares in graves:{}".format(count - 1))

	#if remoteCall(targetPlayer, 'antiDiscard', ['GENERALCHECK', me]): return

	for i in range(0, count):
		remoteCall(targetPlayer, 'randomDiscard', convertGroupIntoGroupNameList(targetPlayer.hand))

# do some anti-discard inside dat randomdisc function

#Move a card from Mana to hand/graveyard
def fromMana(count=1, TypeFilter="ALL", CivFilter="ALL", RaceFilter="ALL", show=True, toGrave=False, filterFunction='True', ask=False):
	mute()
	if ask:
			choice = askYN("Would you like to remove {} Card(s) from Mana?".format(count))
			if choice != 1: return
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

	cardsInGroup_CivTypeRaceandFunction_Filtered = [c for c in cardsInGroup_CivTypeandRace_Filtered if eval(filterFunction, allowed_globals, {'c': c})]

	if len(cardsInGroup_CivTypeRaceandFunction_Filtered) == 0: return
	if me.isInverted: reverseCardList(cardsInGroup_CivTypeRaceandFunction_Filtered)
	count = min(count, len(cardsInGroup_CivTypeRaceandFunction_Filtered))
	choices = askCard2(cardsInGroup_CivTypeRaceandFunction_Filtered, 'Choose {} Card(s) from the Mana Zone'.format(count), maximumToTake=count, returnAsArray=True)
	if not isinstance(choices,list): return
	for choice in choices:
		if toGrave == True:
			destroy(choice)
		else:
			toHand(choice,show)

#move all cards fulfilling the condition from Mana to hand
def fromManaAll(filterFunction='True'):
	manaCards = [c for c in table if isMana(c) and c.owner == me if eval(filterFunction, allowed_globals, {'c': c})]
	if len(manaCards)== 0: return
	for c in manaCards:
		toHand(c)

def killAndSearch(play=False, singleSearch=False):
	# looks like this is only used for Transmogrify
	mute()
	cardList = [c for c in table if isCreature(c) and not isBait(c) and not isUntargettable(c)]
	if len(cardList) == 0: return
	if me.isInverted: reverseCardList(cardList)
	choice = askCard2(cardList, 'Choose a Creature to destroy')
	if type(choice) is not Card: return
	remoteCall(choice.owner, 'destroy', convertCardListIntoCardIDsList(choice))
	if singleSearch:
		return
	else:
		remoteCall(choice.owner, 'loopThroughDeck', [choice.owner._id, play])

def loopThroughDeck(playerId, play=False):
	mute()
	player = getPlayerById(playerId)
	group = player.Deck
	if len(group) == 0: return
	newCard = group[0]
	newCard.isFaceUp = True
	notify("{} reveals {}".format(player, newCard.Name))

	if re.search("Creature", newCard.Type) and not re.search("Evolution Creature", newCard.Type):
		if play == True:
			remoteCall(newCard.owner, 'toPlay', convertCardListIntoCardIDsList(newCard))
			return
		else:
			#moveTo is a API function, cannot convert Group
			remoteCall(newCard.owner, 'moveTo', newCard.owner.hand)
			return
	else:
		remoteCall(newCard.owner, 'toDiscard', convertCardListIntoCardIDsList(newCard))
		remoteCall(newCard.owner, 'loopThroughDeck', [playerId, play])

def eurekaProgram(ask=True):
	mute()
	cardList = [card for card in table if isCreature(card) and not isBait(card) and card.owner == me]
	cardList = [card for card in cardList if not re.search("Psychic", card.Type)]
	if len(cardList) == 0: return
	if me.isInverted: reverseCardList(cardList)
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

		if cardCostComparator(card,originalCost+1,"==","Creature"):
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
		card.resetProperties()
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
	group = ensureGroupObject(group)
	if len(group) == 0: return
	maximumToTake = min(count,len(group))
	dialogText = 'Search {} '.format(maximumToTake) + '{}(s) to take to hand'
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
	while(True):
		choices = askCard2(sort_cardList(cardsInGroup), dialogText,maximumToTake=maximumToTake,returnAsArray=True)
		if not isinstance(choices,list):
			group.shuffle()
			notify("{} finishes searching their {}".format(me, group.name))
			return
		if all(c in cardsInGroup_CivTypeandRace_Filtered for c in choices):
			for choice in choices:
				toHand(choice, show)
			break
	group.shuffle()
	notify("{} finishes searching their {}".format(me, group.name))

#Pick a card from any Player's Deck and send it to Graveyard
def fromDeckToGrave(count=1, onlyOpponent=False):
	mute()
	group = []
	targetPlayer = getTargetPlayer(onlyOpponent=onlyOpponent)
	if not targetPlayer: return
	group = targetPlayer.deck
	if len(group) == 0: return
	count = min(count,len(group))
	cardsInGroup = sort_cardList([card for card in group])
	choices = askCard2(cardsInGroup, 'Search {} Card(s) to put to Graveyard'.format(count), maximumToTake=count, returnAsArray=True)
	if not isinstance(choices,list):
		remoteCall(targetPlayer,'shuffle',convertGroupIntoGroupNameList(group))
		notify("{} finishes searching {}'s {} and shuffles the deck.".format(me, targetPlayer, group.name))
		return
	for choice in choices:
		remoteCall(targetPlayer,'toDiscard',convertCardListIntoCardIDsList(choice))
	update()

	remoteCall(targetPlayer,'shuffle', convertGroupIntoGroupNameList(group))
	update()
	notify("{} finishes searching {}'s {} and shuffles the deck.".format(me, targetPlayer, group.name))

#Pick a card from your deck and place it into Mana.
def fromDeckToMana(count=1, filterFunction="True"):
	mute()
	group = me.deck
	if len(group) == 0: return
	count = min(count,len(group))
	cardsInGroup = sort_cardList([card for card in group])
	validChoices = [c for c in cardsInGroup if eval(filterFunction, allowed_globals, {'c': c})]
	while (True):
		choices = askCard2(cardsInGroup, 'Search {} Card(s) to put to Mana'.format(count), maximumToTake=count, returnAsArray=True)
		if not isinstance(choices, list):
			shuffle(group)
			notify("{} finishes searching their {} and shuffles the deck.".format(me, group.name))
			return
		if all(elem in validChoices for elem in choices):
			for choice in choices:
				toMana(choice)
			break
	shuffle(group)
	notify("{} finishes searching their {} and shuffles the deck.".format(me, group.name))

#Target creatures, if they match the filter, they get destroyed.
def kill(powerFilter='ALL', tapFilter='ALL', civFilter='ALL', count=1, targetOwn=False, rulesFilter='ALL', filterFunction="True"):
	mute()
	if powerFilter == 'ALL':	powerFilter = float('inf')
	if targetOwn:
		cardList = [c for c in table if isCreature(c) and not isBait(c) and int(c.Power.strip('+')) <= powerFilter]
	else:
		cardList = [c for c in table if isCreature(c) and not isBait(c) and not c.owner == me and int(c.Power.strip('+')) <= powerFilter]
	if tapFilter != 'ALL':
		if tapFilter == 'Untap':
			cardList = [c for c in cardList if c.orientation == Rot0]
		if tapFilter == 'Tap':
			cardList = [c for c in cardList if c.orientation == Rot90]
	if civFilter != "ALL":
		cardList = [c for c in cardList if re.search(civFilter, c.Civilization)]
	if rulesFilter != 'ALL':
		cardList = [c for c in cardList if re.search(rulesFilter, c.Rules)]
	cardList = [c for c in cardList if eval(filterFunction, allowed_globals, {'c': c}) and not isUntargettable(c)]
	if len(cardList) == 0:
		whisper("No valid targets on the table.")
		return

	count = min(count, len(cardList))
	targets = [c for c in table if c.targetedBy == me and isCreature(c) and not isUntargettable(c)]
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
		remoteCall(card.owner, "destroy", convertCardListIntoCardIDsList(card))

#Mass Destruction handling, call this instead of destroy() if you are destroying more than 1 Creature at once.
def destroyAll(group, condition=False, powerFilter='ALL', civFilter="ALL", AllExceptFiltered=False, exactPower=False, dontAsk=False):
	mute()
	group = ensureGroupObject(group)
	clear(group)
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
						isCreature(card) and (int(card.Power.strip('+')) == powerFilter if exactPower else int(card.Power.strip('+')) <= powerFilter)
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
		cardToBeSaved != card and isCreature(card) and card.owner == me and not isBait(card) and re.search("Saver",card.rules) and (
			re.search(cardToBeSaved.properties['Race'], card.rules) or re.search(
			"Saver: All Races", card.rules))]
		if len(possibleSavers) > 0:
			if confirm("Prevent {}'s destruction by using a Saver on your side of the field?\n\n".format(
					cardToBeSaved.Name)):
				if me.isInverted: reverseCardList(possibleSavers)
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
			#notify('DEBUG: Added {} to {}'.format(cardScripts.get(card.Name).get('onDestroy'), card.Name))
			functionList = cardScripts.get(card.Name).get('onDestroy')
		if re.search("Survivor", card.Race):
			for surv in survivors:
				if surv != card and cardScripts.get(surv.name, {}).get('onDestroy', []):
					#notify('DEBUG: Added {} to {}'.format(cardScripts.get(surv.name).get('onDestroy'), card.Name))
					functionList.extend(cardScripts.get(surv.name).get('onDestroy'))
		for function in functionList:
			waitingFunct.append([card, function])
	orderEvaluatingFunctions()
	evaluateWaitingFunctions()
	if len(opponentList):
		remoteCall(opponentList[0].owner, "destroyAll", [convertCardListIntoCardIDsList(opponentList), False])

def destroyMana(count=1):
	mute()
	cardList = [card for card in table if isMana(card) and card.owner != me]
	count = min(count,len(cardList))
	if count == 0:
		return
	if me.isInverted: reverseCardList(cardList)
	choices = askCard2(cardList, 'Choose {} Mana Card(s) to destroy'.format(count), maximumToTake=count, returnAsArray=True)
	if not isinstance(choices,list): return
	for choice in choices:
		remoteCall(choice.owner, "destroy", convertCardListIntoCardIDsList(choice))

def destroyAllMana(group, civFilter="ALL", AllExceptFiltered=False):
	mute()
	group = ensureGroupObject(group)
	cardList = []
	if(civFilter != "ALL"):
			cardList = [card for card in group if isMana(card) and (bool(re.search(civFilter, card.Civilization)) != AllExceptFiltered)]
	else:
		cardList = [card for card in group if isMana(card)]
	if len(cardList) == 0: return
	for card in cardList:
		remoteCall(card.owner, "destroy", convertCardListIntoCardIDsList(card))

def burnShieldKill(count=1, targetOwnSh=False, powerFilter='ALL', killCount=0, targetOwnCr=False):  # Mainly for destroying shields. Kill is optional.
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
		validKillTargets = [c for c in table if isCreature(c) and not isBait(c) and not isUntargettable(c) and int(c.Power.strip(' +')) <= powerFilter]
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
		remoteCall(shield.owner, "destroy", [convertCardListIntoCardIDsList(shield), 0, 0, True])
	for card in targetCr:
		remoteCall(card.owner, "destroy", convertCardListIntoCardIDsList(card))

#Shows Deck
def fromDeck():
	mute()
	notify("{} looks at their Deck.".format(me))
	me.Deck.lookAt(-1)
#Shows Graveyard
def fromGrave():
	mute()
	notify("{} looks at their Graveyard.".format(me))
	me.piles['Graveyard'].lookAt(-1)

#Shows X cards from top or bottom of the deck
def lookAtCards(count=1, isTop=True, opponent=False):
	mute()
	if opponent:
		targetPlayer =getTargetPlayer(onlyOpponent=opponent)
	else:
		targetPlayer = me
	if isTop == False:
		notify("{} looks at {} cards from bottom of their deck.".format(targetPlayer, count))
	notify("{} looks at {} cards from top of their deck.".format(targetPlayer, count))
	targetPlayer.Deck.lookAt(count, isTop)

#Destroy your own creature
def sacrifice(power=float('inf'), count=1):
	mute()
	cardList = [card for card in table if
				isCreature(card) and not isBait(card) and card.owner == me and re.search("Creature", card.Type)]
	cardList = [card for card in cardList if int(card.Power.strip('+')) <= power]
	if len(cardList) == 0:
		return
	if me.isInverted: reverseCardList(cardList)
	choices = askCard2(cardList, 'Choose {} Creature(s) to destroy'.format(count), maximumToTake=count, returnAsArray=True)
	if not isinstance(choices,list): return
	for choice in choices:
		destroy(choice)

#Return targeted creatures to hand
def bounce(count=1, opponentOnly=False, toDeckTop=False, filterFunction='True', conditionalFromLastFunction=False):
	mute()
	if count == 0: return
	global evaluateNextFunction
	if conditionalFromLastFunction: #for example in case of Dondon Vacuuming Now
		if not evaluateNextFunction:
			evaluateNextFunction = True
			return
	if opponentOnly:
		cardList = [c for c in table if
					isCreature(c) and c.owner != me and not isBait(c) and not isUntargettable(c) and eval(filterFunction, allowed_globals, {'c': c})]
	else:
		cardList = [c for c in table if
					isCreature(c) and not isBait(c) and not isUntargettable(c) and eval(filterFunction, allowed_globals, {'c': c})]
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
			remoteCall(card.owner, "toDeck", convertCardListIntoCardIDsList(card))
		else:
			remoteCall(card.owner, "toHand", convertCardListIntoCardIDsList(card))

#Return every creature that matches filters
def bounceAll(group=table, opponentCards=True, myCards=True, filterFunction = "True"):
	mute()
	group=ensureGroupObject(group)
	cardList = [c for c in group if isCreature(c)
										and not isBait(c)
										and ((opponentCards and c.owner != me) or (myCards and c.owner == me))
										and eval(filterFunction, allowed_globals, {'c': c})]
	if len(cardList) == 0: return
	for card in cardList:
		remoteCall(card.owner, "toHand", convertCardListIntoCardIDsList(card))

#Used for array of shields.
def peekShields(shields):
	for shield in shields:
		shield.peek()
		notify("{} peeks at shield#{}".format(me, shield.markers[shieldMarker]))

#Used to target a shield(s) and peek at them.
def peekShield(count = 1, onlyOpponent = False):
	if onlyOpponent:
		targetPlayer = getTargetPlayer(onlyOpponent=True)
		if not targetPlayer: return
	cardList = [c for c in table if isShield(c) and (not onlyOpponent or c.owner == targetPlayer) and not me in c.peekers]
	if len(cardList) == 0: return
	count = min(count, len(cardList))
	targets = []
	if count != len(cardList):
		whisper('Target the opponent shield(s).')
		targets = [c for c in table if c.targetedBy == me and c in cardList]
		if len(targets) != count:
			whisper('Wrong target(s)!')
			return True
		else:
			clear(targets)
	else:
		targets = cardList
	peekShields(targets)

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
		else:
			whisper("Wrong target(s)!")
			return True #true return forces wait. The same function is called again when targets change.

	for card in bounceList:
		remoteCall(card.owner, "toHand", [convertCardListIntoCardIDsList(card), False])

def gear(str):
	mute()
	if str == 'kill':
		cardList = [card for card in table if isGear(card)
					and not card.owner == me]
		if len(cardList) == 0:
			return
		if me.isInverted: reverseCardList(cardList)
		choice = askCard2(cardList, 'Choose a Cross Gear to send to Graveyard')
		if type(choice) is not Card:
			return
		remoteCall(choice.owner, 'destroy', convertCardListIntoCardIDsList(choice))
	elif str == 'bounce':
		cardList = [card for card in table if isGear(card)]
		if len(cardList) == 0:
			return
		if me.isInverted: reverseCardList(cardList)
		choice = askCard2(cardList, 'Choose a Cross Gear to send to Hand')
		if type(choice) is not Card:
			return
		if choice.owner == me:
			toHand(choice)
		else:
			remoteCall(choice.owner, 'toHand', convertCardListIntoCardIDsList(choice))
	elif str == 'mana':
		cardList = [card for card in table if isGear(card)]
		if len(cardList) == 0:
			return
		if me.isInverted: reverseCardList(cardList)
		choice = askCard2(cardList, 'Choose a Cross Gear to send to Mana')
		if type(choice) is not Card:
			return
		if choice.owner == me:
			toHand(choice)
		else:
			remoteCall(choice.owner, 'toMana', convertCardListIntoCardIDsList(choice))

#Called for Creatures by tapMultiple, which is the same as Ctrl+G or "Tap / Untap"
def processTapUntapCreature(card, processTapEffects = True):
	card = ensureCardObjects(card)
	mute()
	card.orientation ^= Rot90
	evoBaits = getEvoBaits(card)
	for bait in evoBaits:
		bait.orientation = card.orientation
	update()
	if card.orientation & Rot90 == Rot90:
		notify('{} taps {}.'.format(me, card))
		global arrow
		activatedTapEffect = False
		#Helper inner function for onAllyTap
		def handleOnAllyTapEffects(card):
			creaturesonAllyTapList = [c for c in table if isCreature(c) and not isBait(c) and c.controller == me and cardScripts.get(c.Name, {}).get('onAllyTap', [])]
			#remove duplicates from list, only one Tap Effect can be activated at a time.
			if len(creaturesonAllyTapList) == 0: return False
			creaturesonAllyTapList = {c.name: c for c in creaturesonAllyTapList}.values()
			for creature in creaturesonAllyTapList:
				functionList=[]
				functionsonAllyTapList = cardScripts.get(creature.name).get('onAllyTap')
				for functiononAllyTap in functionsonAllyTapList:
					condition = functiononAllyTap[0]
					c = card
					if eval(condition, allowed_globals, {'c': c}):
						functionList.extend(functiononAllyTap[1])
				if len(functionList)>0:
					choice = askYN("Activate Tap Effect(s) for {} by tapping {}?\n\n{}".format(creature.Name, card.Name, creature.Rules), ["Yes", "No"])
					if choice != 1: return False
					notify('{} uses Tap Effect of {} by tapping {}'.format(me, creature, card))
					for index, function in enumerate(functionList):
						waitingFunct.insert(index + 1, [card, function])
					evaluateWaitingFunctions()
					return True
			return False
		#Tap Effects can only activate during active Player's turn.
		if processTapEffects and getActivePlayer() == me and not isBait(card) and not card._id in arrow:
			functionList = cardScripts.get(card.name, {}).get('onTap', [])
			if len(functionList)>0:
				choice = askYN("Activate Tap Effect(s) for {}?\n\n{}".format(card.Name, card.Rules), ["Yes", "No"])
				if choice == 1:
					notify('{} uses Tap Effect of {}'.format(me, card))
					activatedTapEffect = True
					for index, function in enumerate(functionList):
						waitingFunct.insert(index + 1, [card, function])
					evaluateWaitingFunctions()
				else:
					activatedTapEffect = handleOnAllyTapEffects(card)
			else:
				activatedTapEffect = handleOnAllyTapEffects(card)

		#OnAttack Effects can only activate during active Player's turn.
		if processTapEffects and getActivePlayer() == me and not isBait(card) and not activatedTapEffect:
			functionList = cardScripts.get(card.Name, {}).get('onAttack', [])
			if re.search("Survivor",card.Race):
				survivors = getSurvivorsOnYourTable()
				for surv in survivors:
					if surv._id != card._id and cardScripts.get(surv.name, {}).get('onAttack', []):
						functionList.extend(cardScripts.get(surv.Name).get('onAttack'))
			if len(functionList)>0:
				choice = 1
				if(card._id not in arrow):
					choice = askYN("Activate on Attack Effect(s) for {}?\n\n{}".format(card.Name, card.Rules), ["Yes", "No"])
				if choice == 1:
					notify('{} uses on Attack Effect of {}'.format(me, card))
					for index, function in enumerate(functionList):
						waitingFunct.insert(index + 1, [card, function])
					evaluateWaitingFunctions()
	else:
		notify('{} untaps {}.'.format(me, card))

def processOnTurnEndEffects():
	cardList = [card for card in table if card.controller == me and isCreature(card) and not isBait(card)]
	for card in cardList:
		functionList = cardScripts.get(card.name, {}).get('onTurnEnd', [])
		if re.search("Survivor", card.Race):
			survivors = getSurvivorsOnYourTable()
			for surv in survivors:
				if surv._id != card._id and cardScripts.get(surv.name, {}).get('onTurnEnd', []):
					functionList.extend(cardScripts.get(surv.Name).get('onTurnEnd'))
		if len(functionList)>0:
			notify('{} acitvates at the end of {}\'s turn'.format(card.Name, me))
			for function in functionList:
				waitingFunct.append([card, function])
	orderEvaluatingFunctions()
	evaluateWaitingFunctions()

def processOnTurnStartEffects():
	cardList = [card for card in table if card.controller == me and isCreature(card) and not isBait(card)]
	for card in cardList:
		functionList = cardScripts.get(card.name, {}).get('onTurnStart', [])
		if re.search("Survivor", card.Race):
			survivors = getSurvivorsOnYourTable()
			for surv in survivors:
				if surv._id != card._id and cardScripts.get(surv.name, {}).get('onTurnStart', []):
					functionList.extend(cardScripts.get(surv.Name).get('onTurnStart'))
		if len(functionList)>0:
			notify('{} acitvates at the start of {}\'s turn'.format(card.Name, me))
			for function in functionList:
				waitingFunct.append([card, function])
	orderEvaluatingFunctions()
	evaluateWaitingFunctions()

#Send Creature/Mana to shields
def sendToShields(count=1, opponentCards=True, myCards = False, creaturesFilter = True, manaFilter = False, filterFunction='True'):
	mute()
	cardList = [c for c in table if ((creaturesFilter and isCreature(c) and not isBait(c) and not isUntargettable(c)) or (manaFilter and isMana(c)))
			  and ((myCards and c.owner == me) or (opponentCards and c.owner != me)) and eval(filterFunction, allowed_globals, {'c': c})]
	if len(cardList) == 0: return
	count = min(count, len(cardList))
	if count == 0: return
	targets = [c for c in table if c.targetedBy == me and c in cardList]
	if len(targets) != count:
		whisper("Wrong number of targets!")
		return True
	for target in targets:
		target.target(False)
		remoteCall(target.owner, "toShields", convertCardListIntoCardIDsList(target))

#Send creature to Mana
def sendToMana(count=1, opponentCards = True, myCards = False, filterFunction = "True"):
	mute()
	cardList = [c for c in table if isCreature(c)
		  and not isBait(c)
		  and not isUntargettable(c)
		  and ((opponentCards and c.owner != me) or (myCards and c.owner == me))
		  if eval(filterFunction, allowed_globals, {'c': c})]
	if len(cardList) == 0: return
	if me.isInverted: reverseCardList(cardList)
	choices = askCard2(cardList, 'Choose {} Creature(s) to send to Mana Zone'.format(count), maximumToTake=count, returnAsArray=True)
	if not isinstance(choices,list):return
	for choice in choices:
		remoteCall(choice.owner,"toMana", convertCardListIntoCardIDsList(choice))

def selfDiscard(count=1):
	mute()
	cardList = [card for card in me.hand]
	if len(cardList)==0: return
	reverseCardList(cardList)
	count = min(count, len(cardList))
	if len(cardList) == count:
		cardChoices = cardList
	else:
		cardChoices = askCard2(cardList, "Choose {} Card(s) to discard".format(count), minimumToTake=count, maximumToTake=count, returnAsArray=True)
	if not isinstance(cardChoices, list):
		notify("Discard cancelled.")
		return
		# do anti-discard check here
	for cardChoice in cardChoices:
		toDiscard(cardChoice)
		update()

#Summon creature after it got discarded
def toPlayAfterDiscard(card, onlyOnOpponentTurn = True):
	if not onlyOnOpponentTurn or getActivePlayer() != me:
		choice = askYN("Summon {} because it was discarded during opponent's turn?\n\n{}".format(card.Name, card.Rules), ["Yes", "No"])
		if choice == 1:
			toPlay(card)

def suicide(card, action, args):
	mute()
	choiceList = ['Yes', 'No']
	colorsList = ['#FF0000', '#FF0000']
	choice = askChoice("Destroy the card to activate effect?", choiceList, colorsList)
	if choice != 1: return
	toDiscard(card)
	action(*args)

def opponentSacrifice(sacrificeArgs=[]):
	targetPlayer = getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer, 'sacrifice', sacrificeArgs)

def opponentToDiscard(count = 1):
	mute()
	targetPlayer = getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'selfDiscard', count)

def opponentSendToMana(count = 1):
	mute()
	targetPlayer = getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'sendToMana',[count, False, True])

def opponentSearch(args):
	targetPlayer = getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'search', args)

def oppponentFromMana(count=1):
	targetPlayer = getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'fromMana',[count,"ALL","ALL","ALL",True,True])

def bothPlayersFromMana(count = 1, toGrave=False, filterFunction='True'):
	for player in players:
		remoteCall(player, "fromMana", [count, "ALL","ALL","ALL",True, toGrave, filterFunction])

def opponentManaToHand(count=1):
	manaList = [card for card in table if isMana(card) and card.owner != me]
	if len(manaList)==0:return
	if me.isInverted: reverseCardList(manaList)
	count = min(count,len(manaList))
	choices = askCard2(manaList, "Choose {} Card(s) from the opponent's Mana Zone".format(count), maximumToTake=count, returnAsArray=True)
	if not isinstance(choices, list):return
	for choice in choices:
		remoteCall(choice.owner,"toHand",convertCardListIntoCardIDsList(choice))

#If opponent has more mana that you charge/draw
def manaCompare(count=1, charge=False, draw=False, shield=False):
	manaCards = [c for c in table if isMana(c) and c.owner == me]
	oppMana = [c for c in table if isMana(c) and c.owner != me]
	if len(oppMana)>len(manaCards):
		if charge:
			mana(me.Deck,count)
		if draw:
			draw(me.Deck, False, count)
		if shield:
			shields(me.Deck,count)

#Generic function to Tap Creature(s). targetAll flag means it won't ask and tap every opp creature
def tapCreature(count=1, targetALL=False, includeOwn=False, onlyOwn=False, filterFunction="True"):
	mute()
	if targetALL:
		cardList = []
		if onlyOwn:
			cardList = [card for card in table if isCreature(card) and card.orientation == Rot0 and card.owner == me]
		elif includeOwn == True:
			cardList = [card for card in table if isCreature(card) and card.orientation == Rot0]
		else:
			cardList = [card for card in table if isCreature(card) and card.orientation == Rot0 and card.owner != me]
		cardList = [c for c in cardList if eval(filterFunction, allowed_globals, {'c': c})]
		if len(cardList) == 0:
			return
		for card in cardList:
			remoteCall(card.owner, "processTapUntapCreature", [convertCardListIntoCardIDsList(card), False])
	else:
		cardList=[]
		if onlyOwn:
			cardList = [card for card in table if isCreature(card) and card.orientation == Rot0 and card.owner == me]
		elif includeOwn:
			cardList = [card for card in table if isCreature(card) and card.orientation == Rot0]
		else:
			cardList = [card for card in table if isCreature(card) and card.orientation == Rot0 and card.owner != me]
		cardList = [c for c in cardList if not isBait(c) and not isUntargettable(c) and eval(filterFunction, allowed_globals, {'c': c})]
		if len(cardList) == 0:
			return
		if me.isInverted: reverseCardList(cardList)
		count = min(count, len(cardList))
		choices = askCard2(cardList, 'Choose {} Creature(s) to tap'.format(count), maximumToTake=count,returnAsArray=True)
		if not isinstance(choices, list): return
		for choice in choices:
			remoteCall(choice.owner, "processTapUntapCreature", [convertCardListIntoCardIDsList(choice), False])

def semiReset():
	mute()
	if confirm("Are you sure you want to continue?"):
		currentPlayers = getPlayers()
		for player in currentPlayers:
			cardsInHand = [c for c in player.hand]
			cardsInGrave = [c for c in player.piles['Graveyard']]
			if cardsInHand or cardsInGrave:
				for card in cardsInHand:
					remoteCall(player, 'toDeck', convertCardListIntoCardIDsList(card))
				for card in cardsInGrave:
					remoteCall(player, 'toDeck', card)
			remoteCall(player, 'shuffle', convertGroupIntoGroupNameList(player.deck))
			remoteCall(player, 'draw', [convertGroupIntoGroupNameList(player.deck), False, 5])

def swapManaAndHand(tapped = True):
	manaZoneList = [card for card in table if isMana(card) and card.controller == me]
	handList = [card for card in me.hand]
	for manaCard in manaZoneList:
		toHand(manaCard)
	for handCard in handList:
		toMana(handCard)
		if tapped:
			handCard.orientation = Rot270

def lonely(card):
	if len([c for c in table if isCreature(c) and not isBait(c) and c.controller == me])==1: destroy(card)
	notify("{} got destroyed because it was alone on board!".format(card))

# Special Card Group Automatization

def waveStriker(functionArray, card):
	if callable(functionArray):
		functionArray=[functionArray]
	global wscount
	wscount = getWaveStrikerCount()
	if functionArray and wscount >= 3:
		for index, funct in enumerate(functionArray):
			waitingFunct.insert(index + 1, [card, funct])

def mode(functionArray,card, choiceText=[], deb=False, count=1):
	if callable(functionArray):
		functionArray=[functionArray]
	if len(choiceText)==0:
		for f in range(0,len(functionArray)):
			choiceText.append(str(f+1))
	if deb and len([c for c in table if re.search("Evolution", c.Type) and not isBait(c)]) != 0:
		choice = askYN("Do you want to use both effects of {}?".format(card))
		if choice == 1:
			#add choices to waiting list. Usually 2 but maybe there will be exceptions
			for i in range (0,len(functionArray)):
				waitingFunct.insert(i+1, [card,functionArray[i]])
			return
	for i in range (0, count):
		choice = askChoice("Which effect do you want to activate?",choiceText,[])
		if choice == 0: return
		waitingFunct.insert(1, [card,functionArray[choice-1]])
		notify("{} chose {} effect of {}".format(me,choiceText[choice-1],card))

#Used for Meteorburn's: Whenever this creature attacks, you may put a card under this creature into your graveyard. If you do, "EFFECT".
def meteorburn(functionArray, card, minimum=1, maximum=1):
	if callable(functionArray):
		functionArray=[functionArray]
	baitList = detachBait(card, minimumToTake=minimum, maximumToTake=maximum)
	if functionArray and len(baitList)>0:
		for index, funct in enumerate(functionArray):
			waitingFunct.insert(index + 1, [card, lambda card = card, baitList=baitList: funct(card, baitList)])

#Special Card Automatization

def apocalypseVise():
	powerLeft=8000
	creaturesToDestroy=[]
	creatureList = [card for card in table if isCreature(card) and card.owner!=me and not isBait(card) and not isUntargettable(card) and int(card.Power.strip('+'))<=powerLeft]
	if me.isInverted: reverseCardList(creatureList)
	while powerLeft>0 and len(creatureList)>0:
		creatureChoice = askCard2(creatureList, 'Choose a Creature to destroy.')
		if type(creatureChoice) is not Card: break
		powerLeft = powerLeft-int(creatureChoice.Power.strip('+'))
		creatureChoice.target()
		creaturesToDestroy.append(creatureChoice)
		creatureList.remove(creatureChoice)
		notify("Apocalypse Vise - Power Spent: {}".format(8000-powerLeft))
		creatureList = [card for card in creatureList if int(card.Power.strip('+'))<=powerLeft]
	if len(creaturesToDestroy)>0:
		destroyAll(creaturesToDestroy, False)

def bronks():
	creatureList = [c for c in table if isCreature(c) and not isBait(c)]
	minPower = min(int(c.Power.strip('+')) for c in creatureList)
	notify("Lowest Power found: {}".format(minPower))
	leastPowerCreatureList = [c for c in creatureList if int(c.Power.strip('+')) == minPower]
	if len(leastPowerCreatureList == 1):
		remoteCall(leastPowerCreatureList[0].owner,'destroy', convertCardListIntoCardIDsList(leastPowerCreatureList[0]))
		return

	opponentCreatures = [card for card in creatureList if card.owner != me and not isUntargettable(card)]
	myCreatures = [card for card in creatureList if card.owner == me]
	leastPowerCreatureList = sorted(leastPowerCreatureList, key=lambda x: (
	   	int(me.isInverted) if x in opponentCreatures else int(not me.isInverted),
		(opponentCreatures + myCreatures).index(x)))

	if me.isInverted:
		reverseCardList(leastPowerCreatureList)
	else:
		leastPowerCreatureList = sorted(leastPowerCreatureList, key=lambda x: (
	   	 	0 if x in opponentCreatures else 1,
			(opponentCreatures + myCreatures).index(x)))
	choice = askCard2(leastPowerCreatureList, "Select a card to destroy (Opponent's are shown first).")
	if type(choice) is not Card: return
	remoteCall(choice.owner,'destroy', convertCardListIntoCardIDsList(choice))

def cyclonePanic():
	if confirm("Are you sure you want to continue?"):
		currentPlayers = getPlayers()
		for player in getPlayers():
			cardInHand = [c for c in player.hand]
			for c in cardInHand:
				remoteCall(player, 'toDeck', convertCardListIntoCardIDsList(c))
			remoteCall(player, 'shuffle', convertGroupIntoGroupNameList(player.deck))
			remoteCall(player, 'draw', [convertGroupIntoGroupNameList(player.deck), False, len(cardInHand)])

def raptorFish():
	choice=askYN("Raptor Fish wants to redraw your hand. Proceed?")
	if choice:
		cardInHand = [c for c in me.hand]
		for c in cardInHand:
			toDeck(c)
		shuffle(me.Deck)
		draw(me.Deck,False,len(cardInHand))

def darkpact(card):
	manaList=[c for c in table if isMana(c) and c.owner == me]
	if me.isInverted: reverseCardList(manaList)
	targetsMana = askCard2(manaList, "Select cards from Mana", maximumToTake=len(manaList),returnAsArray=True)
	if not isinstance(targetsMana,list): return
	destroyAll(targetsMana)
	draw(me.Deck, count=len(targetsMana))

def deklowazDiscard():
	mute()
	targetPlayer = getTargetPlayer(onlyOpponent=True)
	cardList = [card for card in targetPlayer.hand]
	reverseCardList(cardList)
	cardChoice = askCard2(cardList, "Look at opponent's hand. (close pop-up or select any card to finish.)")
	for card in cardList:
		if re.search("Creature", card.Type) and int(card.Power.strip('+')) <= 3000:
			remoteCall(targetPlayer, 'toDiscard', convertCardListIntoCardIDsList(card))

def dolmarks():
	sacrifice()
	fromMana(1,"ALL","ALL","ALL",True,True)
	targetPlayer = getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'sacrifice',[])
	remoteCall(targetPlayer,'fromMana',[1,"ALL","ALL","ALL",True,True])

def shieldswap(card, count = 1):
	if len([c for c in table if isShield(c) and c.owner == me]) == 0 or len([me.hand])==0: return
	choice = askYN("Use {}'s effect?".format(card.Name))
	if choice != 1: return
	handList = [c for c in me.hand]
	count=min(count, len(handList))
	reverseCardList(handList)
	choices = askCard2(handList,"Select {} Card(s) to put as Shield", maximumToTake=count, returnAsArray=True)
	if not isinstance(choices, list): return
	for choice in choices:
		toShields(choice)
	waitingFunct.insert(1, [card, lambda card=card, counter=len(choices): bounceShield(counter)])

def funkyWizard():
	for player in players:
		remoteCall(player, "draw", [convertGroupIntoGroupNameList(player.Deck), True])

def ghastlyDrain(card):
	number=askNumber("How many shields to return?", 1)
	notify("{} chose {} shields".format(me,number))
	waitingFunct.insert(1, [card, lambda card=card, counter=number: bounceShield(counter)])

def returnAndDiscard(card):
	choice = askYN("Return {} to hand?".format(card.name))
	if choice != 1: return
	toHand(card)
	selfDiscard()

#Sadly we cannot just call targetDiscard with 'mana'argument and opponentManaToHand, because the mana wouldn't be updated in time to display new card added.
def gigandura(card):
	targetPlayer = getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	cardList = [card for card in targetPlayer.hand]
	#Both players see their opponent's hand reversed
	reverseCardList(cardList)
	choice = askCard2(cardList, "Pick a Card to place to Mana from opponent's hand.")
	if type(choice) is not Card: return
	remoteCall(targetPlayer, 'toMana', convertCardListIntoCardIDsList(choice))
	manaList = [card for card in table if isMana(card) and card.owner == targetPlayer]
	manaList.append(choice)
	if me.isInverted: reverseCardList(manaList)
	update()
	manaChoice = askCard2(manaList, "Choose a Card from the opponent's Mana Zone")
	if type(manaChoice) is not Card: return
	remoteCall(targetPlayer,"toHand",convertCardListIntoCardIDsList(manaChoice))

def hydroHurricane(card):
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	lightCards=[c for c in table if isCreature(c) and not isBait(c) and c.owner==me and re.search("Light", c.Civilization)]
	darknessCards=[c for c in table if isCreature(c) and not isBait(c) and c.owner==me and re.search("Darkness", c.Civilization)]
	oppMana=[c for c in table if c.owner == targetPlayer and isMana(c)]
	oppCreatures=[c for c in table if c.owner == targetPlayer and isCreature(c) and not isBait(c) and not isUntargettable(c)]
	if len(oppMana)>0 and len(lightCards)>0:
		if me.isInverted: reverseCardList(oppMana)
		count = min(len(oppMana), len(lightCards))
		choices = askCard2(oppMana,"Select up to {} Cards from Mana".format(count), maximumToTake=count, returnAsArray=True)
		if not isinstance(choices,list):choices=[]
		for choice in choices:
			remoteCall(targetPlayer, "toHand", convertCardListIntoCardIDsList(choice))
	if len(oppCreatures)>0 and len(darknessCards)>0:
		if me.isInverted: reverseCardList(oppCreatures)
		count = min(len(oppCreatures), len(darknessCards))
		choices = askCard2(oppCreatures, "Select up to {} Creatures from Battle Zone".format(count),maximumToTake=count,returnAsArray=True)
		if not isinstance(choices,list):choices=[]
		for choice in choices:
			remoteCall(targetPlayer, "toHand", convertCardListIntoCardIDsList(choice))

def kingAquakamui(card):
	choice = askYN("Return all Angel Commands and Demon Commands from Graveyard to Hand?")
	if choice != 1: return
	cardsInGrave=[c for c in me.piles['Graveyard'] if re.search("Angel Command", c.Race) or re.search("Demon Command", c.Race)]
	for c in cardsInGrave:
		toHand(c)

def klujadras():
	for player in players:
		count = getWaveStrikerCount(player)
		if count:
			remoteCall(player, "draw", [convertGroupIntoGroupNameList(player.Deck), False, count])

def dracobarrier():
	cardList = [card for card in table if isCreature(card) and card.orientation == Rot0 and card.owner != me]
	if len(cardList) == 0:
			return
	choice = askCard2(cardList, 'Choose a Creature to tap')
	if type(choice) is not Card: return
	remoteCall(choice.owner, "processTapUntapCreature", [convertCardListIntoCardIDsList(choice), False])
	if re.search(r'Dragon\b', choice.Race, re.I):
		shields(me.deck)

def waveLance():
	cardList=[c for c in table if
				isCreature(c)
				and not isBait(c)
				and not isUntargettable(c)]
	if len(cardList) == 0:
		whisper("No valid targets on the table.")
		return
	target = [c for c in table if c.targetedBy == me and c in cardList]
	if len(target) != 1:
		whisper("Wrong number of targets!")	
		return True
	else:
		remoteCall(target[0].owner, "toHand", convertCardListIntoCardIDsList(target))
		if re.search(r'Dragon\b', target[0].Race, re.I):
			draw(group=me.Deck, ask=True)


def mechadragonsBreath():
	power = askNumber()

	if(power>6000 or power<0):
		notify("{} chose incorrect Power ({}).".format(me, power))
		return
	notify("{} chose {} Power.".format(me, power))
	destroyAll(table,True,power,"ALL",False,True)

def miraculousMeltdown(card):
	mute()
	targetPlayer = 	getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	myShields = [c for c in table if c.owner == me and isShield(c)]
	opponentShields = [c for c in table if c.owner == targetPlayer and isShield(c)]
	if len(opponentShields)<=len(myShields):
		whisper("You cannot cast this spell!")
		return
	remoteCall(targetPlayer,'_eMMHelper', [card._id, len(myShields)])

def declareRace(card, excludedRace=None):
	all_zones = itertools.chain(me.deck, [c for c in table if c.owner == me], me.hand, me.graveyard, me.Hyperspatial, me.Gacharange)
	all_races = itertools.chain.from_iterable(re.split(r'/+', card.race) for card in all_zones if card.race!='')

	race_counts = {}
	for race in all_races:
		if race in race_counts:
			race_counts[race] += 1
		else:
			race_counts[race] = 1

	# Sort races by count in descending order
	sorted_races = sorted(race_counts.items(), key=lambda x: x[1], reverse=True)
	race_names = [race for race, count in sorted_races if race !=excludedRace]
	choice = askChoice("Select a race:", race_names, customButtons=["Custom Race"])
	if choice == 0:
		notify("{} didn't declare a race".format(me))
		return
	if choice > 0:
		chosenRace = race_names[choice-1]
	if choice < 0:
		chosenRace = askString("Type a custom race to declare:",'')
	notify('{} declares {} Race'.format(me, chosenRace))
	card.properties["Rules"] = '(Declared: {})\n{}'.format(chosenRace,card.properties["Rules"])

def divineRiptide():
	opponent=getTargetPlayer(onlyOpponent=True)
	fromManaAll()
	remoteCall(opponent,"fromManaAll",'True')

def shockHurricane(card):
	myCreatures=[c for c in table if isCreature(c) and not isBait(c) and c.owner==me]
	chosenCreatures=[]
	enemyCreatures=[c for c in table if isCreature(c) and not isBait(c) and c.owner!=me and not isUntargettable(c)]
	enemyChosen=[]
	if me.isInverted: reverseCardList(myCreatures)
	while(len(myCreatures)>0):
		choice = askCard2(myCreatures, 'Choose a Creature to return to Hand')
		if type(choice) is not Card: break
		chosenCreatures.append(choice)
		myCreatures.remove(choice)
	bounceAll(chosenCreatures)
	count = min(len(chosenCreatures), len(enemyCreatures))
	for i in range(0, count):
		choice = askCard2(enemyCreatures, 'Choose an opponent\'s Creature to return to Hand')
		enemyChosen.append(choice)
		enemyCreatures.remove(choice)
	bounceAll(enemyChosen)

def crisisBoulder(card):
	targetPlayer = getTargetPlayer(onlyOpponent = True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'_eCrisisBoulderHelper',[card._id])

def _eCrisisBoulderHelper(cardId):
	waitingFunct.insert(0, [Card(cardId),lambda card: _enemyCrisisBoulder()])
	evaluateWaitingFunctions()

def _enemyCrisisBoulder():
	choiceList = ['Creature', 'Mana']
	colorsList = ['#FF0000', '#11FF11']
	choice = askChoice("Put Creature or Mana to Graveyard?",choiceList,colorsList)
	if choice == 1:
		cardsToChooseFrom = [c for c in table if isCreature(c) and not isBait(c) and c.owner == me]
		if me.isInverted: reverseCardList(cardsToChooseFrom)
		selected = askCard2(cardsToChooseFrom, "Select a Creature to put to Graveyard")
	elif choice == 2:
		cardsToChooseFrom = [c for c in table if isMana(c) and c.owner == me]
		if me.isInverted: reverseCardList(cardsToChooseFrom)
		selected = askCard2(cardsToChooseFrom, "Select Mana to put to Graveyard")
	else: return
	toDiscard(selected)

def grinningHunger(card):
	targetPlayer = getTargetPlayer(onlyOpponent = True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'_eGHHelper',[card._id])

def _eGHHelper(cardId):
	waitingFunct.insert(0, [Card(cardId),lambda card: _enemyGrinningHunger(card)])
	evaluateWaitingFunctions()

def _enemyGrinningHunger(card):
	choiceList = ['Creature', 'Shield']
	colorsList = ['#FF1111', '#FFFF11']
	choice = askChoice("Put Creature or Shield to Graveyard?", choiceList, colorsList)
	if choice == 1:
		notify("{} is destroying a Creature.".format(me))
		waitingFunct.insert(1, [card, lambda card: sacrifice()])
	elif choice == 2:
		notify("{} is destroying a Shield.".format(me))
		waitingFunct.insert(1, [card,lambda card: burnShieldKill(1, True)])
	else:
		notify("{} didn't make a choice.".format(me))
		return

#We use this function to queue the real function, to allow targetting of shields to work
def _eMMHelper(cardId,count):
	waitingFunct.insert(0, [Card(cardId),lambda card, count=count: _enemyMiraculousMeltdown(count)])
	evaluateWaitingFunctions()

def _enemyMiraculousMeltdown(count):
	whisper("Choose {} Shields for the effect of Miraculous Meltdown".format(count))
	targets = [c for c in table if c.targetedBy == me and isShield(c) and c.owner == me]
	if len(targets) != count:
		return True
	notSelectedShields = [c for c in table if c.owner == me and isShield(c) and c not in targets]
	peekShields(notSelectedShields)

def miraculousPlague():
	mute()
	creatureList = [card for card in table if isCreature(card) and not isBait(card) and card.owner != me and not isUntargettable(card)]
	if len(creatureList) != 0:
		if len(creatureList) == 1:
			remoteCall(creatureList[0].owner, "toHand", convertCardListIntoCardIDsList(creatureList[0]))
		else:
			if me.isInverted: reverseCardList(creatureList)
			creatureChoices = askCard2(creatureList, 'Choose 2 Creatures for your opponent.',minimumToTake=2, maximumToTake=2)
			if not isinstance(creatureChoices,list): return
			for cchoice in creatureChoices:
				cchoice.target()
			#sort the choices to reflect the table state.
			creatureChoices = sorted(creatureChoices, key= lambda x: [card for card in table if isCreature(card) and card.owner != me].index(x))

			remoteCall(creatureChoices[0].owner,"_miraculousPlagueChooseToHand", [convertCardListIntoCardIDsList(creatureChoices)])

	manaList = [card for card in table if isMana(card) and card.owner != me]
	if len(manaList) != 0:
		if len(manaList) == 1:
			remoteCall(manaList[0].owner, "toHand", convertCardListIntoCardIDsList(manaList[0]))
		else:
			if me.isInverted: reverseCardList(manaList)
			manaChoices = askCard2(manaList, 'Choose 2 Mana Cards for your opponent',minimumToTake=2, maximumToTake=2)
			if not isinstance(manaChoices,list): return
			for mchoice in manaChoices:
				mchoice.target()
			#sort the choices to reflect the table state.
			sorted(manaChoices, key=lambda x: [card for card in table if isMana(card) and card.owner != me].index(x))

			remoteCall(manaChoices[0].owner,"_miraculousPlagueChooseToHand", [convertCardListIntoCardIDsList(manaChoices)])

def _miraculousPlagueChooseToHand(cardList):
	cardList = ensureCardObjects(cardList)
	if me.isInverted: reverseCardList(cardList)
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
				and card.owner != me
				and not isUntargettable(card)
				and int(card.Power.strip('+')) <= 5000]
	if len(cardList) == 0:
		whisper("No valid targets on the table.")
		return
	targetCard = [c for c in table if c.targetedBy == me and c in cardList]
	if len(targetCard) != 1:
		whisper("Wrong number of targets!")
		return True
	remoteCall(targetCard[0].owner, "destroy", convertCardListIntoCardIDsList(targetCard[0]))
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
		if cardCostComparator(choice,targetCost,'==', 'Creature'):
			validChoice = choice
			break
	group.shuffle()
	notify("{} finishes searching their {}.".format(me, group.name))
	toPlay(validChoice)

def rothus():
	sacrifice()
	opponentSacrifice()

def dracodanceTotem(card):
	if len([c for c in table if isMana(c) and re.search(r'Dragon\b', choice.Race, re.I)])>0:
		fromMana(1,"ALL","ALL","Dragon")
		toMana(card)

def soulSwap():
	mute()
	# targetPlayer = getTargetPlayer()
	# if not targetPlayer: return
	#list of creatures in battlezone
	targets = [c for c in table if c.targetedBy == me and isCreature(c) and not isUntargettable(c)]
	if len(targets) != 1:
		return True
	cardsToMana = getEvoBaits(targets[0])
	cardsToMana.insert(0,targets[0])
	remoteCall(targets[0].owner, "toMana", convertCardListIntoCardIDsList(targets[0]))
	update()
	remoteCall(me,'_fromManaToField',[targets[0].owner._id, cardsToMana])

def tanzanyte():
	cardList = [card for card in me.piles['Graveyard'] if re.search('Creature', card.Type)]
	choice = askCard2(sort_cardList(cardList), 'Select a Creature to return all copies of from Graveyard.')
	if type(choice) is not Card: return
	for card in cardList:
		if card.Name == choice.Name:
			toHand(card, True)

def upheaval():
	for player in players:
		remoteCall(player, 'swapManaAndHand', [])

def intenseEvil():
	myCreatures=[c for c in table if isCreature(c) and not isBait(c) and c.owner==me]
	if me.isInverted: reverseCardList(myCreatures)
	chosenCreatures = askCard2(myCreatures, 'Choose Creatures to destroy', maximumToTake=len(myCreatures),returnAsArray=True)
	if not isinstance(chosenCreatures,list):return

	destroyAll(chosenCreatures)
	draw(me.Deck,False,len(chosenCreatures))
#The additional targets list is used to handle evo creatures moving their baits with them to mana too late to catch this in this function.
def _fromManaToField(targetPlayerId, additionalTargetsList=[]):
	mute()
	targetPlayer = getPlayerById(targetPlayerId)
	#Count the number of cards in mana zone for the one that will be added.
	fullManaList = [card for card in table if isMana(card) and card.controller == targetPlayer]
	for additionalTarget in additionalTargetsList:
		if additionalTarget not in fullManaList:
			fullManaList.append(additionalTarget)
	count = len(fullManaList)
	#get valid targets from mana
	manaList = [card for card in fullManaList if re.search("Creature", card.Type) and not re.search("Evolution Creature", card.Type) and cardCostComparator(card,count,'<=',"Creature")]
	if me.isInverted: reverseCardList(manaList)
	manaChoice = askCard2(manaList, 'Choose a Creature to play from Mana')

	if type(manaChoice) is not Card:
		return
	remoteCall(targetPlayer, "toPlay", convertCardListIntoCardIDsList(manaChoice))

def fromGraveyardToMana(count=1,filterFunction="True", ask=False):
	mute()
	group=me.piles['Graveyard']
	if len(group) == 0: return
	if ask:
		choice = askYN("Would you like to put {} Card(s) from Graveyard to Mana?".format(count))
		if choice != 1: return
	count = min(count,len(group))
	cardsInGroup = sort_cardList([c for c in group if eval(filterFunction, allowed_globals, {'c': c})])
	choices = askCard2(cardsInGroup, 'Search {} Card(s) to put to Mana'.format(count),minimumToTake=1,maximumToTake=count, returnAsArray=True)
	if not isinstance(choices,list):
			notify("{} finishes searching their {}.".format(me, group.name))
			return
	for c in choices:
		toMana(c)

def fromGraveyard(count=1,filterFunction="True", ask=False, moveToMana=True, moveToHand=False):
    mute()
    group=me.piles['Graveyard']
    if len(group) == 0: return
    if ask:
        choice = askYN("Would you like to move {} Card(s) from Graveyard?".format(count))
        if choice != 1: return
    count = min(count,len(group))
    cardsInGroup = sort_cardList([c for c in group if eval(filterFunction)])
    for i in range(count):
        choice = askCard2(cardsInGroup, 'Pick a Card to put to Mana (1 at a time)')
        if type(choice) is not Card:
            notify("{} finishes searching their {}.".format(me, group.name))
            return
        cardsInGroup.remove(choice)
        if moveToMana: toMana(choice)
        elif moveToHand: toHand(choice)

def fromGraveyardAll(filterFunction="True",moveToMana=True, moveToHand=False, ask=False):
    group=me.piles['Graveyard']
    if len(group) == 0: return
    if ask:
        choice = askYN("Would you like to move Cards from Graveyard?")
        if choice != 1: return
    cardsInGroup = sort_cardList([c for c in group if eval(filterFunction)])
    if len(cardsInGroup) == 0: notify("No cards to move!") 
    for c in cardsInGroup:
        if moveToMana: toMana(c)
        elif moveToHand: toHand(c)

def fromDeckToField(filterFunction="True", count = 1):
	mute()
	group = me.deck
	if len(group) == 0: return
	cardsInGroup = sort_cardList([card for card in group])
	validChoices = [c for c in cardsInGroup if eval(filterFunction)]	
	for i in range(count):
		while (True):
			c = askCard2(cardsInGroup, 'Search a Card to put to the Battle Zone (1 at a time)')
			if type(c) is not Card:
				shuffle(group)
				notify("{} finishes searching their {}.".format(me, group.name))
				return
			if c in validChoices:
				cardsInGroup.remove(c)
				toPlay(c)
				break
	shuffle(group)


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
		card.resetProperties()
		card.target(False)
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
		clearArrowOnMove(args)
		card.resetProperties()
		evolveDict = eval(me.getGlobalVariable("evolution"), allowed_globals)
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
		if evolveDict != eval(me.getGlobalVariable("evolution"), allowed_globals):
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
	evolveDict = eval(me.getGlobalVariable("evolution"), allowed_globals)

	for card in table:
		if card.controller == me and not isCastle(card) and not card.anchor and not card._id in list(
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
	global arrow
	arrow = {}
	for card in group:
		card.target(False)

def clearFunctionsAndTargets(group, x=0, y=0):
	mute()
	clear(group)
	clearWaitingFuncts()

#Set Up Battlezone
def setup(group, x=0, y=0):
	mute()
	global arrow
	arrow = {}
	cardsInTable = [c for c in table if c.controller == me and c.owner == me and not isPsychic(c)]
	cardsInHand = [c for c in me.hand if not isPsychic(c)]
	cardsInGrave = [c for c in me.piles['Graveyard'] if not isPsychic(c)]

	psychicsInTable = [c for c in table if c.controller == me and c.owner == me and isPsychic(c)]
	psychicsInHand = [c for c in me.hand if isPsychic(c)]
	psychicsInGrave = [c for c in me.piles['Graveyard'] if isPsychic(c)]

	gacharangeInTable = [c for c in table if c.controller == me and c.owner == me and isGacharange(c)]

	if cardsInTable or cardsInHand or cardsInGrave or psychicsInTable or psychicsInGrave or psychicsInHand:
		if confirm("Are you sure you want to setup battlezone? Current setup will be lost"):
			clearFunctionsAndTargets(table)
			for card in cardsInTable:
				card.resetProperties()
				card.moveTo(me.Deck)
			for card in cardsInHand:
				card.resetProperties()
				card.moveTo(me.Deck)
			for card in cardsInGrave:
				card.resetProperties()
				card.moveTo(me.Deck)

			for card in psychicsInTable:
				card.resetProperties()
				card.moveTo(me.Hyperspatial)
			for card in psychicsInHand:
				card.resetProperties()
				card.moveTo(me.Hyperspatial)
			for card in psychicsInGrave:
				card.resetProperties()
				card.resetProperties()
				card.moveTo(me.Hyperspatial)
			for card in gacharangeInTable:
				card.resetProperties()
				card.moveTo(me.Gacharange)
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
		if isGacharange(card):
			whisper("You cannot have Gacharange creatures in your main deck")
			return

	me.setGlobalVariable("shieldCount", "0")
	me.setGlobalVariable("evolution", "{}")
	me.Gacharange.shuffle()
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

def initiateRPS(group, x=0, y=0):
	mute()
	opponent = getTargetPlayer(onlyOpponent=True)
	choice = askChoice('Pick Rock/Paper/Scissors:',['Rock','Paper','Scissors'])
	if choice==0: return
	remoteCall(opponent,'finishRPS',[me,choice])

def finishRPS(opponent,oppChoice):
	mute()
	choice = askChoice('Pick Rock/Paper/Scissors:',['Rock','Paper','Scissors'])
	if choice == 0: notify("{} didn't make a choice!".format(me))
	choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
	rules = {
		1: 3,  # Rock beats Scissors
		2: 1,  # Paper beats Rock
		3: 2   # Scissors beats Paper
	}
	if(choice == oppChoice):
		notify("It's a draw! - Both picked {}".format(choices[choice]))
	elif rules[choice] == oppChoice:
		notify("{} Wins! - {} beats {}".format(me, choices[choice], choices[oppChoice]))
	else:
		notify("{} Wins! - {} beats {}".format(opponent, choices[oppChoice], choices[choice]))

#untaps everything, creatures and mana
def untapAll(group=table, x=0, y=0, isNewTurn=False):
	mute()
	group = ensureGroupObject(group)
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
		# Untap Mana
		if card.orientation == Rot270:
			card.orientation = Rot180

	orderEvaluatingFunctions()
	evaluateWaitingFunctions()
	if isNewTurn:
		processOnTurnStartEffects()
	notify("{} untaps all their cards.".format(me))

#Default call for Destroy (del key), handles mass creature destruction effects
def destroyMultiple(cards, x=0, y=0):
	if len(cards) == 1:
		destroy(cards[0])
	else:
		creatureList = []
		for card in cards:
			if isCreature(card):
				creatureList.append(card)
			else:
				destroy(card)
		if creatureList:
			destroyAll(creatureList, dontAsk=True)

def tapMultiple(cards, x=0, y=0, clearFunctions = True): #batchExecuted for multiple cards tapped at once(manually)
	global lastExecutionTime, DEBOUNCE_DELAY, lastTappedCards
	currentTime = time.time()
	if currentTime - lastExecutionTime < DEBOUNCE_DELAY and any(c in lastTappedCards for c in cards):
		whisper('You are tapping and untapping the same cards too quickly! Slow down!')
		return
	lastExecutionTime = currentTime
	lastTappedCards = cards

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
	card = ensureCardObjects(card)
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
			#notify("On trig list is".format(trigFunctions[0]))
			for function in trigFunctions:
				conditionalTrigger = conditionalTrigger and trigFunctions[0]()
		if conditionalTrigger and re.search("{SHIELD TRIGGER}", card.Rules):
			choice = askYN("Activate Shield Trigger for {}?\n\n{}".format(card.Name, card.Rules), ["Yes", "No", "Wait"])
			if choice==1:

				notify("{} uses {}'s Shield Trigger.".format(me, card.Name))
				card.isFaceUp = True
				card.target(False)
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
					if me.isInverted: reverseCardList(cardsInHandWithStrikeBackAbilityThatCanBeUsed)
					choice = askCard2(cardsInHandWithStrikeBackAbilityThatCanBeUsed, 'Choose Strike Back to activate')
					if type(choice) is Card:
						shieldCard.isFaceUp = True

						toPlay(choice, notifymute=True)
						toDiscard(shieldCard)
						notify("{} destroys {} to use {}'s Strike Back.".format(me, shieldCard.name, choice.name))
						return
		notify("{}'s shield #{} is broken.".format(me, shieldCard.markers[shieldMarker]))
		shieldCard.target(False)
		shieldCard.moveTo(shieldCard.owner.hand)
	elif isMana(card) or ignoreEffects:
		toDiscard(card)
	else:
		cardToBeSaved = card
		possibleSavers = [c for c in table if
						  cardToBeSaved != c and isCreature(c) and c.owner == me and not isBait(c) and re.search("Saver",c.rules)
						  and (re.search(cardToBeSaved.properties['Race'], c.rules) or re.search("Saver: All Races", c.rules))]
		if len(possibleSavers) > 0:
			if confirm("Prevent {}'s destruction by using a Saver on your side of the field?\n\n".format(
					cardToBeSaved.Name)):
				if me.isInverted: reverseCardList(possibleSavers)
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
		for index, function in enumerate(functionList):
			waitingFunct.insert(index + 1, [card, function])
		evaluateWaitingFunctions()

#untaps creature
def untapCreature(card, ask = True):
	if card.orientation == Rot90:
		if ask:
			card.target()
			choice = askYN("Would you like to Untap {}?".format(card.name))
			card.target(False)
			if choice != 1: return
		tapMultiple([card], clearFunctions=False)

def untapCreatureAll(ask = True):
	cardList = [c for c in table if isCreature(c) and c.controller == me and c.orientation == Rot90]
	if ask:
		choice = askYN("Would you like to Untap All Your Creatures?")
		if choice != 1: return
	tapMultiple(cardList, clearFunctions=False)

#Deck Menu Options
def shuffle(group, x=0, y=0):
	mute()
	group = ensureGroupObject(group)
	if len(group) == 0: return
	for card in group:
		if card.isFaceUp:
			card.isFaceUp = False
	group.shuffle()
	notify("{} shuffled their {}".format(me, group.name))

def draw(group, conditional=False, count=1, x=0, y=0, ask=False):
	mute()
	group = ensureGroupObject(group)
	if ask:
		choice = askYN("Would you like to Draw {} Card(s)?".format(count))
		if choice != 1: return
	for i in range(0, count):
		if len(group) == 0:
			return
		if conditional == True:
			choiceList = ['Yes', 'No']
			colorsList = ['#FF0000', '#FF0000']
			choice = askChoice("Draw a card?", choiceList, colorsList)
			if choice != 1:return
		card = group[0]
		card.moveTo(card.owner.hand)
		notify("{} draws a card.".format(me))

def drawX(group, x=0, y=0):
	group = (ensureGroupObject(group))
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
		if choice != 1:return
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
	group = ensureGroupObject(group)
	if len(group) == 0: return
	card = group.random()
	toDiscard(card, notifymute=True)
	notify("{} randomly discards {}.".format(me, card))

def fromTopPickX(group, x=0, y=0):
	if len(group) == 0: return
	count = askInteger("Look at how many cards?", 5)
	if count == None: return
	lookAtTopCards(num=count, count=count)

#Function used for "Detach Bait" option in right click menu for Evos. Returns newly removed card(s)
def detachBait(card, x=0, y=0, minimumToTake=None, maximumToTake=None):
	mute()
	cardList = getEvoBaits(card)
	if minimumToTake is None:
		minimumToTake = 1
	if maximumToTake is None:
		maximumToTake = len(cardList)
	if len(cardList) < minimumToTake:
		whisper('No cards to detach.')
		return []
	choices = askCard2(cardList, "Choose Card(s) to detach from Evo",minimumToTake=minimumToTake,maximumToTake=maximumToTake, returnAsArray=True)
	if not isinstance(choices,list): return []
	newBaitList = [c for c in cardList if c not in choices]
	notify('{} detaches {} from {}'.format(me, ", ".join([c.name for c in choices]), card))
	for choice in choices:
		toDiscard(choice, notifymute=True)
	processEvolution(card, newBaitList)
	align()
	return choices

#Function used for "Attach Bait" option in right click menu for Evos. Returns newly added card(s)
def attachBait(card, x=0, y=0):
	mute()
	cardList = [c for c in table if not isMana(c) and not isShield(c) and c.owner==me and not isBait(c) and c != card]
	if len(cardList) == 0:
		whisper('No cards on the field to attach.')
		return []
	if me.isInverted:
		reverseCardList(cardList)
	choices = askCard2(cardList, "Choose Card(s) to attach to Evo",maximumToTake=len(cardList), returnAsArray=True)
	if not isinstance(choices,list): return []
	notify('{} attaches {} to {}'.format(me, ", ".join([c.name for c in choices]), card))
	newBaitList = choices
	newBaitList.extend(getEvoBaits(card))
	processEvolution(card, newBaitList)
	align()
	return choices

#Charge Top Card as Mana
def mana(group, count=1, ask=False, tapped=False, postAction="NONE", postArgs=[], postCondition='True', preCondition=True):
	mute()
	if not preCondition:
		return
	if ask:
		choice = askYN("Charge top {} Card(s) as Mana?".format(count))
		if choice != 1: return
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
	# implement BounceIfCiv for Dondon Vacuuming Now? Maybe make a whole different function for ifCiv or ifRace just to evaluate the conditon based on args
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
	if eval(postCondition, allowed_globals, {'card': card}):  # eg. Faerie Miracle
		eval(postAction, allowed_globals, {'card': card})  # simple eval of a function, if postCondition is satisfied(is true by default)

#Charge top X cards as mana (not yet used)
def massMana(group, conditional=False, x=0, y=0):
	mute()
	cardList = [card for card in table if isMana(card) and card.owner == me]
	count = len(cardList)
	if conditional == True:
		choiceList = ['Yes', 'No']
		colorsList = ['#FF0000', '#FF0000']
		choice = askChoice("Charge top {} cards to mana?".format(count), choiceList, colorsList)
		if choice != 1: return
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
	card = ensureCardObjects(card)
	if isMana(card) and (x or y):
		global civ_order
		for player in players:
			totalMana = [c for c in table if isMana(c) and c.owner == player]
			totalUntappedMana = [c for c in totalMana if c.orientation == Rot180]
			unique_civilizations = sorted({civ for card in totalMana if card.orientation == Rot180 for civ in card.Civilization.split('/')}, key=civ_order.index)
			notify("{} has {} Mana in total. ({} Untapped)\nAvailable: {}".format(player, len(totalMana), len(totalUntappedMana), ", ".join(unique_civilizations)))
		return
	if isPsychic(card):
		toHyperspatial(card)
		return
	card.resetProperties()
	card.target(False)
	cardWasCreature = isCreature(card) and checkEvo
	##notify("Removing from tracked evos if its bait or an evolved creature")
	if checkEvo:
		baitList = removeIfEvo(card)
		for baitCard in baitList:
			toMana(baitCard, checkEvo=False, alignCheck=False)
	if isShield(card):
		card.resetProperties()
		card.moveTo(me.hand)  # in case it is charged from shields
	card.moveToTable(0, 0)
	card.orientation = Rot180

	if re.search("/", card.Civilization):  # multi civ card
		card.orientation = Rot270
	if alignCheck:
		align()
	if notifymute == False:
		notify("{} charges {} as mana.".format(me, card))

	#Handle on Remove From Battle Zone effects:
	if cardWasCreature:
		functionList=[]
		if cardScripts.get(card.Name,{}).get('onLeaveBZ',[]):
			functionList = cardScripts.get(card.Name).get('onLeaveBZ')
			for index, function in enumerate(functionList):
				waitingFunct.insert(index + 1, [card, function])
			evaluateWaitingFunctions()

#Set as shield menu option / Ctrl+H (both from hand and battlezone)
def toShields(card, x=0, y=0, notifymute=False, alignCheck=True, checkEvo=True):
	mute()
	card = ensureCardObjects(card)
	if isShield(card):
		whisper("This is already a shield.")
		return
	if isPsychic(card):
		toHyperspatial(card)
		return
	cardWasCreature = isCreature(card) and checkEvo
	count = int(me.getGlobalVariable("shieldCount")) + 1
	me.setGlobalVariable("shieldCount", convertToString(count))
	if notifymute == False:
		if isCreature(card) or isMana(
				card):  ##If a visible card in play is turning into a shield, we want to record its name in the notify
			notify("{} sets {} as shield #{}.".format(me, card, count))
		else:
			notify("{} sets a card in {} as shield #{}.".format(me, card.group.name, count))
	card.resetProperties()
	card.target(False)
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

	#Handle on Remove From Battle Zone effects:
	if cardWasCreature:
		functionList=[]
		if cardScripts.get(card.Name,{}).get('onLeaveBZ',[]):
			functionList = cardScripts.get(card.Name).get('onLeaveBZ')
			for index, function in enumerate(functionList):
				waitingFunct.insert(1, [card,function])
			evaluateWaitingFunctions()

#Play Card menu option (both from hand and battlezone)
def toPlay(card, x=0, y=0, notifymute=False, evolveText='', ignoreEffects=False, isEvoMaterial = False):
	mute()
	card = ensureCardObjects(card)
	#global alreadyEvaluating #is true when already evaluating some functions of the last card played, or when continuing after wait for Target
	#notify("DEBUG: AlreadyEvaluating is "+str(alreadyEvaluating))
	if card.group == card.owner.hand:
		clearWaitingFuncts() # this ensures that waiting for targers is cancelled when a new card is played from hand(not when through a function).

	if not re.search("Star Max Evolution", card.Type,re.IGNORECASE) and (re.search("Evolution", card.Type) or re.search('{NEO EVOLUTION}', card.Rules))and not isEvoMaterial:
		targets= []
		textBox = 'Select Creature(s) to put under Evolution{}'
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
			maximumToTake = 1
			if(isMultiMaterial):
				maximumToTake = len(materialList)
			targets = askCard2(materialList,textBox.format(' from Graveyard'),maximumToTake=maximumToTake, returnAsArray=True)
			if not isinstance(targets,list): return
			for target in targets:
				toPlay(target,0, 0,True,' for Graveyard Evolution of {}'.format(card),True, True)
		#Mana Evolutions
		elif re.search(r"Mana(?:\s+Galaxy)?(?:\s+Vortex)?\s+evolution", card.Rules, re.IGNORECASE):
			materialList = [c for c in table if isMana(c) and c.owner == me and re.search("Creature", c.Type)]
			if me.isInverted: reverseCardList(materialList)
			isMultiMaterial = False
			maximumToTake = 1
			if re.search(r"Mana(?:\s+Galaxy)?(?:\s+Vortex)\s+evolution", card.Rules, re.IGNORECASE):
				isMultiMaterial = True
				maximumToTake=len(materialList)
			if len(materialList)==0:
					whisper("Cannot play {}, you don't have any Creatures in Mana Zone for it.".format(card))
					return
			textBox = textBox.format(' from Mana')
			targets = askCard2(materialList,textBox, maximumToTake=maximumToTake,returnAsArray=True)
			if not isinstance(targets,list): return
			for target in targets:
				toPlay(target,0, 0,True,' for Mana Evolution of {}'.format(card),True, True)
		#Hand Evolutions
		elif re.search("Hand Evolution", card.Rules, re.IGNORECASE):
			materialList = [c for c in me.hand if re.search("Creature", c.Type) and c != card]
			reverseCardList(materialList)
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
			materialListGY = [c for c in me.piles['Graveyard'] if re.search("Creature",c.Type)]
			materialListMana = [c for c in table if isMana(c) and c.owner == me and re.search("Creature", c.Type)]
			materialListBZ = [c for c in table if (isCreature(c) or isGear(c)) and c.owner == me and not isBait(c)]
			if me.isInverted:
				reverseCardList(materialListMana)
				reverseCardList(materialListBZ)
			if re.search("Galaxy Vortex Evolution Omega", card.Rules, re.IGNORECASE):
				isGalaxy = True
				evoTypeText = 'Galaxy Vortex Evolution Omega'
			targetsGY = []
			targetsMana = []
			targetsBZ = []
			whisper("Pick cards from Graveyard, Mana and Battle Zone in that order. Close the Pop-Up to proceed to the next selection.")

			maximumToTake=len(materialListGY)
			if maximumToTake>0:
				if isGalaxy:
					maximumToTake = 1
				targetsGY = askCard2(materialListGY,textBox.format(' from Graveyard'), maximumToTake=maximumToTake, returnAsArray=True)
				if not isinstance(targetsGY, list): targetsGY = []

			maximumToTake=len(materialListMana)
			if maximumToTake>0:
				if isGalaxy:
					maximumToTake = 1
				targetsMana = askCard2(materialListMana,textBox.format(' from Mana'), maximumToTake=maximumToTake,returnAsArray=True)
				if not isinstance(targetsMana, list): targetsMana = []

			maximumToTake=len(materialListBZ)
			if maximumToTake>0:
				if isGalaxy:
					maximumToTake = 1
			targetsBZ = askCard2(materialListBZ,textBox.format(' from Battle Zone'), maximumToTake=maximumToTake, returnAsArray=True)
			if not isinstance(targetsBZ, list): targetsBZ = []

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
			clear(targets)
			if len(targets) == 0:
				materialList = [c for c in table if not isShield(c) and not isMana(c) and c.controller == me and not isBait(c) and c._id != card._id]
				if me.isInverted: reverseCardList(materialList)
				minimumToTake = 1
				isNeoEvolution = False
				if re.search('{NEO EVOLUTION}', card.Rules):
					minimumToTake = 0
					isNeoEvolution = True
				elif len(materialList) == 0:
					whisper("Cannot play {}, you don't have any Cards in Battle Zone for it.".format(card))
					whisper("Hint: Play a Creature or Gear first to evolve this card onto.")
					return
				isMultiMaterial = False
				maximumToTake = 1
				if re.search(r"(?:Galaxy\s+)?Vortex Evolution",card.Rules, re.IGNORECASE) or re.search('Super Infinite Evolution', card.Rules, re.IGNORECASE):
					maximumToTake = len(materialList)
					isMultiMaterial = True
				if len(materialList)>0:
					targets = askCard2(materialList,'Select Card(s) to use as Material for Evolution.', minimumToTake=minimumToTake, maximumToTake=maximumToTake, returnAsArray=True)
					if not isinstance(targets, list): targets = []

		if len(targets) == 0:
			if not isNeoEvolution:
				whisper("No targets for {}'s Evolution selected. Aborting...".format(card))
				return
		else:
			if re.search('{NEO EVOLUTION}', card.Rules):
				card.Type = 'Neo Evolution Creature'
			evolveText = ", evolving {}".format(", ".join([c.name for c in targets]))
			processEvolution(card, targets)
	if isMana(card) or isShield(card):
		card.moveTo(me.hand)
	card.moveToTable(0, 0)
	if shieldMarker in card.markers:
		card.markers[shieldMarker] = 0
	align()
	if notifymute == False and not card.hasProperty('Name1'):
		notify("{} plays {}{}.".format(me, card, evolveText))

	if not ignoreEffects:
		card.resetProperties()
		#Twin Pact Handling
		if card.hasProperty('Name1'):
			choice = askYN('Which Side?',[card.properties['Name1'], card.properties['Name2']])
			if choice == 0: return
			card.properties["Name"]=card.properties['Name{}'.format(choice)]
			card.Civilization=card.properties['Civilization{}'.format(choice)]
			card.Cost=card.properties['Cost{}'.format(choice)]
			card.Type=card.properties['Type{}'.format(choice)]
			card.Race=card.properties['Race{}'.format(choice)]
			card.Rules=card.properties['Rules{}'.format(choice)]

			notify("{} plays {} as {}{}.".format(me,card,card.properties['Name{}'.format(choice)],evolveText))
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

		for index, function in enumerate(functionList):
			waitingFunct.insert(index + 1, [card, function]) # This fuction will be queued(along with the card that called it). RN it's waiting.
			#notify("DEBUG: Function added to waiting list: "+str(function))
		evaluateWaitingFunctions() #evaluate all the waiting functions. This thing stop evaluation if a function returns true(ie. its waiting for target)
	if not waitingFunct: #Don't put card in grave if it's waiting for some effect.
		#BUG: This check will always be reached first by a spell without any automation being played with Hogan Blaster. And since HB is still in waitingFunct...the spell never goes to grave automatically
		#Soulution: Instead of this simple chcek make an intermediate function that checks if this card is in waitingFunct. If not, then do endOfFunctionality.
		endOfFunctionality(card)

def endOfFunctionality(card):
	#Magical bugfix to remove Peek symbol
	rnd(1,1)
	if card and isSpellInBZ(card):
		if re.search("Charger", card.name, re.IGNORECASE) and re.search("Charger", card.rules, re.IGNORECASE):
			toMana(card)
			align()
		else:
			card.resetProperties()
			card.target(False)
			card.moveTo(card.owner.piles['Graveyard'])
			align()

#Discard Card menu option
def toDiscard(card, x=0, y=0, notifymute=False, alignCheck=True, checkEvo=True):
	mute()
	card = ensureCardObjects(card)
	src = card.group
	cardWasCreature = isCreature(card) and checkEvo
	if src == table and checkEvo:
		baitList = removeIfEvo(card)
		for baitCard in baitList:
			toDiscard(baitCard, checkEvo=False, alignCheck=False)

	if isPsychic(card):
		toHyperspatial(card)
		return

	cardWasMana = isMana(card)
	card.resetProperties()
	card.target(False)
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
			for index, function in enumerate(functionList):
				waitingFunct.insert(index + 1, [card, function])
			evaluateWaitingFunctions()

	#Handle on Remove From Battle Zone effects:
	if cardWasCreature:
		functionList=[]
		if cardScripts.get(card.Name,{}).get('onLeaveBZ',[]):
			functionList = cardScripts.get(card.Name).get('onLeaveBZ')
			for index, function in enumerate(functionList):
				waitingFunct.insert(index + 1, [card, function])
			evaluateWaitingFunctions()

#Move To Hand (from battlezone)
def toHand(card, show=True, x=0, y=0, alignCheck=True, checkEvo=True):
	mute()
	card = ensureCardObjects(card)
	card.target(False)
	src = card.group
	if isPsychic(card):
		toHyperspatial(card)
		return
	cardWasCreature = isCreature(card) and checkEvo
	if show:
		card.isFaceUp = True
		# need to use just card instead of card.Name for link to card
		# but it won't show as card name if card is not visible to a player, so turning it face up first
		notify("{} moved {} to hand from {}.".format(me, card, src.name))
		# card.isFaceUp = False
		card.resetProperties()
		card.target(False)
		card.moveTo(card.owner.hand)
	else:
		# here, move the card to hand first so it will only show card link to only the player who can see the hand
		# if you show first then move to hand 'card' won't show card name to the owner in the notify message
		card.target(False)
		card.moveTo(card.owner.hand)
		card.resetProperties()
		notify("{} moved {} to hand from {}.".format(me, card, src.name))

	if checkEvo:
		baitList = removeIfEvo(card)
		for baitCard in baitList:
			toHand(baitCard, checkEvo=False, alignCheck=False)

	if alignCheck:
		align()

	#Handle on Remove From Battle Zone effects:
	if cardWasCreature:
		functionList=[]
		if cardScripts.get(card.Name,{}).get('onLeaveBZ',[]):
			functionList = cardScripts.get(card.Name).get('onLeaveBZ')
			for index, function in enumerate(functionList):
				waitingFunct.insert(index + 1, [card,function])
			evaluateWaitingFunctions()

#Move to Bottom (from battlezone)
def toDeckBottom(card, x=0, y=0):
	mute()
	toDeck(card, bottom=True)

#Move to Topdeck (from battlezone)
def toDeck(card, bottom=False):
	mute()
	card = ensureCardObjects(card)
	card.target(False)
	if isPsychic(card):
		toHyperspatial(card)
		return
	cardWasCreature = isCreature(card)
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
				card.resetProperties()
				c.moveToBottom(c.owner.Deck)
			else:
				notify("{} moves {} to top of Deck.".format(me, c))
				card.resetProperties()
				c.moveTo(c.owner.Deck)
	align()
	#Handle on Remove From Battle Zone effects:
	if cardWasCreature:
		functionList=[]
		if cardScripts.get(card.Name,{}).get('onLeaveBZ',[]):
			functionList = cardScripts.get(card.Name).get('onLeaveBZ')
			for index, function in enumerate(functionList):
				waitingFunct.insert(index + 1, [card, function])
			evaluateWaitingFunctions()

allowed_globals = {
    '__builtins__': None,
	'True': True,
	'False': False,
	'None': None,
    're': re,
    'int': int,
	'str': str,
	'float': float,
	'list': list,
	'dict': dict,
	'set': set,
    'cardCostComparator': cardCostComparator,
	'me': me,
}