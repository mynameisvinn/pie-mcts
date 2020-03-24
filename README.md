# pie-mcts
a toy implementation of monte carlo tree search. it is one of the most powerful methods for balancing exploration versus exploitation.

## how dey do dat's
mcts samples trajectories, starting from all possible children nodes of the root. the payout of a trajectory is "propagated" upwards through its ancestor nodes. 

nodes that have high payouts are sampled more often (due to high ucb scores). at the end of mcts, we select the root child that was played the most.