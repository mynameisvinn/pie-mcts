# pie-mcts
a toy implementation of monte carlo tree search. mcts is used to identify promising actions/trajectories.

## how dey do dat's
mcts simulates rollouts, starting from all possible children from the current state (root). after each rollout, the reward is "propagated" through every node that was visited in that specific rollout.

nodes that consistently lead to higher rewards receive larger ucb scores and are therefore are sampled more often.

finally, when we'd like to predict the best action to take from root, we select the action that would lead us to a state with the highest play count.