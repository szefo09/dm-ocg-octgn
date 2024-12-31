# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Constant and Variables Values
# ------------------------------------------------------------------------------
import re
import itertools
import time
import operator
from _random import Random

shields=[]
playerside=None
sideflip=None
diesides=20
civ_order=['Colorless', 'Light', 'Water', 'Darkness', 'Fire', 'Nature']
shieldMarker=('Shield', 'a4ba770e-3a38-4494-b729-ef5c89f561b7')
sealMarker=('Seal', '0d9c9e74-7d60-4433-b0b2-361aef2b18ea')
waitingFunct=[]  # Functions waiting for targets. Please replace this with FUNCTIONS waiting for targets later. If a card calls 2 functions both will happen again otherwise
endOfTurnFunct=[]  # Functions waiting for end of turn to resolve.
startOfTurnFunct=[]  # Functions waiting for end of turn to resolve.
evaluateNextFunction=True #For conditional evaluation of one function after the other, currently only implemented for bounce() in IVT
alreadyEvaluating=False
wscount=0
arrow={}
lastExecutionTime=0
lastTappedCards=[]
DEBOUNCE_DELAY=0.5
my_challenge=None
validated=False
global_timer=None
start_time=None


# Start of Automation code

cardScripts={
	# ON PLAY EFFECTS

	'All Sunrise': {'onPlay': [lambda card: allSunrise()]},
	'Alshia, Spirit of Novas': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Spell")]},
	'Ancient Horn, the Watcher': {'onPlay': [lambda card: untapAll(getMana(me), clearWaitingFunctions=False) if len(getShields(me))>=5 else None]},
	'Angila, Electro-Mask': {'onPlay': [lambda card: waveStriker(lambda card:search(me.piles["Graveyard"], 1, "Creature"), card)]},
	'Aures, Spirit Knight': {'onPlay': [lambda card: mana(me.Deck)]},
	'Aquan': {'onPlay': [lambda card: revealFromDeckAndAddToHand(5, 're.search(r"Light|Darkness", c.Civilization)')]},
	'Aqua Bouncer': {'onPlay': [lambda card: bounce()]},
	'Aqua Deformer': {'onPlay': [lambda card: bothPlayersFromMana(2, exactCount=True)]},
	'Aqua Hulcus': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Aqua Hulk': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Aqua Sniper': {'onPlay': [lambda card: bounce(2, upTo=True)]},
	'Aqua Strummer': {'onPlay': [lambda card: me.Deck.lookAt(5)]},
	'Aqua Surfer': {'onPlay': [lambda card: bounce()]},
	'Aqua Trickster': {'onPlay': [lambda card: waveStriker(lambda card: tapCreature(), card)]},
	'Armored Decimator Valkaizer': {'onPlay': [lambda card: kill(4000)]},
	'Artisan Picora': {'onPlay': [lambda card: fromMana(1,"ALL","ALL","ALL",False,True)]},
	'Astral Warper': {'onPlay': [lambda card: draw(me.Deck, True, 3)]},
	'Baban Ban Ban, Earth\'s Blessing': {'onPlay': [lambda card: massMana(me.Deck, True)]},
	'Ballom, Master of Death': {'onPlay': [lambda card: destroyAll(getCreatures(), True, "ALL", "Darkness", True)]},
	'Baraga, Blade of Gloom': {'onPlay': [lambda card: bounceShield(optional=False)]},
	'Bega, Vizier of Shadow': {'onPlay': [lambda card: shields(me.Deck), lambda card:targetDiscard(True)]},
	'Belix, the Explorer': {'onPlay': [lambda card: fromMana(1,"Spell")]},
	'Berochika, Channeler of Suns': {'onPlay': [lambda card: shields(me.Deck) if len(getShields(me))>=5 else None]},
	'Black Feather, Shadow of Rage': {'onPlay': [lambda card: sacrifice()]},
	'Bombazar, Dragon of Destiny': {'onPlay': [lambda card: destroyAll([c for c in getCreatures() if c!=card], True, 6000, "ALL", False, True)]},
	'Bonfire Lizard': {'onPlay': [lambda card: waveStriker(lambda card: kill(count=2, rulesFilter="{BLOCKER}"), card)]},
	'Bronze-Arm Tribe': {'onPlay': [lambda card: mana(me.Deck)]},
	'Bronze Chain Sickle': {'onPlay': [lambda card: mana(me.Deck)]},
	'Bubble Lamp': {'onPlay': [lambda card: draw(me.Deck, True) if len([c for c in me.piles["Graveyard"] if re.search("Bubble Lamp", c.properties["Name"])])>0 else None]},
	'Buinbe, Airspace Guardian': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Carnival Totem': {'onPlay': [lambda card: swapManaAndHand()]},
	'Cebu Aquman Jr.': {'onPlay': [lambda card: revealFromDeckAndAddToHand(3, 're.search(r"Light|Darkness", c.Civilization)')]},
	'Chaos Worm': {'onPlay': [lambda card: kill()]},
	'Chief De Baula, Machine King of Mystic Light': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Spell")]},
	'Cobalt Hulcus, Aqua Savage': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Core-Crash Lizard': {'onPlay': [lambda card: burnShieldKill(1)]},
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
	'Dedreen, the Hidden Corrupter': {'onPlay': [lambda card: targetDiscard(True) if len(getShields(getTargetPlayer(onlyOpponent=True)))<=3 else None]},
	'Dimension Splitter': {'onPlay': [lambda card: fromGraveyardAll("re.search(r'Dragon\\b', c.Race, re.I)", True, False, True)]},
	'Drill Mutant': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Evolution Creature")]},
	'Doboulgyser, Giant Rock Beast': {'onPlay': [lambda card: kill(3000)]},
	'Dolgeza, Strong Striker': {'onPlay': [lambda card: draw(me.Deck, True, len([c for c in getElements(me) if re.search("Earth Eater", c.Race)])), lambda card: draw(me.Deck, True, len([c for c in getElements(me) if re.search("Giant", c.Race)]))]},
	'Dolmarks, the Shadow Warrior': {'onPlay': [lambda card: dolmarks()]},
	'Dorballom, Lord of Demons': {'onPlay': [lambda card: destroyAll(getCreatures(), True, "ALL", "Darkness", True), lambda card: destroyAllMana(getMana(), "Darkness", True)]},
	'Earth Ripper, Talon of Rage': {'onPlay': [lambda card: ([toHand(c) for c in getMana(me) if isTapped(c)], False)[1]]}, #We do a tuple and return element at index 1, to not return array, as it would evaluate to True and ask for target.
	'Emperor Himiko': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Emeral': {'onPlay': [lambda card: shieldswap(card)]},
	'Emperor Marco': {'onPlay': [lambda card: draw(me.Deck, True, 3)]},
	'Estol, Vizier of Aqua': {'onPlay': [lambda card: shields(me.Deck), lambda card: peekShield(1, True)]},
	'Eviscerating Warrior Lumez': {'onPlay': [lambda card: waveStriker(lambda card: destroyAll(getCreatures(), True, 2000), card)]},
	'Evolution Totem': {'onPlay': [lambda card: search(me.Deck, 1, "Evolution Creature")]},
	'Explosive Fighter Ucarn': {'onPlay': [lambda card: fromMana(2, toGrave=True, exactCount=True)]},
	'Explosive Trooper Zalmez': {'onPlay': [lambda card:kill(3000) if len(getShields(getTargetPlayer(onlyOpponent=True)))<=2 else None]},
	'Extreme Crawler': {'onPlay': [lambda card: bounceAll([c for c in table if c!=card])]},
	'Factory Shell Q': {'onPlay': [lambda card: search(me.Deck, 1, "ALL", "ALL", "Survivor")]},
	'Fighter Dual Fang': {'onPlay': [lambda card: mana(me.Deck,2)]},
	'Fist Dragoon': {'onPlay': [lambda card: kill(2000)]},
	'Flame Trooper Goliac': {'onPlay': [lambda card: waveStriker(lambda card: kill(5000), card)]},
	'Flameburn Dragon': {'onPlay': [lambda card: kill(4000)]},
	'Fonch, the Oracle': {'onPlay': [lambda card: tapCreature()]},
	'Forest Sword, Great Hero': {'onPlay': [lambda card: mana(me.Deck)]},
	'Fortress Shell': {'onPlay': [lambda card: destroyMana(2)]},
	'Forbos, Sanctum Guardian Q': {'onPlay': [lambda card: search(me.Deck, 1, "Spell")]},
	'Frantic Chieftain': {'onPlay': [lambda card: bounce(1, filterFunction="c.owner==me and cardCostComparator(c,4,'<=','Creature')")]},
	'Funky Wizard': {'onPlay': [lambda card: funkyWizard()]},
	'Gajirabute, Vile Centurion': {'onPlay': [lambda card: burnShieldKill(1)]},
	'Galek, the Shadow Warrior': {'onPlay': [lambda card: kill(count=1, rulesFilter="{BLOCKER}"), lambda card: targetDiscard(True)]},
	'Galklife Dragon': {'onPlay': [lambda card: destroyAll(getCreatures(), True, 4000, "Light")]},
	'Gardner, the Invoked': {'onPlay': [lambda card: gear("mana")]},
	'Gigabalza': {'onPlay': [lambda card: targetDiscard(True)]},
	'Gigaberos': {'onPlay': [lambda card: sacrifice(count=2) if len(getCreatures(me))>1 else destroy(card)]},
	'Gigabuster': {'onPlay': [lambda card: bounceShield(optional=False)]},
	'Gigandura': {'onPlay': [lambda card: gigandura(card)]},
	'Gigarayze': {'onPlay': [lambda card: search(me.piles["Graveyard"],1, "Creature", filterFunction='re.search(r"Water|Fire",c.Civilization)')]},
	'Gigargon': {'onPlay': [lambda card: search(me.piles["Graveyard"], 2, "Creature")]},
	'Grape Globbo': {'onPlay': [lambda card: lookAtOpponentHand()]},
	'Grave Worm Q': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "ALL", "ALL", "Survivor")]},
	'Gunes Valkyrie, Holy Vizier': {'onPlay': [lambda card: tapCreature()]},
	'Gylus, Larval Lord': {'onPlay': [lambda card: targetDiscard(True)], 'onLeaveBZ': [lambda card: opponentSearch([targetPlayer.piles["Graveyard"]])]},
	'Gyulcas, Sage of the East Wind': {'onPlay': [lambda card: search(me.Deck, 1, "Cross Gear")]},
	'Hawkeye Lunatron': {'onPlay': [lambda card: search(me.Deck, 1, "ALL", "ALL", "ALL", False)]},
	'Hazaria, Duke of Thorns': {'onPlay': [lambda card: waveStriker(lambda card:opponentSacrifice(), card)]},
	'Honenbe, Skeletal Guardian': {'onPlay': [lambda card: mill(me.Deck, 3, True), lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Hormone, Maxim Bronze': {'onPlay': [lambda card: mana(me.Deck)]},
	'Hot Spring Crimson Meow': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Hulk Crawler': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Hurlosaur': {'onPlay': [lambda card: kill(1000)]},
	'Hurricane Crawler': {'onPlay': [lambda card: hurricaneCrawler()]},
	'Imen=Bugo, Dragon Edge': {'onPlay': [lambda card: fromHyperspatial(1, 're.search("Dragheart", c.Type) and re.search("Nature",c.Civilization) and cardCostComparator(c,4,"<=")')]},
	'Imen=Bugo, Dragon Ruler': {'onPlay': [lambda card: fromHyperspatial(1, 're.search("Dragheart", c.Type) and re.search("Nature",c.Civilization) and cardCostComparator(c,4,"<=")')]},
	'Iron Arm Tribe': {'onPlay': [lambda card: mana(me.Deck)]},
	'Izana Keeza': {'onPlay': [lambda card: kill(2000)]},
	'Jagila, the Hidden Pillager': {'onPlay': [lambda card: waveStriker(lambda card: targetDiscard(True, "grave", 3), card)]},
	'Jasmine, Mist Faerie': {'onPlay': [lambda card: suicide(card, mana, [me.Deck])]},
	'Jelly, Dazzling Electro-Princess': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Jenny, the Dismantling Puppet': {'onPlay': [lambda card: targetDiscard()]},
	'Jenny, the Suicide Doll': {'onPlay': [lambda card: suicide(card, targetDiscard, [True])]},
	'Jet R.E, Brave Vizier': {'onPlay': [lambda card: shields(me.Deck)]},
	'Katta Kirifuda & Katsuking -Story of Passion-': {'onTrigger': [lambda card: askYN("Do you have 2 or less shields to treat {} as a Shield Trigger?".format(card.properties["Name"]))==1],
		'onPlay': [lambda card: lookAtTopCards(5, "card", "hand", "bottom", True, "BOUNCE", ["Fire", "Nature"]), lambda card: bounce(conditionalFromLastFunction=True)]},
	'King Aquakamui': {'onPlay': [lambda card: kingAquakamui(card)]},
	'King Mazelan': {'onPlay': [lambda card: bounce()]},
	'King Ripped-Hide': {'onPlay': [lambda card: draw(me.Deck, True, 2)]},
	'King Muu Q': {'onPlay': [lambda card: bounce()]},
	'King Tsunami': {'onPlay': [lambda card: bounceAll(group=[c for c in table if c!=card])]},
	'Klujadras': {'onPlay': [lambda card: waveStriker(lambda card: klujadras(), card)]},
	'Kolon, the Oracle': {'onPlay': [lambda card: tapCreature()]},
	'Kulus, Soulshine Enforcer': {'onPlay': [lambda card: manaCompare(1,True)]},
	'Larba Geer, the Immaculate': {'onPlay': [lambda card: tapCreature(1, True, filterFunction='re.search(r"{BLOCKER}", c.Rules)')]},
	'Lena, Vizier of Brilliance': {'onPlay': [lambda card: fromMana(1,"Spell")]},
	'Lucky Ball': {'onPlay': [lambda card: draw(me.Deck,True, 2) if len(getShields(getTargetPlayer(onlyOpponent=True)))<=3 else None]},
	'Lugias, The Explorer': {'onPlay': [lambda card: tapCreature()]},
	'Locomotiver': {'onPlay': [lambda card: targetDiscard(True)]},
	'Loth Rix, the Iridescent': {'onPlay': [lambda card: shields(me.deck)]},
	'Magris, Vizier of Magnetism': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Magmarex': {'onPlay': [lambda card: destroyAll(getCreatures(), True, 1000,"ALL", False, True)]},
	'Marinomancer': {'onPlay': [lambda card: revealFromDeckAndAddToHand(3, 're.search(r"Light|Darkness", c.Civilization)')]},
	'Masked Horror, Shadow of Scorn': {'onPlay': [lambda card: targetDiscard(True)]},
	'Metal Avenger Solid, Dragon Edge': {'onPlay': [lambda card: fromHyperspatial(1, 're.search("Dragheart", c.Type) and re.search("Water", c.Civilization) and cardCostComparator(c,4, "<=")'), lambda card: bounce(filterFunction='cardCostComparator(c, 6, "<=", "Creature")')]},
	'Metal Avenger Solid, Dragon Ruler': {'onPlay': [lambda card: fromHyperspatial(1, 're.search("Dragheart", c.Type) and re.search("Water", c.Civilization) and cardCostComparator(c,4, "<=")'), lambda card: bounce(filterFunction='cardCostComparator(c, 6, "<=", "Creature")'),]},
	'Mechadragon\'s Breath': {'onPlay': [lambda card: mechadragonsBreath()]},
	'Meteosaur': {'onPlay': [lambda card: kill(2000)]},
	'Miele, Vizier of Lightning': {'onPlay': [lambda card: tapCreature()]},
	'Midnight Crawler': {'onPlay': [lambda card: opponentManaToHand()]},
	'Mizoy, the Oracle': {'onPlay': [lambda card: tapCreature(filterFunction='re.search(r"Darkness|Fire", c.Civilization)')]},
	'Moors, the Dirty Digger Puppet': {'onPlay': [lambda card: search(me.piles["Graveyard"])]},
	'Muramasa\'s Socket': {'onPlay': [lambda card: kill(1000)]},
	'Murian': {'onPlay': [lambda card: suicide(card, draw, [me.Deck])]},
	'Nam=Daeddo, Bronze Style': {'onPlay': [lambda card: mana(me.Deck, preCondition=manaArmsCheck("Nature",3))]},
	'Necrodragon Bryzenaga': {'onPlay': [lambda card: peekShields(getShields(me))]},
	'Necrodragon Zalva': {'onPlay': [lambda card: remoteCall(getTargetPlayer(onlyOpponent=True), "draw", [])]},
	'Neve, the Leveler': {'onPlay': [lambda card: search(me.Deck, len(getCreatures(getTargetPlayer(onlyOpponent=True)))-len(getCreatures(me)), "Creature")]},
	'Niofa, Horned Protector': {'onPlay': [lambda card: search(me.Deck, 1, "ALL", "Nature")]},
	'Ochappi, Pure Hearted Faerie': {'onPlay': [lambda card: fromGraveyardToMana(ask=True)]},
	'Onslaughter Triceps': {'onPlay': [lambda card: fromMana(toGrave=True)]},
	'Pakurio': {'onPlay': [lambda card: targetDiscard(False,"shield")]},
	'Phal Eega, Dawn Guardian': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Spell")]},
	'Phal Pierro, Apocalyptic Guardian': {'onPlay': [lambda card: suicide(card, search, [me.piles["Graveyard"], 1, "Spell"])]},
	'Phal Reeze, Apocalyptic Sage': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Spell")]},
	'Piara Heart': {'onPlay': [lambda card: kill(1000)]},
	'Pointa, the Aqua Shadow': {'onPlay': [lambda card: peekShield(1, True), lambda card: targetDiscard(True)]},
	'Poison Worm': {'onPlay': [lambda card: kill(3000, 1, targetOwn=True)]},
	'Pouch Shell': {'onPlay': [lambda card: pouchShell()]},
	'Prometheus, Splash Axe': {'onPlay': [lambda card: mana(me.Deck, 2, False, True)]},
	'Punch Trooper Bronks': {'onPlay': [lambda card: bronks()]},
	'Q-tronic Hypermind': {'onPlay': [lambda card: draw(me.Deck, True, len(getSurvivorsOnYourTable(False)))]},
	'Qurian': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Raiden, Lightfang Ninja': {'onPlay': [lambda card: tapCreature()]},
	'Rayla, Truth Enforcer': {'onPlay': [lambda card: search(me.Deck, 1, "Spell")]},
	'Raptor Fish': {'onPlay': [lambda card: raptorFish()]},
	'Rimuel, Cloudbreak Elemental': {'onPlay': [lambda card: tapCreature(len([c for c in getMana(me) if re.search("Light", c.Civilization) and not isTapped(c)]))]},
	'Ripple Lotus Q': {'onPlay': [lambda card: tapCreature()]},
	'Rom, Vizier of Tendrils': {'onPlay': [lambda card: tapCreature()]},
	'Rothus, the Traveler': {'onPlay': [lambda card: opponentSacrifice() if not sacrifice(returnTrueIfNoDestruction=True) else None]},
	'Romanesk, the Dragon Wizard': {'onPlay': [lambda card: mana(me.Deck, 4)]},
	'Rumbling Terahorn': {'onPlay': [lambda card: search(me.Deck, 1, "Creature")]},
	'Rv Penicillin, Dragment Symbol': {'onPlay': [lambda card: bounceAll(myCards=False) if revolution(card,2) else None]},
	'Ryokudou, the Principle Defender': {'onPlay': [lambda card: mana(me.Deck,2), lambda card: fromMana()]},
	'Sarvarti, Thunder Spirit Knight': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Spell")]},
	'Saucer-Head Shark': {'onPlay': [lambda card: bounceAll(filterFunction="c.Power!='Infinity' and int(c.Power.strip('+'))<=2000")]},
	'Sasoris, Dragon Edge': {'onPlay': [lambda card: fromHyperspatial(1,'re.search("Dragheart",c.Type) and (cardCostComparator(c,2,"<=") or (re.search("Nature") and cardCostComparator(c,4,"<=")))')],
						  	'onDestroy': [lambda card: toMana(card)]},
	'Sasoris, Dragon Ruler': {'onPlay': [lambda card: fromHyperspatial(1,'re.search("Dragheart",c.Type) and (cardCostComparator(c,2,"<=") or (re.search("Nature") and cardCostComparator(c,4,"<=")))')],
						   	'onDestroy': [lambda card: toMana(card)]},
	'Scissor Scarab': {'onPlay': [lambda card: search(me.deck,1,"ALL","ALL","Giant Insect")]},
	'Shtra': {'onPlay': [lambda card: bothPlayersFromMana()]},
	'Self-Destructing Gil Poser': {'onPlay': [lambda card: suicide(card, kill, [2000])]},
	'Sir Navaal, Thunder Mecha Knight': {'onPlay': [lambda card: fromMana(1,"Spell")]},
	'Sir Virginia, Mystic Light Insect': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Scarlet Skyterror': {'onPlay': [lambda card: destroyAll([c for c in getCreatures() if re.search("{BLOCKER}", c.Rules)], True)]},
	'Skeleton Thief, the Revealer': {'onPlay': [lambda card: search(me.piles["Graveyard"], RaceFilter="Living Dead")]},
	'Skyscraper Shell': {'onPlay': [lambda card: waveStriker(lambda card: opponentSendToMana(), card)]},
	'Skysword, the Savage Vizier': {'onPlay': [lambda card: mana(me.Deck), lambda card: shields(me.deck)]},
	'Solidskin Fish': {'onPlay': [lambda card: fromMana()]},
	'Spark Chemist, Shadow of Whim': {'onPlay': [lambda card: fromManaAll()]},
	'Spiritual Star Dragon': {'onPlay': [lambda card: search(me.Deck, 1, "Creature", filterFunction='re.search("Evolution", c.Type)')]},
	'Splash Zebrafish': {'onPlay': [lambda card: fromMana()]},
	'Storm Shell': {'onPlay': [lambda card: opponentSendToMana()]},
	'Steamroller Mutant': {'onPlay': [lambda card: waveStriker(lambda card: destroyAll(getCreatures(), True), card)]},
	'Stinger Worm': {'onPlay': [lambda card: sacrifice()]},
	'Swamp Worm': {'onPlay': [lambda card: opponentSacrifice()]},
	'Syforce, Aurora Elemental': {'onPlay': [lambda card: fromMana(1,"Spell")]},
	'Telitol, the Explorer': {'onPlay': [lambda card: peekShields(getShields(me))]},
	'Tekorax': {'onPlay': [lambda card: peekShields(getShields(getTargetPlayer(onlyOpponent=True)))]},
	'Terradragon Zalberg': {'onPlay': [lambda card: destroyMana(2)]},
	'The=Deadman, Dragon Edge': {'onPlay': [lambda card: fromHyperspatial(1,'re.search("Dragheart", c.Type) and re.search("Nature",c.Civilization) and cardCostComparator(c, 5,"<=")')]},
	'The=Deadman, Dragon Ruler': {'onPlay': [lambda card: fromHyperspatial(1,'re.search("Dragheart", c.Type) and re.search("Nature",c.Civilization) and cardCostComparator(c, 5,"<=")')]},
	'Thorny Mandra': {'onPlay': [lambda card: fromGraveyardToMana(ask=True)]},
	'Thrash Crawler': {'onPlay': [lambda card: fromMana()]},
	'Three-Faced Ashura Fang': {'onPlay': [lambda card: bounceShield(optional=False)]},
	'Titan Giant': {'onPlay': [lambda card: mana (me.Deck, 2, True)]},
	'Torpedo Cluster': {'onPlay': [lambda card: fromMana()]},
	'Trenchdive Shark': {'onPlay': [lambda card: shieldswap(card,2)]},
	'Triple Mouth, Decaying Savage': {'onPlay': [lambda card: mana(me.Deck), lambda card: targetDiscard(True)]},
	'Trombo, Fractured Doll': {'onPlay': [lambda card: waveStriker(lambda card: sercah(me.piles["Graveyard"], 1, "Creature"), card)]},
	'Trox, General of Destruction': {'onPlay': [lambda card: targetDiscard(randomDiscard=True, count=len([c for c in getCreatures(me) if re.search("Darkness", c.Civilization) and c._id!=card._id]))]},
	'Uncanny Turnip': {'onPlay': [lambda card: waveStriker([lambda card: mana(me.Deck), lambda card: fromMana(1,'Creature')], card)]},
	'Unicorn Fish': {'onPlay': [lambda card: bounce()]},
	'Vampire Silphy': {'onPlay': [lambda card: destroyAll(getCreatures(), True, 3000)]},
	'Velyrika Dragon': {'onPlay': [lambda card: search(me.Deck, 1, "ALL", "ALL", "Armored Dragon")]},
	'Viblo Blade, Hulcus Range': {'onPlay': [lambda card: draw(me.Deck, True)]},
	'Walmiel, Electro-Sage': {'onPlay': [lambda card: tapCreature()]},
	'Whispering Totem': {'onPlay': [lambda card: fromDeck()]},
	'Wily Carpenter': {'onPlay': [lambda card: draw(me.Deck, True, 2), lambda card: selfDiscard(2)]},
	'Wind Axe, the Warrior Savage': {'onPlay': [lambda card: kill(count=1, rulesFilter="{BLOCKER}"), lambda card: mana(me.Deck)]},
	'Zardia, Spirit of Bloody Winds': {'onPlay': [lambda card: shields(me.Deck)]},
	'Zemechis, the Explorer': {'onPlay': [lambda card: gear("kill")]},

	# ON CAST EFFECTS

	'Abduction Charger': {'onPlay': [lambda card: bounce(2, upTo=True)]},
	'Apocalypse Day': {'onPlay': [lambda card: destroyAll(getCreatures()) if len(getCreatures())>5 else None]},
	'Apocalypse Vise': {'onPlay': [lambda card: apocalypseVise()]},
	'Aquan Jr.\'s Delivery': {'onPlay': [lambda card: revealFromDeckAndAddToHand(3, 're.search(r"Light|Darkness", c.Civilization)')]},
	'Big Beast Cannon': {'onPlay': [lambda card: kill(7000)]},
	'Blizzard of Spears': {'onPlay': [lambda card: destroyAll(getCreatures(), True, 4000)]},
	'Bomber Doll': {'onPlay': [lambda card: kill(2000)]},
	'Bonds of Justice': {'onPlay': [lambda card: tapCreature(1, True, True, filterFunction='not re.search(r"{BLOCKER}", c.Rules)')]},
	'Bone Dance Charger': {'onPlay': [lambda card: mill(me.Deck, 2)]},
	'Boomerang Comet': {'onPlay': [lambda card: fromMana()]},
	'Brain Charger': {'onPlay': [lambda card: draw(me.Deck)]},
	'Brain Cyclone': {'onPlay': [lambda card: draw(me.Deck, False, 1)]},
	'Brain Re:Charger': {'onPlay': [lambda card: draw(me.Deck)]},
	'Brain Serum': {'onPlay': [lambda card: draw(me.Deck, False, 2)]},
	'Brutal Charge': {'onPlay': [lambda card: addDelayedEffect({"card":card, "effects":[lambda card, args: search(me.Deck, askNumber("Enter a number of broken opponent shields.", 1, True), "Creature")] }, None)]},
	'Burst Shot': {'onPlay': [lambda card: destroyAll(getCreatures(), True, 2000)]},
	'Cannonball Sling': {'onPlay': [lambda card: kill(2000)],
						 'onMetaMorph': [lambda card: kill(6000)]},
	'Cataclysmic Eruption': {'onPlay': [lambda card: destroyMana(len([c for c in getCreatures(me) if re.search(r'Nature',c.Civilization)]))]},
	'Chains of Sacrifice': {'onPlay': [lambda card: kill("ALL","ALL","ALL",2), lambda card:sacrifice()]},
	'Child Festival of Faerie Fire': {'onPlay':[ lambda card: lookAtTopCards(2, 'card', 'mana', toManaTapped=True), lambda card: toHand(card) if re.search("Fire",getMana(me)[-1].Civilization) else None]},
	'Clone Factory': {'onPlay': [lambda card: fromMana(2)]},
	'Cloned Blade': {'onPlay': [lambda card: cloned(lambda card, count: kill('3000', count=count),card)]},
	'Cloned Deflector': {'onPlay': [lambda card: cloned(lambda card, count: tapCreature(count),card)]},
	'Cloned Nightmare': {'onPlay': [lambda card: cloned(lambda card, count: targetDiscard(True, count=count),card)]},
	'Cloned Spiral': {'onPlay': [lambda card: cloned(lambda card, count: bounce(count),card)]},
	'Comet Missile': {'onPlay': [lambda card: kill(6000, count=1, rulesFilter="{BLOCKER}")]},
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
	'Death Cruzer, the Annihilator': {'onPlay': [lambda card: destroyAll([c for c in getCreatures(me) if c!=card], True)]},
	'Death Gate, Gate of Hell': {'onPlay': [lambda card: kill("ALL","Untap"), lambda card: fromGrave()]},
	'Death Smoke': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Decopin Crash': {'onPlay': [lambda card: kill(4000)]},
	'Devil Hand': {'onPlay': [lambda card: kill(), lambda card: mill(me.Deck, 3, True)]},
	'Devil Smoke': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Diamondia, the Blizzard Rider': {'onPlay': [lambda card: fromGraveyardAll("re.search(r'Snow Faerie', c.Race)",False,False,True),lambda card: fromManaAll("re.search(r'Snow Faerie', c.Race)")]},
	'Dimension Gate': {'onPlay': [lambda card: search(me.Deck, 1, "Creature")]},
	'Divine Riptide': {'onPlay': [lambda card: divineRiptide()]},
	'Slash Charger': {'onPlay': [lambda card: fromDeckToGrave()]},
	'Dracobarrier': {'onPlay': [lambda card: dracobarrier()]},
	'Drill Bowgun': {'onPlay': [lambda card: gear("kill")]},
	'Eldritch Poison': {'onPlay': [lambda card: fromMana(1, "Creature") if not sacrifice(filterFunction='re.search("Darkness",c.Civilization)', returnTrueIfNoDestruction=True) else None]},
	'Emergency Typhoon': {'onPlay': [lambda card: draw(me.Deck, True, 2), lambda card: selfDiscard()]},
	'Enchanted Soil': {'onPlay': [lambda card: fromGraveyardToMana(2, "re.search('Creature', c.Type)")]},
	'Energy Re:Light': {'onPlay': [lambda card: draw(me.Deck, False, 2)]},
	'Energy Stream': {'onPlay': [lambda card: draw(me.Deck, False, 2)]},
	'Enigmatic Cascade': {'onPlay': [lambda card: enigmaticCascade()]},
	'Eureka Charger': {'onPlay': [lambda card: draw(me.Deck)]},
	'Eureka Program': {'onPlay': [lambda card: eurekaProgram(True)]},
	'Faerie Crystal': {'onPlay': [lambda card: mana(me.Deck, postAction="ManaIfCiv", postArgs=["Zero"])]},
	'Faerie Life': {'onPlay': [lambda card: mana(me.Deck)]},
	'Faerie Re:Life': {'onPlay': [lambda card: mana(me.Deck)]},
	'Faerie Miracle': {'onPlay': [lambda card: mana(me.Deck, postAction="mana(me.Deck)", postCondition="manaArmsCheck()")]},
	'Faerie Shower': {'onPlay': [lambda card: lookAtTopCards(2,"card","hand","mana", False)]},
	'Flame-Absorbing Palm': {'onPlay': [lambda card: kill(2000)]},
	'Fire Crystal Bomb': {'onPlay': [lambda card: kill(5000)]},
	'Flame Lance Trap': {'onPlay': [lambda card: kill(5000)]},
	'Flood Valve': {'onPlay': [lambda card: fromMana()]},
	'Freezing Icehammer': {'onPlay': [lambda card: sendToMana(filterFunction='re.search(r"Water|Darkness", c.Civilization)')]},
	'Future Slash': {'onPlay': [lambda card: fromDeckToGrave(2,True)]},
	'Gardening Drive': {'onPlay': [lambda card: mana(me.Deck)]},
	'Gatling Cyclone': {'onPlay': [lambda card: kill(2000)]},
	'Geo Bronze Magic': {'onPlay': [lambda card: mana(me.Deck, postAction="DrawIfCiv", postArgs=["Fire", "Light"])]},
	'Ghastly Drain': {'onPlay': [lambda card: ghastlyDrain(card)]},
	'Ghost Clutch': {'onPlay': [lambda card: targetDiscard(True)]},
	'Ghost Touch': {'onPlay': [lambda card: targetDiscard(True)]},
	'Glory Snow': {'onPlay': [lambda card: manaCompare(2,True)]},
	'Goren Cannon': {'onPlay': [lambda card: kill(3000)]},
	'Grinning Hunger': {'onPlay': [lambda card: grinningHunger(card)]},
	'Goromaru Communication': {'onPlay': [lambda card: search(me.Deck, 1, "Creature")]},
	'Hell Chariot': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Hell Hand': {'onPlay': [lambda card: hellHand()]},
	'Hide and Seek': {'onPlay': [lambda card: bounce(1, True, filterFunction='not re.search("Evolution", c.Type)'), lambda card: targetDiscard(True)]},
	'Hirameki Program': {'onPlay': [lambda card: eurekaProgram(True)]},
	'Hogan Blaster': {'onPlay': [lambda card: drama(True, "creature or spell", "battlezone", "top")]},
	'Holy Awe': {'onPlay': [lambda card: tapCreature(1, True)]},
	'Hopeless Vortex': {'onPlay': [lambda card: kill()]},
	'Hydro Hurricane': {'onPlay': [lambda card: hydroHurricane(card)]},
	'Hyperspatial Storm Hole': {'onPlay': [lambda card: kill(5000)]},
	'Hyperspatial Bolshack Hole': {'onPlay': [lambda card: kill(5000)]},
	'Hyperspatial Kutt Hole': {'onPlay': [lambda card: kill(5000)]},
	'Hyperspatial Guard Hole': {'onPlay': [lambda card: sendToShields(1, True, True, True, False, 'not re.search(r"Evolution", c.Type)')]},
	'Hyperspatial Vice Hole': {'onPlay': [lambda card: targetDiscard()]},
	'Hyperspatial Shiny Hole': {'onPlay': [lambda card: tapCreature()]},
	'Hyperspatial Energy Hole': {'onPlay': [lambda card: draw(me.Deck, False, 1)]},
	'Hyperspatial Faerie Hole': {'onPlay': [lambda card: mana(me.Deck)]},
	'Hyperspatial Revive Hole': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Illusionary Merfolk': {'onPlay': [lambda card: draw(me.Deck, True, 3) if len([c for c in getCreatures(me) if re.search("Cyber Lord", c.Race)])>0 else None]},
	'Impossible Tunnel': {'onPlay': [lambda card: declareRace(card)]},
	'Infernal Smash': {'onPlay': [lambda card: kill()]},
	'Intense Evil': {'onPlay': [lambda card: intenseEvil()]},
	'Dondon Vacuuming Now': {'onPlay': [lambda card: lookAtTopCards(5, "card", "hand", "bottom", True, "BOUNCE", ["Fire", "Nature"]), lambda card: bounce(conditionalFromLastFunction=True)]},
	'Invincible Abyss': {'onPlay': [lambda card: destroyAll([c for c in getCreatures() if c.controller!=me], True)]},
	'Invincible Aura': {'onPlay': [lambda card: shields(me.Deck, 3, True)]},
	'Invincible Cataclysm': {'onPlay': [lambda card: burnShieldKill(3)]},
	'Invincible Technology': {'onPlay': [lambda card: search(me.Deck, len(me.Deck))]},
	'Judgement of the Flame\'s Spear and the Water\'s Blade': {'onPlay': [lambda card: flamespearWaterblade()]},
	'Justice Jamming': {'onPlay': [lambda card: mode([lambda card: tapCreature(targetALL=True, includeOwn=True, filterFunction='re.search(r"Darkness",c.Civilization)'), lambda card: tapCreature(targetALL=True, includeOwn=True, filterFunction='re.search(r"Fire",c.Civilization)')], card, ["Tap all Darkness Creatures","Tap all Fire Creatures"])]},
	'Laser Whip': {'onPlay': [lambda card: tapCreature()]},
	'Lifeplan Charger': {'onPlay': [lambda card: lookAtTopCards(5, "Creature")]},
	'Lightning Charger': {'onPlay': [lambda card: tapCreature()]},
	'Like a Rolling Storm': {'onPlay': [lambda card: mill(me.Deck, 3, True), lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Lionic Phantom Dragon\'s Flame': {'onPlay': [lambda card: kill(2000)]},
	'Liquid Scope': {'onPlay': [lambda card: lookAtOpponentHand(), lambda card: peekShields(getShields(getTargetPlayer(onlyOpponent=True)))]},
	'Living Lithograph': {'onPlay': [lambda card: mana(me.Deck)]},
	'Logic Cube': {'onPlay': [lambda card: search(me.Deck, 1, "Spell")]},
	'Logic Sphere': {'onPlay': [lambda card: fromMana(1, "Spell")]},
	'Lost Re:Soul': {'onPlay': [lambda card: discardAll()]},
	'Lost Soul': {'onPlay': [lambda card: discardAll()]},
	'Lunar Charger': {'onPlay': [lambda card: lunarCharger(card)]},
	'Mana Crisis': {'onPlay': [lambda card: destroyMana()]},
	'Mana Nexus': {'onPlay': [lambda card: sendToShields(1, False, True, False, True)]},
	'Martial Law': {'onPlay': [lambda card: gear("kill")]},
	'Magic Shot - Arcadia Egg': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Magic Shot - Chain Spark': {'onPlay': [lambda card: tapCreature()]},
	'Magic Shot - Open Brain': {'onPlay': [lambda card: draw(me.Deck, False, 2)]},
	'Magic Shot - Panda Full Life': {'onPlay': [lambda card: mana(me.Deck)]},
	'Magic Shot - Soul Catcher': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Magic Shot - Sword Launcher': {'onPlay': [lambda card: kill(3000)]},
	'Magical Pot': {'onPlay': [lambda card: bounce(1, filterFunction='re.search("Evolution Creature", c.Type)')]},
	'Mana Bonanza': {'onPlay': [lambda card: massMana(me.Deck, False)]},
	'Mendelssohn': {'onPlay': [lambda card: lookAtTopCards(2, targetZone="mana",remainingZone='grave', count=2, revealAll=True, filterFunction='re.search(r"\\bDragon\\b",c.Race)', toManaTapped=True)]},
	'Miraculous Meltdown': {'onPlay': [lambda card: miraculousMeltdown(card)]},
	'Miraculous Plague': {'onPlay': [lambda card: miraculousPlague()]},
	'Miraculous Rebirth': {'onPlay': [lambda card: miraculousRebirth()]},
	'Miraculous Snare': {'onPlay': [lambda card: sendToShields(1, True, True, True, False, 'not re.search(r"Evolution", c.Type)')]},
	'Moonlight Flash': {'onPlay': [lambda card: tapCreature(2)]},
	'Morbid Medicine': {'onPlay': [lambda card: search(me.piles["Graveyard"], 2, "Creature")]},
	'Mulch Charger': {'onPlay': [lambda card: sendToMana(opponentCards=False, myCards=True)]},
	'Mystery Cube': {'onPlay': [lambda card: drama()]},
	'Mystic Dreamscape': {'onPlay': [lambda card: fromMana(3)]},
	'Mystic Inscription': {'onPlay': [lambda card: shields(me.Deck)]},
	'Mystic Treasure Chest': {'onPlay': [lambda card: fromDeckToMana(1, "not re.search(r\'Nature\', c.Civilization)")]},
	'Natural Snare': {'onPlay': [lambda card: sendToMana()]},
	'Nightmare Machine': {'onPlay': [lambda card: nigthmareMachine()]},
	'Persistent Prison of Gaia': {'onPlay': [lambda card: bounce(1, True, filterFunction='not re.search("Evolution", c.Type)'), lambda card: targetDiscard(True)]},
	'Phantom Dragon\'s Flame': {'onPlay': [lambda card: kill(2000)]},
	'Phantasm Clutch': {'onPlay': [lambda card: kill("ALL", "Tap")]},
	'Pixie Cocoon': {'onPlay': [lambda card: fromMana(1, "Creature")]},
	'Pixie Life': {'onPlay': [lambda card: mana(me.Deck, 1, False, False), lambda card: fromMana(1, "ALL", "Zero")]},
	'Primal Scream': {'onPlay': [lambda card: mill(me.Deck, 4, True), lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Proclamation of Death': {'onPlay': [lambda card: opponentSacrifice()] },
	'Psychic Shaper': {'onPlay': [lambda card: revealFromDeckAndAddToHand(4, 're.search("Water",c.Civilization)')]},
	'Punish Hold': {'onPlay': [lambda card: tapCreature(2)]},
	'Purgatory Force': {'onPlay': [lambda card: search(me.piles["Graveyard"], 2, "Creature")]},
	'Rain of Arrows': {'onPlay': [lambda card: lookAtHandAndDiscardAll(filterFunction='re.search(r"Darkness",c.Civilization) and re.search(r"Spell",c.Type)')]},
	'Rainbow Gate': {'onPlay': [lambda card: search(me.Deck, 1,"Creature", "/")]},
	'Rainbow Stone': {'onPlay': [lambda card: fromDeckToMana()]},
	'Rapid Reincarnation': {'onPlay': [lambda card: rapidReincarnation()]},
	'Reap and Sow': {'onPlay': [lambda card: destroyMana(), lambda card: mana(me.Deck)]},
	'Reaper Hand': {'onPlay': [lambda card: kill()]},
	'Recon Operation': {'onPlay': [lambda card: peekShield(3, True)]},
	'Reflecting Ray': {'onPlay': [lambda card: tapCreature()]},
	'Relentless Blitz': {'onPlay': [lambda card: declareRace(card)]},
	'Reverse Cyclone': {'onPlay': [lambda card: tapCreature()]},
	'Reverse Re:Charger': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Riptide Charger': {'onPlay': [lambda card: bounce()]},
	'Roar of the Earth': {'onPlay': [lambda card: fromMana(1,"Creature",filterFunction="cardCostComparator(c,6,'>=', typeFilter='Creature')")]},
	'Roulette of Ruin': {'onPlay': [lambda card: rouletteOfRuin()]},
	'Samurai Decapitation Sword': {'onPlay': [lambda card: kill(5000)]},
	'Scheming Hands': {'onPlay': [lambda card: targetDiscard()]},
	'Screaming Sunburst': {'onPlay': [lambda card: tapCreature(1, True, True, filterFunction='not re.search(r"Light", c.Civilization)')]},
	'Screw Rocket': {'onPlay': [lambda card: gear("kill")]},
	'Seventh Tower': {'onPlay': [lambda card: mana(me.Deck)],
				   'onMetamorph': [lambda card: mana(me.Deck,3)]},
	'Searing Wave': {'onPlay': [lambda card: destroyAll([c for c in getCreatures() if c.controller!=me], True, 3000), lambda card: burnShieldKill(1, True)]},
	'Shock Hurricane': {'onPlay': [lambda card: shockHurricane(card)]},
	'Siren Concerto': {'onPlay': [lambda card: fromMana(), lambda card: fromHandToMana()]},
	'Skeleton Vice': {'onPlay': [lambda card: targetDiscard(True, "grave", 2)]},
	'Snake Attack': {'onPlay': [lambda card: burnShieldKill(1,True)]},
	'Solar Grace': {'onPlay': [lambda card: tapCreature()]},
	'Solar Ray': {'onPlay': [lambda card: tapCreature()]},
	'Solar Trap': {'onPlay': [lambda card: tapCreature()]},
	'Soulswap': {'onPlay': [lambda card: soulSwap()]},
	'Soul Gulp': {'onPlay': [lambda card: opponentToDiscard(len([c for c in getCreatures(getTargetPlayer(onlyOpponent=True)) if re.search("Light", c.Civilization)]))]},
	'Spastic Missile': {'onPlay': [lambda card: kill(3000)]},
	'Sphere of Wonder': {'onPlay': [lambda card: manaCompare(1,shield=True)]},
	'Spiral Drive': {'onPlay': [lambda card: bounce()]},
	'Spiral Gate': {'onPlay': [lambda card: bounce()]},
	'Spiral Lance': {'onPlay': [lambda card: gear("bounce")]},
	'Static Warp': {'onPlay': [lambda card: staticWarp()]},
	'Stronghold of Lightning and Flame': {'onPlay': [lambda card: kill(3000), lambda card: tapCreature()]},
	'Submarine Project': {'onPlay': [lambda card: lookAtTopCards(4)]},
	'Super Burst Shot': {'onPlay': [lambda card: destroyAll([c for c in getCreatures() if c.owner!=me], True, 2000)]},
	'Super Infernal Gate Smash': {'onPlay': [lambda card: kill()]},
	'Super Spark': {'onPlay': [lambda card: tapCreature(1,True)]},
	'Teleportation': {'onPlay': [lambda card: bounce(2, upTo=True)]},
	'Ten-Ton Crunch': {'onPlay': [lambda card: kill(3000)]},
	'Terror Pit': {'onPlay': [lambda card: kill("All")]},
	'The Grave of Angels and Demons': {'onPlay': [lambda card: theGraveOfAngelsAndDemons()]},
	'The Strong Spiral': {'onPlay': [lambda card: bounce()]},
	'The Strong Breath': {'onPlay': [lambda card: kill("ALL","Untap")]},
	'Thought Probe': {'onPlay': [lambda card: draw(me.Deck, False, 3) if len(getCreatures(getTargetPlayer(onlyOpponent=True)))>=3 else None]},
	'Thunder Net': {'onPlay': [lambda card: tapCreature(count=len([c for c in getCreatures(me) if re.search(r'Water',c.Civilization)]))]},
	'Timeless Garden': {'onPlay': [lambda card: mana(me.Deck)]},
	'Tornado Flame': {'onPlay': [lambda card: kill(4000)]},
	'Transmogrify': {'onPlay': [lambda card: killAndSearch(True)]},
	'Treasure Map': {'onPlay': [lambda card: lookAtTopCards(5, "Creature", filterFunction='re.search("Nature",c.Civilization)')]},
	'Triple Brain': {'onPlay': [lambda card: draw(me.Deck, False, 3)]},
	'Ultimate Force': {'onPlay': [lambda card: mana(me.Deck, 2)]},
	'Unified Resistance': {'onPlay': [lambda card: declareRace(card)]},
	'Upheaval': {'onPlay': [lambda card: upheaval()]},
	'Vacuum Gel': {'onPlay': [lambda card: kill(filterFunction='re.search(r"Light|Nature",c.Civilization)')]},
	'Vacuum Ray': {'onPlay': [lambda card: tapCreature()]},
	'Valiant Spark': {'onPlay': [lambda card: tapCreature()],
					  'onMetamorph': [lambda card: tapCreature(1,True)]},
	'Vine Charger': {'onPlay': [lambda card: opponentSendToMana()]},
	'Virtual Tripwire': {'onPlay': [lambda card: tapCreature()]},
	'Volcanic Arrows': {'onPlay': [lambda card: burnShieldKill(1, True, 6000, 1, True)]},
	'Volcano Charger': {'onPlay': [lambda card: kill(2000)]},
	'Wave Lance': {'onPlay': [lambda card: waveLance()]},
	'Wave Rifle': {'onPlay': [lambda card: gear("bounce")]},
	'Whisking Whirlwind': {'onPlay': [lambda card: addDelayedEffect({'card':card, "effects":[lambda card, args: untapCreatureAll(False)]}, None)]},
	'White Knight Spark': {'onPlay': [lambda card: tapCreature(1,True)]},
	'Wizard Resurrection': {'onPlay': [lambda card: mana(me.Deck), lambda card: fromMana(1,"Spell")]},
	'XENOM, the Reaper Fortress': {'onPlay': [lambda card: targetDiscard(True)]},
	'Zombie Carnival': {'onPlay': [lambda card: declareRace(card), lambda card: search(me.piles["Graveyard"], 3, "Creature")]},
	'Zombie Cyclone': {'onPlay': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},

	# ON DESTROY EFFECTS

	'Akashic First, Electro-Dragon': {'onDestroy': [lambda card: toHand(card)]},
	'Akashic Second, Electro-Spirit': {'onPlay': [lambda card: draw(me.Deck, True)],
									'onDestroy': [lambda card: toMana(card)]},
	'Aless, the Oracle': {'onDestroy': [lambda card: toShields(card)]},
	'Aqua Agent': {'onDestroy': [lambda card: toHand(card)]},
	'Aqua Knight': {'onDestroy': [lambda card: toHand(card)]},
	'Aqua Ranger': {'onDestroy': [lambda card: toHand(card)]},
	'Aqua Skydiver': {'onDestroy': [lambda card: toHand(card)]},
	'Aqua Soldier': {'onDestroy': [lambda card: toHand(card)]},
	'Aqua Warrior': {'onDestroy': [lambda card: draw(me.Deck, True, 2)]},
	'Asylum, Elemental Dragon Knight': {'onDestroy': [lambda card: toShields(card)]},
	'Balloonshroom Q': {'onDestroy': [lambda card: toMana(card)]},
	'Bat Doctor, Shadow of Undeath': {'onDestroy': [lambda card: search(me.piles["Graveyard"], 1, "Creature")]},
	'Bombersaur': {'onDestroy': [lambda card: bothPlayersFromMana(2,True, exactCount=True)]},
	'Bone Piercer': {'onDestroy': [lambda card: fromMana(1, "Creature")]},
	'Bruiser Dragon': {'onDestroy': [lambda card: burnShieldKill(1,True)]},
	'Cetibols': {'onDestroy': [lambda card: draw(me.Deck, True)]},
	'Chilias, the Oracle': {'onDestroy': [lambda card: toHand(card)]},
	'Coiling Vines': {'onDestroy': [lambda card: toMana(card)]},
	'Crasher Burn': {'onDestroy': [lambda card: kill(3000)]},
	'Crystal Jouster': {'onDestroy': [lambda card: toHand(card)]},
	'Cubela, the Oracle': {'onDestroy': [lambda card: tapCreature()]},
	'Death Monarch, Lord of Demons': {'onDestroy': [lambda card: summonFromGrave(len([c for c in me.piles["Graveyard"] if not re.search("Evolution",c.type)]),"Creature", "ALL", "Demon Command")]},
	'Dracodance Totem': {'onDestroy': [lambda card: dracodanceTotem(card)]},
	'Engineer Kipo': {'onDestroy': [lambda card: bothPlayersFromMana(1,True)]},
	'Fly Lab, Crafty Demonic Tree': {'onDestroy': [lambda card: targetDiscard(True)]},
	'Gigagrax': {'onDestroy': [lambda card: kill()]},
	'Gigastand': {'onDestroy': [lambda card: returnAndDiscard(card)]},
	'Glider Man': {'onDestroy': [lambda card: targetDiscard()]},
	'Hammerhead Cluster': {'onDestroy': [lambda card: bounce()]},
	'Jewel Spider': {'onDestroy': [lambda card: bounceShield()]},
	'Jil Warka, Time Guardian': {'onDestroy': [lambda card: tapCreature(2)]},
	'Kalute, Vizier of Eternity': {'onDestroy': [lambda card: toHand(card) if any(c for c in getCreatures(me) if c.properties["Name"]==card.properties["Name"]) else None]},
	'Mighty Shouter': {'onDestroy': [lambda card: toMana(card)]},
	'Ouks, Vizier of Restoration': {'onDestroy': [lambda card: toShields(card)]},
	'Peace Lupia': {'onDestroy': [lambda card: tapCreature()]},
	'Peru Pere, Viral Guardian': {'onDestroy': [lambda card: toHand(card)]},
	'Pharzi, the Oracle': {'onDestroy': [lambda card: search(me.piles["Graveyard"], 1, "Spell")]},
	'Dream Pirate, Shadow of Theft': {'onDestroy': [lambda card: returnAndDiscard(card)]},
	'Propeller Mutant': {'onDestroy': [lambda card: targetDiscard(True)]},
	'Proxion, the Oracle': {'onDestroy': [lambda card: toHand(card)]},
	'Raza Vega, Thunder Guardian': {'onDestroy': [lambda card: toShields(card)]},
	'Ryudmila, Channeler of Suns': {'onDestroy': [lambda card: toDeck(card), lambda card: shuffle(me.Deck)]},
	'Schuka, Duke of Amnesia': {'onDestroy': [lambda card: discardAll(onlySelf=True), lambda card: discardAll()]},
	'Shaman Broccoli': {'onDestroy': [lambda card: toMana(card)]},
	'Shout Corn': {'onDestroy': [lambda card: toMana(card)]},
	'Sinister General Damudo': {'onDestroy': [lambda card: destroyAll(getCreatures(), True, 3000)]},
	'Solid Horn': {'onDestroy': [lambda card: toMana(card)]},
	'Stallob, the Lifequasher': {'onDestroy': [lambda card: destroyAll(getCreatures(), True)]},
	'Jasper, the Stubborn': {'onDestroy': [lambda card: toHand(card)]},
	'Red-Eye Scorpion': {'onDestroy': [lambda card: toMana(card)]},
	'Revival Soldier': {'onDestroy': [lambda card: waveStriker(lambda card: toHand(card), card)]},
	'Worm Gowarski, Masked Insect': {'onDestroy': [lambda card: targetDiscard(True)]},

	#ON REMOVE FROM BATTLE ZONE
	'Aura Pegasus, Avatar of Life': {'onAttack': [lambda card: auraPegasus()], 'onLeaveBZ': [lambda card: auraPegasus()]},
	'Cruel Naga, Avatar of Fate': {'onLeaveBZ': [lambda card: destroyAll(getCreatures(), True)]},
	'Death Phoenix, Avatar of Doom': {'onButton': [lambda card: burnShieldKill(2)], 'onLeaveBZ': [lambda card: discardAll()]},
	'Eternal Phoenix, Dragonflame Phoenix': {'onLeaveBZ': [lambda card: eternalPhoenix()]},
	'Wise Starnoid, Avatar of Hope': {'onAttack': [lambda card: shields(me.deck)], 'onLeaveBZ': [lambda card: shields(me.deck)]},

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
	'Adomis, the Oracle': {'onTap': [lambda card: peekShield(1)]},
	'Aeropica': {'onTap': [lambda card: bounce()]},
	'Aqua Fencer': {'onTap': [lambda card: opponentManaToHand()]},
	'Bliss Totem, Avatar of Luck': {'onTap': [lambda card: fromGraveyardToMana(3)]},
	'Brood Shell': {'onTap': [lambda card: fromMana(TypeFilter="Creature")]},
	'Charmilia, the Enticer': {'onTap': [lambda card: search(me.Deck, TypeFilter="Creature")]},
	'Chen Treg, Vizier of Blades': {'onTap': [lambda card: tapCreature()]},
	'Cosmogold, Spectral Knight': {'onTap': [lambda card: fromMana(1, "Spell")]},
	'Crath Lade, Merciless King': {'onTap': [lambda card: targetDiscard(randomDiscard=True, count=2)]},
	'Deklowaz, the Terminator': {'onTap': [lambda card: destroyAll(getCreatures(), True, 3000), lambda card: deklowazDiscard()]},
	'Gandar, Seeker of Explosions': {'onTap': [lambda card: addDelayedEffect({"card":card, "effects": [lambda card, args: untapCreatureAll(False, 're.search("Light",c.Civilization)')]}, None)]},
	'Gigio\'s Hammer': {'onTap': [lambda card: declareRace(card)]},
	'Grim Soul, Shadow of Reversal': {'onTap': [lambda card: search(me.piles["Graveyard"],1,"Creature","Darkness")]},
	'Kachua, Keeper of the Icegate': {'onTap': [lambda card: fromDeckToField(me.Deck, 1,'re.search("Creature",c.Type) and re.search(r"Dragon\\b", c.Race, re.I)', {"card":card, "effects":[lambda card, args: destroy(*args) if isCreature(*args) and not isRemovedFromPlay(*args) else None]})]},
	'Heavyweight Dragon': {'onTap': [lambda card: heavyweightDragon(card)]},
	'Hokira': {'onTap': [lambda card: declareRace(card)]},
	'Kipo\'s Contraption': {'onTap': [lambda card: kill(2000)]},
	'Mummy Wrap, Shadow of Fatigue': {'onTap': [lambda card: randomDiscard(me.Hand, remote=True), lambda card: targetDiscard(True)]},
	'Neon Cluster': {'onTap': [lambda card: draw(me.Deck,False,2)]},
	'Popple, Flowerpetal Dancer': {'onTap': [lambda card: mana(me.Deck)]},
	'Rikabu\'s Screwdriver': {'onTap': [lambda card: kill(count=1, rulesFilter="{BLOCKER}")]},
	'Rondobil, the Explorer': {'onTap': [lambda card: sendToShields(1, False, True)]},
	'Silvermoon Trailblazer': {'onTap': [lambda card: declareRace(card)]},
	'Sky Crusher, the Agitator': {'onTap': [lambda card: bothPlayersFromMana(toGrave=True)]},
	'Tanzanyte, the Awakener': {'onTap': [lambda card: tanzanyte()]},
	'Tank Mutant': {'onTap': [lambda card: opponentSacrifice()]},
	'Techno Totem': {'onTap': [lambda card: tapCreature()]},
	'Tra Rion, Penumbra Guardian': {'onTap': [lambda card: addDelayedEffect({'card':card, "effects":[lambda card, args: untapCreatureAll(False, 're.search("{}", c.Race)'.format(*args))]}, declareRace(card, returnRace=True))]},
	'Venom Worm': {'onTap': [lambda card: declareRace(card)]},

	#ON ALLY TAP EFFECTS (Effects that give their on Tap Effect to other creatures)
	#########IMPORTANT DIFFERENCE vvvvvvvvvvvv ################
	# Pass an array like this one: [['Condition Function to filter who gets the effect',['ACTUAL EFFECT]]]
	# 'c' is the variable of card to check with condition before allowing the Tap Effect.
	#########IMPORTANT DIFFERENCE ^^^^^^^^^^^^ ################

	'Arc Bine, the Astounding': {'onAllyTap': [['re.search("Light", c.Civilization)', [lambda card:tapCreature()]]]},
	'Fort Megacluster': {'onAllyTap': [['re.search("Water", c.Civilization)', [lambda card: draw(me.Deck)]]]},
	'Living Citadel Vosh': {'onAllyTap': [['re.search("Nature", c.Civilization)', [lambda card: mana(me.Deck)]]]},
	'Phantasmal Horror Gigazald': {'onAllyTap': [['re.search("Darkness", c.Civilization)', [lambda card: targetDiscard(True)]]]},

	#ON YOUR TURN END EFFECTS

	'Aqua Officer': {'onTurnEnd': [lambda card: tapCreature(2, onlyOwn=True)], 'onTurnStart': [lambda card: draw(me.Deck, True, 2)]},
	'Balesk Baj, the Timeburner': {'onTurnEnd': [lambda card: toHand(card)]},
	'Ballus, Dogfight Enforcer Q': {'onTurnEnd': [lambda card: untapCreature(card, False)]},
	'Bazagazeal Dragon': {'onTurnEnd': [lambda card: toHand(card)]},
	'Betrale, the Explorer': {'onTurnEnd': [lambda card: untapCreature(card, True)]},
	'Cutthroat Skyterror': {'onTurnEnd': [lambda card: toHand(card)]},
	'Comet Eye, the Spectral Spud': {'onTurnEnd': [lambda card: ([untapCreature(c) for c in getCreatures(me) if re.search(r"Wild Veggie|Rainbow Phantom",c.Race)], False)[1]]},
	'Frei, Vizier of Air': {'onTurnEnd': [lambda card: untapCreature(card)]},
	'Gnarvash, Merchant of Blood': {'onTurnEnd': [lambda card: lonely(card)]},
	'Hazard Hopper': {'onTurnEnd': [lambda card: toHand(card) if isTapped(card) and askYN("Did Hazard Hopper broke any shields this turn?")==1 else None]},
	'Hearty Cap\'n Polligon': {'onTurnEnd': [lambda card: toHand(card) if isTapped(card) and askYN("Did Hearty Cap'n Polligon broke any shields this turn?")==1 else None]},
	'Laveil, Seeker of Catastrophe': {'onTurnEnd': [lambda card: untapCreature(card)]},
	'Lone Tear, Shadow of Solitude': {'onTurnEnd': {lambda card: lonely(card)}},
	'Lukia Lex, Pinnacle Guardian': {'onTurnEnd': [lambda card: untapCreature(card, True)]},
	'Nial, Vizier of Dexterity': {'onTurnEnd': [lambda card: untapCreature(card)]},
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
	'Bulgluf, the Spydroid': {'silentSkill': [lambda card: shields(me.deck)]},
	'Charge Whipper': {'silentSkill': [lambda card: shieldswap(card, 1)]},
	'Flohdani, the Spydroid': {'silentSkill': [lambda card: tapCreature(2)]},
	'Gazer Eyes, Shadow of Secrets': {'silentSkill': [lambda card: targetDiscard()]},
	'Gigamente': {'silentSkill': [lambda card: search(me.piles["Graveyard"], TypeFilter="Creature")]},
	'Hustle Berry': {'silentSkill': [lambda card: mana(me.Deck)]},
	'Kaemira, the Oracle': {'silentSkill': [lambda card: shields(me.deck)]},
	'Milporo': {'silentSkill': [lambda card: draw(me.Deck)]},
	'Minelord Skyterror': {'silentSkill': [lambda card: destroyAll(getCreatures(), True, 3000)]},
	'Pinpoint Lunatron': {'silentSkill': [lambda card: pinpointLunatron()]},
	'Soderlight, the Cold Blade': {'silentSkill': [lambda card: opponentSacrifice()]},
	'Sporeblast Erengi': {'silentSkill': [lambda card: search(me.Deck, 1, "Creature")]},
	'Vorg\'s Engine': {'silentSkill': [lambda card: destroyAll(getCreatures(), True, 2000)]},

	#ON ATTACK EFFECTS
	'Amber Piercer': {'onAttack': [lambda card: search(me.piles["Graveyard"], TypeFilter="Creature")]},
	'Armored Warrior Quelos': {'onAttack': [lambda card: bothPlayersFromMana(1,True,"not re.search(r'Fire',c.Civilization)")]},
	'Aqua Grappler': {'onAttack': [lambda card: draw(me.Deck,True,len([c for c in getCreatures(me) if c!=card and isTapped(c)]))]},
	'Bloodwing Mantis': {'onAttack': [lambda card: fromMana(2,"Creature", exactCount=True)]},
	'Bolzard Dragon': {'onAttack': [lambda card: destroyMana()]},
	'Cavern Raider': {'onAttack': [lambda card: search(me.Deck, 1, "Creature")]},
	'Chaos Fish': {'onAttack': [lambda card: draw(group=me.Deck,count=len([c for c in getCreatures(me) if re.search("Water", c.Civilization) and c._id!=card._id]),ask=True)]},
	'Curious Eye': {'onAttack': [lambda card: peekShield(1, True)]},
	'Cyclolink, Spectral Knight': {'onAttack': [lambda card: search(me.Deck, 1, "Spell")]},
	'Daidalos, General of Fury': {'onAttack': [lambda card: kill(targetOwn=True)]},
	'Dark Titan Maginn': {'onAttack': [lambda card: targetDiscard(True)]},
	'Earthstomp Giant': {'onAttack': [lambda card: fromManaAll("re.search(r'Creature',c.Type)")]},
	'Flametropus': {'onAttack': [lambda card: fromMana(toGrave=True,ask=True)]},
	'Gamil, Knight of Hatred': {'onAttack': [lambda card: search(me.piles["Graveyard"], CivFilter="Darkness")]},
	'General Dark Fiend': {'onAttack': [lambda card: burnShieldKill(1,True)]},
	'Geoshine, Spectral Knight': {'onAttack': [lambda card: tapCreature(includeOwn=True, filterFunction='re.search(r"Fire|Darkness",c.Civilization)')]},
	'Headlong Giant': {'onAttack': [lambda card: selfDiscard()]},
	'Horrid Worm': {'onAttack': [lambda card: targetDiscard(True)]},
	'Hypersquid Walter': {'onAttack': [lambda card: draw(me.Deck, True)]},
	'King Neptas': {'onAttack': [lambda card: bounce(1,filterFunction="c.Power!='Infinity' and int(c.Power.strip('+'))<=2000")]},
	'King Ponitas': {'onAttack': [lambda card: search(me.Deck, CivFilter="Water")]},
	'Lalicious': {'onAttack': [lambda card: lookAtOpponentHand(),lambda card: lookAtCards(opponent=True) ]},
	'Laguna, Lightning Enforcer': {'onAttack': [lambda card: search(me.Deck, TypeFilter="Spell")]},
	'Le Quist, the Oracle': {'onAttack': [lambda card: tapCreature(1,filterFunction='re.search(r"Fire|Darkness",c.Civilization)')]},
	'Melcap, the Mutant Explorer': {'onAttack': [lambda card: tapCreature(1, True)]},
	'Metalwing Skyterror': {'onAttack': [lambda card: kill(rulesFilter="{BLOCKER}")]},
	'Muramasa, Duke of Blades': {'onAttack': [lambda card: kill(2000)]},
	'Necrodragon Galbazeek': {'onAttack': [lambda card: burnShieldKill(1,True)]},
	'Plasma Chaser': {'onAttack': [lambda card: draw(me.Deck, ask=True, count=len(getCreatures(getTargetPlayer(onlyOpponent=True))))]},
	'Psyshroom': {'onAttack': [lambda card: fromGraveyardToMana(filterFunction="re.search(r'Nature',c.Civilization)",ask=True)]},
	'Ra Vu, Seeker of Lightning': {'onAttack': [lambda card: search(me.piles["Graveyard"], 1, "Spell","Light")]},
	'Sabermask Scarab': {'onAttack': [lambda card: fromMana()]},
	'Shock Trooper Mykee': {'onAttack': [lambda card: kill(3000)]},
	'Silver Axe': {'onAttack': [lambda card: mana(me.Deck,ask=True)]},
	'Skullsweeper Q': {'onAttack': [lambda card: opponentToDiscard()]},
	'Smile Angler': {'onAttack': [lambda card: opponentManaToHand()]},
	'Sniper Mosquito': {'onAttack': [lambda card: fromMana()]},
	'Stained Glass': {'onAttack': [lambda card: bounce(opponentOnly=True, filterFunction='re.search(r"Fire|Nature",c.Civilization)')]},
	'Steam Rumbler Kain': {'onAttack': [lambda card: burnShieldKill(1, True)]},
	'Stinger Ball': {'onAttack': [lambda card: peekShield(1, True)]},
	'Split-Head Hydroturtle Q': {'onAttack': [lambda card: draw(me.Deck,True)]},
	'Supernova Jupiter King Empire': {'onAttack': [lambda card: meteorburn([lambda card, baitList: toPlay(baitList[0])],card, 1, 1)]},
	'Tentacle Cluster': {'onAttack': [lambda card: bounce()]},
	'Tick Tick, Swift Viral Swordfighter': {'onAttack': [lambda card: draw(me.Deck)]},
	'Trixo, Wicked Doll': {'onAttack': [lambda card: opponentSacrifice()]},
	'Quakesaur': {'onAttack': [lambda card: oppponentFromMana(toGrave=True)]},
	'Windmill Mutant': {'onAttack': [lambda card: targetDiscard(True)]},
	'Wyn, the Oracle': {'onAttack': [lambda card: peekShield(1,True)]},
	'Überdragon Bajula': {'onAttack': [lambda card: destroyMana(2)]},

	# ON SHIELD TRIGGER CHECKS - condtion for a card to be shield trigger(functions used here should ALWAYS return a boolean)
	'"Boyan", Fireball Spell': {'onTrigger': [lambda card: civilCount("Fire")],
						'onPlay': [lambda card: kill(5000)]},
	'"Dogoru", Ground Spell': {'onTrigger': [lambda card: civilCount("Nature")],
						'onPlay': [lambda card: sendToMana()]},
	'"Frizzen", Freezing Spell': {'onTrigger': [lambda card: civilCount("Water")]},
	'"Pikabim", Prison Spell': {'onTrigger': [lambda card: civilCount("Light")],
						'onPlay': [lambda card: sendToShields(1, True, False, False, False, 're.search(r"Creature|Tamaseed", c.Type) and cardCostComparator(c,5,"<=",r"Creature|Tamaseed")')]},
	'Awesome! Hot Spring Gallows': {'onTrigger': [lambda card: manaArmsCheck("Water", 3)]},
	'Awesome! Onsen Gallows': {'onTrigger': [lambda card: manaArmsCheck("Water", 3)]},
	'Chopin, Dragon King': {'onTrigger': [lambda card: len([c for c in getElements(me) if re.search(r"\bDragon\b",c.Type)])]},
	'Dogiragon, Royal Revolution': {'onTrigger': [lambda card: revolution(card,2,True)]},
	'Dokeidaimos <Grave Star>': {'onTrigger': [lambda card: len(getTamaseeds(me))]},
	'Dotou Henge <Sturm Ogre>': {'onTrigger': [lambda card: len(getTamaseeds(me))]},
	'Fleece, Satori\'s Whirlwind': {'onTrigger': [lambda card: len([c for c in getCreatures(me) if re.search('Colorless',c.Civilization)])]},
	'Guerrillafugan, Beast Army X': {'onTrigger': [lambda card: len(getMana(me))>=6],
								  'onPlay': [lambda card: tapThis(card, True)],
								  'onDestroy': [lambda card: summonFromMana(CivFilter='Nature',filterFunction='cardCostComparator(c,6,"<=","Creature")')]},
	'Hunbolt, Demonic Elemental': {'onTrigger': [lambda card: any(count>1 for count in {name: names.count(name) for names in [[c.properties["Name"] for c in getCreatures(getTargetPlayer(onlyOpponent=True))]] for name in names}.values())]},
	'Hyperspatial Basara Hole': {'onTrigger': [lambda card: len([c for c in getElements(me) if re.search(r"Darkness|Fire",c.Civilization) and re.search("Command",c.Race)])]},
	'Just in You': {'onTrigger': [lambda card: civilCount("Darkness")],
					'onPlay': [lambda card: mill(me.Deck, 4), lambda card: summonFromGrave(RaceFilter="Abyss", filterFunction='cardCostComparator(c,4,"<=","Creature")')]},
	'Mettagils, Passion Dragon': {'onTrigger': [lambda card: manaArmsCheck("Fire", 5)]},
	'Mysterious Ogre Duel': {'onTrigger': [lambda card: len([c for c in getElements(me) if re.search("Human", c.Race)])],
							'onPlay': [lambda card: mysteriousOgreDuel(card)]},
	'Nova! Belunare': {'onTrigger': [lambda card: manaArmsCheck("Light", 5)]},
	'Oracion, Mysterious Samurai': {'onTrigger': [lambda card: len(getCastles(me))]},
	'Perfect Alcadeia': {'onTrigger': [lambda card: revolution(card, 2, True)],
						'onPlay': [lambda card: mode(
						[lambda card: lookAtTopCards(2, count=2, revealAll=True, filterFunction='re.search(r"Light|Water",c.Civilization)'),
						lambda card: shields(me.deck),
						lambda card: sendToShields(1, True, True, False, False, 'cardCostComparator(c, 3, "<=")')], card,
						["Reveal the top 2 cards of your deck. Put all Light and Water cards from among them into your hand, and put the rest on the bottom of your deck in any order.",
		  				"Shieldify the top card of your deck.",
						"Choose an element that costs 3 or less and shieldify it."], False, 2)]},
	'Perfect Coldflame': {'onTrigger': [lambda card: len([c for c in me.Graveyard if re.search("Spell",c.Type)])>=2]},
	'Perfect Freestyle': {'onTrigger': [lambda card: len([c for c in getCreatures(getTargetPlayer(onlyOpponent=True)) if cardCostComparator(c,len(getMana(getTargetPlayer(onlyOpponent=True))),'>', "Creature")])]},
	'Perfect Oratoriocles': {'onTrigger': [lambda card: askYN("Did you put a creature this turn to treat {} as a Shield Trigger?".format(card.properties["Name"]))==1]},
	'Polaris, Goldkind': {'onTrigger': [lambda card: len([c for c in getMana(me) if re.search(r"Light|Nature",c.Civilization)])>=7]},
	'Prison Spark': {'onTrigger': [lambda card: len(c for c in getElements(me) if re.search('Light',c.Civilization) and re.search('Demon Command',c.Race))],
				  	'onPlay': [lambda card: tapCreature(1, True)]},
	'Pure Zaru': {'onTrigger': [lambda card: len(getGears(me))]},
	'Rain, Accurate Reaper': {'onTrigger': [lambda card: askYN("♫Is the music playing?♫")==1]},
	'Reef, Revolution Captain': {'onTrigger': [lambda card: len([c for c in getCreatures(me) if re.search("Water",c.Civilization)])]},
	'Sg Spagelia, Dragment Symbol': {'onTrigger': [lambda card: manaArmsCheck("Water", 5)]},
	'Soul Garde, Storage Dragon Elemental': {'onTrigger': [lambda card: manaArmsCheck("Light", 5)]},
	'Star Paladin <Kolon Star>': {'onTrigger': [lambda card: len(getTamaseeds(me))]},
	'Tamatango Panzer': {'onTrigger': [lambda card: len(c for c in getMana(c) if re.search('Creature', c.type) and (c.Power=='Infinite' or int(c.Power.strip('+'))>=12000))>=5]},
	'Traptops, Green Trap Toxickind': {'onTrigger': [lambda card: manaArmsCheck("Nature", 5)]},
	'Zanjides, Tragedy Demon Dragon': {'onTrigger': [lambda card: manaArmsCheck("Darkness", 5)]},

	# Untargettable Cards
	'Petrova, Channeler of Suns': {'untargettable':True,
							   'onPlay': [lambda card: declareRace(card, "Mecha Del Sol")]},
	'Warlord Ailzonius': {'untargettable':True},
	'Yuliana, Channeler of Suns': {'untargettable':True},

	# On Button (Manual trigger effects) - for cards that require a lot of automation to detect the trigger,
	# so manual it is for now.
	'Auzesu, Demonic Elemental': {'onButton': [lambda card: kill(tapFilter='TAP')]},
	'Bluum Erkis, Flare Guardian': {'onButton': [lambda card: bluumErkis(card)]},
	'Bolmeteus Steel Dragon': {'onButton': [lambda card: burnShieldKill(2)]},
	'Evil Incarnate': {'onButton': [lambda card: remoteCall(getActivePlayer(), 'sacrifice', []) if getActivePlayer() is not None else None]},
	'Gachack, Mechanical Doll': {'onButton': [lambda card: kill(targetOwn=True)]},
	'Gigaclaws': {'onButton': [lambda card: discardAll()]},
	'Gigavrand': {'onButton': [lambda card: discardAll()]},
	'Ice Vapor, Shadow of Anguish': {'onButton': [lambda card: opponentToDiscard(), lambda card: oppponentFromMana(toGrave=True)]},
	'Joe\'s Toolkit': {'onButton': [lambda card: kill(2000)]},
	'Pocopen, Counterattacking Faerie': {'onButton': [lambda card: oppponentFromMana(toGrave=True)]},
	'Rieille, the Oracle': {'onButton': [lambda card: tapCreature()]},
	'Scream Slicer, Shadow of Fear': {'onButton': [lambda card: bronks()]},
	'Slaphappy Soldier Galback': {'onButton': [lambda card: kill(4000)]},
	'Solar Grass': {'onButton': [lambda card: untapCreatureAll(False, 'not re.search("Solar Grass",c.properties["Name"])')]},
	'Super Dragon Machine Dolzark': {'onButton': [lambda card: sendToMana(1, filterFunction="c.Power!='Infinity' and int(c.Power.strip('+'))<=5000")]},
	'Turtle Horn, the Imposing': {'onButton': [lambda card: search(me.Deck, 1, "Creature")]},
	'Thrumiss, Zephyr Guardian': {'onButton': [lambda card: tapCreature()]},
	'Vikorakys': {'onButton': [lambda card: search(me.Deck, 1, "ALL", "ALL", "ALL", False)]},
	'Zero Nemesis, Shadow of Panic': {'onButton': [lambda card: targetDiscard(True)]}
}

######### Events ##################
def endTurn(args, x=0, y=0):
	mute()
	clearWaitingFuncts()
	nextPlayer=args.player
	if nextPlayer==None or "":
		# normally passed without green button
		currentPlayers=getPlayers()
		if len(currentPlayers)>1:
			nextPlayer=currentPlayers[1]
		else:
			nextPlayer=me
	if turnNumber()>0:
		if nextPlayer==me and len(getPlayers())>1:
			whisper("You shall not pass the turn to yourself!")
		elif getActivePlayer()!=me:
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
	if not getAutomationsSetting(): notify('{} has " My Card Script Automation" setting disabled.'.format(me))
	if getAskBeforeDiscardingOwnCardsSetting(): notify('{} has "Ask before discarding Cards from my Hand" setting enabled.'.format(me))
	if not getWelcomePageSetting():
		showWelcomeMessage()
	for player in getPlayers():
		if player!=me:
			initiate_handshake(player)

def onTarget(args): #this is triggered by OCTGN events when any card is targeted or untargeted. Used to continue evaluating functions that are waiting for target
	numberOfTargets=len([c for c in table if c.targetedBy==me])
	if numberOfTargets==0:
		return
	if waitingFunct:
		evaluateWaitingFunctions()

def onArrow(args):
	player=args.player
	fromCard=args.fromCard
	toCard=args.toCard
	targeted=args.targeted
	scripted=args.scripted
	global arrow
	if targeted:
		if fromCard._id in arrow:
			if toCard._id not in arrow[fromCard._id]:
				arrow[fromCard._id].append(toCard._id)
		else:
			arrow[fromCard._id]=[toCard._id]
	else:
		if fromCard._id in arrow:
				del arrow[fromCard._id]

def clearArrowOnMove(args):
	global arrow
	if not arrow or table not in args.fromGroups:
		return
	cardsMoved=args.cards
	arrowKeysToRemove=[]
	for card in cardsMoved:
		if card._id in arrow:
			arrowKeysToRemove.append(card._id)
		for targetterId, targets in arrow.items():
			if card._id in targets:
				card.arrow(Card(targetterId),False)
				targets.remove(card._id)
			if not targets:
				arrowKeysToRemove.append(targetterId)
	for key in arrowKeysToRemove:
		del arrow[key]
		Card(key).target(False)

######### Network Related functions #########
def getPlayerById(playerId):
	for player in players:
		if player._id==playerId:
			return player
	return None

def findCardByIdAndGroup(cardId, playerId, groupName):
	# Check if we need to search in the global table
	if groupName=="Table":
		# Search in the shared table pile
		for card in table:
			if card._id==cardId:
				return card
	else:
		# Retrieve the specific player by controller ID and search in their group
		controller=getPlayerById(playerId)  # Assume getPlayerById retrieves a player by their ID
		if controller:
			pile=controller.piles.get(groupName)
			if pile:
				for card in pile:
					if card._id==cardId:
						return card
	return None

def retrieveCardsFromData(cardDataList):
	cards=[]
	for cardData in cardDataList:
		card=findCardByIdAndGroup(cardData["id"], cardData["playerId"], cardData["groupName"])
		if card:
			cards.append(card)
	return cards
#Handles both a single Card object and a list
def ensureCardObjects(cardInput, keepAsList=False):
	if not isinstance(cardInput, list):
		cardInput=[cardInput]
	if all(isinstance(card, Card) for card in cardInput):
		cards=cardInput
	elif all(isinstance(card, dict) and "id" in card for card in cardInput):
		cards=retrieveCardsFromData(cardInput)
	if keepAsList:
		return cards
	return cards[0] if len(cards)==1 else cards

def findGroupByNameAndPlayer(groupName, playerId):
	if groupName=="Table":
		return table

	player=getPlayerById(playerId)
	return player.piles[groupName]

def ensureGroupObject(group):
	if isinstance(group, Group):
		return group
	if isinstance(group, list):
		return ensureCardObjects(group, True)
	if isinstance(group, dict):
		return findGroupByNameAndPlayer(group['name'], group['playerId'])

## IMPORTANT: Send this object instead of Card/CardList for remoteCall!
def convertCardListIntoCardIDsList(cardList):
	if not isinstance(cardList,list):
		cardList=[cardList]
	return [{"id": card._id,"playerId": card.controller._id,"groupName": card.group.name} for card in cardList]
## IMPORTANT: Send this object instead of Group for remoteCall!
def convertGroupIntoGroupNameList(group):
	return {"name":group.name, "playerId":group.player._id if group.player else None}

############################################ Misc utility functions ####################################################################################

def askCard2(list, title="Select a card", buttonText="Select", minimumToTake=1, maximumToTake=1, returnAsArray=False, noSorting=False):  # askCard function was changed. So using the same name but with the new functionalit
#this is for showing a dialog box with the cards in the incoming list. Careful, all cards will be visible, even if they're facedown.
	#this handles displaying big cards in reverse order than normal cards.
	bigCards=[c for c in list if c.size in {"tall", "square"}]
	if bigCards:
		normalCards=[c for c in list if c.size in {"Default", "wide"}]
		if normalCards:
			reverseCardList(bigCards)
			if me.isInverted:
				list=normalCards + bigCards
			else:
				list=bigCards + normalCards
		else:
			reverseCardList(list)

	dlg=cardDlg(list)
	dlg.title=title

	if minimumToTake==0 and not returnAsArray:
		# if this dialog is opened without any card to take, that means it's for rearranging cards.
		dlg.min, dlg.max=0, 0
		dlg.text="← Closer to the top | Closer to the bottom → (drag to rearrange):"
		dlg.show()
		return dlg.list
	else:
		dlg.min, dlg.max=minimumToTake, maximumToTake
		result=dlg.show()

	if minimumToTake==0 and maximumToTake==0 and returnAsArray:
		return dlg.list
	if result is None:
		return None
	if len(result)==1 and not returnAsArray:
		return result[0]
	else:
		return result

def askYN(text="Proceed?", choices=["Yes", "No"], colorsList=['#FF0000', '#FF0000', '#FF0000']):
	# this asks a simple Y N question, but Yes or No can be replaced by other words. Returns 1 if yes, 2 for No and 0 if the box is closed

	choice=askChoice(text, choices, colorsList)
	return choice

def askNumber(text="Enter a Number", defaultAnswer=1000, alwaysReturnNumber=False):
	choice=askInteger(text, defaultAnswer)
	if not choice and alwaysReturnNumber:
		return 0
	return choice

def getTargetPlayer(text="Pick a player:", onlyOpponent=False):
		playerList=[]
		currentPlayers=getPlayers()
		for player in currentPlayers:
			playerList.append(player.name)
		if onlyOpponent and len(playerList)==2:
			return currentPlayers[1]
		choicePlayer=askChoice(text, playerList)
		if choicePlayer < 1: return
		return currentPlayers[choicePlayer - 1]

def removeBaits(card, evolveDict=None):
	if evolveDict==None:
		evolveDict=eval(me.getGlobalVariable("evolution"), allowed_globals)
	# Will remove passed card from the list of tracked evos/baits
	# returns a list of bait cards if evo was removed
	# returns empty list if not found or bait was removed
	modified=False
	resultList=[]
	for evo in evolveDict.keys():
		if evo==card._id:
			for cardID in evolveDict[evo]:
				resultList.append(Card(cardID))
			del evolveDict[evo]
			modified=True
			# notify("Evo removed from evo in dict")
			break
		baitList=evolveDict[evo]
		if card._id in baitList:
			baitList.remove(card._id)
			modified=True
			evolveDict[evo]=baitList
			# notify("Bait removed from evo in dict")
			break
	if modified:
		me.setGlobalVariable("evolution", str(evolveDict))
	return resultList

def antiDiscard(card, sourcePlayer):
	# sourcePlayer=the player trying play the discarding effect, not the target player
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
	if alreadyEvaluating:
		return
	alreadyEvaluating=True
	while len(waitingFunct)>0:
			if not getAutomationsSetting():
				del waitingFunct[0]
				continue
			card=waitingFunct[0][0]
			#notify("{}, {}".format(card,waitingFunct[0][1]))
			if waitingFunct[0][1](card):
				waitForTarget()
				break #stop evaluating further functions, will start again when target is triggered
			else:
				#notify("DEBUG: card, function deQueued: {}".format(waitingFunct[0]))
				cardBeingPlayed=waitingFunct[0][0]
				del waitingFunct[0] #deQueue
				if len(waitingFunct)==0:
					endOfFunctionality(cardBeingPlayed)
				elif cardBeingPlayed!=waitingFunct[0][0]: #the next card is a different one
					endOfFunctionality(cardBeingPlayed)
				#notify("DEBUG: Waiting list is now: {}".format(str(waitingFunct)))
	alreadyEvaluating=False

def clearWaitingFuncts():  # clears any pending plays for a card that's waiting to choose targets etc
	if waitingFunct:
		for funct in waitingFunct:
			cardBeingPlayed=waitingFunct[0][0]
			del waitingFunct[0]
			notify("Waiting for target/effect for {} cancelled.".format(cardBeingPlayed))
			if cardBeingPlayed and isSpellInBZ(cardBeingPlayed):
				endOfFunctionality(cardBeingPlayed)
	global alreadyEvaluating, evaluateNextFunction
	alreadyEvaluating=False
	evaluateNextFunction=True #this should always be True, unless you're waiting for the next function to evaluate

def orderEvaluatingFunctions():
	global alreadyEvaluating, waitingFunct
	if not getDialogSimultaneousCardEffectsSetting():
		return
	if waitingFunct:
		waitingFunctions=list(waitingFunct)
		effectAlreadyProcessing=None
		if alreadyEvaluating and waitingFunctions:
			effectAlreadyProcessing=waitingFunctions.pop(0)

		cardList=[]
		for card, _ in waitingFunctions:
			if card not in cardList:
				cardList.append(card)
		if len(cardList)>1:
			if me.isInverted: reverseCardList(cardList)
			cardOrder=askCard2(cardList,'Choose the order of effects to activate (from left to right)', minimumToTake=0, maximumToTake=0, returnAsArray=True)
			if not cardOrder: return
			cardOrderMap={card: index for index, card in enumerate(cardOrder)}
			waitingFunctions=sorted(waitingFunctions, key=lambda x: cardOrderMap.get(x[0]))
			if(effectAlreadyProcessing):
				waitingFunctions.insert(0, effectAlreadyProcessing)
			waitingFunct=waitingFunctions

def manaArmsCheck(civ='ALL5', num=0):
	manaCards=getMana(me)
	if civ=='ALL5':  # check if you have all 5 civs in mana zone
		civList=['Light', 'Water', 'Darkness', 'Fire', 'Nature']
		flags=[False] * 5  # one flag for each corresponding civ [False, False, False, False, False]
		for card in manaCards:
			for i in range(0, 5):
				if not flags[i] and re.search(civList[i], card.Civilization):
					flags[i]=True
			if flags[0] and flags[1] and flags[2] and flags[3] and flags[4]:
				return True
		return False
	else:
		manaCards=[card for card in manaCards if re.search(civ, card.Civilization)]
		if len(manaCards) >= num:
			return True

def sort_cardList(cards, sortCiv=True, sortCost=True, sortName=True):
	def _civilization_rank(card_civilization):
		civilization_order={
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

	sorted_list=sorted(cards,key=lambda card: (
		(_civilization_rank(card.Civilization) if sortCiv else float('inf')),
		(card.Cost if sortCost else float('inf')),
		(card.properties["Name"] if sortName else float('inf'))
		))
	return sorted_list

def reverseCardList(list):
	list.reverse()
	return list

def updateBaits(card, targets, evolveDict=None):
	if isCreature(card):
		if any(c.orientation==Rot90 for c in targets):
			card.orientation=Rot90
		for c in targets:
			c.orientation=card.orientation
	targetList=[c._id for c in targets]
	if evolveDict==None:
		evolveDict=eval(me.getGlobalVariable("evolution"), allowed_globals)  ##evolveDict tracks all cards 'underneath' the evolution creature
	for evolveTarget in targets:  ##check to see if the evolution targets are also evolution creatures
		if evolveTarget._id in evolveDict:  ##if the card already has its own cards underneath it
			if evolveTarget in table:
				targetList += evolveDict[evolveTarget._id]  ##add those cards to the new evolution creature
			del evolveDict[evolveTarget._id]
	evolveDict[card._id]=targetList
	me.setGlobalVariable("evolution", str(evolveDict))

def processExLife(card):
	group=me.Deck
	isExLife=re.search("{Ex Life}",card.Rules,re.IGNORECASE)
	isExtraExLife=re.search("Extra Ex Life",card.Rules,re.IGNORECASE)
	if len(group)==0 or (not isExLife and not isExtraExLife): return
	shieldCount=int(me.getGlobalVariable("shieldCount")) + 1
	if isExLife or (isExtraExLife and len(group)==1):
		card.properties["Rules"]='(Ex Life - Shield #{})\n{}'.format(shieldCount, card.properties["Rules"])
		toShields(group[0], notifymute=True)
		notify("{} sets top card of {} as Shield for Ex Life of {}.".format(me, group.name, card))
	elif isExtraExLife:
		card.properties["Rules"]='(Extra Ex Life - Shield #{} and #{})\n{}'.format(shieldCount,shieldCount+1, card.properties["Rules"])
		toShields(group[0], notifymute=True)
		toShields(group[0], notifymute=True)
		notify("{} sets top 2 cards of {} as Shields for Extra Ex Life of {}.".format(me, group.name, card))

#Useful to handle Twinpacts
def cardCostComparator(card, value, comparisonOperator='==', typeFilter="ALL"):
	comparisons={
		'==': operator.eq,
		'!=': operator.ne,
		'<': operator.lt,
		'<=': operator.le,
		'>': operator.gt,
		'>=': operator.ge
	}

	# If the card is a Twinpact (has both Cost1 and Cost2)
	if card.hasProperty("Cost1") and card.hasProperty("Cost2") and card not in table:
		if card.Cost1!="Infinity":
			cost1=int(card.Cost1)
		else:
			cost1=float('inf')
		if card.Cost2!="Infinity":
			cost2=int(card.Cost2)
		else:
			cost2=float('inf')

		if typeFilter=="ALL":
			return (card.Cost1 and comparisons[comparisonOperator](cost1, value)) or (card.Cost2 and comparisons[comparisonOperator](cost2, value))

		else:
			if re.search(typeFilter,card.Type1) and card.Cost1 and comparisons[comparisonOperator](cost1, value):
				return True
			if re.search(typeFilter,card.Type2) and card.Cost2 and comparisons[comparisonOperator](cost2, value):
				return True

	# If it's not a Twinpact card, just compare the single cost
	elif card.hasProperty("Cost"):
		if card.Cost!='Infinity':
			cost=int(card.Cost)
		else:
			cost=float('inf')
		if typeFilter=="ALL":
			return card.Cost and comparisons[comparisonOperator](cost, value)

		if re.search(typeFilter,card.Type) and card.Cost and comparisons[comparisonOperator](cost, value):
			return True

	return False

################ Quick card attribute checks ####################

def isCreature(card):
	if card.isFaceUp and not isShield(card) and not card.orientation in {Rot180, Rot270} and re.search("Creature", card.Type) and card in table:
		return True
	#by default python functions will return None, which is more or less the same as False

def isElement(card):
	if card.isFaceUp and not isShield(card) and not card.orientation in {Rot180, Rot270} and card in table and not re.search(r"Spell|Cell|Castle|Core|Ceremony|Nebula|Rule Plus|Land", card.Type, re.IGNORECASE):
		return True

def isSpellInBZ(card):
	if not isShield(card) and not isMana(card) and re.search("Spell", card.Type) and card in table:
		return True

def isGod(card):
	if isCreature(card) and re.search("God", card.Race):
		return True

def isGear(card):
	if isElement(card) and re.search("Cross Gear", card.Type):
		return True

def isCastle(card):
	if not isMana(card) and not isShield(card) and re.search("Castle", card.Type) and not re.search("Dragheart", card.Type):
		return True

def isMana(card):
	if not isShield(card) and not card.orientation in {Rot0, Rot90} and card in table:
		return True

def isShield(card):
	if card.markers[shieldMarker]>0 and card in table:
		return True

def isPsychic(card):
	if re.search(r"Psychic|Dragheart", card.Type):
		return True

def isGacharange(card):
	if re.search("Gacharange", card.Type):
		return True

def isTapped(card):
	if not isMana(card):
		return card.orientation==Rot90
	else:
		if card.size=='wide' and card.isFaceUp:
			return card.orientation==Rot180
		else:
			return card.orientation==Rot270

#We pass evolveDict if possible to minimize the amount of calls if doing loops
def isBait(card, evolveDict=None):  # check if card is under and evo(needs to be ignored by most things) This is (probably)inefficient, maybe make a func to get all baits once
	if evolveDict==None:
		evolveDict=eval(card.owner.getGlobalVariable("evolution"), allowed_globals)
	for evo in evolveDict.keys():
		baitList=evolveDict[evo]
		if card._id in baitList:
			return True

#We pass evolveDict if possible to minimize the amount of calls if doing loops
def removeFromBaits(card, evolveDict=None):
	if evolveDict==None:
		evolveDict=eval(me.getGlobalVariable("evolution"), allowed_globals)
	modified=False
	for evo in evolveDict.keys():
		baitList=evolveDict[evo]
		if card._id in baitList:
			baitList.remove(card._id)
			modified=True
		if len(baitList)==0:
			del evolveDict[evo]
			modified=True
		else:
			evolveDict[evo]=baitList
	if modified:
		me.setGlobalVariable("evolution", str(evolveDict))

#We pass sealDict if possible to minimize the amount of calls if doing loops
def isSealed(card, sealDict=None):
	if sealDict==None:
		sealDict=eval(card.owner.getGlobalVariable("seal"), allowed_globals)
	if card._id in sealDict:
		return True

#We pass sealDict if possible to minimize the amount of calls if doing loops
def isSeal(card, sealDict=None):
	if sealDict==None:
		sealDict=eval(card.owner.getGlobalVariable("seal"), allowed_globals)
	for seal in sealDict.keys():
		sealList=sealDict[seal]
		if card._id in sealList:
			return True

#We pass sealDict if possible to minimize the amount of calls if doing loops
def getSeals(card, sealDict=None):
	if sealDict==None:
		sealDict=eval(card.owner.getGlobalVariable("seal"), allowed_globals)
	if card._id in sealDict:
		return [Card(cardId) for cardId in sealDict[card._id]]
	return []

#We pass sealDict if possible to minimize the amount of calls if doing loops
def isSealedOrSeal(card, sealDict=None):
	if sealDict==None:
		sealDict=eval(card.owner.getGlobalVariable("seal"), allowed_globals)
	return isSeal(card, sealDict) or isSealed(card, sealDict)

#We pass evolveDict and sealDict if possible to minimize the amount of calls if doing loops
def isRemovedFromPlay(card, evolveDict=None, sealDict=None):
	if evolveDict==None or sealDict==None:
		(evolveDict, sealDict)=getEvolveDictAndSealDict(card)
	return isBait(card, evolveDict) or isSealedOrSeal(card, sealDict)

#Function that returns ours or card.owners Evolve and SealDicts (used to optimize the amount of calls to getGlobalVariable and evals if doing loops)
def getEvolveDictAndSealDict(card=None):
	if card==None:
		return (eval(me.getGlobalVariable("evolution"), allowed_globals), eval(me.getGlobalVariable("seal"), allowed_globals))
	return (eval(card.owner.getGlobalVariable("evolution"), allowed_globals), eval(card.owner.getGlobalVariable("seal"), allowed_globals))

#Generic List functions from table
def getCreatures(player=None, evolveDict=None, sealDict=None):
	if player==None:
		return [c for c in table if isCreature(c) and not isRemovedFromPlay(c, evolveDict, sealDict)]
	return [c for c in table if c.controller==player and isCreature(c) and not isRemovedFromPlay(c, evolveDict, sealDict)]

def getShields(player=None, evolveDict=None, sealDict=None):
	if player==None:
		return [c for c in table if isShield(c) and not isRemovedFromPlay(c, evolveDict, sealDict)]
	return [c for c in table if c.controller==player and isShield(c) and not isRemovedFromPlay(c, evolveDict, sealDict)]

def getMana(player=None, evolveDict=None, sealDict=None):
	if player==None:
		return [c for c in table if isMana(c) and not isRemovedFromPlay(c, evolveDict, sealDict)]
	return [c for c in table if c.controller==player and isMana(c) and not isRemovedFromPlay(c, evolveDict, sealDict)]

def getElements(player=None, evolveDict=None, sealDict=None):
	if player==None:
		return [c for c in table if isElement(c) and not isRemovedFromPlay(c, evolveDict, sealDict)]
	return [c for c in table if c.controller==player and isElement(c) and not isRemovedFromPlay(c, evolveDict, sealDict)]

def getTamaseeds(player=None, evolveDict=None, sealDict=None):
	if player==None:
		return [c for c in table if isElement(c) and not isRemovedFromPlay(c) and re.search("Tamaseed",c.Type)]
	return [c for c in table if c.controller==player and isElement(c) and not isRemovedFromPlay(c, evolveDict, sealDict) and re.search("Tamaseed",c.Type)]

def getGears(player=None, evolveDict=None, sealDict=None):
	if player==None:
		return [c for c in table if isGear(c) and not isRemovedFromPlay(c)]
	return [c for c in table if c.controller==player and isGear(c) and not isRemovedFromPlay(c, evolveDict, sealDict)]

def getCastles(player=None):
	if player==None:
		return [c for c in table if isCastle(c)]
	return [c for c in table if c.controller==me and isCastle(c)]

#Get a list of bait materials under Evo
def getCardBaits(card, evolveDict=None):
	if evolveDict==None:
		evolveDict=eval(card.owner.getGlobalVariable("evolution"), allowed_globals)
	if card._id in evolveDict:
		return [Card(cardId) for cardId in evolveDict[card._id]]
	return []

def isEvo(cards, x=0, y=0):
	if not isinstance(cards, list):
		cards=[cards]
	if len(cards)==0: return False
	c=cards[len(cards)-1]
	if c and re.search("Evolution", c.Type) and isElement(c) and not isRemovedFromPlay(c):
		return True
	return False

def hasButtonEffect(cards, x=0, y=0):
	if not isinstance(cards, list):
		cards=[cards]
	if len(cards)==0: return False
	c=cards[len(cards)-1]
	if c and cardScripts.get(c.properties["Name"], {}).get('onButton') and (isElement(c) and not isRemovedFromPlay(c) or c in me.Graveyard):
		return True
	return False

def getHasButtonEffect(cards, x=0, y=0):
	if not isinstance(cards, list):
		cards=[cards]
	if len(cards)==0: return ''
	c=cards[len(cards)-1]
	return '■ Trigger {} Effect'.format(c.properties["Name"])

def isUntargettable(card):
	if card in table and card.owner!=me and cardScripts.get(card.properties["Name"], {}).get('untargettable', False):
		return True

def metamorph():
	cardList=getMana(me)
	if len(cardList) >= 7:
		return True

def revolution(card, number, shieldTrigger=False):
	shieldList=[c for c in getShields(me) if c!=card and me in c.peekers]
	return len(shieldList)<=number or (shieldTrigger and askYN("Do you have {} or less shields to treat {} as a Shield Trigger?".format(number,card.properties["Name"]))==1)

def getWaveStrikerCount(player='ALL'):
	cardList=[]
	if player!='ALL':
		cardList=[card for card in getCreatures(player) if re.search('wave striker', card.Rules, re.IGNORECASE)]
	else:
		cardList=[card for card in getCreatures() if re.search('wave striker', card.Rules, re.IGNORECASE)]
	return len(cardList)

def getSurvivorsOnYourTable(searchForEffects=True, evolveDict=None, sealDict=None):
	if evolveDict==None or sealDict==None:
		(evolveDict, sealDict)=getEvolveDictAndSealDict()
	if searchForEffects:
		return [card for card in getCreatures(me, evolveDict, sealDict) if re.search('\{SURVIVOR\}', card.Rules)]
	else:
		return [card for card in getCreatures(me, evolveDict, sealDict) if re.search('Survivor', card.Race)]

def civilCount(civilization="ALL", count=2):
	creaturesAndTamaseeds=getCreatures(me)+getTamaseeds(me)
	if civilization=="ALL":
		return len(creaturesAndTamaseeds)>=count
	return len([c for c in creaturesAndTamaseeds if re.search(civilization,c.Civilization)])>=count

################ Functions used in the Automation dictionaries.####################

def summonFromGrave(count=1, TypeFilter="ALL", CivFilter="ALL", RaceFilter="ALL",noEvo=True, filterFunction='True'):  # Temporary Fix for not allowing Evolutions
	mute()
	if TypeFilter!="ALL" and noEvo:
		cardsInGroup_Type_Filtered=[card for card in me.piles["Graveyard"] if
									  re.search(TypeFilter, card.Type) and not re.search("Evolution", card.type)]
	else:
		cardsInGroup_Type_Filtered=[card for card in me.piles["Graveyard"]]
	if CivFilter!="ALL":
		cardsInGroup_CivandType_Filtered=[card for card in cardsInGroup_Type_Filtered if
											re.search(CivFilter, card.properties['Civilization'])]
	else:
		cardsInGroup_CivandType_Filtered=cardsInGroup_Type_Filtered
	if RaceFilter!="ALL":
		cardsInGroup_CivTypeandRace_Filtered=[card for card in cardsInGroup_CivandType_Filtered if
												re.search(RaceFilter, card.properties['Race'])]
	else:
		cardsInGroup_CivTypeandRace_Filtered=cardsInGroup_CivandType_Filtered
	if filterFunction!='True':
		cardsInGroup_CivTypeandRace_Filtered=[c for c in cardsInGroup_CivTypeandRace_Filtered if eval(filterFunction, allowed_globals, {'c': c})]
	if len(cardsInGroup_CivTypeandRace_Filtered)==0: return
	count=min(count, len(cardsInGroup_CivTypeandRace_Filtered))
	choices=askCard2(cardsInGroup_CivTypeandRace_Filtered, 'Choose {} Creature(s) to Summon from the Graveyard'.format(count),
					  'Graveyard', maximumToTake=count, returnAsArray=True)
	if not isinstance(choices, list): return
	for choice in choices:
		toPlay(choice)

def summonFromMana(count=1, TypeFilter="ALL", CivFilter="ALL", RaceFilter="ALL",noEvo=True, filterFunction='True'):
	mute()
	if TypeFilter!="ALL" and noEvo:
		cardsInGroup_Type_Filtered=[card for card in getMana(me) if re.search(TypeFilter, card.Type) and not re.search("Evolution", card.type)]
	else:
		cardsInGroup_Type_Filtered=getMana(me)
	if CivFilter!="ALL":
		cardsInGroup_CivandType_Filtered=[card for card in cardsInGroup_Type_Filtered if re.search(CivFilter, card.properties['Civilization'])]
	else:
		cardsInGroup_CivandType_Filtered=cardsInGroup_Type_Filtered
	if RaceFilter!="ALL":
		cardsInGroup_CivTypeandRace_Filtered=[card for card in cardsInGroup_CivandType_Filtered if re.search(RaceFilter, card.properties['Race'])]
	else:
		cardsInGroup_CivTypeandRace_Filtered=cardsInGroup_CivandType_Filtered
	if filterFunction!='True':
		cardsInGroup_CivTypeandRace_Filtered=[c for c in cardsInGroup_CivTypeandRace_Filtered if eval(filterFunction, allowed_globals, {'c': c})]
	if len(cardsInGroup_CivTypeandRace_Filtered)==0: return
	count=min(count, len(cardsInGroup_CivTypeandRace_Filtered))
	choices=askCard2(cardsInGroup_CivTypeandRace_Filtered, 'Choose {} Creature(s) to Summon from Mana Zone'.format(count),
					  'Mana', maximumToTake=count, returnAsArray=True)
	if not isinstance(choices, list): return
	for choice in choices:
		toPlay(choice)

def drama(shuffle=True, type='creature', targetZone='battlezone', failZone='mana', conditional=True):
	# drama=getting creatures from top of deck for free, eg. Mystery Cube, Balga Raiser, Hogan Blaster
	mute()
	if shuffle:
		me.Deck.shuffle()
		notify("{} shuffles their Deck.".format(me))
	card=me.Deck.top()
	card.isFaceUp=True
	notify("Top Card is {}".format(card))
	played=False  # Flag for resolving after shuffle, unused rn
	if type=='creature':
		success=re.search("Creature", card.Type)
	elif type=='creature or spell':
		success=re.search(r"Creature|Spell", card.Type)
	if success:
		if conditional:
			choice=askYN("Put {} into {}?\n\n {}".format(card.properties["Name"], targetZone, card.Rules))
			# more conditions for non-bz to be added?
			if choice==1:
				toPlay(card)
				played=True
				return
			elif choice==0: #player closes the window
				failzone='backOnTop'
		else:
			toPlay(card)
			played=True
			return
	if failZone=='mana':
		toMana(card)
	elif failZone=='hand':
		toHand(card)
	else:
		notify("{} puts {} back on top of Deck".format(me, card))
		card.isFaceUp=False

def lookAtTopCards(num, cardType='card', targetZone='hand', remainingZone='bottom', reveal=True, specialaction='NONE', specialaction_civs=[], count=1, revealAll=False, filterFunction='True', toManaFaceDown=False, toManaTapped=False):
	mute()
	notify("{} looks at the top {} Cards of their Deck".format(me, num))
	cardList=[card for card in me.Deck.top(num)]
	if revealAll:
		for c in cardList:
			c.isFaceUp=True
		notify("{} reveals: ".format(me) + ", ".join('{} '.format(c) for c in cardList))
		for c in cardList:
			c.isFaceUp=False
	count=min(count, len(cardList))
	choices=[]
	if count>0:
		choices=askCard2(cardList, 'Choose up to {} Card(s) to put into {}'.format(count, targetZone), minimumToTake=0, maximumToTake=count, returnAsArray=True)
		cards_for_special_action=[]
		if isinstance(choices, list):
			if filterFunction!='True':
				choices=[c for c in choices if eval(filterFunction,allowed_globals, {'c': c})]
			for choice in choices:
				if not 'NONE' in specialaction:
					cards_for_special_action.append(choice)
				if cardType=='card' or re.search(cardType, choice.Type):
					# use switch instead, when more zones are added here
					if targetZone=='mana':
						toMana(choice, faceDown=toManaFaceDown, tapped=toManaTapped)
					else:
						# to hand is default rn
						toHand(choice, show=reveal)
				else:
					notify("Please select a {}! Action cancelled.".format(cardType))
					return
		else:
			notify("Nothing selected! Action cancelled.")
			return
	cardList=[card for card in me.Deck.top(num-len(choices))]
	if len(cardList)>1 and remainingZone=='bottom':
		cardList=askCard2(cardList, 'Rearrange the remaining Cards to put to {}'.format(remainingZone), 'OK', 0, 0)
	for card in cardList:
		if remainingZone=='mana':
			toMana(card)
		elif remainingZone=='grave':
			toDiscard(card)
		else:
			card.resetProperties()
			card.moveToBottom(me.Deck)
			notify("{} moved a Card to the bottom of their Deck.".format(me))
	if specialaction=="BOUNCE":
		if not any(re.search(civs, card.properties['Civilization']) for civs in specialaction_civs for card in cards_for_special_action):
			global evaluateNextFunction
			evaluateNextFunction=False

#Random discard or look at hand and select discard FOR OPPONENT, also setting cards as shield from hand for some reason?!
#TODO:Split discarding and setting shield
def targetDiscard(randomDiscard=False, targetZone='grave', count=1):
	mute()
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	if randomDiscard:
		remoteCall(targetPlayer, 'randomDiscard', [convertGroupIntoGroupNameList(targetPlayer.hand), 0, 0, True, count])
		return
	cardList=[card for card in targetPlayer.hand]
	#Both players see the opponent's hand reversed
	reverseCardList(cardList)
	count=min(count, len(cardList))
	if len(cardList)==count:
		cardChoices=cardList
	else:
		cardChoices=askCard2(cardList, "Choose {} Card(s) to discard.".format(count),minimumToTake=count, maximumToTake=count, returnAsArray=True)
	if not isinstance(cardChoices,list):
		notify("Discard cancelled.")
		return
	if targetZone=='grave':
		remoteCall(targetPlayer, 'toDiscard', [convertCardListIntoCardIDsList(cardChoices), 0, 0, False, True, True, False, True])
		return
	for cardChoice in cardChoices:
		if targetZone=='mana':
			whisper("Putting {} as Mana.".format(cardChoice))
			remoteCall(targetPlayer, 'toMana', convertCardListIntoCardIDsList(cardChoice))
		if targetZone=='shield':
			whisper("Setting {} as Shield.".format(cardChoice))
			remoteCall(targetPlayer, 'toShields', convertCardListIntoCardIDsList(cardChoice))

def lookAtOpponentHand():
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	cardList=[card for card in targetPlayer.hand]
	#Both players see their opponent's hand reversed
	reverseCardList(cardList)
	notify("{} looks at {}'s Hand.".format(me,targetPlayer))
	askCard2(cardList, "Opponent's Hand. (Close to continue)", minimumToTake=0)

#Look at selected player's hand and discard all cards matching filterFunction
def lookAtHandAndDiscardAll(filterFunction='True'):
	mute()
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	cardList=[c for c in targetPlayer.hand]
	#Both players see their opponent's hand reversed
	reverseCardList(cardList)
	askCard2(cardList, "Opponent's Hand. (Close to continue)", minimumToTake=0)
	if filterFunction!="True":
		choices=[c for c in cardList if eval(filterFunction, allowed_globals, {'c': c})]
	else:
		choices=cardList
	remoteCall(targetPlayer, 'toDiscard', [convertCardListIntoCardIDsList(choices), 0, 0, False, True, True, False, True])

def discardAll(onlyOpponent=True, onlySelf=False):
	mute()
	cardList=[]
	targetPlayer=me
	if onlySelf==False: targetPlayer=getTargetPlayer(onlyOpponent=onlyOpponent)
	if not targetPlayer: return
	cardList=[card for card in targetPlayer.hand]
	remoteCall(targetPlayer, 'toDiscard', [convertCardListIntoCardIDsList(cardList), 0, 0, False, True, True, False, onlyOpponent])

# do some anti-discard inside dat randomdisc function

#Move a card from Mana to hand/graveyard
def fromMana(count=1, TypeFilter="ALL", CivFilter="ALL", RaceFilter="ALL", show=True, toGrave=False, filterFunction='True', ask=False, exactCount=False):
	mute()
	if ask:
			choice=askYN("Would you like to remove {} Card(s) from Mana?".format(count))
			if choice!=1: return
	if TypeFilter!="ALL":
		cardsInGroup_Type_Filtered=[card for card in getMana(me) if re.search(TypeFilter, card.Type)]
	else:
		cardsInGroup_Type_Filtered=getMana(me)
	if CivFilter!="ALL":
		cardsInGroup_CivandType_Filtered=[card for card in cardsInGroup_Type_Filtered if
											re.search(CivFilter, card.properties['Civilization'])]
	else:
		cardsInGroup_CivandType_Filtered=cardsInGroup_Type_Filtered
	if RaceFilter!="ALL":
		cardsInGroup_CivTypeandRace_Filtered=[card for card in cardsInGroup_CivandType_Filtered if
												re.search(RaceFilter, card.properties['Race'])]
	else:
		cardsInGroup_CivTypeandRace_Filtered=cardsInGroup_CivandType_Filtered
	if filterFunction!="True":
		cardsInGroup_CivTypeRaceandFunction_Filtered=[c for c in cardsInGroup_CivTypeandRace_Filtered if eval(filterFunction, allowed_globals, {'c': c})]
	else:
		cardsInGroup_CivTypeRaceandFunction_Filtered=cardsInGroup_CivTypeandRace_Filtered

	if len(cardsInGroup_CivTypeRaceandFunction_Filtered)==0: return
	if me.isInverted: reverseCardList(cardsInGroup_CivTypeRaceandFunction_Filtered)
	count=min(count, len(cardsInGroup_CivTypeRaceandFunction_Filtered))
	minimumToTake=1
	if exactCount:
		minimumToTake=count
	if count==0: return
	choices=askCard2(cardsInGroup_CivTypeRaceandFunction_Filtered, 'Choose {} Card(s) from the Mana Zone'.format(count),"Select", minimumToTake, count, True)
	if not isinstance(choices,list): return
	for choice in choices:
		if toGrave==True:
			destroy(choice)
		else:
			toHand(choice,show)

#move all cards fulfilling the condition from Mana to hand
def fromManaAll(filterFunction='True'):
	if filterFunction!='True':
		manaCards=[c for c in getMana(me) if eval(filterFunction, allowed_globals, {'c': c})]
	else:
		manaCards=getMana(c)
	if len(manaCards)==0: return
	for c in manaCards:
		toHand(c)

def killAndSearch(play=False, singleSearch=False):
	# looks like this is only used for Transmogrify
	mute()
	cardList=[c for c in getCreatures() if not isUntargettable(c)]
	if len(cardList)==0: return
	if me.isInverted: reverseCardList(cardList)
	choice=askCard2(cardList, 'Choose a Creature to destroy')
	if type(choice) is not Card: return
	remoteCall(choice.owner, 'destroy', convertCardListIntoCardIDsList(choice))
	if singleSearch:
		return
	else:
		remoteCall(choice.owner, 'loopThroughDeck', [choice.owner._id, play])

def revealFromDeckAndAddToHand(count=1, filterFunction='True'):
	mute()
	cardList=[card for card in me.Deck.top(count)]
	notify("{} reveals the top {} Cards of their deck:".format(me, count))
	for c in cardList:
		c.isFaceUp=True
		notify("{} reveals {}".format(me, c))
	for c in cardList:
		if filterFunction=='True' or eval(filterFunction, allowed_globals, {'c':c}):
			toHand(c)
		else:
			toDiscard(c)

def loopThroughDeck(playerId, play=False):
	mute()
	player=getPlayerById(playerId)
	group=player.Deck
	if len(group)==0: return
	newCard=group[0]
	newCard.isFaceUp=True
	notify("{} reveals {}".format(player, newCard))

	if re.search("Creature", newCard.Type) and not re.search("Evolution Creature", newCard.Type):
		if play==True:
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
	cardList=getCreatures(me)
	cardList=[card for card in cardList if not re.search("Psychic", card.Type)]
	if len(cardList)==0: return
	if me.isInverted: reverseCardList(cardList)
	choice=askCard2(cardList, 'Choose a Creature to destroy')
	if type(choice) is not Card: return
	originalCost=int(choice.Cost)
	found=False
	destroy(choice)
	notify("Looking for a Creature with cost {}...".format(originalCost + 1))

	for card in me.Deck:
		card=me.Deck[0]
		card.isFaceUp=True
		cost=int(card.Cost)
		notify("{} reveals {}".format(me, card))

		if cardCostComparator(card,originalCost+1,"==","Creature"):
			if re.search("Creature", card.Type):
				if not re.search("Evo", card.Type):
					if ask:
						yn=askYN("Put {} into the battle zone?\n\n {}".format(card.properties["Name"], card.Rules))
						if yn==1:
							found=True
							toPlay(card, ignoreEffects=True)
							choice=card
					##add card to resolve list
					break
				else:
					if ask:
						yn=askYN("Put {} into the battle zone?\n\n {}".format(card.properties["Name"], card.Rules))
						if yn==1:
							found=True
							toPlay(card, ignoreEffects=True)
							choice=card
							##add card to resolve list
							card.moveToTable(0, 0)
							align()
					break
		card.resetProperties()
		card.moveToBottom(me.Deck)
	for card in me.Deck:
		if card.isFaceUp:
			card.isFaceUp=False
	me.Deck.shuffle()
	notify("{} shuffles their Deck.".format(me))
	if found:
		## Temporary fix without a proper resolve list
		toPlay(choice, notifymute=True)
	else:
		notify("No Card with cost {} found or action cancelled.".format(originalCost + 1))

def search(group, count=1, TypeFilter="ALL", CivFilter="ALL", RaceFilter="ALL", show=True, x=0, y=0, filterFunction='True'):
	mute()
	group=ensureGroupObject(group)
	if len(group)==0: return
	maximumToTake=min(count,len(group))
	if maximumToTake<=0: return
	dialogText='Search {} '.format(maximumToTake) + '{}(s) to take to hand'
	cardsInGroup=[card for card in group]
	if TypeFilter!="ALL":
		cardsInGroup_Type_Filtered=[card for card in group if re.search(TypeFilter, card.Type)]
		dialogText=dialogText.format(TypeFilter)
	else:
		cardsInGroup_Type_Filtered=[card for card in group]
	if CivFilter!="ALL":
		cardsInGroup_CivandType_Filtered=[card for card in cardsInGroup_Type_Filtered if
											re.search(CivFilter, card.properties['Civilization'])]
	else:
		cardsInGroup_CivandType_Filtered=cardsInGroup_Type_Filtered
	if RaceFilter!="ALL":
		cardsInGroup_CivTypeandRace_Filtered=[card for card in cardsInGroup_CivandType_Filtered if
												re.search(RaceFilter, card.properties['Race'])]
		dialogText=dialogText.format(RaceFilter)
	else:
		cardsInGroup_CivTypeandRace_Filtered=cardsInGroup_CivandType_Filtered
	if filterFunction!='True':
		filteredCardsInGroup=[c for c in cardsInGroup_CivTypeandRace_Filtered if eval(filterFunction, allowed_globals, {'c':c})]
	else:
		filteredCardsInGroup=cardsInGroup_CivTypeandRace_Filtered
	dialogText=dialogText.format('Card')
	while(True):
		choices=askCard2(sort_cardList(cardsInGroup), dialogText,maximumToTake=maximumToTake,returnAsArray=True)
		if not isinstance(choices,list):
			group.shuffle()
			notify("{} finishes searching their {}".format(me, group.name))
			return
		if all(c in filteredCardsInGroup for c in choices):
			for choice in choices:
				toHand(choice, show)
			break
	group.shuffle()
	notify("{} finishes searching their {}".format(me, group.name))

#Pick a card from any Player's Deck and send it to Graveyard
def fromDeckToGrave(count=1, onlyOpponent=False):
	mute()
	group=[]
	targetPlayer=getTargetPlayer(onlyOpponent=onlyOpponent)
	if not targetPlayer: return
	group=targetPlayer.deck
	if len(group)==0: return
	count=min(count,len(group))
	cardsInGroup=sort_cardList([card for card in group])
	choices=askCard2(cardsInGroup, 'Search {} Card(s) to put to Graveyard'.format(count), maximumToTake=count, returnAsArray=True)
	if not isinstance(choices,list):
		remoteCall(targetPlayer,'shuffle',convertGroupIntoGroupNameList(group))
		notify("{} finishes searching {}'s {} and shuffles the Deck.".format(me, targetPlayer, group.name))
		return
	remoteCall(targetPlayer,'toDiscard',convertCardListIntoCardIDsList(choices))
	update()

	remoteCall(targetPlayer,'shuffle', convertGroupIntoGroupNameList(group))
	update()
	notify("{} finishes searching {}'s {} and shuffles the Deck.".format(me, targetPlayer, group.name))

#Pick a card from your deck and place it into Mana.
def fromDeckToMana(count=1, filterFunction='True'):
	mute()
	group=me.deck
	if len(group)==0: return
	count=min(count,len(group))
	cardsInGroup=sort_cardList([card for card in group])
	validChoices=[c for c in cardsInGroup if filterFunction=='True' or eval(filterFunction, allowed_globals, {'c': c})]
	while (True):
		choices=askCard2(cardsInGroup, 'Search {} Card(s) to put to Mana'.format(count), maximumToTake=count, returnAsArray=True)
		if not isinstance(choices, list):
			shuffle(group)
			notify("{} finishes searching their {} and shuffles the Deck.".format(me, group.name))
			return
		if all(elem in validChoices for elem in choices):
			for choice in choices:
				toMana(choice)
			break
	shuffle(group)
	notify("{} finishes searching their {} and shuffles the Deck.".format(me, group.name))

#Target creatures, if they match the filter, they get destroyed.
def kill(powerFilter='ALL', tapFilter='ALL', civFilter='ALL', count=1, targetOwn=False, rulesFilter='ALL', filterFunction='True'):
	mute()
	if targetOwn:
		cardList=[c for c in getCreatures() if (powerFilter=='ALL' or c.Power!='Infinity' and int(c.Power.strip('+')) <= powerFilter) and not isUntargettable(c)]
	else:
		cardList=[c for c in getCreatures() if c.owner!=me if (powerFilter=='ALL' or c.Power!='Infinity' and int(c.Power.strip('+')) <= powerFilter) and not isUntargettable(c)]
	if tapFilter!='ALL':
		if tapFilter=='Untap':
			cardList=[c for c in cardList if c.orientation==Rot0]
		if tapFilter=='Tap':
			cardList=[c for c in cardList if c.orientation==Rot90]
	if civFilter!="ALL":
		cardList=[c for c in cardList if re.search(civFilter, c.Civilization)]
	if rulesFilter!='ALL':
		cardList=[c for c in cardList if re.search(rulesFilter, c.Rules)]
	if filterFunction!='True':
		cardList=[c for c in cardList if eval(filterFunction, allowed_globals, {'c': c})]
	if len(cardList)==0:
		whisper("No valid targets on the table.")
		return

	count=min(count, len(cardList))
	if count==0:
		whisper("No valid targets.")
		return
	targets=[c for c in cardList if c.targetedBy==me]
	if len(targets)!=count:
		whisper("Wrong number of targets!")
		return True  # return true activates the cardStack/waiting for targets mechanism

	destroyAll(targets)

#Mass Destruction handling, call this instead of destroy() if you are destroying more than 1 Creature at once.
def destroyAll(group, condition=False, powerFilter='ALL', civFilter="ALL", AllExceptFiltered=False, exactPower=False, dontAsk=False):
	mute()
	group=ensureGroupObject(group)
	clear(group)
	cardlist=[]
	if condition==True:
		if civFilter=="ALL":
			cardList=[c for c in group if isCreature(c) and (powerFilter=='ALL' or c.Power!="Infinity" and int(c.Power.strip('+'))==powerFilter if exactPower else int(c.Power.strip('+')) <= powerFilter)]
		else:
			if AllExceptFiltered:
				cardList=[c for c in group if isCreature(c) and (powerFilter=='ALL' or c.Power!="Infinity" and int(c.Power.strip('+'))==powerFilter if exactPower else int(c.Power.strip('+')) <= powerFilter)
						and not re.search(civFilter, c.properties['Civilization'])]
			else:
				cardList=[c for c in group if isCreature(c) and (powerFilter=='ALL' or c.Power!="Infinity" and int(c.Power.strip('+'))==powerFilter if exactPower else int(c.Power.strip('+')) <= powerFilter)
						and re.search(civFilter, c.properties['Civilization'])]
	else:
		cardList=group

	if len(cardList)==0:
		return

	if not dontAsk and condition:
		if askYN('Destroy automatically?')!=1: return
	global wscount
	if not wscount:
		wscount=getWaveStrikerCount()

	# We do this to handle survivor/wavestriker effects properly.
	(evolveDict, sealDict)=getEvolveDictAndSealDict()
	myCardList=[card for card in cardList if card.owner==me and not isRemovedFromPlay(card, evolveDict, sealDict)]
	opponentList=[card for card in cardList if card.owner!=me]

	survivors=[]
	if any(re.search("Survivor", card.Race) for card in myCardList):
		survivors=getSurvivorsOnYourTable(True, evolveDict, sealDict)

	for c in myCardList:
		cardToBeSaved=c
		possibleSavers=[card for card in getCreatures(me) if
		cardToBeSaved!=card and re.search(r"(?<!Shield )Saver",card.rules, re.IGNORECASE)]
		if len(possibleSavers)>0:
			if confirm("Prevent {}'s destruction by using a Saver on your side of the field?\n\n".format(
					cardToBeSaved.properties["Name"])):
				if me.isInverted: reverseCardList(possibleSavers)
				choice=askCard2(possibleSavers, 'Choose Saver to destroy')
				if type(choice) is Card:
					toDiscard(choice)
					cardList.remove(choice)
					cardList=[card for card in cardList]
					notify("{} destroys {} to prevent {}'s destruction.".format(me, choice.properties["Name"], cardToBeSaved.properties["Name"]))
					continue

		toDiscard(cardToBeSaved)
		c=cardToBeSaved  # fix for onDestroy effect, as toDiscard somehow changes card

		functionList=[]
		if cardScripts.get(c.properties["Name"], {}).get('onDestroy'):
			#notify('DEBUG: Added {} to {}'.format(cardScripts.get(card.properties["Name"]).get('onDestroy'), card.Name))
			functionList=list(cardScripts.get(c.properties["Name"]).get('onDestroy', []))
		if re.search("Survivor", c.Race):
			for surv in survivors:
				if surv!=c and cardScripts.get(surv.properties["Name"], {}).get('onDestroy'):
					#notify('DEBUG: Added {} to {}'.format(cardScripts.get(surv.properties["Name"]).get('onDestroy'), card.Name))
					functionList.extend(cardScripts.get(surv.properties["Name"]).get('onDestroy', []))
		for function in functionList:
			waitingFunct.append([c, function])
	orderEvaluatingFunctions()
	evaluateWaitingFunctions()
	if len(opponentList):
		remoteCall(opponentList[0].owner, "destroyAll", [convertCardListIntoCardIDsList(opponentList), False])

def destroyMana(count=1):
	mute()
	cardList=getMana(getTargetPlayer(onlyOpponent=True))
	count=min(count,len(cardList))
	if count==0:
		return
	if me.isInverted: reverseCardList(cardList)
	choices=askCard2(cardList, 'Choose {} Mana Card(s) to destroy'.format(count), maximumToTake=count, returnAsArray=True)
	if not isinstance(choices,list): return
	for choice in choices:
		remoteCall(choice.owner, "destroy", convertCardListIntoCardIDsList(choice))

def destroyAllMana(group, civFilter="ALL", AllExceptFiltered=False):
	mute()
	group=ensureGroupObject(group)
	cardList=[]
	if(civFilter!="ALL"):
			cardList=[card for card in group if isMana(card) and (bool(re.search(civFilter, card.Civilization))!=AllExceptFiltered)]
	else:
		cardList=[card for card in group if isMana(card)]
	if len(cardList)==0: return
	for card in cardList:
		remoteCall(card.owner, "destroy", convertCardListIntoCardIDsList(card))

def burnShieldKill(count=1, targetOwnSh=False, powerFilter='ALL', killCount=0, targetOwnCr=False):  # Mainly for destroying shields. Kill is optional.
	mute()
	targets=[c for c in table if c.targetedBy==me]
	targetSh=[]
	targetCr=[]
	for c in targets:
		if isShield(c) and not isBait(c):
			targetSh.append(c)
		elif isCreature(c):
			targetCr.append(c)

	if killCount=="ALL" or killCount>0:
		validKillTargets=[c for c in getCreatures() if not isUntargettable(c) and (powerFilter=='ALL' or (c.Power!='Infinity' and int(c.Power.strip(' +'))<=powerFilter))]
		if not targetOwnCr:
			validKillTargets=[c for c in validKillTargets if not c.owner==me]
			targetCr=[c for c in targetCr if not c.owner==me and c in validKillTargets]
		if killCount=="ALL":
			targetCr=validKillTargets
			killCount=len(targetCr)
		else:
			targetCr=[c for c in targetCr if c in validKillTargets]
			killCount=min(killCount, len(validKillTargets))

	myShields=len(getShields(me))
	oppShields=len([c for c in getShields() if c.owner!=me])

	if targetOwnSh:
		targetSh=[c for c in targetSh if c.owner==me]
		count=min(count, myShields)
	else:
		targetSh=[c for c in targetSh if c.owner!=me]
		count=min(count, oppShields)

	if count==0 and killCount==0:  # No shields left to burn, nothing to kill
		whisper("No valid targets.")
		return

	if len(targetSh)!=count or len(targetCr)!=killCount:
		whisper("Invalid Shields and/or Creatures targeted.")
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
		targetPlayer=getTargetPlayer(onlyOpponent=opponent)
	else:
		targetPlayer=me
	if isTop==False:
		notify("{} looks at {} Cards from bottom of their Deck.".format(targetPlayer, count))
	notify("{} looks at {} Cards from top of their Deck.".format(targetPlayer, count))
	targetPlayer.Deck.lookAt(count, isTop)

#Destroy your own creature
def sacrifice(power='inf', count=1, filterFunction='True', returnTrueIfNoDestruction=False):
	mute()
	cardList=[c for c in getCreatures(me) if (power=='inf' or c.Power!='Infinity' and int(c.Power.strip('+')) <= power) and (filterFunction=='True' or eval(filterFunction, allowed_globals, {'c': c}))]
	if len(cardList)==0:
		if returnTrueIfNoDestruction:
			return True
		return
	if me.isInverted: reverseCardList(cardList)
	choices=askCard2(cardList, 'Choose {} Creature(s) to destroy'.format(count, ), maximumToTake=count, returnAsArray=True)
	if not isinstance(choices,list) or not choices:
		if returnTrueIfNoDestruction:
			return True
		return
	for choice in choices:
		destroy(choice)

	if returnTrueIfNoDestruction and len(choices)<count: return True

#Return targeted creatures to hand
def bounce(count=1, opponentOnly=False, toDeckTop=False, filterFunction='True', conditionalFromLastFunction=False, upTo=False):
	mute()
	if count==0: return
	global evaluateNextFunction
	if conditionalFromLastFunction: #for example in case of Dondon Vacuuming Now
		if not evaluateNextFunction:
			evaluateNextFunction=True
			return
	if opponentOnly:
		cardList=[c for c in getElements() if c.owner!=me and not isUntargettable(c) and (filterFunction=='True' or eval(filterFunction, allowed_globals, {'c': c}))]
	else:
		cardList=[c for c in getElements() if not isUntargettable(c) and (filterFunction=='True' or eval(filterFunction, allowed_globals, {'c': c}))]
	if len(cardList)==0:
		whisper("No valid targets on the Table.")
		return
	count=min(count, len(cardList))
	targets=[c for c in cardList if c.targetedBy==me]
	if (not upTo and len(targets)!=count) or (upTo and len(targets)==0):
		return True #forcing octgn to go to targets function and wait
	if upTo and len(targets) and len(targets)<count:
		choice =  askYN("Pick another target?")
		if choice == 1: return True

	for card in targets:
		if toDeckTop:
			remoteCall(card.owner, "toDeck", convertCardListIntoCardIDsList(card))
		else:
			remoteCall(card.owner, "toHand", convertCardListIntoCardIDsList(card))

#Return every creature that matches filters
def bounceAll(group=table, opponentCards=True, myCards=True, filterFunction='True'):
	mute()
	group=ensureGroupObject(group)
	cardList=[c for c in group if isCreature(c) and not isRemovedFromPlay(c) and ((opponentCards and c.controller!=me) or (myCards and c.controller==me)) and (filterFunction=='True' or eval(filterFunction, allowed_globals, {'c': c}))]
	if len(cardList)==0: return
	for card in cardList:
		remoteCall(card.owner, "toHand", convertCardListIntoCardIDsList(card))

#Used for array of shields.
def peekShields(shields, checkEvo=True):
	mute()
	for shield in shields:
		if not isShield(shield): return
		shield.peek()
		notify("{} peeks at Shield#{}".format(me, shield.markers[shieldMarker]))
		if checkEvo:
			baits=getCardBaits(shield)
			peekShields(baits, False)

#Used to target a shield(s) and peek at them.
def peekShield(count=1, onlyOpponent=False):
	if onlyOpponent:
		targetPlayer=getTargetPlayer(onlyOpponent=True)
		if not targetPlayer: return
	cardList=[c for c in getShields() if (not onlyOpponent or c.owner==targetPlayer) and not me in c.peekers]
	if len(cardList)==0: return
	count=min(count, len(cardList))
	targets=[]
	if count!=len(cardList):
		whisper('Target opponent\'s Shield(s).')
		targets=[c for c in cardList if c.targetedBy==me]
		if len(targets)!=count:
			whisper('Wrong target(s)!')
			return True
		else:
			clear(targets)
	else:
		targets=cardList
	peekShields(targets)

#for Effects that return shield and don't trigger shield triggers
def bounceShield(count=1, selfOnly=True, optional=True):
	mute()
	cardList=[]
	if selfOnly:
		cardList=getShields(me)
	else:
		cardList=getShields()
	if len(cardList)==0: return
	count=min(count, len(cardList))
	if not optional and count==len(cardList):
		targets=cardList
	else:
		targets=[c for c in cardList if c.targetedBy==me]
		if len(targets)!=count:
			whisper("Target {} Shield(s) to return to Hand.".format(count))
			return True #forcing octgn to go to targets function and wait
	bounceList=[]
	for i in range(0, count):
		if (targets[i] in cardList):
			choice=targets[i]
			bounceList.append(choice)
		else:
			whisper("Wrong target(s)!")
			return True #true return forces wait. The same function is called again when targets change.

	for card in bounceList:
		remoteCall(card.owner, "toHand", [convertCardListIntoCardIDsList(card), False])

def gear(str):
	mute()
	if str=='kill':
		cardList=getGears(me)
		if len(cardList)==0:
			return
		if me.isInverted: reverseCardList(cardList)
		choice=askCard2(cardList, 'Choose a Cross Gear to send to Graveyard')
		if type(choice) is not Card:
			return
		remoteCall(choice.owner, 'destroy', convertCardListIntoCardIDsList(choice))
	elif str=='bounce':
		cardList=getGears()
		if len(cardList)==0:
			return
		if me.isInverted: reverseCardList(cardList)
		choice=askCard2(cardList, 'Choose a Cross Gear to send to Hand')
		if type(choice) is not Card:
			return
		if choice.owner==me:
			toHand(choice)
		else:
			remoteCall(choice.owner, 'toHand', convertCardListIntoCardIDsList(choice))
	elif str=='mana':
		cardList=getGears()
		if len(cardList)==0:
			return
		if me.isInverted: reverseCardList(cardList)
		choice=askCard2(cardList, 'Choose a Cross Gear to send to Mana')
		if type(choice) is not Card:
			return
		if choice.owner==me:
			toHand(choice)
		else:
			remoteCall(choice.owner, 'toMana', convertCardListIntoCardIDsList(choice))

#Called for Creatures by tapMultiple, which is the same as Ctrl+G or "Tap / Untap"
def processTapUntapCreature(card, processTapEffects=True):
	card=ensureCardObjects(card)
	mute()
	card.orientation ^= Rot90
	evoBaits=getCardBaits(card)
	for bait in evoBaits:
		bait.orientation=card.orientation
	update()
	if card.orientation & Rot90==Rot90:
		notify('{} taps {}.'.format(me, card))
		global arrow
		activatedTapEffect=False
		(evolveDict, sealDict)=getEvolveDictAndSealDict(card)

		#Helper inner function for onAllyTap
		def handleOnAllyTapEffects(card):
			creaturesonAllyTapList=[c for c in getCreatures(me) if cardScripts.get(c.properties["Name"], {}).get('onAllyTap')]
			#remove duplicates from list, only one Tap Effect can be activated at a time.
			if len(creaturesonAllyTapList)==0: return False
			creaturesonAllyTapList={c.properties["Name"]: c for c in creaturesonAllyTapList}.values()
			for creature in creaturesonAllyTapList:
				functionList=[]
				functionsonAllyTapList=list(cardScripts.get(creature.properties["Name"]).get('onAllyTap', []))
				for functiononAllyTap in functionsonAllyTapList:
					condition=functiononAllyTap[0]
					c=card
					if eval(condition, allowed_globals, {'c': c}):
						functionList.extend(functiononAllyTap[1])
				if len(functionList)>0:
					choice=askYN("Activate Tap Effect(s) for {} by tapping {}?\n\n{}".format(creature.properties["Name"], card.properties["Name"], creature.Rules), ["Yes", "No"])
					if choice!=1: return False
					notify('{} uses Tap Effect of {} by tapping {}'.format(me, creature, card))
					for index, function in enumerate(functionList):
						waitingFunct.insert(index + 1, [card, function])
					evaluateWaitingFunctions()
					return True
			return False

		#Tap Effects can only activate during active Player's turn.
		if processTapEffects and getActivePlayer()==me and not isRemovedFromPlay(card, evolveDict, sealDict) and not card._id in arrow:
			functionList=list(cardScripts.get(card.properties["Name"], {}).get('onTap', []))
			if len(functionList)>0:
				choice=askYN("Activate Tap Effect(s) for {}?\n\n{}".format(card.properties["Name"], card.Rules), ["Yes", "No"])
				if choice==1:
					notify('{} uses Tap Effect of {}'.format(me, card))
					activatedTapEffect=True
					for index, function in enumerate(functionList):
						waitingFunct.insert(index + 1, [card, function])
					evaluateWaitingFunctions()
				else:
					activatedTapEffect=handleOnAllyTapEffects(card)
			else:
				activatedTapEffect=handleOnAllyTapEffects(card)

		#OnAttack Effects can only activate during active Player's turn.
		if processTapEffects and getActivePlayer()==me and not isRemovedFromPlay(card, evolveDict, sealDict) and not activatedTapEffect:
			functionList=list(cardScripts.get(card.properties["Name"], {}).get('onAttack', []))
			if re.search("Survivor",card.Race):
				survivors=getSurvivorsOnYourTable(True, evolveDict, sealDict)
				for surv in survivors:
					if surv._id!=card._id and cardScripts.get(surv.properties["Name"], {}).get('onAttack'):
						functionList.extend(cardScripts.get(surv.properties["Name"]).get('onAttack', []))
			if len(functionList)>0:
				choice=1
				if(card._id not in arrow):
					choice=askYN("Activate on Attack Effect(s) for {}?\n\n{}".format(card.properties["Name"], card.Rules), ["Yes", "No"])
				if choice==1:
					notify('{} uses on Attack Effect of {}'.format(me, card))
					for index, function in enumerate(functionList):
						waitingFunct.insert(index + 1, [card, function])
					evaluateWaitingFunctions()
	else:
		notify('{} untaps {}.'.format(me, card))

def processOnTurnEndEffects():
	(evolveDict, sealDict)=getEvolveDictAndSealDict()
	cardList=getCreatures(me, evolveDict, sealDict)
	for card in cardList:
		functionList=list(cardScripts.get(card.properties["Name"], {}).get('onTurnEnd', []))
		if re.search("Survivor", card.Race):
			survivors=getSurvivorsOnYourTable(True, evolveDict, sealDict)
			for surv in survivors:
				if surv._id!=card._id and cardScripts.get(surv.properties["Name"], {}).get('onTurnEnd', []):
					functionList.extend(cardScripts.get(surv.properties["Name"]).get('onTurnEnd', []))
		if len(functionList)>0:
			notify('{} activates at the end of {}\'s turn'.format(card, me))
			for function in functionList:
				waitingFunct.append([card, function])

	#endOfTurnFunct is an array: [requireCardOnFieldToActivate, removeAfterActivation, [card, functionList]]
	for function in list(endOfTurnFunct):
		requireCardOnFieldToActivate=function[0]
		removeAfterActivation=function[1]
		cardFunctList=function[2]
		if requireCardOnFieldToActivate and (not isElement(card) or isRemovedFromPlay(card)):
			endOfTurnFunct.remove(function)
			return
		notify('{} activates at the end of {}\'s turn'.format(cardFunctList[0], me))
		waitingFunct.append(cardFunctList)
		if removeAfterActivation:
			endOfTurnFunct.remove(function)
	orderEvaluatingFunctions()
	evaluateWaitingFunctions()

def processOnTurnStartEffects():
	(evolveDict, sealDict)=getEvolveDictAndSealDict()
	cardList=getCreatures(me, evolveDict, sealDict)
	for card in cardList:
		functionList=list(cardScripts.get(card.properties["Name"], {}).get('onTurnStart', []))
		if re.search("Survivor", card.Race):
			survivors=getSurvivorsOnYourTable(True, evolveDict, sealDict)
			for surv in survivors:
				if surv._id!=card._id and cardScripts.get(surv.properties["Name"], {}).get('onTurnStart', []):
					functionList.extend(cardScripts.get(surv.properties["Name"]).get('onTurnStart', []))
		if len(functionList)>0:
			notify('{} activates at the start of {}\'s turn'.format(card, me))
			for function in functionList:
				waitingFunct.append([card, function])
	#startOfTurnFunct is an array: [requireCardOnFieldToActivate, removeAfterActivation, [card, functionList]]
	for function in list(startOfTurnFunct):
		requireCardOnFieldToActivate=function[0]
		removeAfterActivation=function[1]
		cardFunctList=function[2]
		if requireCardOnFieldToActivate and (not isElement(card) or isRemovedFromPlay(card)):
			startOfTurnFunct.remove(function)
			return
		notify('{} activates at the start of {}\'s turn'.format(function[1][0], me))
		waitingFunct.append(cardFunctList)
		if removeAfterActivation:
			startOfTurnFunct.remove(function)
	orderEvaluatingFunctions()
	evaluateWaitingFunctions()

#Send Creature/Mana to shields
def sendToShields(count=1, opponentCards=True, myCards=False, creaturesFilter=True, manaFilter=False, filterFunction='True'):
	mute()
	cardList=[c for c in table if not isShield(c) and not isRemovedFromPlay(c) and not isUntargettable(c)
			and ((creaturesFilter and isCreature(c)) or (manaFilter and isMana(c)) or isElement(c))
			and ((myCards and c.owner==me) or (opponentCards and c.owner!=me))
			and (filterFunction=='True' or eval(filterFunction, allowed_globals, {'c': c}))]
	if len(cardList)==0: return
	count=min(count, len(cardList))
	if count==0: return
	targets=[c for c in cardList if c.targetedBy==me]
	if len(targets)!=count:
		whisper("Wrong number of targets!")
		return True
	for target in targets:
		if target.targetedBy:
			target.target(False)
		remoteCall(target.owner, "toShields", convertCardListIntoCardIDsList(target))

#Send creature to Mana
def sendToMana(count=1, opponentCards=True, myCards=False, filterFunction='True'):
	mute()
	cardList=[c for c in getElements() if not isUntargettable(c) and ((opponentCards and c.owner!=me) or (myCards and c.owner==me)) and (filterFunction=='True' or eval(filterFunction, allowed_globals, {'c': c}))]
	if len(cardList)==0: return
	if me.isInverted: reverseCardList(cardList)
	choices=askCard2(cardList, 'Choose {} Creature(s) to send to Mana Zone'.format(count), maximumToTake=count, returnAsArray=True)
	if not isinstance(choices,list): return
	for choice in choices:
		remoteCall(choice.owner,"toMana", convertCardListIntoCardIDsList(choice))

def selfDiscard(count=1):
	mute()
	cardList=[card for card in me.hand]
	if len(cardList)==0: return
	reverseCardList(cardList)
	count=min(count, len(cardList))
	if len(cardList)==count:
		cardChoices=cardList
	else:
		cardChoices=askCard2(cardList, "Choose {} Card(s) to discard".format(count), minimumToTake=count, maximumToTake=count, returnAsArray=True)
	if not isinstance(cardChoices, list):
		notify("Discard cancelled.")
		return
		# do anti-discard check here
	toDiscard(cardChoices)
	update()

#Summon creature after it got discarded
def toPlayAfterDiscard(card, onlyOnOpponentTurn=True):
	if not onlyOnOpponentTurn or getActivePlayer()!=me:
		choice=askYN("Summon {} because it was discarded during opponent's turn?\n\n{}".format(card.properties["Name"], card.Rules), ["Yes", "No"])
		if choice==1:
			toPlay(card)

def suicide(card, action, args):
	mute()
	choiceList=['Yes', 'No']
	colorsList=['#FF0000', '#FF0000']
	choice=askChoice("Destroy the card to activate effect?", choiceList, colorsList)
	if choice!=1: return
	toDiscard(card)
	action(*args)

def opponentSacrifice(sacrificeArgs=[]):
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer, 'sacrifice', sacrificeArgs)

def opponentToDiscard(count=1):
	mute()
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'selfDiscard', count)

def opponentSendToMana(count=1):
	mute()
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'sendToMana',[count, False, True])

def opponentSearch(args):
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'search', args)

def oppponentFromMana(count=1, toGrave=False, filterFunction='True', exactCount=False):
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'fromMana',[count,"ALL","ALL","ALL",True,toGrave,filterFunction,exactCount])

def bothPlayersFromMana(count=1, toGrave=False, filterFunction='True', exactCount=False):
	for player in getPlayers():
		remoteCall(player, "fromMana", [count, "ALL","ALL","ALL",True, toGrave, filterFunction, exactCount])

def opponentManaToHand(count=1):
	manaList=getMana(getTargetPlayer(onlyOpponent=True))
	if len(manaList)==0:return
	if me.isInverted: reverseCardList(manaList)
	count=min(count,len(manaList))
	choices=askCard2(manaList, "Choose {} Card(s) from the opponent's Mana Zone".format(count), maximumToTake=count, returnAsArray=True)
	if not isinstance(choices, list):return
	for choice in choices:
		remoteCall(choice.owner,"toHand",convertCardListIntoCardIDsList(choice))

#If opponent has more mana that you charge/draw
def manaCompare(count=1, charge=False, draw=False, shield=False):
	manaCards=getMana(me)
	oppMana=getMana(getTargetPlayer(onlyOpponent=True))
	if len(oppMana)>len(manaCards):
		if charge:
			mana(me.Deck,count)
		if draw:
			draw(me.Deck, False, count)
		if shield:
			shields(me.Deck,count)

#Generic function to Tap Creature(s). targetAll flag means it won't ask and tap every opp creature
def tapCreature(count=1, targetALL=False, includeOwn=False, onlyOwn=False, filterFunction='True'):
	mute()
	if targetALL:
		cardList=[card for card in getCreatures() if card.orientation==Rot0]
		if onlyOwn:
			cardList=[card for card in cardList if card.controller==me]
		elif not includeOwn:
			cardList=[card for card in cardList if card.controller!=me]
		if filterFunction!='True':
			cardList=[c for c in cardList if eval(filterFunction, allowed_globals, {'c': c})]
		if len(cardList)==0:
			return
		for card in cardList:
			remoteCall(card.owner, "processTapUntapCreature", [convertCardListIntoCardIDsList(card), False])
	else:
		cardList=[card for card in getCreatures() if card.orientation==Rot0]
		if onlyOwn:
			cardList=[card for card in cardList if card.controller==me]
		elif not includeOwn:
			cardList=[card for card in cardList if card.controller!=me]
		cardList=[c for c in cardList if not isUntargettable(c) and (filterFunction=='True' or eval(filterFunction, allowed_globals, {'c': c}))]
		if len(cardList)==0:
			return
		if me.isInverted: reverseCardList(cardList)
		count=min(count, len(cardList))
		if count==0: return
		choices=askCard2(cardList, 'Choose {} Creature(s) to tap'.format(count), maximumToTake=count,returnAsArray=True)
		if not isinstance(choices, list): return
		for choice in choices:
			remoteCall(choice.owner, "processTapUntapCreature", [convertCardListIntoCardIDsList(choice), False])

def semiReset():
	mute()
	if confirm("Are you sure you want to continue?"):
		currentPlayers=getPlayers()
		for player in currentPlayers:
			cardsInHand=[c for c in player.hand]
			cardsInGrave=[c for c in player.piles['Graveyard']]
			if cardsInHand or cardsInGrave:
				for card in cardsInHand:
					remoteCall(player, 'toDeck', convertCardListIntoCardIDsList(card))
				for card in cardsInGrave:
					remoteCall(player, 'toDeck', card)
			remoteCall(player, 'shuffle', convertGroupIntoGroupNameList(player.deck))
			remoteCall(player, 'draw', [convertGroupIntoGroupNameList(player.deck), False, 5])

def swapManaAndHand(tapped=True):
	manaZoneList=getMana(me)
	handList=[card for card in me.hand]
	for manaCard in manaZoneList:
		toHand(manaCard)
	for handCard in handList:
		toMana(handCard)
		if tapped:
			handCard.orientation=Rot270

def lonely(card):
	if len(getCreatures(me))==1:
		destroy(card)
		notify("{} got destroyed because it was alone on board!".format(card))

# Special Card Group Automatization

def cloned(functionArray, card):
	if callable(functionArray):
		functionArray=[functionArray]
	count=1
	for player in getPlayers():
		for c in player.piles["Graveyard"]:
			if re.search(c.properties["Name"], card.properties["Name"]):
				count += 1
	notify("{}s in Graveyards:{}".format(card.properties["Name"], count - 1))
	for index, funct in enumerate(functionArray):
		waitingFunct.insert(index + 1, [card, lambda card=card, count=count: funct(card, count)])

def waveStriker(functionArray, card):
	if callable(functionArray):
		functionArray=[functionArray]
	global wscount
	wscount=getWaveStrikerCount()
	if functionArray and wscount >= 3:
		for index, funct in enumerate(functionArray):
			waitingFunct.insert(index + 1, [card, funct])

def mode(functionArray,card, choiceText=[], deb=False, count=1):
	if callable(functionArray):
		functionArray=[functionArray]
	if len(choiceText)==0:
		for f in range(0,len(functionArray)):
			choiceText.append(str(f+1))
	if deb and len([c for c in getElements(me) if re.search("Evolution", c.Type)])!=0:
		choice=askYN("Do you want to use both effects of {}?".format(card))
		if choice==1:
			#add choices to waiting list. Usually 2 but maybe there will be exceptions
			for i in range (0,len(functionArray)):
				waitingFunct.insert(i+1, [card,functionArray[i]])
			return
	for i in range (0, count):
		choice=askChoice("Which effect do you want to activate?",choiceText,[])
		if choice==0: return
		waitingFunct.insert(1, [card,functionArray[choice-1]])
		notify("{} chose {} effect of {}".format(me,choiceText[choice-1],card))

#addDelayedEffect allows you to add an effect to activate on turn Start or on turn End. Args are passed down to the function to activate.
#effectDictionary is a dictionary with those keys: {"delayTo", "card", "effects", "requireCardOnFieldToActivate", "removeAfterActivation"}
#it appends to either EndOfTurnFunct or startOfTurnFunct arrays looking like so: [requireCardOnFieldToActivate, removeAfterActivation, [card,function]
def addDelayedEffect(effectDictionary, args):
	if type(effectDictionary) is not dict:
		return
	if type(args) is not list:
		args=[args]
	delayTo=effectDictionary.get("delayTo", "EndOfTurn")
	card=effectDictionary.get("card")
	functionArray=effectDictionary.get("effects")
	if callable(functionArray):
		functionArray=[functionArray]
	requireCardOnFieldToActivate=effectDictionary.get("requireCardOnFieldToActivate", False)
	removeAfterActivation=effectDictionary.get("removeAfterActivation", True)
	if delayTo=="EndOfTurn":
		listToAppendTo=endOfTurnFunct
	elif delayTo=="StartOfTurn":
		listToAppendTo=startOfTurnFunct
	else:
		return
	for funct in functionArray:
		listToAppendTo.append([requireCardOnFieldToActivate, removeAfterActivation, [card, lambda card=card, args=args: funct(card, args)]])

def activateButtonEffect(card, x=0, y=0):
	mute()
	notify('{} triggers the effect of {}'.format(me, card))
	functionList=[]
	if re.search('Survivor', card.Race):
		survivors=getSurvivorsOnYourTable()
		#for non-sharing survivors
		if card not in survivors:
			survivors.insert(0, card)
		for surv in survivors:
			if cardScripts.get(surv.properties["Name"], {}).get('onButton'):
				functionList.extend(cardScripts.get(surv.properties["Name"]).get('onButton', []))
	elif cardScripts.get(card.properties["Name"], {}).get('onButton'):
		functionList=list(cardScripts.get(card.properties["Name"]).get('onButton', []))
	for index, function in enumerate(functionList):
		waitingFunct.insert(index + 1, [card, function])
	evaluateWaitingFunctions()

#Used for Meteorburn's: Whenever this creature attacks, you may put a card under this creature into your graveyard. If you do, "EFFECT".
def meteorburn(functionArray, card, minimum=1, maximum=1):
	if callable(functionArray):
		functionArray=[functionArray]
	baitList=detachBait(card, minimumToTake=minimum, maximumToTake=maximum)
	if functionArray and len(baitList)>0:
		for index, funct in enumerate(functionArray):
			waitingFunct.insert(index + 1, [card, lambda card=card, baitList=baitList: funct(card, baitList)])

#Special Card Automatization

def allSunrise():
	mute()
	shieldList=getShields(me)
	evolveDict=eval(me.getGlobalVariable("evolution"), allowed_globals)
	for shield in list(shieldList):
		baits=removeBaits(shield, evolveDict)
		if baits:
			shieldList.extend(baits)
	group=me.Deck
	if len(group)>0:
		deckList=[c for c in group]
		topCard=deckList.pop(0)
		if len(deckList)>0:
			#we reverse the decklist here to put bottom cards as shields first, so they have lower #.
			for c in reversed(deckList):
				toShields(c, 0, 0, True, False, False)
			toShields(topCard, 0, 0, True, False, False)
			updateBaits(topCard, deckList, evolveDict)
		else:
			toShields(topCard)
	notify('{} puts their Deck as a single Shield #{}.'.format(me, me.getGlobalVariable("shieldCount")))
	shuffleToBottom(shieldList)
	align()

def apocalypseVise():
	powerLeft=8000
	creaturesToDestroy=[]
	creatureList=[c for c in getCreatures() if c.owner!=me and c.Power!='Infinity' and int(c.Power.strip('+'))<=powerLeft]
	if me.isInverted: reverseCardList(creatureList)
	while powerLeft>0 and len(creatureList)>0:
		creatureChoice=askCard2(creatureList, 'Choose a Creature to destroy.')
		if type(creatureChoice) is not Card: break
		powerLeft=powerLeft-int(creatureChoice.Power.strip('+'))
		creatureChoice.target()
		creaturesToDestroy.append(creatureChoice)
		creatureList.remove(creatureChoice)
		notify("Apocalypse Vise - Power Spent: {}".format(8000-powerLeft))
		creatureList=[c for c in creatureList if int(c.Power.strip('+'))<=powerLeft]
	if len(creaturesToDestroy)>0:
		destroyAll(creaturesToDestroy, False)

def auraPegasus():
	if len(me.Deck)==0: return
	notify("{} looks at the top Card of their Deck".format(me))
	card=me.Deck[0]
	card.isFaceUp=True
	notify("{} reveals {}".format(me, card))
	if re.search("Creature", newCard.Type) and not re.search("Evolution Creature", newCard.Type):
		toPlay(card)
	else:
		toHand(card)

def bluumErkis(card):
	mute()
	shieldList=[c for c in getShields() if c.owner!=me and not isRemovedFromPlay(c)]
	targets=[c for c in shieldList if c.targetedBy==me]
	count=min(1, len(shieldList))
	if count==0:
		whisper("No valid targets.")
		return
	if len(targets)!=count:
		return True
	for shield in targets:
		remoteCall(shield.owner, 'flip', [convertCardListIntoCardIDsList(shield)])
		update()
		if re.search("Spell", shield.Type) and re.search("{SHIELD TRIGGER}", shield.Rules, re.IGNORECASE):
			notify('{} casts {} from {}\'s Shields'.format(me, shield.properties["Name"], shield.owner))
			if cardScripts.get(shield.properties["Name"], {}).get('onPlay'):
				functionList=list(cardScripts.get(shield.properties["Name"], {}).get('onPlay', []))
				functionList.append(lambda card: remoteCall(card.owner, 'toDiscard', convertCardListIntoCardIDsList(card)))
				for index, function in enumerate(functionList):
					waitingFunct.insert(index + 1, [shield, function])
			if shield.targetedBy:
				shield.target(False)
		else:
			remoteCall(shield.owner, 'toHand', [convertCardListIntoCardIDsList(shield)])
	orderEvaluatingFunctions()
	evaluateWaitingFunctions()

def bronks():
	creatureList=[c for c in getCreatures() if c.Power!='Infinity']
	minPower=min(int(c.Power.strip('+')) for c in creatureList)
	notify("Lowest Power found: {}".format(minPower))
	leastPowerCreatureList=[c for c in creatureList if int(c.Power.strip('+'))==minPower]
	if len(leastPowerCreatureList)==1:
		remoteCall(leastPowerCreatureList[0].owner,'destroy', convertCardListIntoCardIDsList(leastPowerCreatureList[0]))
		return

	opponentCreatures=[card for card in creatureList if card.owner!=me and not isUntargettable(card)]
	myCreatures=[card for card in creatureList if card.owner==me]
	leastPowerCreatureList=sorted(leastPowerCreatureList, key=lambda x: (
	   	int(me.isInverted) if x in opponentCreatures else int(not me.isInverted),
		(opponentCreatures + myCreatures).index(x)))

	if me.isInverted:
		reverseCardList(leastPowerCreatureList)
	else:
		leastPowerCreatureList=sorted(leastPowerCreatureList, key=lambda x: (
	   	 	0 if x in opponentCreatures else 1,
			(opponentCreatures + myCreatures).index(x)))
	choice=askCard2(leastPowerCreatureList, "Select a card to destroy (Opponent's are shown first).")
	if type(choice) is not Card: return
	remoteCall(choice.owner,'destroy', convertCardListIntoCardIDsList(choice))

def cyclonePanic():
	if confirm("Are you sure you want to continue?"):
		for player in getPlayers():
			cardInHand=[c for c in player.hand]
			for c in cardInHand:
				remoteCall(player, 'toDeck', convertCardListIntoCardIDsList(c))
			remoteCall(player, 'shuffle', convertGroupIntoGroupNameList(player.deck))
			remoteCall(player, 'draw', [convertGroupIntoGroupNameList(player.deck), False, len(cardInHand)])

def raptorFish():
	choice=askYN("Raptor Fish wants to redraw your hand. Proceed?")
	if choice:
		cardInHand=[c for c in me.hand]
		for c in cardInHand:
			toDeck(c)
		shuffle(me.Deck)
		draw(me.Deck,False,len(cardInHand))

def darkpact(card):
	manaList=getMana(me)
	if me.isInverted: reverseCardList(manaList)
	targetsMana=askCard2(manaList, "Select cards from Mana", maximumToTake=len(manaList),returnAsArray=True)
	if not isinstance(targetsMana,list): return
	destroyAll(targetsMana)
	draw(me.Deck, count=len(targetsMana))

def deklowazDiscard():
	mute()
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	cardList=[card for card in targetPlayer.hand]
	reverseCardList(cardList)
	cardChoice=askCard2(cardList, "Look at opponent's hand. (close pop-up or select any card to finish.)")
	cardsToDiscard=[c for c in cardList if re.search("Creature", c.Type) and c.Power!='Infinity' and int(c.Power.strip('+')) <= 3000]
	remoteCall(targetPlayer, 'toDiscard',[convertCardListIntoCardIDsList(cardsToDiscard), 0, 0, False, True, True, False, True])

def dolmarks():
	sacrifice()
	fromMana(1,"ALL","ALL","ALL",True,True)
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'sacrifice',[])
	remoteCall(targetPlayer,'fromMana',[1,"ALL","ALL","ALL",True,True])

