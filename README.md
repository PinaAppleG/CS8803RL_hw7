# CS8803RL_hw7

Homework 7
Problem
Messing with Rewards

We saw in the lesson that regardless of the potential-based shaping function given, the optimal policy will remain unchanged. The purpose of choosing a particular shaping function, however, is to try to speed learning. In this question, we will explore how to pick a potential-based shaping function to speed up the convergence of policy iteration (PI).

Consider the following MDP:
MDP 1

int numStates = 2;

int numActions = 2;

double[][][] probabilitiesOfTransitions = {{{1.0,0.0},{0.0,1.0}},{{0.0,1.0},{0.0,1.0}}}

double[][][] rewards ={{{1.0,0.0},{0.0,4.0}},{{0.0,0.0},{0.0,0.0}}}

double gamma = 0.6666666667;

#Expected Output
4.0, 0.0


Your goal is to develop a potential function Φ
defined on each state so that shaping the reward function using Φ will cause PI to converge in as few iterations as possible starting from a 0-initialized value function. Your goal should be to make it converge in one PI iteration.


Convert format:
```
echo "{{{0.0,0.55,0.45,0.0},{0.0,0.0,0.0,1.0}},{{0.0,1.0,0.0,0.0},{0.0,1.0,0.0,0.0}},{{0.0,0.0,1.0,0.0},{0.0,0.0,1.0,0.0}},{{0.0,0.0,0.0,1.0},{0.0,0.0,0.0,1.0}}}" | sed 's/{/[/g' | sed 's/}/]/g'
```