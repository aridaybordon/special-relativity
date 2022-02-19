import numpy as np

c = 1     # Light velocity

def beta(v_rel) -> float:
    return v_rel/c


def gamma(v_rel) -> float:
    return 1 / np.sqrt(1 - beta(v_rel)**2)


def lorentz_boost(coords, v_rel) -> list:
    coords = np.matrix([[x] for x in coords]) if type(coords) == list else coords
    
    b = beta(v_rel)
    trans = gamma(v_rel) * np.matrix([[1, -b], [-b, 1]])    
    return [float(x) for x in trans.dot(coords)]