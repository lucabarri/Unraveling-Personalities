import random
from typing import List, Sequence, Tuple


def _euclidean(p: Sequence[float], q: Sequence[float]) -> float:
    return sum((a - b) ** 2 for a, b in zip(p, q)) ** 0.5


def _mean_point(points: List[Sequence[float]]) -> List[float]:
    n = len(points[0])
    return [sum(p[i] for p in points) / len(points) for i in range(n)]


def kmeans(X: List[Sequence[float]], k: int, max_iters: int = 300) -> Tuple[List[int], List[List[float]]]:
    """Simple k-means clustering implementation without external dependencies."""
    if k <= 0:
        raise ValueError("k must be positive")
    if k > len(X):
        raise ValueError("k cannot exceed number of data points")

    centroids = [X[i] for i in random.sample(range(len(X)), k)]

    for _ in range(max_iters):
        labels = []
        for x in X:
            distances = [_euclidean(x, c) for c in centroids]
            labels.append(distances.index(min(distances)))

        new_centroids = []
        changed = False
        for i in range(k):
            cluster_points = [x for x, label in zip(X, labels) if label == i]
            if cluster_points:
                new_c = _mean_point(cluster_points)
            else:
                new_c = centroids[i]
            if new_c != centroids[i]:
                changed = True
            new_centroids.append(new_c)

        centroids = new_centroids
        if not changed:
            break

    return labels, centroids
