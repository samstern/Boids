from flock import Flock
import argparse
from matplotlib import pyplot as plt
from matplotlib import animation


def parser():
    parser = argparse.ArgumentParser(description = 'Python2 simulation of the Boids algorithm')
    parser.add_argument('--num_boids','-n', type=int, default='50', required=False, help='The number of boids in the simulation')

    args=parser.parse_args()
    return args
args=parser()
flock=Flock(args.num_boids)

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
flock_xs=[boid.getPosition()['x'] for boid in flock.boids]
flock_ys=[boid.getPosition()['y'] for boid in flock.boids]
#print(zip(flock_xs,flock_ys))
scatter=axes.scatter(flock_xs,flock_ys)
def animate(frame):
    flock_xs=[boid.getPosition()['x'] for boid in flock.boids]
    flock_ys=[boid.getPosition()['y'] for boid in flock.boids]
    flock.update_boids()
    scatter.set_offsets(zip(flock_xs,flock_ys))

anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()