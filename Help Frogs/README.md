# Help the frogs reach the opposite side of the line

White frogs and N Black frogs are placed on either side of a line made up of 2*N + 1 spaces. The 1 "leftover" 
space is therefore empty, and is at the center of the line.
 
The N White frogs are placed on the left side and all face rightwards, and the N Black frogs are placed on the right side all face leftwards.

The goal is to get all the White frogs to the right half of the line, and all the Black frogs to the left half of the line. So, again, with the N=2 example,
the desired end state is:

BB_WW

A White frog must always move first. Then after this initial White frog move, at each step, there are only 3 possible moves for you to choose from:

- A White frog walks rightwards into the empty space.
- A Black frog walks leftwards into the empty space.
- Any frog JUMPS OVER 1 (and only 1) FROG, OF THE OPPOSITE COLOR ONLY, and only if they can land in the empty space.

Your goal, therefore, is to develop a general algorithm for arbitrary N that moves all the frogs to their end positions in the fewest number of moves.

## Inputs
You will be given an integer N which specifies the number of both types of frogs. N White and N Black frogs. The board will therefore always be of size 2*N + 1.

Output
Return a string, consisting of lowercase characters 'w','b','j'.

## How did I solve it?

In this case, I applied the BFS search Algorithm to complete this exercise. I created a class named Frogs_State which I used to stand for the configuration of the state
and their possible movements.

For an input value of 1 the output is the search solution: wjw
