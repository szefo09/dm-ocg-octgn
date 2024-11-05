## This is the Duel Masters OCG Definition for OCTGN 
#### based on https://github.com/PranjalBishtNX/dm-ocg-octgn with new automations and fixes for existing cards.

#### *I'm a freelance developer doing this in my free time. If you feel that what I'm doing it worthwhile for the community and deserves a coffee, consider donating to [my Paypal](<https://www.paypal.com/paypalme/szefo09>)*

All automations are based on python. OCTGN plugin dev refernce: https://github.com/octgn/OCTGN/wiki https://github.com/octgn/OCTGN/wiki/OCTGN-Python-3.1.0.2-API-Reference

## Changelog

### New Features
- **New Cards Added**:
  - **Apocalypse Vise**: Destroy creatures up to a combined total power of 8000.
  - **Bubble Lamp** and **Illusionary Merfolk**: Conditional draw mechanics.
  - **Carnival Totem**: Added effect.
  - **Cranium Clamp**: Opponent chooses two cards from their hand to discard.
  - **Critical Blade and Comet Missile**: Added as new spell options.
  - **Dolmarks, the Shadow Warrior**: Similar to Rothus, but also burns mana.
  - **Emergency Typhoon**: Draw up to two cards, then discard one.
  - **Magmarex**: Destroys all creatures with exactly 1000 power.
  - **Mechadragon's Breath**: Choose a power number; all creatures with that power are destroyed.
  - **Miraculous Plague**: Select two cards from the field and opponent chooses one to take to their hand, and the other is sent to Graveyard. Repeat for cards in Mana Zone.
  - **Proclamation of Death**: Rothus-like effect, prompting destruction.
  - **Slash Charger**: View entire deck of selected player, pick one card to send to Graveyard.
  - **Soulswap**: Select side, pick a creature on the field to send to mana, and choose a creature to play from mana.
  - **Galklife Dragon**: Destroys all cards with 4000 Power or less from Light civilization
  - **Scarlet Skyterror**: Destroys all cards with Blocker.
  - **Death Cruzer, the Annihilator**: Destroys all other creatures of the player.
  - **Dorballom, Lord of Demons**: Destroys all non-darkness creatures and puts non-darkness mana into graveyard.
  - **Stallob the Lifequasher**: Destroys all creatures after being destroyed.
  - **Jewel Spider**: After it's destroyed, you can target a shield and it comes to your hand.


- **Wavestrikers Added**:
  - **Wavestriker cards got special encapsulated effects that trigger only if Wavestriker is active** *(3 or more on board)*.
  - **New Cards Added**:
    - Angila, Electro-Mask
    - Aqua Trickster,
    - Bonfire Lizard,
    - Hazaria, Duke of Thorns,
    - Eviscerating Warrior Lumez,
    - Flame Trooper Goliac,
    - Jagila the Hidden Pillager,
    - Klujadras,
    - Revival Soldier,
    - Skyscraper Shell,
    - Steamroller Mutant,
    - Trombo, Fractured Doll,
    - Uncanny Turnip
- **Survivor Automation**: Shared effects are now automated for Survivors.
- **Tap Effects Added**: 
  - **During Your Turn, if you tap an automated Creature with Tap Effect, you'll get a prompt if you want to use the Tap effect!** *You can bypass the prompt by declaring an attack by arrow targeting before tapping.*
  - **New Cards Added**:
    - Bliss Totem, Avatar of Luck,
    - Charmilia, the Enticer,
    - Cosmogold, Spectral Knight,
    - Deklowaz, the Terminator,
    - Rikabu's Screwdriver,
    - Rondobil, the Explorer,
    - Tanzanyte, the Awakener,
    - Techno Totem (only Tap effect for now)
- **Silent Skill Effects Added**: 
  - **After your opponent ends turn, during the untapping phase, if you have a Silent Skill creature tapped on your side of the board, you'll get a prompt if you want it tapped to activate Silent Skill effect!**
  - **New Cards Added**:
    - Hustle Berry,
    - Soderlight, the Cold Blade

- **"At the end of your turn" Effects Added**: 
  - **When you pass the turn to your opponent, all of the automated cards' effects will trigger!**
  - **New Cards Added**:
    - Aqua Officer
    - Balesk Baj, the Timeburner
    - Ballus, Dogfight Enforcer Q
    - Bazagazeal Dragon
    - Cutthroat Skyterror
    - Pyrofighter Magnus

- **Other Improvements**
  - **Deck Search Sorting**: Added sorting feature to deck search results.
  - **Card Choice Header Update**: Now displays card type (Spell/Creature/Race) for better clarity during search.
  - **toDiscard Function**: Enables cards like Bingole the Explorer, Dava Torey, Seeker of Clouds, Sanfist the Savage Vizier, Sir Matthias, Ice Fang Admiral, Terradragon Arque Delacerna, Algo Bardiol, Devil Admiral, Baiken, Blue Dragon of the Hidden Blade, Gauss Blazer, Flame Dragon Admiral, Mecha Admiral Sound Shooter, Lanerva Stratus, Poseidon's Admiral, Sephia Parthenon, Spirit Admiral, Zack Pichi, Winged Dragon Admiral to come into play from the opponent’s hand due to Lost Soul.

### Fixes
- **Card Fixes**
  - **Boomerang Comet and Pixie Cocoon**: Now properly go to mana after being played.
  - **Emperor Marco, Cyber Brain**: Fixed to prompt for stopping the draw when applicable.
  - **Miraculous Snare**: Fixed issue preventing setting own card to shield.
  - **Rothus the Traveller**: Now prompts enemy to destroy a monster on the field.
  - **Skeleton Vice**: Correctly discards two cards at random.
  - **Galek, the Shadow Warrior**: Allows you to destroy enemy blocker.
  - **Wind Axe, the Warrior Savage**: Allows you to destroy enemy blocker.
- **Mechanics Fixes**
  - **Player B’s Card Choice Order**: Fixed inconsistent order when selecting cards.
  - **Targeting Issue**: Resolved infinite wait if a card required more targets than available on the field (for Destroy/Bounce effects).

#### Additional Notes
- **XML Updates**: Minor changes for races, civilizations, and types; fixed typos and standardized spell power values.
- **Mass-Destruction Effects Rewritten**: Improved order of operations for mass-destruction effects to support Survivors and Wave Strikers, enhancing interactions with cards like Balloonshroom Q and Revival Soldier.