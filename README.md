## This is the Duel Masters OCG Definition for OCTGN 
#### based on https://github.com/PranjalBishtNX/dm-ocg-octgn with new automations and fixes for existing cards.


All automations are based on python. OCTGN plugin dev refernce: https://github.com/octgn/OCTGN/wiki https://github.com/octgn/OCTGN/wiki/OCTGN-Python-3.1.0.2-API-Reference

## Changelog

### Fixes
- **Card Fixes**
  - **Boomerang Comet and Pixie Cocoon**: Now properly go to mana after being played.
  - **Emperor Marco, Cyber Brain**: Fixed to prompt for stopping the draw when applicable.
  - **Miraculous Snare**: Fixed issue preventing setting own card to shield.
  - **Rothus the Traveller**: Now prompts enemy to destroy a monster on the field.
  - **Skeleton Vice**: Correctly discards two cards at random.
- **Mechanic Fixes**
  - **Player B’s Card Choice Order**: Fixed inconsistent order when selecting cards.
  - **Targeting Issue**: Resolved infinite wait if a card required more targets than available on the field (for Destroy/Bounce effects).

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
- **Other Improvements**
  - **Deck Search Sorting**: Added sorting feature to deck search results.
  - **Card Choice Header Update**: Now displays card type (Spell/Creature/Race) for better clarity during search.
  - **toDiscard Function**: Enables cards like Bingole the Explorer, Dava Torey, Seeker of Clouds, Lanerva Stratus, Poseidon's Admiral, Sanfist the Savage Vizier, Sir Matthias, Ice Fang Admiral, and Terradragon Arque Delacerna to come into play from the opponent’s hand due to Lost Soul.

#### Additional Notes
- **XML Updates**: Minor changes for races, civilizations, and types; fixed typos and standardized spell power values.
- **Mass-Destruction Effects Rewritten**: Improved order of operations for mass-destruction effects to support Survivors and Wave Strikers, enhancing interactions with cards like Balloonshroom Q and Revival Soldier.
