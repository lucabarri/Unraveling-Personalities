import os
import sys
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from kmeans import kmeans


def test_kmeans_basic():
    random.seed(0)
    k = 3
    centers = [(0, 0), (5, 5), (-5, -5)]
    data = []
    for cx, cy in centers:
        for _ in range(30):
            data.append([random.gauss(cx, 0.1), random.gauss(cy, 0.1)])

    labels, centroids = kmeans(data, k)

    assert len(centroids) == k
    assert all(len(c) == 2 for c in centroids)
    assert len(labels) == len(data)
    assert min(labels) >= 0
    assert max(labels) < k

