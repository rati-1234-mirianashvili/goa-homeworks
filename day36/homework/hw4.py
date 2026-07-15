A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.intersection(B))
# გამოიტანს: {3, 4}

print(A.union(B))
# გამოიტანს: {1, 2, 3, 4, 5, 6}

print(A.difference(B))
# გამოიტანს: {1, 2}

print(A.symmetric_difference(B))
# გამოიტანს: {1, 2, 5, 6}