import numpy as np

c = 1     # Light velocity

def beta(v_rel):
    return v_rel/c


def gamma(v_rel):
    return 1 / np.sqrt(1 - beta(v_rel)**2)


def lorentz_boost(coords, v_rel):
    b = beta(v_rel)
    trans = gamma(v_rel) * np.matrix([[1, -b], [-b, 1]])
    return trans.dot(coords)