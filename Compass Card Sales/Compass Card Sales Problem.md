Compass Card Sales

Picture via Wikimedia Commons, public domain
Katla has recently stopped playing the collectible card game Compass. As you might remember, Compass is a game where each card has a red, a green and a blue angle, each one between 0 and 359, as well as an ID. Since she has stopped playing, Katla has decided to sell all her cards. However, she wants to keep her deck as unique as possible while selling off the cards. Can you help her figure out the order in which she should sell the cards?
To decide how unique a card is in the deck, she proceeds as follows. For each of the three colors she finds the closest other card in both directions, and then computes the angle between these two other cards. For instance if she has three cards with red angles 42, 90 and 110, then the uniqueness values of their red angles are 340, 68, and 312, respectively. If two cards A and B have the same angle, B is considered the closest to A in both directions so that the uniqueness value of A (and B) for that color is 0.

By summing the uniqueness values over the three colours, Katla finds how unique each card is. When selling a card, Katla sells the currently least unique card (smallest uniqueness value). If two cards have the same uniqueness value, she will sell the one with the higher ID first. After each card is sold, the uniqueness values of the remaining cards are updated before selling the next card.

Input
The first line of input contains an integer n, the number of cards (1<=n<=10^5). Then follows n lines. Each of these n lines contains 4 integers r,g,b,id (0<=r,g,b<360, 0<=id<2^31), giving the red, green and blue angles as well as the ID of a card. No two cards have the same ID.

Output
Output n lines, containing the IDs of the cards in the order they are to be sold, from first (least unique) to last (most unique).

Sample Input 1	

3

42 1 1 1

90 1 1 2

110 1 1 3

Sample Output 1

2

3

1

Sample Input 2	

4

0 0 0 0

120 120 120 120

240 240 240 240

0 120 240 2017

Sample Output 2

2017

240

120

0
