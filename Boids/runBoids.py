from flock import Flock
from matplotlib import pyplot as plt
from matplotlib import animation

flock=Flock(50)

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