def eternalPhoenix():
	creatureList=[c for c in me.piles["Graveyard"] if re.search("Fire", c.Civilization) and re.search("Creature", c.Type) and not re.search("Evolution", c.Type)]
	for creature in creatureList:
		toHand(creature)

def enigmaticCascade():
	handList=[c for c in me.hand]
	choices=askCard2(handList,"Select Cards to discard", maximumToTake=len(handList), returnAsArray=True)
	for choice in choices:
		toDiscard(choice)
	draw(me.Deck,False,len(choices))

def shieldswap(card, count=1, ask=False):
	if len(getShields(me))==0 or len(me.hand)==0: return
	if ask:
		choice=askYN("Use {}'s effect?".format(card.properties["Name"]))
		if choice!=1: return
	handList=[c for c in me.hand]
	count=min(count, len(handList))
	reverseCardList(handList)
	choices=askCard2(handList,"Select {} Card(s) to put as Shield".format(count), maximumToTake=count, returnAsArray=True)
	if not isinstance(choices, list): return
	for choice in choices:
		toShields(choice)
	waitingFunct.insert(1, [card, lambda card=card, counter=len(choices): bounceShield(counter, True, False)])

def flamespearWaterblade():
	if askYN('Destroy automatically?')!=1: return
	creatureList=[c for c in getCreatures() if c.Power!='Infinity' and int(c.Power.strip('+')) <= 3000]
	destroyAll(table, True, 3000, dontAsk=True)
	draw(me.Deck, True, len(creatureList))

