
# Theoretical Explonation

K-means clustering is an itearative method that minimizes the cost function for each iteration. (Like a gradient descent algorithm)

The cost function is;

![cost_func.png](attachment:cost_func.png)

https://medium.com/dataregressed/k-means-clustering-the-premier-league-2592d1870dc5


So after the initialization of the cluster centers, the algorithm will perform a greedy approach to reduce the cost. This greedy approach makes the algorithm dependent on the cost of initial centers and algorithm stucks at the local minimum. In other words, for each different set of initial centers, there will a different cost. 
Like in the graph bellow,

![mVhnT.png](attachment:mVhnT.png)

https://stackoverflow.com/questions/53633262/implementing-k-means-with-euclidean-distance-vs-manhattan-distance

As seen, depending on the initial centers, the k-means algorithm can return different costs. So a bad choice of initial centers will effect the performance of the algorithm.

The graph bellow shows how k-means clustering can stuck in local optimal

![821d704878b16fa3daf27644a7491f49.jpg](attachment:821d704878b16fa3daf27644a7491f49.jpg)

To avoid this problem, metaheuristic algorithms like simulated annealing or Genetic algorithm can be used to select the initial centers. But to find optimal solution,the cost of all possible initial centers should be calculated. Which will take exponential amount of time and in most of the cases, the set of nodes (centers) is a continuous set. So it is impossible to try all possibble points.
