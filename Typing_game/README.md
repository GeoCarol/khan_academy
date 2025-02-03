**The basic game**

First, get to know the basic mechanics of the game. We’ve provided an example of a single-level game with three rounds. Each round, the player is presented with a word or phrase to type and a time limit. If they correctly spell the words within the time limit, they pass!

Take a look at the function definitions in typer.py. These are the building blocks you’ll have available to design your levels.

**Gathering requirements**

Start your design by thinking about your audience. Are they typing on a physical keyboard or a phone? Are they just learning to type, practicing their spelling, or looking to be entertained? Consider how your target audience might influence what the right rule set and challenge threshold is.

Then, decide how the difficulty will progress from level to level. You can vary the combination of word length, number of words, time limit, and number of rounds, or you can imagine an entirely new set of mechanics!

Design at least five unique game levels that increase in difficulty.

Write down your plan for each level as you go. This will guide how you organize your code.

**Game over**

Finally, think about how a player wins, loses, or completes the game.

Design a way to end the game that provides some indication of the player’s progress.

The game might end as soon as a player misses a round, printing out the number of levels they completed, or the game might continue to the end of the last level, printing out an overall accuracy score. You decide!

**Function breakdown**

Plan out what functions you want, what parameters they need, and what value they return. Each function should handle one specific task, like calculating a score, determining a time limit, or playing a bonus level. Then, assemble the functions to build the final game logic!

Add at least three new function definitions to typer.py to support your leveling system.

Use the functions to build your game logic in main.py.

Remember to test your game as you go, thinking through any edge cases.

**More to explore**

Imagine players are taken to a menu screen when they first open the game. Add a prompt that asks the user to select between multiple game options, and then use that option to adapt the gameplay. For example, players might choose between overall difficulty modes, like easy, medium, and hard, that shift the difficulty of all levels.

Playtest your game with friends and family. Observe where they’re getting stuck or which levels they’re winning too easily. How can you adjust the balance of challenge and reward in your game to better keep them motivated and engaged?