def funkyWizard():
	for player in getPlayers():
		remoteCall(player, "draw", [convertGroupIntoGroupNameList(player.Deck), True])

def ghastlyDrain(card):
	number=askNumber("How many shields to return?", 1)
	if number==None:
		notify("{} didn't make a choice.".format(me))
		return
	notify("{} chose {} Shields".format(me,number))
	waitingFunct.insert(1, [card, lambda card=card, counter=number: bounceShield(counter, True, False)])

def returnAndDiscard(card):
	choice=askYN("Return {} to hand?".format(card.properties["Name"]))
	if choice!=1: return
	toHand(card)
	selfDiscard()

#Sadly we cannot just call targetDiscard with 'mana'argument and opponentManaToHand, because the mana wouldn't be updated in time to display new card added.
def gigandura(card):
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	cardList=[card for card in targetPlayer.hand]
	#Both players see their opponent's hand reversed
	reverseCardList(cardList)
	choice=askCard2(cardList, "Pick a Card to place to Mana from opponent's hand.")
	if type(choice) is not Card: return
	remoteCall(targetPlayer, 'toMana', convertCardListIntoCardIDsList(choice))
	manaList=getMana(targetPlayer)
	manaList.append(choice)
	if me.isInverted: reverseCardList(manaList)
	update()
	manaChoice=askCard2(manaList, "Choose a Card from the opponent's Mana Zone")
	if type(manaChoice) is not Card: return
	remoteCall(targetPlayer,"toHand",convertCardListIntoCardIDsList(manaChoice))

