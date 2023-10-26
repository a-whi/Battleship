# Battleship

How to play: 
Battleship is a classic two-player strategy board game where each player arranges a fleet of ships on a grid and takes turns guessing the coordinates of their opponent's ships to sink them. The objective is to sink all of the opponent's ships before they do the same to you. The game typically includes various types of ships, such as aircraft carriers, battleships, cruisers, destroyers, and submarines, each with different lengths.
----------------------------------------------------------------------------------------------------------------------------
I'm not a fan of battleship, but I'm even less of a fan of losing so I've made this program to help me win.
It's not a complex program, but still an interesting one.

----------------------------------------------------------------------------------------------------------------------------

****I tested my program on these websites:****

- Battleship game website
https://papergames.io/en/battleship

The game is not the standard battleship version, there are special power-ups that the bot was using, but my program was still able to beat it.

- C. Liam Brown - BATTLESHIP PROBABILITY CALCULATOR
https://cliambrown.com/battleship/

While I played against the bot, I would also input all the moves I used on the calculator to see if the programs were suggesting the same coordinates. 

Generally, they did, sometimes my program would suggest other moves, but looking at the probability map I could still see it had a high probability. 
I'm unsure how the website's probability is programmed so I am going to assume it just comes down to their algorithm.

----------------------------------------------------------------------------------------------------------------------------
**Shortcomings:**
 - The program could probably have a smaller time complexity, there are currently lots of nested loops
 - The code could be cleaner, with lots of 'if' and 'else' statements
 - When the program suggests coordinates to destroy a boat it can sometimes suggest coordinates that aren't on the grid, like (0,-1). This is a simple fix though, just need to add conditions in the destroy_ship function.

**Future ideas:**
 - Somehow get the program to be able to interact with the website game so I don't have to do anything.












