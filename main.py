from scripts.definitions import c, lorentz_boost

import matplotlib as mpl
import matplotlib.pyplot as plt

LIM = 1

def create_figure():
    fig = plt.figure(figsize=(8, 8))
    ax  = fig.add_subplot(1, 1, 1)

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    plt.xticks([])
    plt.yticks([])
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Set limits to x and y axis
    ax.set_xlim(-LIM, LIM)
    ax.set_ylim(-LIM, LIM)
    
    return fig, ax


def add_particle(ax, coords0, v=0):
    # Draw particle with constant velocity and its light cone
    x0, t0 = coords0
    ax.plot([x0, x0 + v], [t0, t0+1], 'k-')
    
    ax.plot([x0, x0 + c], [t0, t0+1], 'r-')
    ax.plot([x0, x0 - c], [t0, t0+1], 'r-')
    
    ax.plot(x0, t0, 'ko')


def main():
    fig, ax = create_figure()
    add_particle(ax, [0.2, 0])
    plt.savefig("test.png")
    
if __name__ == "__main__":
    main()
    