def hellHand():
	mute()
	shieldList=getShields(me)
	if len(shieldList)==0: return
	shieldBaitList=[]
	baitsToKeepDict={}
	evolveDict=eval(me.getGlobalVariable("evolution"), allowed_globals)
	#Turn Shields Face-down, get and separate baits, remove shield markers.
	for shield in shieldList:
		baitsToMove=[]
		if evolveDict:
			baits=removeBaits(shield, evolveDict)
			#Keep face-down baits in shields
			baitsToKeep=[c for c in baits if isShield(c)]
			baitsToMove=[c for c in baits if not isShield(c)]
			baitsToKeepDict[shield._id]=baitsToKeep
		shieldBaitList.append((shield.markers[shieldMarker], shield.index, baitsToMove))
	shuffleToBottom(shieldList, notifymute=True)
	shieldBaitList=sorted(shieldBaitList, key=lambda x: x[0])

	for index, (marker,tableIndex, baits) in enumerate(shieldBaitList):
		shield=shieldList[index]
		shield.moveToTable(0,0, True)
		shield.markers[shieldMarker]=marker
		shield.index=tableIndex
		if baits:
			baitList=baitsToKeepDict.get(shield._id,[])
			baitList.extend(baits)
			updateBaits(shield, baitList, evolveDict)
			#put only face-up baits to Front.
			for bait in baits:
				bait.moveToTable(0,0)
				bait.sendToFront()
	align()
	notify('{} shuffled their shields.'.format(me))

