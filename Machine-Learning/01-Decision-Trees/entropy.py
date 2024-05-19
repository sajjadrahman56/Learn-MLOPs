import numpy as np

Y = np.array([1,0,0,1,1,1])

# no of uniques find
np.unique(Y)

# counts
values , count = np.unique(Y,return_counts=True)
print(f'no of unique values = {values} and no of values = {count}')

def entropy(var):
  N = var.shape[0]
  values , counts = np.unique(var,return_counts=True)

  ent = 0.0

  for i in counts:
    p = i/N
    ent += (p * np.log2(p))

  return -ent

entropy(Y)


