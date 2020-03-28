# pie-mcts
a toy implementation of monte carlo tree search. it is one of the most powerful methods for balancing exploration versus exploitation.

## how dey do dat's
mcts simulates rollouts, starting from all possible children from the current state (root). for each rollout, the payout is "propagated" through all nodes in that particular rollout.

ultimately, nodes that eventually lead to high payouts are sampled more often (due to higher ucb scores). at the end of mcts, we select the child of the root state with the highest play count.