def pinpointLunatron():
	cardList=[c for c in table if (isCreature(c) or isMana(c)) and not isRemovedFromPlay(c)]
	if len(cardList)==0:return
	cardList=[c for c in cardList if c.targetedBy==me]
	if len(cardList)!=1: return True
	toHand(cardList[0])

def pouchShell():
	player=getTargetPlayer(onlyOpponent=True)
	cardList=[c for c in getCreatures(player) if re.search("Evolution", c.Type) and not isUntargettable(c)]
	if cardList==0: return
	choice=askCard2(cardList, "Select an evolution creature")
	if type(choice) is not Card: return
	baits=getCardBaits(choice)
	if len(baits)==0:
		remoteCall(player, 'toDiscard', [choice])
	else:
		remoteCall(player, '_pouchShellOpp', [choice])

def _pouchShellOpp(card):
	evolveDict=eval(me.getGlobalVariable("evolution"), allowed_globals)
	baits=removeBaits(card, evolveDict)
	if len(baits)>1:
		topCard=baits.pop(0)
		updateBaits(topCard,baits, evolveDict)
	toDiscard(card)
	align()

def heavyweightDragon(card):
	cardList=[c for c in getCreatures(getTargetPlayer(onlyOpponent=True)) if not isUntargettable(c) and c.Power!='Infinity']
	if len(cardList)==0: return
	if me.isInverted: reverseCardList(cardList)
	choices=askCard2(cardList, "Select up to 2 Creatures to destroy.",maximumToTake=2, returnAsArray=True)
	if not isinstance(choices, list): return
	totalPower=sum(map(lambda c: int(c.Power.strip('+')), itertools.chain(cardList)))
	if totalPower<int(card.Power.strip('+')):
		destroyAll(choices)
	else:
		notify("{}'s choices ({} Power) exceed {}'s Power".format(me, totalPower, card.Power))

