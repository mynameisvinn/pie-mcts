# pie-mcts
a toy implementation of monte carlo tree search. mcts identifies promising actions.

## how dey do dat's
mcts simulates rollouts, starting all possible children of the current state (root). after each rollout, the final reward is "propagated" through every node visited in that rollout.

nodes that consistently lead to higher rewards receive larger ucb scores and thus are sampled more often.

finally, after mcts, the best action to take is the action that leads to the child node with the highest play count.