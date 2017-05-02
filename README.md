# MDP
For a model of Markov Decision Process, Policy creation via two methods : Value Iteration and Linear Programming

### Model Description
Model world has 4*4 block grid, one positive terminal state, one negative terminal state.
![Here](/problem_statement.pdf) is total description of the world.

## Value Iteration
- ![value_iteration.py](/value_iteration.py) contains the code which runs value iteration algorithm to find the utilities of all states and then final policy. It prints the result of every iteration.
- ![value_iteration2.py](/value_iteration2.py) has the same code but with different world model than given problem statement.

## Linear Programming
- It is another approach to find policy. ![LP.ods](/LP.ods) has the linear solver's output.
- Final output of the solver gives expected utility of start state and policy for the world.