def hurricaneCrawler():
	handList=[c for c in me.Hand]
	if len(handList)==0: return
	for c in handList:
		toMana(c)
	fromMana(len(handList),exactCount=True)

def hydroHurricane(card):
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	myCreatures=getCreatures(me)
	lightCards=[c for c in myCreatures if re.search("Light", c.Civilization)]
	darknessCards=[c for c in myCreatures if re.search("Darkness", c.Civilization)]
	oppMana=getMana(targetPlayer)
	oppCreatures=[c for c in getCreatures(targetPlayer) if not isUntargettable(c)]
	if len(oppMana)>0 and len(lightCards)>0:
		if me.isInverted: reverseCardList(oppMana)
		count=min(len(oppMana), len(lightCards))
		choices=askCard2(oppMana,"Select up to {} Cards from Mana".format(count), maximumToTake=count, returnAsArray=True)
		if not isinstance(choices,list):choices=[]
		for choice in choices:
			remoteCall(targetPlayer, "toHand", convertCardListIntoCardIDsList(choice))
	if len(oppCreatures)>0 and len(darknessCards)>0:
		if me.isInverted: reverseCardList(oppCreatures)
		count=min(len(oppCreatures), len(darknessCards))
		choices=askCard2(oppCreatures, "Select up to {} Creatures from Battle Zone".format(count),maximumToTake=count,returnAsArray=True)
		if not isinstance(choices,list):choices=[]
		for choice in choices:
			remoteCall(targetPlayer, "toHand", convertCardListIntoCardIDsList(choice))

def kingAquakamui(card):
	choice=askYN("Return all Angel Commands and Demon Commands from Graveyard to Hand?")
	if choice!=1: return
	cardsInGrave=[c for c in me.piles['Graveyard'] if re.search(r"Angel Command|Demon Command", c.Race)]
	for c in cardsInGrave:
		toHand(c)

def klujadras():
	for player in getPlayers():
		count=getWaveStrikerCount(player)
		if count:
			remoteCall(player, "draw", [convertGroupIntoGroupNameList(player.Deck), False, count])

def lunarCharger(card):
	creatureList=getCreatures(me)
	if len(creatureList)==0: return
	choices=askCard2(creatureList,"Select up to 2 creatures.","Select", 1, min(2, len(creatureList)), True)
	if not isinstance(choices, list):return
	notify("{} chose {} for the effect of {}".format(me, ", ".join(["{}".format(c) for c in choices]), card))
	addDelayedEffect({"card":card, "effects":[lambda card, args: ([untapCreature(c) for c in choices], False)[0]]}, choices)

def dracobarrier():
	cardList= [card for card in getCreatures(getTargetPlayer(onlyOpponent=True)) if card.orientation==Rot0 and not isUntargettable(card)]
	if len(cardList)==0:
			return
	choice=askCard2(cardList, 'Choose a Creature to tap')
	if type(choice) is not Card: return
	remoteCall(choice.owner, "processTapUntapCreature", [convertCardListIntoCardIDsList(choice), False])
	if re.search(r'Dragon\b', choice.Race, re.I):
		shields(me.deck)

def waveLance():
	cardList=[c for c in getCreatures() if not isUntargettable(c)]
	if len(cardList)==0:
		whisper("No valid targets on the Table.")
		return
	target=[c for c in cardList if c.targetedBy==me]
	if len(target)!=1:
		whisper("Wrong number of targets!")
		return True
	else:
		remoteCall(target[0].owner, "toHand", convertCardListIntoCardIDsList(target))
		if re.search(r'Dragon\b', target[0].Race, re.I):
			draw(group=me.Deck, ask=True)

def mechadragonsBreath():
	power=askNumber()
	if power==None:
		notify("{} didn't make a choice.".format(me))
		return
	if(power>6000 or power<0):
		notify("{} chose incorrect Power ({}).".format(me, power))
		return
	notify("{} chose {} Power.".format(me, power))
	destroyAll(table,True,power,"ALL",False,True)

def miraculousMeltdown(card):
	mute()
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	myShields=getShields(me)
	opponentShields=getShields(targetPlayer)
	if len(opponentShields)<=len(myShields):
		whisper("You cannot cast this Spell!")
		return
	remoteCall(targetPlayer,'_eMMHelper', [card._id, len(myShields)])

def declareRace(card, excludedRace=None, returnRace=False):
	allZones=itertools.chain(me.deck, [c for c in table if c.isFaceUp], me.hand, me.graveyard, me.Hyperspatial, me.Gacharange)

	for player in getPlayers():
		if player!=me:
			allZones=itertools.chain(allZones,player.graveyard)
	allRaces=itertools.chain.from_iterable(re.split(r'/+', card.race) for card in allZones if card.race!='')
	raceCounts={}
	for race in allRaces:
		if race in raceCounts:
			raceCounts[race] += 1
		else:
			raceCounts[race]=1
	# Sort races by count in descending order
	sortedRaces=sorted(raceCounts.items(), key=lambda x: x[1], reverse=True)
	raceNames=[race for race, count in sortedRaces if race!=excludedRace]
	choice=askChoice("Select a race:", raceNames, customButtons=["Custom Race"])
	if choice==0:
		notify("{} didn't declare a Race".format(me))
		if returnRace:
			return "No race"
		else:
			return
	if choice>0:
		chosenRace=raceNames[choice-1]
	if choice < 0:
		chosenRace=askString("Type a custom Race to declare:",'')
	notify('{} declares \'{}\' Race'.format(me, chosenRace))
	card.properties["Rules"]='(Declared: {})\n{}'.format(chosenRace,card.properties["Rules"])
	if returnRace: return(chosenRace)

def divineRiptide():
	opponent=getTargetPlayer(onlyOpponent=True)
	fromManaAll()
	remoteCall(opponent,"fromManaAll",'True')

def shockHurricane(card):
	(evolveDict, sealDict)=getEvolveDictAndSealDict()
	myCreatures=getCreatures(me, evolveDict, sealDict)
	chosenCreatures=[]
	enemyCreatures=[c for c in getCreatures(getTargetPlayer(onlyOpponent=True)) if not isUntargettable(c)]
	enemyChosen=[]
	if me.isInverted: reverseCardList(myCreatures)
	while(len(myCreatures)>0):
		choice=askCard2(myCreatures, 'Choose a Creature to return to Hand')
		if type(choice) is not Card: break
		chosenCreatures.append(choice)
		myCreatures.remove(choice)
	bounceAll(chosenCreatures)
	count=min(len(chosenCreatures), len(enemyCreatures))
	for i in range(0, count):
		choice=askCard2(enemyCreatures, 'Choose an opponent\'s Creature to return to Hand')
		enemyChosen.append(choice)
		enemyCreatures.remove(choice)
	bounceAll(enemyChosen)

def crisisBoulder(card):
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'_eCrisisBoulderHelper',[card._id])

def _eCrisisBoulderHelper(cardId):
	waitingFunct.insert(0, [Card(cardId),lambda card: _enemyCrisisBoulder()])
	evaluateWaitingFunctions()

def _enemyCrisisBoulder():
	choiceList=['Creature', 'Mana']
	colorsList=['#FF0000', '#11FF11']
	choice=askChoice("Put Creature or Mana to Graveyard?",choiceList,colorsList)
	if choice==1:
		cardsToChooseFrom=getElements(me)
		if me.isInverted: reverseCardList(cardsToChooseFrom)
		selected=askCard2(cardsToChooseFrom, "Select a Creature to put to Graveyard")
	elif choice==2:
		cardsToChooseFrom=getMana(me)
		if me.isInverted: reverseCardList(cardsToChooseFrom)
		selected=askCard2(cardsToChooseFrom, "Select Mana to put to Graveyard")
	else: return
	toDiscard(selected)

def grinningHunger(card):
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	if not targetPlayer: return
	remoteCall(targetPlayer,'_eGHHelper',[card._id])

def _eGHHelper(cardId):
	waitingFunct.insert(0, [Card(cardId),lambda card: _enemyGrinningHunger(card)])
	evaluateWaitingFunctions()

def _enemyGrinningHunger(card):
	choiceList=['Creature', 'Shield']
	colorsList=['#FF1111', '#FFFF11']
	choice=askChoice("Put Creature or Shield to Graveyard?", choiceList, colorsList)
	if choice==1:
		notify("{} is destroying a Creature.".format(me))
		waitingFunct.insert(1, [card, lambda card: sacrifice()])
	elif choice==2:
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
	shieldList=getShields(me)
	targets=[c for c in shieldList if c.targetedBy==me]
	if len(targets)!=count:
		return True
	notSelectedShields=[c for c in shieldList if c not in targets]
	peekShields(notSelectedShields)

def theGraveOfAngelsAndDemons():
	if askYN('Destroy automatically?')!=1: return
	creatureList=getCreatures()
	manaList=getMana()

	def groupByName(card_list):
		sortedCards=sorted(card_list, key=lambda card: card.properties["Name"])
		return itertools.groupby(sortedCards, key=lambda card: card.properties["Name"])

	def findDuplicates(groupedCards):
		duplicates=[]
		for name, group in groupedCards:
			groupList=list(group)
			if len(groupList)>1:
				duplicates.extend(groupList)
		return duplicates

	groupedCreatures=groupByName(creatureList)
	groupedMana=groupByName(manaList)
	creaturesToDestroy=findDuplicates(groupedCreatures)
	manaToGraveyard=findDuplicates(groupedMana)

	destroyAll(creaturesToDestroy, dontAsk=True)
	for mana in manaToGraveyard:
		toDiscard(mana)

def miraculousPlague():
	mute()
	targetPlayer=getTargetPlayer(onlyOpponent=True)
	creatureList=[card for card in getCreatures(targetPlayer) if not isUntargettable(card)]
	if len(creatureList)!=0:
		if len(creatureList)==1:
			remoteCall(targetPlayer, "toHand", convertCardListIntoCardIDsList(creatureList[0]))
		else:
			if me.isInverted: reverseCardList(creatureList)
			creatureChoices=askCard2(creatureList, 'Choose 2 Creatures for your opponent.',minimumToTake=2, maximumToTake=2)
			if not isinstance(creatureChoices,list): return
			for cchoice in creatureChoices:
				cchoice.target()
			#sort the choices to reflect the table state.
			creatureChoices=sorted(creatureChoices, key= lambda x: creatureList.index(x))

			remoteCall(targetPlayer,"_miraculousPlagueChooseToHand", [convertCardListIntoCardIDsList(creatureChoices)])

	manaList=getMana(targetPlayer)
	if len(manaList)!=0:
		if len(manaList)==1:
			remoteCall(targetPlayer, "toHand", convertCardListIntoCardIDsList(manaList[0]))
		else:
			if me.isInverted: reverseCardList(manaList)
			manaChoices=askCard2(manaList, 'Choose 2 Mana Cards for your opponent',minimumToTake=2, maximumToTake=2)
			if not isinstance(manaChoices,list): return
			for mchoice in manaChoices:
				mchoice.target()
			#sort the choices to reflect the table state.
			sorted(manaChoices, key=lambda x: manaList.index(x))

			remoteCall(manaChoices[0].owner,"_miraculousPlagueChooseToHand", [convertCardListIntoCardIDsList(manaChoices)])

def _miraculousPlagueChooseToHand(cardList):
	cardList=ensureCardObjects(cardList)
	if me.isInverted: reverseCardList(cardList)
	cardToHand=askCard2(cardList, 'Choose a Card to return to Hand.')
	if type(cardToHand) is not Card: return
	cardList.remove(cardToHand)
	toHand(cardToHand)
	destroy(cardList[0])

def miraculousRebirth():
	mute()
	cardList=[c for c in getCreatures() if
				c.owner!=me
				and not isUntargettable(c)
				and c.Power!='Infinity'
				and int(c.Power.strip('+')) <= 5000]
	if len(cardList)==0:
		whisper("No valid targets on the Table.")
		return
	targetCard=[c for c in cardList if c.targetedBy==me]
	if len(targetCard)!=1:
		whisper("Wrong number of targets!")
		return True
	remoteCall(targetCard[0].owner, "destroy", convertCardListIntoCardIDsList(targetCard[0]))
	targetCost=int(targetCard[0].Cost)
	notify('Miraculous Rebirth destroys a Creature that costs {} Mana.'.format(targetCost))

	group=me.deck
	if len(group)==0: return
	cardsInGroup=sort_cardList([card for card in group])
	validChoice=None
	while (True):
		choice=askCard2(cardsInGroup, 'Search a Creature with {} Cost to put to Play'.format(targetCost))
		if type(choice) is not Card:
			group.shuffle()
			notify("{} finishes searching their {}.".format(me, group.name))
			return
		if cardCostComparator(choice,targetCost,'==', 'Creature'):
			validChoice=choice
			break
	group.shuffle()
	notify("{} finishes searching their {}.".format(me, group.name))
	toPlay(validChoice)

def rapidReincarnation():
	cardList=getCreatures(me)
	if len(cardList)==0:
		whisper("No valid targets on the Table.")
		return
	cardList=[c for c in cardList if c.targetedBy==me]
	if len(cardList)!=1:
		return True
	manaCount=len(getMana(me))
	handList=[c for c in me.Hand if re.search('Creature',c.Type) and cardCostComparator(c, manaCount,'<=',"Creature")]
	if len(handList)==0:
		whisper("No creatures in hand that cost less than or equal to your Mana count.")
		return
	reverseCardList(handList)
	choice=askCard2(handList, "Select a Creature to put into the battle zone", minimumToTake=1)
	if type(choice) is not Card: return
	destroy(cardList[0])
	toPlay(choice, clearWaitingFunctions=False)

def rouletteOfRuin():
	mute()
	chosenNumber=askNumber(defaultAnswer=1)
	if chosenNumber==None:
		notify("{} didn't make a choice.".format(me))
		return
	notify("{} chose {}.".format(me, chosenNumber))
	for player in getPlayers():
		remoteCall(player, 'lookAtHandAndDiscardAll', ["cardCostComparator(c, {}, '==')".format(chosenNumber)])

def mysteriousOgreDuel(card):
	mute()
	opponent=getTargetPlayer(onlyOpponent=True)
	if len(opponent.hand)==0:return
	cardToReveal=opponent.hand.random()
	cost=cardToReveal.cost
	update()
	notify('{} reveals {} randomly. Cost: {}'.format(opponent, cardToReveal.properties["Name"], cost))
	if not cost:
		notify("The revealed card has no cost.")
		return
	if cost=='Infinity':
		cost='ALL'
	if '/' in cost:
		cost=max(int(cardToReveal.Cost1), int(cardToReveal.Cost2))
	waitingFunct.insert(1,[card, lambda card=card, cost=cost:kill('ALL','ALL','ALL',1, False, 'ALL','cardCostComparator(c, {}, "<", "Creature")'.format(cost))])
	whisper('Target a Creature to destroy.')

def nigthmareMachine():
	sacrifice('inf', 1, 'c.orientation==Rot0')
	opponentSacrifice(['inf', 1, 'c.orientation==Rot0'])

def dracodanceTotem(card):
	manaList=[c for c in getMana(me) if re.search(r'Dragon\b', c.Race, re.I)]
	if len(manaList)==0:return
	if me.isInverted: reverseCardList(manaList)
	choice=askCard2(manaList,'Choose a Dragon from the Mana Zone')
	if type(choice) is not Card:return
	toHand(choice)
	toMana(card)

def soulSwap():
	mute()
	# targetPlayer=getTargetPlayer()
	# if not targetPlayer: return
	#list of creatures in battlezone
	targets=[c for c in getCreatures() if c.targetedBy==me and not isUntargettable(c)]
	if len(targets)!=1:
		return True
	cardsToMana=getCardBaits(targets[0])
	cardsToMana.insert(0,targets[0])
	remoteCall(targets[0].owner, "toMana", convertCardListIntoCardIDsList(targets[0]))
	update()
	remoteCall(me,'_fromManaToField',[targets[0].owner._id, cardsToMana])

def staticWarp():
	mute()
	for player in getPlayers():
		remoteCall(player, '_staticWarp',[])

def _staticWarp():
	creatureList=getCreatures(me)
	if len(creatureList)<=1:
		whisper("No valid targets on the Table.")
		return
	choice=askCard2(creatureList, 'Select a Creature for Static Warp.')
	if type(choice) is not Card: return
	for c in creatureList:
		if c!=choice and not isTapped(c):
			processTapUntapCreature(c, False)

def tanzanyte():
	cardList=[card for card in me.piles['Graveyard'] if re.search('Creature', card.Type)]
	choice=askCard2(sort_cardList(cardList), 'Select a Creature to return all copies of from Graveyard.')
	if type(choice) is not Card: return
	for card in cardList:
		if card.properties["Name"]==choice.properties["Name"]:
			toHand(card, True)

def upheaval():
	for player in getPlayers():
		remoteCall(player, 'swapManaAndHand', [])

def intenseEvil():
	myCreatures=getCreatures(me)
	if me.isInverted: reverseCardList(myCreatures)
	chosenCreatures=askCard2(myCreatures, 'Choose Creatures to destroy', maximumToTake=len(myCreatures),returnAsArray=True)
	if not isinstance(chosenCreatures,list):return

	destroyAll(chosenCreatures)
	draw(me.Deck,False,len(chosenCreatures))
#The additional targets list is used to handle evo creatures moving their baits with them to mana too late to catch this in this function.
def _fromManaToField(targetPlayerId, additionalTargetsList=[]):
	mute()
	targetPlayer=getPlayerById(targetPlayerId)
	#Count the number of cards in mana zone for the one that will be added.
	fullManaList=getMana(targetPlayer)
	for additionalTarget in additionalTargetsList:
		if additionalTarget not in fullManaList:
			fullManaList.append(additionalTarget)
	count=len(fullManaList)
	#get valid targets from mana
	manaList=[card for card in fullManaList if re.search("Creature", card.Type) and not re.search("Evolution Creature", card.Type) and cardCostComparator(card,count,'<=',"Creature")]
	if me.isInverted: reverseCardList(manaList)
	manaChoice=askCard2(manaList, 'Choose a Creature to play from Mana')

	if type(manaChoice) is not Card:
		return
	remoteCall(targetPlayer, "toPlay", convertCardListIntoCardIDsList(manaChoice))

def fromGraveyardToMana(count=1, filterFunction='True', ask=False):
	mute()
	group=me.piles['Graveyard']
	if len(group)==0: return
	if ask:
		choice=askYN("Would you like to put {} Card(s) from Graveyard to Mana?".format(count))
		if choice!=1: return
	count=min(count,len(group))
	cardsInGroup=sort_cardList([c for c in group if (filterFunction=='True' or eval(filterFunction, allowed_globals, {'c': c}))])
	choices=askCard2(cardsInGroup, 'Search {} Card(s) to put to Mana'.format(count),minimumToTake=1,maximumToTake=count, returnAsArray=True)
	if not isinstance(choices,list):
			notify("{} finishes searching their {}.".format(me, group.name))
			return
	for c in choices:
		toMana(c)

def fromGraveyardAll(filterFunction='True', ask=False, moveToMana=True, moveToHand=False):
	group=me.piles['Graveyard']
	if len(group)==0: return
	if ask:
		choice=askYN("Would you like to move Cards from Graveyard?")
		if choice!=1: return
	cardsInGroup=sort_cardList([c for c in group if (filterFunction=='True' or eval(filterFunction, allowed_globals, {'c':c}))])
	if len(cardsInGroup)==0:
		notify("No Cards to move!")
		return
	for c in cardsInGroup:
		if moveToMana: toMana(c)
		elif moveToHand: toHand(c)

#delayedEffectDictionary is a dictionary with those keys: {"delayTo", "card", "effects", "requireCardOnFieldToActivate", "removeAfterActivation"}. Learn more from addDelayedEffect() function.
def fromDeckToField(group=me.Deck, count=1, filterFunction='True', delayedEffectDictionary=False):
	mute()
	ensureGroupObject(group)
	if len(group)==0: return
	notify('{} started searching their {}'.format(me, group.name))
	cardsInGroup=sort_cardList([card for card in group])
	validChoices=[c for c in cardsInGroup if (filterFunction=='True' or eval(filterFunction, allowed_globals, {'c':c}))]
	while (True):
		choices=askCard2(cardsInGroup, 'Choose {} Card(s) to play from the Deck'.format(count), maximumToTake=count,returnAsArray=True)
		if not isinstance(choices,list):
			shuffle(group)
			notify("{} finishes searching their {}.".format(me, group.name))
			return
		if all(c in validChoices for c in choices):
			for choice in choices:
				toPlay(choice)
				if delayedEffectDictionary:
					addDelayedEffect(delayedEffectDictionary, choice)
			break
	shuffle(group)
	notify("{} finishes searching their {}.".format(me, group.name))

def fromHandToMana(count=1, filterFunction='True', faceDown=False):
	mute()
	group=me.Hand
	if len(group)==0: return
	cardsInGroup=reverseCardList([card for card in group if (filterFunction=='True' or eval(filterFunction, allowed_globals, {'c':c}))])
	choices=askCard2(cardsInGroup, 'Choose {} Cards(s) to put from your hand to Mana'.format(count), maximumToTake=count,returnAsArray=True)
	if not isinstance(choices,list):return
	for choice in choices:
		toMana(choice, faceDown=faceDown)

def fromHyperspatial(count=1, filterFunction='True'):
	mute()
	if filterFunction=='True':
		cardList=[c for c in me.Hyperspatial]
	else:
		cardList=[c for c in me.Hyperspatial if eval(filterFunction,allowed_globals,{"c":c})]
	count=min(count, len(cardList))
	if count==0:
		whisper("No valid targets.")
		return
	choices=askCard2(cardList, "Select a Card to put from Hyperspatial Zone","Select", maximumToTake=count, returnAsArray=True)
	for choice in choices:
		toPlay(choice, clearWaitingFunctions=False)

# End of Automation Code

# MENU OPTIONS
# Battlezone Options
def flip(card, x=0, y=0):
	mute()
	card=ensureCardObjects(card)
	if (re.search("Psychic", card.Type)):
		forms=list(card.alternates)
		if len(forms)==2:
			altName=card.alternateProperty('awakening', 'name')
			if card.alternate is '':
				card.alternate='awakening'
				notify("{}'s' {} awakens to {}.".format(me, altName, card))
		else:
			current_index=forms.index(card.alternate)  # Find current form index
			oldName=card.alternateProperty(forms[current_index], 'name')
			next_index=(current_index + 1) % len(forms)  # Calculate next form index
			card.alternate=forms[next_index]  # Set to the next form
			altName=card.alternateProperty(forms[next_index], 'name')
			if card.alternate=='':
				notify("{}'s {} reverts to its default form {}.".format(me, oldName, card))
			else:
				notify("{}'s {} cycles to {}.".format(me, oldName, altName))
		align()
		return
	elif (re.search("Dragheart", card.Type)):
		# draghearts
		old=card.properties["Name"]
		forms=card.alternates
		if card.alternate is forms[0]:
			card.alternate=forms[1]
			notify("{}'s' {} dragonsolutions to {}.".format(me, old, card))
		elif card.alternate is forms[1]:
			# Is in 2nd form
			if len(forms)==2:
				# Not 3 sided
				card.alternate=forms[0]
				notify("{}'s {} reverts to {}.".format(me, old, card))
			else:
				# 3 sided card
				card.alternate=forms[2]
				notify("{}'s {} 3D dragonsolutions to {}.".format(me, old, card))
		elif card.alternate is forms[2]:
			card.alternate=forms[0]
			notify("{}'s {} reverts to {}.".format(me, old, card))
		align()
		return

	else:
		if card.isFaceUp:
			notify("{} flips {} Face-down.".format(me, card))
			card.isFaceUp=False
		else:
			card.isFaceUp=True
			notify("{} flips {} Face-up.".format(me, card))
		#Keep the card relative orientation (tapped/untapped) the same when flipping, and wide cards have their positions reversed relative to normal
		if(card.size=="wide" and isMana(card)):
			card.orientation ^= Rot90
			align()

def toHyperspatial(card, x=0, y=0, notifymute=False):
	mute()
	removeBaits(card)
	if card.alternate is not '' and re.search("{RELEASE}", card.Rules):
		flip(card)
		return
	else:
		card.resetProperties()
		if card.targetedBy:
			card.target(False)
		card.moveTo(me.Hyperspatial)
		align()
		if notifymute==False:
			notify("{}'s {} returns to the Hyperspatial Zone.".format(me, card))

def toSuperGacharange(card, x=0, y=0, notifymute=False):
	mute()
	if notifymute==False:
		notify("{}'s {} returns to the Bottom of the Super Gacharange Zone.".format(me, card))
	card.resetProperties()
	if card.targetedBy:
		card.target(False)
	card.moveToBottom(me.Gacharange)
	align()

def moveCards(args): #this is triggered every time a card is moved
	mute()
	clearWaitingFuncts()  # clear the waitingCard if ANY CARD moved
	player=args.player

	fromGroup=args.fromGroups[0]
	toGroup=args.toGroups[0]
	## Old vars are: player, card, fromGroup, toGroup, oldIndex, index, oldX, oldY, x, y, highlights, markers, faceup
	for card in args.cards:
		if player!=me:  ##Ignore for cards you don't control
			return
		##When a player moves top card of deck to bottom of deck
		if fromGroup==me.Deck and toGroup==me.Deck:
			if card==me.Deck.bottom():
				notify("{} moves a Card in their Deck to bottom".format(me))
			elif card==me.Deck.top():
				notify("{} moves a Card in their Deck to top".format(me))
			else:
				notify("{} moves a Card around in their Deck".format(me))
			return

		## This updates the evolution dictionary in the event one of the cards involved in an evolution leaves the battlezone.
		if table not in args.fromGroups:  ## we only want cases where a card is being moved from table to another group
			##notify("Ignored")
			return
		clearArrowOnMove(args)
		if card.targetedBy:
			card.target(False)
		card.resetProperties()
		evolveDict=eval(me.getGlobalVariable("evolution"), allowed_globals)
		#A flag to not save if no changes happened
		evolveDictModified=False
		for evo in evolveDict.keys():
			if Card(evo) not in table:
				del evolveDict[evo]
				evolveDictModified=True
			else:
				evolvedList=evolveDict[evo]
				for evolvedCard in evolvedList:
					if Card(evolvedCard) not in table:
						evolvedList.remove(evolvedCard)
						evolveDictModified=True
				if len(evolvedList)==0:
					del evolveDict[evo]
					evolveDictModified=True
				else:
					evolveDict[evo]=evolvedList
		if evolveDictModified:
			me.setGlobalVariable("evolution", str(evolveDict))

		sealDict=eval(me.getGlobalVariable("seal"), allowed_globals)
		#A flag to not save if no changes happened
		sealDictModified=False
		for sealId in sealDict.keys():
			if Card(sealId) not in table:
				del sealDict[sealId]
				sealDictModified=True
			else:
				sealList=sealDict[sealId]
				for sealCardId in sealList:
					if Card(sealCardId) not in table:
						sealList.remove(sealCardId)
						sealDictModified=True
				if len(sealList)==0:
					del sealDict[sealId]
					sealDictModified=True
				else:
					sealDict[sealId]=sealList
		if sealDictModified:
			me.setGlobalVariable("seal", str(sealDict))

