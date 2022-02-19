from scripts.definitions import c, lorentz_boost

import matplotlib as mpl
import matplotlib.pyplot as plt

LIM = 1


def create_figure():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # Show ticks in the left and lower axes only
    plt.xticks([])
    plt.yticks([])
    ax1.set_yticks([]), ax2.set_yticks([])
    ax1.set_xticks([]), ax2.set_yticks([])
    
    # Set limits to x and y axis
    ax1.set_xlim(0, LIM), ax2.set_xlim(0, LIM)
    ax1.set_ylim(0, LIM), ax2.set_ylim(0, LIM)
    
    return ax1, ax2


def draw_trajectory(ax, coords0, v, u, color='k', marker='_', draw_point=False):
    # Transform coordinates using Lorentz boost
    x0, t0 = lorentz_boost(coords0, v_rel=v)
    coordsf = [x0 + u*LIM, t0 + LIM]
    xf, tf = lorentz_boost(coordsf, v_rel=v)
    
    xf, tf = [x0 + u*LIM, t0 + LIM]
    
    ax.plot([x0, xf], [t0, tf], color=color, marker=marker)
    
    if draw_point:
        ax.plot(x0, t0, 'ko')


def add_particle(axis, coords0, u):
    v_rel   = [0, -.3]
    
    for ax, v in zip(axis, v_rel):
        # Draw light cone
        draw_trajectory(ax, coords0, v=v, u=+c, color='r')
        draw_trajectory(ax, coords0, v=v, u=-c, color='r')
        
        # Draw trajectory
        draw_trajectory(ax, coords0, v=v, u=u-v, draw_point=True)


def main():
    ax1, ax2 = create_figure()
    add_particle([ax1, ax2], [0.2, .05], u=0)
    add_particle([ax1, ax2], [0.7, .05], u=0)
    plt.savefig('test.png')


if __name__ == '__main__':
    main()
    