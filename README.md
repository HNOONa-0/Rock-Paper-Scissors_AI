## RPS AI

How can AI play RPS and win? normally you would think it's not possible, but it's.

We can do alot better than just picking a random hand. Playing a few games of RPS, the player can win. 
But as we increase the number of rounds, it gets harder, as the player will have predictible patterns that
the AI will exploit.

Why? simply, as humans, we can't make random choices.

Below are 3 approaches for a computer to play RPS.

## M1

We can check the player's last **continuous** sequence of hands, say, last 5 hands played and check with earlier subsequences, if the 2 subsequences match 
one another so that 4/5 or 5/5 hands match, this earlier sequence gets to **vote** which hand to play next

After all sequences are checked for matching, in the end, the hand with the most votes is played by M1.


## M2
This one uses a simple **discrete markov chains**, where, the next hand that the computer will play depend only the last hand played
by the player.

For more about **markov chains** read [here](https://setosa.io/ev/markov-chains/)

## M3
This one uses **online machine learning** model **hoefidding classifier** from python 
library **[River](https://riverml.xyz/0.15.0/)**, the library is similar to scikit multiflow.

**Online machine learning** models adapt fast to when player changes sequence, which is typical in an RPS game.

## Comparison
For these models to have any meaningful result, the player needs to play alot, we need to give 
our models a chance to "learn" player's patterns. 100 games of RPS is good enough.

How do these models compare with one another?(currently collecting data)

## Issues to revisit
* ML model does not perform well with alternating sequence ex:[0,1,0,1,0,1,....