def align():
	mute()
	global playerside  ##Stores the Y-axis multiplier to determine which side of the table to align to
	global sideflip  ##Stores the X-axis multiplier to determine if cards align on the left or right half
	if sideflip==0:  ##the 'disabled' state for alignment so the alignment positioning doesn't have to process each time
		return "BREAK"
	if Table.isTwoSided():
		if playerside==None:  ##script skips this if playerside has already been determined
			if me.isInverted:
				playerside=-1  # inverted (negative) side of the table
			else:
				playerside=1
		if sideflip==None:  ##script skips this if sideflip has already been determined
			playersort=sorted(getPlayers(), key=lambda
				player: player._id)  ##makes a sorted players list so its consistent between all players
			playercount=[p for p in playersort if
						   me.isInverted==p.isInverted]  ##counts the number of players on your side of the table
			if len(playercount)>2:  ##since alignment only works with a maximum of two players on each side
				whisper("Cannot align: Too many players on your side of the Table.")
				sideflip=0  ##disables alignment for the rest of the play session
				return "BREAK"
			if playercount[0]==me:  ##if you're the 'first' player on this side, you go on the positive (right) side
				sideflip=1
			else:
				sideflip=-1
	else:  ##the case where two-sided table is disabled
		whisper("Cannot align: Two-sided table is required for card alignment.")
		sideflip=0  ##disables alignment for the rest of the play session
		return "BREAK"

	cardorder=[[], [], []]
	evolveDict=eval(me.getGlobalVariable("evolution"), allowed_globals)
	sealDict=eval(me.getGlobalVariable("seal"), allowed_globals)
	for card in table:
		if card.controller==me and not isCastle(card) and not card.anchor and not card._id in list(
				itertools.chain.from_iterable(evolveDict.values())) and not card._id in list(
				itertools.chain.from_iterable(sealDict.values())):
			if isShield(card):
				cardorder[1].append(card)
			elif isMana(card):
				cardorder[2].append(card)
			else:  ##collect all creatures
				cardorder[0].append(card)

	temp=[c for c in cardorder[0] if c.size not in {"tall, square"}]
	bigCards=[c for c in cardorder[0] if c.size in {"tall, square"}]
	cardorder[0]=temp
	# remove all big cards from normal aligned ones
	xpos=80
	ypos=5 + 10 * max([len(evolveDict[x]) for x in evolveDict if Card(x) in cardorder[0]] or [1])
	for cardtype in cardorder:
		if cardorder.index(cardtype)==1:
			xpos=80
			ypos += 93 + 10 * max([len(evolveDict[x]) for x in evolveDict if Card(x) in cardorder[1]] or [1])
		elif cardorder.index(cardtype)==2:
			xpos=80
			ypos += 93 + 10 * max([len(evolveDict[x]) for x in evolveDict if Card(x) in cardorder[2]] or [1])
		for c in cardtype:
			x=sideflip * xpos
			y=playerside * ypos + (44 * playerside - 44)
			#special aligning for face-up wide cards
			differenceWideCardsWidth=c.width - 63
			differenceWideCardHeight=c.height - 88
			if differenceWideCardsWidth and playerside==-1 and c.isFaceUp:
				x -= differenceWideCardsWidth
			if differenceWideCardHeight and playerside==1 and c.isFaceUp:
				y -= differenceWideCardHeight
			if c.position!=(x, y):
				c.moveToTable(x, y)
			xpos += 79
	for evolution in evolveDict:
		count=0
		reposition=False
		for evolvedCard in evolveDict[evolution]:
			evoCard=Card(evolution)
			bait=Card(evolvedCard)
			x, y=evoCard.position
			count += 1
			newPosition=(x, y - 10 * count * playerside)
			if bait.position!=newPosition:
				bait.moveToTable(*newPosition)
				reposition=True
			if reposition:
				if isShield(evoCard) and bait.isFaceUp:
					bait.sendToFront()
				else:
					bait.sendToBack()
	for seal in sealDict:
		sealedCard=Card(seal)
		cardSide=1
		if Table.isTwoSided():
			if sealedCard.controller.isInverted:
				cardSide=-1
			else:
				cardSide=1
		cx,cy=sealedCard.position
		for sealCardId in list(sealDict[seal]):
			sealCard=Card(sealCardId)
			sealCardMarker=sealCard.markers[sealMarker]
			if(not sealCard or not sealCardMarker or sealCard not in table):
				sealDict[seal].remove(sealCardId)
				if not sealDict[seal]:
					del sealDict[seal]
				me.setGlobalVariable("seal", str(sealDict))
				align()
				return
			newPosition=(cx  + (sealedCard.width / 2 - sealCard.width / 2 - 16 + 2 * sealCardMarker) * cardSide, cy + (sealedCard.height / 2 - sealCard.height / 2 - 16 + 2 * sealCardMarker) * cardSide)
			if sealCard.position!=newPosition:
				sealCard.moveToTable(*newPosition, forceFaceDown=True)
			sealCard.sendToFront()
	# for landscape or large cards
	xpos=15
	if playerside==1:
		xpos -= 93
	ypos=5 + 10 * (max([len(evolveDict[x]) for x in evolveDict]) if len(evolveDict)>0 else 1)
	for c in bigCards:
		if playerside==1:
			xpos += max(c.width, c.height) + 10
		else:
			differenceSquareCards=c.width - 88
			xpos += differenceSquareCards
		x=-1 * sideflip * xpos
		y=playerside * ypos + (c.height/2 * playerside - c.height/2)
		if c.position!=(x, y):
			c.moveToTable(x, y)
		if playerside==-1:
			xpos += max(c.width-88, c.height) + 10 - differenceSquareCards

def displayDeck(group, x=0, y=0):
	if len([c for c in itertools.chain(table,me.Hand) if c.controller==me])>0 and not confirm("WARNING:This feature works with freshly loaded deck. Do you want to continue?"):
		return
	allZones=list(itertools.chain(me.deck, me.Hyperspatial, me.Gacharange))
	if len(allZones)==0:
		whisper("Load a deck first.")
		return
	rowOrder=askChoice("Select layout:", ["Singles layout", "Ladder layout", "Side layout"])
	if rowOrder==0:
		whisper("Operation canceled.")
		return
	defaultNumber={1:10,2:7,3:5}.get(rowOrder)
	rowLimit=askNumber("How many cards per row?", defaultNumber, alwaysReturnNumber=True)
	if rowLimit==0:
		whisper("Operation canceled.")
		return
	def isAlreadyAdded(c):
		return cardsAddedToList.get(c.name, None)
	sideflip=1
	if me.isInverted:
		sideflip=-1
	rows=[]
	cardsAddedToList={}
	cardsReduced=[]
	evolveDict=eval(me.getGlobalVariable("evolution"), allowed_globals)
	for card in allZones:
		existingCard=isAlreadyAdded(card)
		if rowOrder>1 and existingCard:
			baits=removeBaits(existingCard,evolveDict)
			baits.append(card)
			updateBaits(existingCard,baits, evolveDict)
			continue
		else:
			cardsReduced.append(card)
			cardsAddedToList[card.name]=card
	for card in cardsReduced:
		if rows and len(rows[-1])<rowLimit:
			rows[-1].append(card)
		else:
			rows.append([card])

	ypos=-88
	for row in rows:
		xpos=0
		if sideflip==-1:
			xpos-= 64*(rowLimit-1)
			if rowOrder==3:
				xpos-=13*(sum([len(evolveDict[x]) for x in evolveDict if Card(x) in row] or [0]))
		ypos+=89
		if rowOrder==2:
			ypos+= 10*max([len(evolveDict[x]) for x in evolveDict if Card(x) in row] or [0])
		for card in row:
			x=sideflip * xpos
			y=sideflip * ypos + (44 * sideflip - 44)
			differenceWideCardsWidth=card.width - 63
			differenceWideCardHeight=card.height - 88
			if differenceWideCardsWidth and sideflip==-1 and card.isFaceUp:
				x -= differenceWideCardsWidth
			if differenceWideCardHeight and sideflip==1 and card.isFaceUp:
				y -= differenceWideCardHeight
			if card.position!=(x, y):
				card.moveToTable(x, y)
			xpos += 64
			if rowOrder==3:
				xpos += 13*len(evolveDict.get(card._id, []))
	for evolution in evolveDict:
		count=0
		for evolvedCard in evolveDict[evolution]:
			evoCard=Card(evolution)
			bait=Card(evolvedCard)
			x, y=evoCard.position
			count += 1
			if rowOrder==2:
				y-= 10 * count * sideflip
			if rowOrder==3:
				x+= 13 * count * sideflip
			newPosition=(x , y)
			if bait.position!=newPosition:
				bait.moveToTable(*newPosition)
				bait.sendToBack()

#Clear Targets/Arrows
def clear(group, x=0, y=0):
	mute()
	global arrow
	arrow={}
	for card in group:
		if card.targetedBy:
			card.target(False)

def clearFunctionsAndTargets(group, x=0, y=0):
	clear(group)
	clearWaitingFuncts()

#Set Up Battlezone
def setup(group, x=0, y=0):
	mute()
	global arrow
	arrow={}
	cardsInTable=[c for c in table if c.controller==me and c.owner==me and not isPsychic(c)]
	cardsInHand=[c for c in me.hand if not isPsychic(c)]
	cardsInGrave=[c for c in me.piles['Graveyard'] if not isPsychic(c)]

	psychicsInTable=[c for c in table if c.controller==me and c.owner==me and isPsychic(c)]
	psychicsInHand=[c for c in me.hand if isPsychic(c)]
	psychicsInGrave=[c for c in me.piles['Graveyard'] if isPsychic(c)]

	gacharangeInTable=[c for c in table if c.controller==me and c.owner==me and isGacharange(c)]

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
		whisper("Not enough Cards in Deck")
		return

	cardsInDeck=[c for c in me.Deck]
	for card in cardsInDeck:
		if isPsychic(card):
			whisper("You cannot have Psychic Creatures in your Main Deck")
			return
		if isGacharange(card):
			whisper("You cannot have Gacharange Creatures in your Main Deck")
			return

	me.setGlobalVariable("shieldCount", "0")
	me.setGlobalVariable("evolution", "{}")
	me.setGlobalVariable("seal", "{}")
	me.Gacharange.shuffle()
	me.Deck.shuffle()

	for card in me.Deck.top(5): toShields(card, notifymute=True)
	for card in me.Deck.top(5): card.moveTo(card.owner.hand)
	align()
	notify("{} sets up their battle zone.".format(me))

def rollDie(group, x=0, y=0):
	mute()
	global diesides
	n=rnd(1, diesides)
	notify("{} rolls {} on a {}-sided die.".format(me, n, diesides))

def initiateRPS(group, x=0, y=0):
	mute()
	opponent=getTargetPlayer(onlyOpponent=True)
	if not opponent: return
	choice=askChoice('Pick Rock/Paper/Scissors:',['Rock','Paper','Scissors'])
	if choice==0: return
	remoteCall(opponent,'finishRPS',[me,choice])

def finishRPS(opponent,oppChoice):
	mute()
	choice=askChoice('Pick Rock/Paper/Scissors:',['Rock','Paper','Scissors'])
	if choice==0: notify("{} didn't make a choice!".format(me))
	choices={1: "Rock", 2: "Paper", 3: "Scissors"}
	rules={
		1: 3,  # Rock beats Scissors
		2: 1,  # Paper beats Rock
		3: 2   # Scissors beats Paper
	}
	if(choice==oppChoice):
		notify("It's a draw! - Both picked {}".format(choices[choice]))
	elif rules[choice]==oppChoice:
		notify("{} Wins! - {} beats {}".format(me, choices[choice], choices[oppChoice]))
	else:
		notify("{} Wins! - {} beats {}".format(opponent, choices[oppChoice], choices[choice]))

def createCard(group, x=0, y=0):
	mute()
	cardGuid, quantity=askCard(title="Choose a Card to create on the table.")
	if cardGuid and quantity:
		temporary=confirm("Make the chosen card(s) temporary? (Remove them from game if they leave the table.)")
		#We reverse temporary in the function call below, because it asks for persistant card.
		cards=table.create(cardGuid, x, y, quantity, not temporary)
		if not isinstance(cards,list): cards=[cards]
		notify('{} creates {} {} on the Table{}'.format(me, quantity, cards[0], " (Temporary)" if temporary else " (Persistent)"))
		align()

#untaps everything, creatures and mana
def untapAll(group=table, x=0, y=0, isNewTurn=False, clearWaitingFunctions=True):
	mute()
	group=ensureGroupObject(group)
	if clearWaitingFunctions:
		clearWaitingFuncts()
	evolveDict=eval(me.getGlobalVariable("evolution"), allowed_globals)
	silentSkillCards=[]
	for card in group:
		if not card.owner==me:
			continue
		if isSealedOrSeal(card):
			continue
		# Untap Creatures
		if card.orientation==Rot90:
			if not isNewTurn:
				card.orientation=Rot0
			elif not isCreature(card) or isBait(card, evolveDict) or not cardScripts.get(card.properties["Name"], {}).get('silentSkill'):
				if getAutoUntapCreaturesSetting():
					card.orientation=Rot0
			#Silent Skill Check
			else:
					silentSkillCards.append(card)
					continue
		# Untap Mana (wide cards are treated as untaped if Rot270)
		if isTapped(card) and getAutoUntapManaSetting():
			card.orientation^=Rot90
	for card in silentSkillCards:
		choice=askYN("Activate Silent Skill for {}?\n\n{}".format(card.properties["Name"], card.Rules), ["Yes", "No"])
		if choice!=1:
			card.orientation=Rot0
			continue
		notify('{} uses Silent Skill of {}'.format(me, card))
		functionList=list(cardScripts.get(card.properties["Name"]).get('silentSkill', []))
		# THERE ARE CURRENTLY NO SURVIVORS THAT HAVE SILENT SKILL
		for function in functionList:
			waitingFunct.append([card, function])
	notify("{} untaps all their Cards.".format(me))
	if isNewTurn:
		processOnTurnStartEffects()

#Default call for Destroy (del key), handles mass creature destruction effects
def destroyMultiple(cards, x=0, y=0):
	if len(cards)==1:
		destroy(cards[0])
	else:
		if me.isInverted: reverseCardList(cards)
		creatureList=[]
		for card in cards:
			if isCreature(card):
				creatureList.append(card)
			else:
				destroy(card)
		if creatureList:
			destroyAll(creatureList, dontAsk=True)

def tapMultiple(cards, x=0, y=0, clearFunctions=True): #batchExecuted for multiple cards tapped at once(manually)
	global lastExecutionTime, DEBOUNCE_DELAY, lastTappedCards
	currentTime=time.time()
	if currentTime - lastExecutionTime < DEBOUNCE_DELAY and any(c in lastTappedCards for c in cards):
		whisper('You are tapping and untapping the same Cards too quickly! Slow down!')
		return
	lastExecutionTime=currentTime
	lastTappedCards=cards

	mute()
	if clearFunctions:
		clearWaitingFuncts()
	mana=[card for card in cards if isMana(card)]
	creatures=[card for card in cards if isCreature(card)]
	tappedMana=0
	for card in creatures:
		processTapUntapCreature(card)

	for card in mana:
		card.orientation ^= Rot90
		#Wide cards are treated opposite to normal
		if (card.orientation & Rot90==Rot90 and (not card.isFaceUp or card.size!="wide")) or (card.orientation & Rot90==Rot0 and card.isFaceUp and card.size=="wide"):
			tappedMana+=1
	untappedMana=len(mana) - tappedMana

	if len(mana)==1:
		if tappedMana:
			notify('{} taps {} in Mana.'.format(me, mana[0]))
		else:
			notify('{} untaps {} in Mana.'.format(me,  mana[0]))
	elif len(mana)>1:
		if tappedMana>0 and untappedMana>0:
			notify('{} taps Mana {} and untaps {} Mana.'.format(me, tappedMana, untappedMana))
		elif tappedMana>0:
			notify('{} taps {} Mana.'.format(me, tappedMana))
		else:
			notify('{} untaps {} Mana.'.format(me, untappedMana))

def destroy(card, x=0, y=0, dest=False, ignoreEffects=False):
	mute()
	card=ensureCardObjects(card)
	if isSealed(card):
		choice=askYN('Are you sure you want to destroy Sealed Card?\n(All seals will be put to Graveyard.)')
		if choice!=1: return
		sealList=getSeals(card)
		for seal in sealList:
			toDiscard(seal)
	#Returns True if Shield leaves table or False if it stayed.
	def processShield(card):
		#check conditional trigger for cards like Awesome! Hot Spring Gallows or Traptops
		conditionalTrigger=False
		if cardScripts.get(card.properties["Name"], {}).get('onTrigger'):
			conditionalTrigger=True
			trigFunctions=list(cardScripts.get(card.properties["Name"]).get('onTrigger', []))
			for function in trigFunctions:
				if conditionalTrigger==False:
					break
				conditionalTrigger=function(card)
		if conditionalTrigger or re.search(r"SHIELD TRIGGER[\sPLUS]{0,}}", card.Rules, re.IGNORECASE):
			choice=askYN("Activate Shield Trigger for {}?\n\n{}".format(card.properties["Name"], card.Rules), ["Yes", "No", "Wait"])
			if choice==1:
				card.isFaceUp=True
				if card.targetedBy:
					card.target(False)
				notify("{} uses {}'s Shield Trigger.".format(me, card))
				processShieldBaits(card)
				toPlay(card, notifymute=True)
				return True
			elif choice==3 or choice==0:
				card.peek()
				notify("{} peeks at Shield#{}".format(me, card.markers[shieldMarker]))
				processShieldBaits(card)
				return False
		if re.search("{GUARD STRIKE}", card.Rules, re.IGNORECASE):
			choice=askYN("Activate Guard Strike for {}?\n\n{}".format(card.properties["Name"], card.Rules), ["Yes", "No", "Wait"])
			if choice==1:
				card.isFaceUp=True
				if card.targetedBy:
					card.target(False)
				notify("{} uses {}'s Guard Strike.".format(me, card))
				creatureList=[c for c in getCreatures() if c.owner!=me]
				if len(creatureList)>0:
					if me.isInverted: reverseCardList(creatureList)
					choice=askCard2(creatureList)
					if type(choice) is Card:
						notify('Guard Strike: {} cannot attack this turn.'.format(choice))
				else:
					whisper("No targets.")
			elif choice==3 or choice==0:
				card.peek()
				notify("{} peeks at Shield#{}".format(me, card.markers[shieldMarker]))
				return False
		shieldCard=card
		cardsInHandWithStrikeBackAbility=[c for c in me.hand if re.search("Strike Back", c.rules, re.IGNORECASE)]
		if len(cardsInHandWithStrikeBackAbility)>0:
			cardsInHandWithStrikeBackAbilityThatCanBeUsed=[]
			for cardInHandWithStrikeBackAbility in cardsInHandWithStrikeBackAbility:
				if re.search("Super Strike Back", cardInHandWithStrikeBackAbility.rules, re.IGNORECASE):  # special case for Deadbrachio
					if manaArmsCheck():
						cardsInHandWithStrikeBackAbilityThatCanBeUsed.append(cardInHandWithStrikeBackAbility)
				elif re.search("Strike Back.*Hunter", cardInHandWithStrikeBackAbility.rules):
					if re.search("Hunter", shieldCard.Race):  # special case for Aqua Advisor
						cardsInHandWithStrikeBackAbilityThatCanBeUsed.append(cardInHandWithStrikeBackAbility)
				elif re.search("Strike Back", cardInHandWithStrikeBackAbility.rules, re.IGNORECASE) and re.search(cardInHandWithStrikeBackAbility.Civilization, shieldCard.Civilization, re.IGNORECASE):
					cardsInHandWithStrikeBackAbilityThatCanBeUsed.append(cardInHandWithStrikeBackAbility)
			if len(cardsInHandWithStrikeBackAbilityThatCanBeUsed)>0:
				if confirm("Activate Strike Back by sending {} to the graveyard?\n\n{}".format(shieldCard.properties["Name"],
																							   shieldCard.Rules)):
					if me.isInverted: reverseCardList(cardsInHandWithStrikeBackAbilityThatCanBeUsed)
					choice=askCard2(cardsInHandWithStrikeBackAbilityThatCanBeUsed, 'Choose Strike Back to activate')
					if type(choice) is Card:
						shieldCard.isFaceUp=True
						toPlay(choice, notifymute=True)
						toDiscard(shieldCard)
						notify("{} destroys {} to use {}'s Strike Back.".format(me, shieldCard, choice))
						return True
		notify("{}'s Shield #{} is broken.".format(me, shieldCard.markers[shieldMarker]))
		if shieldCard.targetedBy:
			shieldCard.target(False)
		shieldCard.moveTo(shieldCard.owner.hand)
		processShieldBaits(shieldCard)
		return True

	def processShieldBaits(shieldCard):
		evolveDict=eval(me.getGlobalVariable("evolution"), allowed_globals)
		baits =	removeBaits(shieldCard, evolveDict)
		if baits:
			for bait in list(baits):
				if isShield(bait):
					shieldLeft=processShield(bait)
					if shieldLeft:
						baits.remove(bait)
				else:
					notify('{} moves {} from Shield to Hand'.format(bait.owner, bait))
					bait.moveTo(bait.owner.hand)
					baits.remove(bait)
			if shieldCard.markers[shieldMarker]:
				baits.insert(0, shieldCard)
			if len(baits)>1:
				topBait=baits.pop(0)
				updateBaits(topBait, baits, evolveDict)
			align()

	if isShield(card):
		if dest==True:
			toDiscard(card)
			return
		processShield(card)

	elif isMana(card) or ignoreEffects:
		toDiscard(card)
	else:
		cardToBeSaved=card
		possibleSavers=[c for c in getCreatures(me) if cardToBeSaved!=c and re.search(r"(?<!Shield )Saver",c.rules, re.IGNORECASE)]
		if len(possibleSavers)>0:
			if confirm("Prevent {}'s destruction by using a Saver on your side of the field?\n\n".format(
					cardToBeSaved.properties["Name"])):
				if me.isInverted: reverseCardList(possibleSavers)
				choice=askCard2(possibleSavers, 'Choose Saver to destroy')
				if type(choice) is Card:
					toDiscard(choice)
					notify("{} destroys {} to prevent {}'s destruction.".format(me, choice.properties["Name"], cardToBeSaved.properties["Name"]))
					return
		global wscount
		wscount=getWaveStrikerCount()
		toDiscard(cardToBeSaved)
		card=cardToBeSaved

		functionList=[]
		if cardScripts.get(card.properties["Name"], {}).get('onDestroy'):
			functionList=list(cardScripts.get(card.properties["Name"]).get('onDestroy', []))
		if re.search("Survivor", card.Race):
			survivors=getSurvivorsOnYourTable()
			for surv in survivors:
				if cardScripts.get(surv.properties["Name"], {}).get('onDestroy'):
					functionList.extend(cardScripts.get(surv.properties["Name"]).get('onDestroy', []))
		for index, function in enumerate(functionList):
			waitingFunct.insert(index + 1, [card, function])
		evaluateWaitingFunctions()

#taps specified Card
def tapThis(card, ask=True):
	if isTapped(card):
		if ask:
			choice=askYN("Would you like to Tap {}?".format(card.properties["Name"]))
			if choice!=1: return
		tapMultiple([card], clearFunctions=False)

#untaps creature
def untapCreature(card, ask=True):
	if card.orientation==Rot90:
		if ask:
			choice=askYN("Would you like to Untap {}?".format(card.properties["Name"]))
			if choice!=1: return
		tapMultiple([card], clearFunctions=False)

def untapCreatureAll(ask=True, filterFunction='True'):
	if filterFunction=='True':
		cardList=[c for c in getCreatures(me) if isTapped(c)]
	else:
		cardList=[c for c in getCreatures(me) if isTapped(c) if eval(filterFunction, allowed_globals, {"c":c})]
	if ask:
		choice=askYN("Would you like to Untap All Your Creatures?")
		if choice!=1: return
	tapMultiple(cardList, clearFunctions=False)

def shuffleCardList(cardList):
	rng=Random()
	for i in range(len(cardList) - 1, 0, -1):
		j=int(rng.random() * (i + 1))
		cardList[i], cardList[j]=cardList[j], cardList[i]
	return cardList

def shuffleToBottom(cards, x=0, y=0, notifymute=False):
	mute()
	cardNames=" ({})".format(", ".join('{}'.format(c) for c in cards if c.isFaceUp)) if any(c.isFaceUp for c in cards) else ""
	shuffleCardList(cards)
	for card in cards:
		src=card.group
		if card.isFaceUp:
			card.isFaceUp=False
		card.moveToBottom(me.Deck)
	if not notifymute:
		notify('{} shuffled {} Card(s){} from {} to the Bottom of their Deck'.format(me, len(cards), cardNames, src.name))

def showWelcomeMessage():
	mute()
	welcomeMessage="""WELCOME TO DUEL MASTERS ON OCTGN!\n────────────────────────────────────────
This platform provides manual play with some card effect automation, helping you enjoy smooth and engaging gameplay. Currently, over {} cards have scripts designed to speed up the action.

Make sure you have Image Packs installed and take a moment to learn key shortcuts—they’ll enhance your experience and keep the game flowing smoothly.

You will still need to handle a few things manually:
- Drawing a card at the start of each turn.
- Declaring and selecting attack targets.
- Tracking Creatures' Power changes from effects.
- Breaking shields.

If you find any issues or want to learn more about the project, you can open it by clicking 'Open Project Page' button.

(You can reopen this window at any moment by right-clicking on the table > Other Options: > Change Settings > Show Welcome Message)

──────────────Let's play!──────────────
"""

	choice=askChoice(welcomeMessage.format(len(cardScripts.keys())), ["Got it!", "Join IDC TCG Tournament Community" , "Open Project Page"], ["#902000","#5865F2", "#2b5ba9"])
	setSetting("welcomePage", True)
	if choice==2:
		openUrl("https://discord.gg/DkJXpTEBNe")
	if choice==3:
		openUrl("https://github.com/szefo09/dm-ocg-octgn")
	if choice>1:
		showWelcomeMessage()

def showSettingWindow(group,x=0,y=0):
	mute()
	options= {1: ("automations", "My Cards' Script Automation", lambda: getAutomationsSetting()),
				2: ("autoUntapCreatures", "Untap my Creatures at the start of your Turn", lambda: getAutoUntapCreaturesSetting()),
				3: ("autoUntapMana", "Untap my Mana at the start of your Turn", lambda: getAutoUntapManaSetting()),
				4: ("autoMoveSpellsAfterPlay", "Move my Spells to Graveyard after play", lambda: getAutoMoveSpellsAfterPlaySetting()),
				5: ("askBeforeDiscardingACardFromHand", "Ask before discarding Cards from my Hand", lambda: getAskBeforeDiscardingOwnCardsSetting()),
				6: ("showDialogSimultaneousCardEffects", "Pick order of simultaneous Card Effects activating", lambda: getDialogSimultaneousCardEffectsSetting())}
	ret=1
	while ret>0:
		names=[]
		colors=[]
		for value in options.values():
			names.append(value[1])
			colors.append("#6a6f76" if not value[2]() else "#2b5ba9")

		ret=askChoice("Toggle Automation Settings:\n(Those settings stay between games)", names, colors, ["Show Welcome Message", "Restore defaults"])
		if ret==-1:
			showWelcomeMessage()
			return
		if ret==-2:
			defaults={
				"automations": True,
				"autoUntapCreatures": True,
				"autoUntapMana": True,
				"autoMoveSpellsAfterPlay": True,
				"askBeforeDiscardingACardFromHand": False,
				"showDialogSimultaneousCardEffects": True}
			for key, value in defaults.items():
				setSetting(key, value)
			notify('{} restores the settings to defaults.'.format(me))
			return
		if ret>0:
			key, title, currentSetting = options[ret]
			newSetting = not currentSetting()
			setSetting(key, newSetting)
			notify('{} changes {} to: "{}"'.format(me, title, newSetting))

def getAutomationsSetting():
	return getSetting("automations", True)
def getAutoUntapCreaturesSetting():
	return getSetting("autoUntapCreatures", True)
def getAutoUntapManaSetting():
	return getSetting("autoUntapMana", True)
def getAutoMoveSpellsAfterPlaySetting():
	return getSetting("autoMoveSpellsAfterPlay", True)
def getAskBeforeDiscardingOwnCardsSetting():
	return getSetting("askBeforeDiscardingACardFromHand", False)
def getDialogSimultaneousCardEffectsSetting():
	return getSetting("showDialogSimultaneousCardEffects", True)
def getWelcomePageSetting():
	return getSetting("welcomePage", False)

#Deck Menu Options
def shuffle(group, x=0, y=0):
	mute()
	group=ensureGroupObject(group)
	if len(group)==0: return
	for card in group:
		if card.isFaceUp:
			card.isFaceUp=False
	group.shuffle()
	notify("{} shuffled their {}".format(me, group.name))

def draw(group=None, conditional=False, count=1, x=0, y=0, ask=False):
	mute()
	if group==None:
		group==me.Deck
	else:
		group=ensureGroupObject(group)
	if ask:
		choice=askYN("Would you like to Draw {} Card(s)?".format(count))
		if choice!=1: return
	for i in range(0, count):
		if len(group)==0:
			return
		if conditional==True:
			choiceList=['Yes', 'No']
			colorsList=['#FF0000', '#FF0000']
			choice=askChoice("Draw a card?", choiceList, colorsList)
			if choice!=1:return
		card=group[0]
		card.moveTo(card.owner.hand)
		notify("{} draws a Card.".format(me))

def drawX(group, x=0, y=0):
	group=(ensureGroupObject(group))
	if len(group)==0: return
	mute()
	count=askInteger("Draw how many cards?", 7)
	if count==None: return
	for card in group.top(count): card.moveTo(card.owner.hand)
	notify("{} draws {} Cards.".format(me, count))

#Discard top card
def mill(group, count=1, conditional=False, x=0, y=0):
	mute()
	if len(group)==0:
		notify("No Cards left in Deck!")
		return
	if conditional:
		choiceList=['Yes', 'No']
		colorsList=['#FF0000', '#FF0000']
		choice=askChoice("Discard top {} Cards?".format(count), choiceList, colorsList)
		if choice!=1:return
	if len(group) < count: count=len(group)
	for card in group.top(count):
		toDiscard(card, notifymute=True)
		notify("{} discards {} from top of Deck.".format(me, card))

#Discard top X cards
def millX(group, x=0, y=0):
	mute()
	if len(group)==0: return
	count=askInteger("Discard how many cards?", 1)
	if count==None: return
	for card in group.top(count): toDiscard(card, notifymute=True)
	notify("{} discards top {} cards of Deck.".format(me, count))

#Random discard function (from hand)
def randomDiscard(group, x=0, y=0, remote=False, count=1):
	mute()
	group=ensureGroupObject(group)
	count=min(count, len(group))
	if count==0:return
	shuffledGroup=shuffleCardList(list(group))
	toDiscard(shuffledGroup[:count], wasRandom=True, remote=remote)

