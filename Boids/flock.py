from boid import Boid

class Flock():

    def __init__(self,num_boids):
        self.boids= [Boid() for boid in range(num_boids)]
        self.num_boids=num_boids

    def update_boids(self):
        #update positions only after all boids' velocities have been adjusted
        self.__update_velocities()
        self.__updat_positions()

    def __update_velocities(self):
        for boid in self.boids:
            for neighbour in self.boids:
                boid.towardsMiddle(neighbour,self.num_boids)
                boid.awayFromNeighbour(neighbour)
                boid.matchSpeedOfNeighbour(neighbour,self.num_boids)

    def __updat_positions(self):
        for boid in self.boids:
            boid.move()