def fromTopPickX(group, x=0, y=0):
	if len(group)==0: return
	count=askInteger("Look at how many cards?", 5)
	if count==None: return
	lookAtTopCards(num=count, count=count)

#Function used for "Detach Bait" option in right click menu for Evos. Returns newly removed card(s)
def detachBait(card, x=0, y=0, minimumToTake=None, maximumToTake=None):
	mute()
	cardList=[c for c in getCardBaits(card) if c.isFaceUp]
	if minimumToTake is None:
		minimumToTake=1
	if maximumToTake is None:
		maximumToTake=len(cardList)
	if len(cardList) < minimumToTake:
		whisper('No Cards to detach.')
		return []
	choices=askCard2(cardList, "Choose Card(s) to detach",minimumToTake=minimumToTake,maximumToTake=maximumToTake, returnAsArray=True)
	if not isinstance(choices,list): return []
	newBaitList=[c for c in cardList if c not in choices]
	notify('{} detaches {} from {}'.format(me, ", ".join('{}'.format(c) for c in choices), card))
	for choice in choices:
		toDiscard(choice, notifymute=True)
	updateBaits(card, newBaitList)
	align()
	return choices

#Function used for "Attach Bait" option in right click menu for Evos. Returns newly added card(s)
def attachBait(card, x=0, y=0):
	mute()
	cardList=[c for c in table if c!=card and not isShield(c) and not isMana(c) and c.owner==me and not isRemovedFromPlay(c)]
	if len(cardList)==0:
		whisper('No Cards on the field to attach.\nIf you want to attach Opponent\'s Cards, take control of them first.')
		return []
	if me.isInverted:
		reverseCardList(cardList)
	choices=askCard2(cardList, "Choose Card(s) to attach",maximumToTake=len(cardList), returnAsArray=True)
	if not isinstance(choices,list): return []
	notify('{} attaches {} to {}'.format(me, ", ".join('{}'.format(c) for c in choices), card))
	newBaitList=getCardBaits(card) + choices
	updateBaits(card, newBaitList)
	align()
	return choices

#apply a seal to a card.
def seal(card, x=0, y=0):
	mute()
	cardSide=1
	if Table.isTwoSided():
			if card.controller.isInverted:
				cardSide=-1
			else:
				cardSide=1
	group=me.Deck
	if len(group)==0:
		return
	if not card.isFaceUp and not confirm("Do you want to seal a face-down card?"):
		return
	topCard=group[0]
	cx, cy=card.position
	topCard.moveToTable(cx, cy, True)
	topCard.orientation=Rot90
	sealDict=eval(me.getGlobalVariable("seal"), allowed_globals)
	if card._id in sealDict:
		for cId in list(sealDict[card._id]):
			c=Card(cId)
			if c and not c.markers[sealMarker] or c not in table:
				sealDict[card._id].remove(cId)
		sealDict[card._id].append(topCard._id)
	else:
		sealDict[card._id]=[topCard._id]
	topCard.markers[sealMarker]=len(sealDict[card._id])
	topCard.moveToTable(cx  + (card.width / 2 - topCard.width / 2 - 16 + 2 * len(sealDict[card._id])) * cardSide, cy + (card.height / 2 - topCard.height / 2 - 16 + 2 * len(sealDict[card._id])) * cardSide, True)
	me.setGlobalVariable("seal", str(sealDict))
	notify('{} seals {} with the top Card of their Deck.'.format(me, card))

#Allow selection of opponent Elements
def sealOpponentElements(group, x=0, y=0):
	creatureList=[c for c in group if c.owner!=me and isElement(c) and not isBait(c)]
	creatureListCount=len(creatureList)
	deckCount=len(me.Deck)
	maxSeals=min(creatureListCount, deckCount)
	if maxSeals==0: return
	if me.isInverted: reverseCardList(creatureList)
	choices=askCard2(creatureList, "Select up to {} Elements to Seal".format(maxSeals), "Seal", 1, maxSeals, True)
	if not isinstance(choices,list): return
	for choice in choices:
		seal(choice)

#Add a marker to card
def addCustomMarker(card, x=0, y=0):
	marker, qty=askMarker()
	if marker!=shieldMarker and marker!=sealMarker:
		card.markers[marker] += qty

#Charge Top Card as Mana
def mana(group=None, count=1, ask=False, tapped=False, postAction="NONE", postArgs=[], postCondition='True', preCondition=True):
	mute()
	if group==None:
		group=me.Deck
	if not preCondition:
		return
	if ask:
		choice=askYN("Charge top {} Card(s) as Mana?".format(count))
		if choice!=1: return
	for i in range(0, count):
		if len(group)==0: return
		card=group[0]
		toMana(card, notifymute=True)
		if tapped and ((card.orientation & Rot90!=Rot90 and card.isFaceUp or card.size!='wide') or (card.orientation & Rot90!=Rot0 and card.size=='wide')):
			card.orientation ^= Rot90
		notify("{} charges {} from top of {} as Mana.".format(me, card, group.name))
	doPostAction(card, postAction, postArgs, postCondition)

#Charge Top Card as Mana Face-Down
def manaFaceDown(group, count=1, ask=False, tapped=False, postAction="NONE", postArgs=[], postCondition='True', preCondition=True):
	mute()
	if not preCondition:
		return
	if ask:
		choice=askYN("Charge top {} Card(s) as Mana Face-Down?".format(count))
		if choice!=1: return
	for i in range(0, count):
		if len(group)==0: return
		card=group[0]
		toMana(card, notifymute=True, faceDown=True)
		if tapped and card.orientation & Rot90!=Rot90:
			card.orientation ^= Rot90
		notify("{} charges {} from top of {} as Mana.".format(me, card, group.name))
	doPostAction(card, postAction, postArgs, postCondition)

#Reveal cards from top deck until a card with X cost or lower is revealed, play it, shuffle the rest to bottom of the deck.
def yobinion(group):
	mute()
	group=me.Deck
	if len(group)==0:
		return
	number=askNumber("Declare the card cost for Yobinion.", 1)
	if not number:
		return
	notify('{} resolves Yobinion {}'.format(me, number))
	cardList=[]
	for card in group:
		card.isFaceUp=True
		notify("{} reveals {}".format(me, card))
		if re.search('Creature', card.Type) and cardCostComparator(card, number, '<=', "Creature"):
			toPlay(card)
			break
		else:
			cardList.append(card)

	shuffleToBottom(cardList)

#Graveyard Menu Options
def chooseAndShuffleToBottom(group):
	choices=askCard2(group, "Select up to {} Cards to shuffle to the bottom of the Deck".format(len(group)), "Shuffle", 1, len(group), True)
	if not isinstance(choices, list): return
	shuffleToBottom(choices)

def doPostAction(card, postAction, postArgs, postCondition):
	# does something more in the effect, might be based on what the first card was; eg: Geo Bronze Magic or simple stuff like Skysword(shield comes after mana)
	# implement BounceIfCiv for Dondon Vacuuming Now? Maybe make a whole different function for ifCiv or ifRace just to evaluate the conditon based on args
	# For example, if there is "IfCiv" in postAction, check args for the civ, if there's "ifRace"(eg Eco Aini) etc. -> This can be done in a separate function instead of here
	if postAction=="NONE":
		return
	if postAction=="DrawIfCiv":  # eg Geo Bronze Magic
		for civs in postArgs:
			if re.search(civs, card.properties['Civilization']):
				draw(me.Deck, True)
				break
		return
	if postAction=="ManaIfCiv":  # eg Faerie Crystal
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
	cardList=getMana(me)
	count=len(cardList)
	if conditional==True:
		choiceList=['Yes', 'No']
		colorsList=['#FF0000', '#FF0000']
		choice=askChoice("Charge top {} cards to Mana?".format(count), choiceList, colorsList)
		if choice!=1: return
	for i in range(0, count):
		if len(group)==0: return
		card=group[0]
		toMana(card, notifymute=True)
		if card.orientation & Rot90!=Rot90:
			card.orientation ^= Rot90
	notify("{} charges top {} cards of {} as Mana.".format(me, count, group.name))

#Set Top Card as Shield
def shields(group=None, count=1, conditional=False, x=0, y=0):
	mute()
	if group==None:
		group==me.Deck
	if conditional==True:
		maxCount=count
		count=askInteger("Set how many cards as Shields? (Max={})".format(maxCount), maxCount)
		if count==0 or count>maxCount: return
	for card in group.top(count):
		if len(group)==0: return
		card=group[0]
		toShields(card, notifymute=True)
		notify("{} sets top card of {} as Shield.".format(me, group.name))

#Charge as Mana menu option / Ctrl+C
def toMana(card, x=0, y=0, notifymute=False, checkEvo=True, alignCheck=True, faceDown=False, tapped=False):
	mute()
	card=ensureCardObjects(card)
	if isMana(card) and (x or y):
		global civ_order
		for player in getPlayers():
			totalMana=getMana(player)
			totalUntappedMana=[c for c in totalMana if not isTapped(c)]
			unique_civilizations=sorted({"Colorless" if not card.isFaceUp else civ for card in totalUntappedMana for civ in card.Civilization.split('/')}, key=civ_order.index)
			whisper("{} has {} Mana in total. ({} Untapped)\nAvailable: {}".format(player, len(totalMana), len(totalUntappedMana), ", ".join(unique_civilizations)))
		return
	cardWasElement=isElement(card) and checkEvo
	if checkEvo:
		baitList=removeBaits(card)
		if not (getAutomationsSetting() and cardWasElement and card.properties["Name"]=="Soul Phoenix, Avatar of Unity"):
			for baitCard in baitList:
				toMana(baitCard, checkEvo=False, alignCheck=False, faceDown=faceDown)
	if isPsychic(card):
		toHyperspatial(card)
		if cardWasElement: handleOnLeaveBZ(card)
		return
	if isGacharange(card):
		toSuperGacharange(card)
		if cardWasElement: handleOnLeaveBZ(card)
		return
	card.resetProperties()
	if card.targetedBy:
		card.target(False)
	src=card.group
	srcName=card.group.name
	if isShield(card):
		srcName="Shield #{}".format(card.markers[shieldMarker])
		card.markers[shieldMarker]=0
		card.isFaceUp=not faceDown
	if card.group!=table:
		card.moveToTable(0, 0, faceDown)
	else:
		card.sendToFront()
		card.isFaceUp=not faceDown
	#Wide cards are treated as untapped with Rot270
	if card.size=="wide" and not faceDown:
		card.orientation=Rot270
	else:
		card.orientation=Rot180
	if re.search("/", card.Civilization) and not faceDown:  # multi civ card
		card.orientation^=Rot90
	if tapped and not isTapped(card):
		card.orientation^=Rot90
	if alignCheck:
		align()
	if notifymute==False:
		if src==card.owner.hand:
			notify("{} charges {} as Mana.".format(me, card))
		else:
			notify("{} charges {} from {} as Mana.".format(me, card, srcName))
	if faceDown:
		card.peek()
	#Handle on Remove From Battle Zone effects:
	if cardWasElement: handleOnLeaveBZ(card)

#Wrapper function for toManaFace to call from Menu or by Ctrl+Shift+C
def toManaFaceDown(card, x=0, y=0, tapped=False):
	toMana(card, x, y, faceDown=True, tapped=tapped)

#Set as shield menu option / Ctrl+H (both from hand and battlezone)
def toShields(card, x=0, y=0, notifymute=False, alignCheck=True, checkEvo=True):
	mute()
	card=ensureCardObjects(card)
	if isShield(card):
		whisper("This is already a Shield.")
		return
	cardWasElement=isElement(card) and checkEvo
	if checkEvo:
		baitList=removeBaits(card)
		if not (getAutomationsSetting() and cardWasElement and card.properties["Name"]=="Soul Phoenix, Avatar of Unity"):
			for baitCard in baitList:
				toShields(baitCard, checkEvo=False, alignCheck=False)
	if isPsychic(card):
		toHyperspatial(card)
		if cardWasElement: handleOnLeaveBZ(card)
		return
	if isGacharange(card):
		toSuperGacharange(card)
		if cardWasElement: handleOnLeaveBZ(card)
		return
	count=int(me.getGlobalVariable("shieldCount")) + 1
	me.setGlobalVariable("shieldCount", convertToString(count))
	if notifymute==False:
		if isElement(card) or isMana(card):  ##If a visible card in play is turning into a shield, we want to record its name in the notify
			notify("{} sets {} as Shield #{}.".format(me, card, count))
		elif card.group==card.owner.piles['Graveyard']:
			notify("{} sets {} from Graveyard as Shield #{} .".format(me, card, count))
		else:
			notify("{} sets a card from {} as Shield #{}.".format(me, card.group.name, count))
	card.resetProperties()
	if card.targetedBy:
		card.target(False)
	if card.group!=table:
		card.moveToTable(0, 0, True)
	else:
		card.sendToFront()
	if card.isFaceUp:
		card.isFaceUp=False
	if card.orientation!=Rot0:
		card.orientation=Rot0
	card.markers[shieldMarker]=count
	if alignCheck:
		align()

	#Handle on Remove From Battle Zone effects:
	if cardWasElement: handleOnLeaveBZ(card)

#Play Card menu option (both from hand and battlezone)
def toPlay(card, x=0, y=0, notifymute=False, evolveText='', ignoreEffects=False, isEvoMaterial=False, clearWaitingFunctions=True):
	mute()
	card=ensureCardObjects(card)
	#global alreadyEvaluating #is true when already evaluating some functions of the last card played, or when continuing after wait for Target
	#notify("DEBUG: AlreadyEvaluating is "+str(alreadyEvaluating))
	src=card.group
	srcName=card.group.name
	if src==card.owner.hand and clearWaitingFunctions:
		clearWaitingFuncts() # this ensures that waiting for targers is cancelled when a new card is played from hand(not when through a function).
	evolveDict=eval(me.getGlobalVariable("evolution"), allowed_globals)
	if isMana(card):
		srcName="Mana"
	if isShield(card):
		baits=removeBaits(card, evolveDict)
		if baits and all(isShield(bait) for bait in baits):
			topBait=baits.pop(0)
			updateBaits(topBait, baits)
		srcName="Shield #{}".format(card.markers[shieldMarker])
		card.markers[shieldMarker]=0
	if card.group==table:
		if evolveDict:
			removeFromBaits(card, evolveDict)
		card.orientation=Rot0
		card.isFaceUp=True
		card.sendToFront()
	#Handle Evolutions coming to Play
	if not re.search("Star Max Evolution", card.Type,re.IGNORECASE) and (re.search("Evolution", card.Type) or re.search('{NEO EVOLUTION}', card.Rules))and not isEvoMaterial:
		targets= []
		textBox='Select Creature(s) to put under Evolution{}'
		#Deck Evolutions
		if re.search("Deck Evolution", card.Rules, re.IGNORECASE):
			if len(me.Deck)==0: return
			if re.search("Mad Deck Evolution", card.Rules, re.IGNORECASE):
				notify("{} uses Deck Evolution of {}".format(me, card))
				topCards=[]
				cardCount=min(3,len(me.Deck))
				for i in range(0, cardCount):
					c=me.Deck[i]
					topCards.append(c)
					c.isFaceUp=True
					notify("{} reveals {} from the top of the Deck".format(me, c))
				topCreatures=[c for c in topCards if re.search("Creature", c.Type)]
				if len(topCreatures)==0:
					notify("No Creatures revealed.")
					for c in topCards:
						toDiscard(c)
					return
				choice=askCard2(topCreatures,textBox.format(''))
				if type(choice) is not Card:
					return
				topCards.remove(choice)
				for c in topCards:
					toDiscard(c)
				toPlay(choice, 0, 0, True, ' for Deck Evolution of {}'.format(card),True, True)
				targets=[choice]
			else:
				topC=me.Deck[0]
				topC.isFaceUp=True
				notify("{} uses Deck Evolution of {}".format(me, card))
				notify("{} reveals {} from the top of the Deck".format(me, topC))
				if re.search("Creature", topC.Type):
					choice=askYN()
					if choice!=1:
						return
					toPlay(topC, 0, 0, True, ' for Deck Evolution of {}'.format(card),True, True)
					targets=[topC]
				else:
					notify("{} is not a Creature".format(topC))
					topC.isFaceUp=False
					return
		#Graveyard Evolutions
		elif re.search(r"Graveyard(?:\s+Galaxy)?(?:\s+Vortex)?\s+evolution", card.Rules, re.IGNORECASE):
			materialList=[c for c in me.piles['Graveyard'] if re.search("Creature",c.Type)]
			isMultiMaterial=False
			if re.search("Super Infinite Graveyard evolution", card.Rules, re.IGNORECASE) or re.search(r"Graveyard(?:\s+Galaxy)?(?:\s+Vortex)\s+evolution", card.Rules, re.IGNORECASE):
				isMultiMaterial=True
			maximumToTake=1
			if(isMultiMaterial):
				maximumToTake=len(materialList)
			targets=askCard2(materialList,textBox.format(' from Graveyard'),maximumToTake=maximumToTake, returnAsArray=True)
			if not isinstance(targets,list): return
			for target in targets:
				toPlay(target, 0, 0,True,' for Graveyard Evolution of {}'.format(card),True, True)
		#Mana Evolutions
		elif re.search(r"Mana(?:\s+Galaxy)?(?:\s+Vortex)?\s+evolution", card.Rules, re.IGNORECASE):
			materialList=[c for c in getMana(me) if re.search("Creature", c.Type)]
			if me.isInverted: reverseCardList(materialList)
			isMultiMaterial=False
			maximumToTake=1
			if re.search(r"Mana(?:\s+Galaxy)?(?:\s+Vortex)\s+evolution", card.Rules, re.IGNORECASE):
				isMultiMaterial=True
				maximumToTake=len(materialList)
			if len(materialList)==0:
					whisper("Cannot play {}, you don't have any Creatures in Mana Zone for it.".format(card))
					return
			textBox=textBox.format(' from Mana')
			targets=askCard2(materialList,textBox, maximumToTake=maximumToTake,returnAsArray=True)
			if not isinstance(targets,list): return
			for target in targets:
				toPlay(target,0, 0,True,' for Mana Evolution of {}'.format(card),True, True)
		#Hand Evolutions
		elif re.search("Hand Evolution", card.Rules, re.IGNORECASE):
			materialList=[c for c in me.hand if re.search("Creature", c.Type) and c!=card]
			reverseCardList(materialList)
			if len(materialList)==0:
					whisper("Cannot play {}, you don't have any other Creatures in Hand for it.".format(card))
					return
			choice=askCard2(materialList,textBox.format(' from Hand'))
			if type(choice) is not Card: return
			toPlay(choice,0, 0,True,' for Hand Evolution of {}'.format(card),True, True)
			targets=[choice]
		#Omega Evolutions
		elif re.search("Super Infinite evolution Omega", card.Rules, re.IGNORECASE) or re.search("Galaxy Vortex Evolution Omega", card.Rules, re.IGNORECASE):
			evoTypeText='Super Infinite evolution Omega'
			isGalaxy=False
			materialListGY=[c for c in me.piles['Graveyard'] if re.search("Creature",c.Type)]
			materialListMana=[c for c in getMana(me) if re.search("Creature", c.Type)]
			materialListBZ=getElements(me)
			if me.isInverted:
				reverseCardList(materialListMana)
				reverseCardList(materialListBZ)
			if re.search("Galaxy Vortex Evolution Omega", card.Rules, re.IGNORECASE):
				isGalaxy=True
				evoTypeText='Galaxy Vortex Evolution Omega'
			targetsGY=[]
			targetsMana=[]
			targetsBZ=[]
			whisper("Pick cards from Graveyard, Mana and Battle Zone in that order. Close the Pop-Up to proceed to the next selection.")

			maximumToTake=len(materialListGY)
			if maximumToTake>0:
				if isGalaxy:
					maximumToTake=1
				targetsGY=askCard2(materialListGY,textBox.format(' from Graveyard'), maximumToTake=maximumToTake, returnAsArray=True)
				if not isinstance(targetsGY, list): targetsGY=[]

			maximumToTake=len(materialListMana)
			if maximumToTake>0:
				if isGalaxy:
					maximumToTake=1
				targetsMana=askCard2(materialListMana,textBox.format(' from Mana'), maximumToTake=maximumToTake,returnAsArray=True)
				if not isinstance(targetsMana, list): targetsMana=[]

			maximumToTake=len(materialListBZ)
			if maximumToTake>0:
				if isGalaxy:
					maximumToTake=1
			targetsBZ=askCard2(materialListBZ,textBox.format(' from Battle Zone'), maximumToTake=maximumToTake, returnAsArray=True)
			if not isinstance(targetsBZ, list): targetsBZ=[]

			targets=targetsGY + targetsMana + targetsBZ
			if len(targets) < 1:
				whisper('No targets selected!')
				return
			for target in targetsGY:
				toPlay(target,0, 0,True,' for {} of {}'.format(evoTypeText, card),True, True)
			for target in targetsMana:
				toPlay(target,0, 0,True,' for {} of {}'.format(evoTypeText,card),True, True)
		#Default or Vortex Evolution
		else:
			targets=[c for c in getElements(me) if c.targetedBy==me]
			clear(targets)
			if len(targets)==0:
				materialList=[c for c in getElements(me) if c!=card]
				if me.isInverted: reverseCardList(materialList)
				minimumToTake=1
				isNeoEvolution=False
				if re.search('{NEO EVOLUTION}', card.Rules):
					minimumToTake=0
					isNeoEvolution=True
				elif len(materialList)==0:
					whisper("Cannot play {}, you don't have any Cards in Battle Zone for it.".format(card))
					whisper("Hint: Play a Creature or Gear first to evolve this card onto.")
					return
				isMultiMaterial=False
				maximumToTake=1
				if re.search(r"(?:Galaxy\s+)?Vortex Evolution",card.Rules, re.IGNORECASE) or re.search('Super Infinite Evolution', card.Rules, re.IGNORECASE):
					maximumToTake=len(materialList)
					isMultiMaterial=True
				if len(materialList)>0:
					targets=askCard2(materialList,'Select Card(s) to use as Material for Evolution.', minimumToTake=minimumToTake, maximumToTake=maximumToTake, returnAsArray=True)
					if not isinstance(targets, list): targets=[]

		if len(targets)==0:
			if not isNeoEvolution:
				whisper("No targets for {}'s Evolution selected. Aborting...".format(card))
				return
		else:
			if re.search('{NEO EVOLUTION}', card.Rules):
				card.Type='Neo Evolution Creature'
			evolveText=", evolving {}".format(", ".join('{}'.format(c) for c in targets))
			updateBaits(card, targets, evolveDict)

	if card.group!=table:
		card.moveToTable(0, 0)
	align()
	if notifymute==False and not card.hasProperty('Name1'):
		if src==card.owner.hand:
			notify("{} plays {}{}.".format(me, card, evolveText))
		else:
			notify("{} plays {}{} from {}.".format(me, card, evolveText, srcName))

	if not ignoreEffects:
		card.resetProperties()
		#Twin Pact Handling
		if card.hasProperty('Name1'):
			choice=askYN('Which Side?',[card.properties['Name1'], card.properties['Name2']])
			if choice==0: return
			card.properties["Name"]=card.properties['Name{}'.format(choice)]
			card.Civilization=card.properties['Civilization{}'.format(choice)]
			card.Cost=card.properties['Cost{}'.format(choice)]
			card.Type=card.properties['Type{}'.format(choice)]
			card.Race=card.properties['Race{}'.format(choice)]
			card.Rules=card.properties['Rules{}'.format(choice)]
			if src==card.owner.hand:
				notify("{} plays {} as {}{}.".format(me,card,card.properties['Name{}'.format(choice)],evolveText))
			else:
				notify("{} plays {} as {}{} from {}.".format(me,card,card.properties['Name{}'.format(choice)],evolveText, src.name))
		processExLife(card)
		functionList=[]
		if metamorph() and cardScripts.get(card.properties["Name"], {}).get('onMetamorph'):
			functionList=list(cardScripts.get(card.properties["Name"]).get('onMetamorph', []))
			notify("Metamorph for {} activated!".format(card))
		elif re.search('Survivor', card.Race):
			survivors=getSurvivorsOnYourTable()
			#for non-sharing survivors
			if card not in survivors:
				survivors.insert(0, card)
			for surv in survivors:
				if cardScripts.get(surv.properties["Name"], {}).get('onPlay'):
					functionList.extend(cardScripts.get(surv.properties["Name"]).get('onPlay', []))
		elif cardScripts.get(card.properties["Name"], {}).get('onPlay'):
			functionList=list(cardScripts.get(card.properties["Name"]).get('onPlay', []))

		for index, function in enumerate(functionList):
			waitingFunct.insert(index + 1, [card, function]) # This fuction will be queued(along with the card that called it). RN it's waiting.
			#notify("DEBUG: Function added to waiting list: "+str(function))
		evaluateWaitingFunctions() #evaluate all the waiting functions. This thing stop evaluation if a function returns true(ie. its waiting for target)
	if not waitingFunct: #Don't put card in grave if it's waiting for some effect.
		#BUG: This check will always be reached first by a spell without any automation being played with Hogan Blaster. And since HB is still in waitingFunct...the spell never goes to grave automatically
		#Soulution: Instead of this simple chcek make an intermediate function that checks if this card is in waitingFunct. If not, then do endOfFunctionality.
		endOfFunctionality(card)

def endOfFunctionality(card):
	if card and card.controller==me and isSpellInBZ(card) and getAutoMoveSpellsAfterPlaySetting():
		if any(name in card.properties["Name"] for name in {'Boomerang Comet', 'Pixie Cocoon'}) or (re.search("Charger", card.properties["Name"], re.IGNORECASE) and re.search("Charger", card.rules, re.IGNORECASE)):
			toMana(card)
		else:
			card.resetProperties()
			if card.targetedBy:
				card.target(False)
			card.moveTo(card.owner.piles['Graveyard'])
	align()

def gacharangeSummon(group, x=0, y=0, notifymute=True, ignoreEffects=False, isEvoMaterial=False):
	if len(group)>0:
		card=group.top()
		toPlay(card, x, y, notifymute, '', ignoreEffects, isEvoMaterial)
		notify('{} Gacharange Summons {}'.format(me, card))
	else:
		whisper('No cards in Super Gacharange Zone to Gacharange Summon.')

#Discard Card menu option
def toDiscard(cards, x=0, y=0, notifymute=False, alignCheck=True, checkEvo=True, wasRandom=False, remote=False):
	mute()
	cards=ensureCardObjects(cards, True)
	if any([c.group==me.Hand for c in cards]) and getAskBeforeDiscardingOwnCardsSetting() and remote:
		if askYN("Card(s) will be discarded from your hand.",choices=["Continue", "Cancel"])!=1:
			notify("{} canceled the discard of Card(s) in their Hand.".format(me))
			return
	for card in cards:
		src=card.group
		cardWasElement=isElement(card) and checkEvo
		if src==table and checkEvo:
			baitList=removeBaits(card)
			if not (getAutomationsSetting() and cardWasElement and card.properties["Name"]=="Soul Phoenix, Avatar of Unity"):
				for baitCard in baitList:
					toDiscard(baitCard, checkEvo=False, alignCheck=False)
		if isPsychic(card):
			toHyperspatial(card)
			if cardWasElement: handleOnLeaveBZ(card)
			return
		if isGacharange(card):
			toSuperGacharange(card)
			if cardWasElement: handleOnLeaveBZ(card)
			return
		cardWasMana=isMana(card)
		card.resetProperties()
		if card.targetedBy:
			card.target(False)
		card.moveTo(card.owner.piles['Graveyard'])
		if notifymute==False:
			if src==table:
				if cardWasMana:
					notify("{} destroys {} from mana.".format(me, card))
				else:
					notify("{} destroys {}.".format(me, card))
				if alignCheck:
					align()
			else:
				notify("{} {}discards {} from {}.".format(me,"randomly " if wasRandom else "", card, src.name))
		#Handle onDiscard effects
		if src==card.owner.hand:
			functionList=[]
			if cardScripts.get(card.properties["Name"], {}).get('onDiscard'):
				functionList=list(cardScripts.get(card.properties["Name"]).get('onDiscard'))
				for index, function in enumerate(functionList):
					waitingFunct.insert(index + 1, [card, function])
		if cardWasElement: handleOnLeaveBZ(card)
	orderEvaluatingFunctions()
	evaluateWaitingFunctions()

	#Handle on Remove From Battle Zone effects:

#Move To Hand (from battlezone)
def toHand(card, show=True, x=0, y=0, alignCheck=True, checkEvo=True):
	mute()
	card=ensureCardObjects(card)
	src=card.group
	cardWasElement=isElement(card) and checkEvo
	if card.targetedBy:
		card.target(False)
	if checkEvo:
		baitList=removeBaits(card)
		if not (getAutomationsSetting() and cardWasElement and card.properties["Name"]=="Soul Phoenix, Avatar of Unity"):
			for baitCard in baitList:
				toHand(baitCard, checkEvo=False, alignCheck=False)
	if isPsychic(card):
		toHyperspatial(card)
		if cardWasElement: handleOnLeaveBZ(card)
		return
	if isGacharange(card):
		toSuperGacharange(card)
		if cardWasElement: handleOnLeaveBZ(card)
		return
	if show:
		card.isFaceUp=True
		# need to use just card instead of card.Name for link to card
		# but it won't show as card name if card is not visible to a player, so turning it face up first
		notify("{} moved {} from {} to Hand.".format(me, card, src.name))
		card.resetProperties()
		card.moveTo(card.owner.hand)
	else:
		# here, move the card to hand first so it will only show card link to only the player who can see the hand
		# if you show first then move to hand 'card' won't show card name to the owner in the notify message
		card.moveTo(card.owner.hand)
		card.resetProperties()
		notify("{} moved {} from {} to Hand.".format(me, card, src.name))
	if alignCheck:
		align()

	#Handle on Remove From Battle Zone effects:
	if cardWasElement: handleOnLeaveBZ(card)

#Move to Bottom (from battlezone)
def toDeckBottom(card, x=0, y=0):
	mute()
	toDeck(card, bottom=True)

def handleOnLeaveBZ(card):
	functionList=[]
	if cardScripts.get(card.properties["Name"],{}).get('onLeaveBZ'):
		functionList=list(cardScripts.get(card.properties["Name"]).get('onLeaveBZ'))
		for index, function in enumerate(functionList):
			waitingFunct.insert(index + 1, [card,function])
		evaluateWaitingFunctions()

#Move to Topdeck (from battlezone)
def toDeck(card, bottom=False):
	mute()

	def chooseCardPlacementInDeck(cardList):
			if len(cardList)==1:
				choices=cardList
			else:
				choices=askCard2(cardList, "Rearrange the Cards to put to {} of the Deck".format("bottom" if bottom else "top"), minimumToTake=0)
			if not bottom:
				reverseCardList(choices)
			for c in choices:
				notify("{} moves {} to {} of Deck.".format(me, c, "bottom" if bottom else "top"))
				c.resetProperties()
				if bottom:
					c.moveToBottom(c.owner.Deck)
				else:
					c.moveTo(c.owner.Deck)

	card=ensureCardObjects(card)
	if card.targetedBy:
		card.target(False)
	cardWasElement=isElement(card)
	if isPsychic(card):
		chooseCardPlacementInDeck(removeBaits(card))
		toHyperspatial(card)
		if cardWasElement: handleOnLeaveBZ(card)
		return
	if isGacharange(card):
		baitList=removeBaits(card)
		chooseCardPlacementInDeck(removeBaits(card))
		toSuperGacharange(card)
		if cardWasElement: handleOnLeaveBZ(card)
		return

	cardList=removeBaits(card)  # baits
	if getAutomationsSetting() and cardWasElement and card.properties["Name"]=="Soul Phoenix, Avatar of Unity":
		cardList=[]
	cardList.insert(0, card)  # top card as well
	chooseCardPlacementInDeck(cardList)
	align()
	#Handle on Remove From Battle Zone effects:
	if cardWasElement: handleOnLeaveBZ(card)

allowed_globals={
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
	'Rot0': Rot0,
	'Rot90': Rot90,
	'Rot180': Rot180,
	'Rot270': Rot270,
	'isElement': isElement
}