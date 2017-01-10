import random
class Boid:


    def __init__(self,*args):
        '''

        :param args: tuple of arguments in the form (x position, y position, x velocity, y velocity)
        '''
        #boundries that the boids position and velocity must be between
        self._x_pos_boundaries = {'low':-450,'high':50.0}
        self._y_pos_boundaries = {'low':300.0,'high':600.0}
        self._x_vel_boundaries = {'low':0,'high':10.0}
        self._y_vel_boundaries = {'low':-20.0,'high':20.0}

        if len(args)==0:
            #initialising boids position and velocity
            self._x_pos=random.uniform(self._x_pos_boundaries['low'],self._x_pos_boundaries['high'])
            self._y_pos=random.uniform(self._y_pos_boundaries['low'],self._y_pos_boundaries['high'])
            self._x_vel=random.uniform(self._x_vel_boundaries['low'],self._x_vel_boundaries['high'])
            self._y_vel=random.uniform(self._y_vel_boundaries['low'],self._y_vel_boundaries['high'])
        else:
            #user defined position of boid
            try:
                x_position,y_position,x_velocity,y_velocity=args
            except ValueError:
                raise ValueError('args expected to be of length 4')
            x_pos_outside_boundary = x_position<self._x_pos_boundaries['low'] or x_position>self._x_pos_boundaries['high']
            y_pos_outside_boundary = y_position<self._y_pos_boundaries['low'] or y_position>self._y_pos_boundaries['high']
            x_vel_outside_boundary = x_velocity<self._x_vel_boundaries['low'] or x_velocity>self._x_vel_boundaries['high']
            y_vel_outside_boundary = y_velocity<self._y_vel_boundaries['low'] or y_velocity>self._y_vel_boundaries['high']
            if x_pos_outside_boundary:
                raise ValueError('x postion coordinate outside boundary')
            elif y_pos_outside_boundary:
                raise ValueError('y position coordinate outside boundary')
            elif x_vel_outside_boundary:
                raise ValueError('x velocity coordinate outside boundary')
            elif y_vel_outside_boundary:
                raise ValueError('y velocity coordinate outside boundary')
            else:
                self._x_pos=x_position
                self._y_pos=y_position
                self._x_vel=x_velocity
                self._y_vel=y_velocity


    def getPosition(self):
        '''
        getter for position
        :return: dictionary of boid position cartesian coordinates
        '''
        return{
            'x':self._x_pos,
            'y':self._y_pos
        }
    def getVelocity(self):
        '''
        getter for velocity
        :return: dictionary of boid velocity in cartesian coordinates
        '''
        return {
            'x':self._x_vel,
            'y':self._y_vel
        }

    def setPosition(self,x,y):
        '''
        set the position of a boid in 2D cartesian space
        :param x: x position
        :param y: y position
        '''

        x_outside_boundary = x<self._x_pos_boundaries['low'] or x>self._x_pos_boundaries['high']
        y_outside_boundary = y<self._y_pos_boundaries['low'] or y>self._y_pos_boundaries['high']
        #if x_outside_boundary:
        #    raise ValueError('x position coordinate outside boundary')
        #elif y_outside_boundary:
        #    raise ValueError('y position coordinate outside boundary')
        #else:
        self._x_pos=x
        self._y_pos=y

    def setVelocity(self,x,y):
        '''
        set the velocity of a boid in 2D cartesian space
        :param x: x position
        :param y: y position
        '''
        x_outside_boundary = x<self._x_vel_boundaries['low'] or x>self._x_vel_boundaries['high']
        y_outside_boundary = y<self._y_vel_boundaries['low'] or y>self._y_vel_boundaries['high']
        #if x_outside_boundary:
        #    raise ValueError('x velocity coordinate outside boundary')
        #elif y_outside_boundary:
        #    raise ValueError('y velocity coordinate outside boundary')
        #else:
        self._x_vel=x
        self._y_vel=y

    def towardsMiddle(self,boid,num_boids):
        '''
        Update velocity so that the boid boid flies towards the middle of the flock
        :param boid: another boid object
        :param num_boids: number of boids in the flock
        '''
        boid_pos=boid.getPosition()
        new_x_vel=self._x_vel+(boid_pos['x']-self._x_pos)*0.01/num_boids
        new_y_vel=self._y_vel+(boid_pos['y']-self._y_pos)*0.01/num_boids
        self.setVelocity(new_x_vel,new_y_vel)


    def awayFromNeighbour(self,boid):
        '''
        If another boid is close then fly away from it
        :param boid: another boid object
        '''
        boid_pos=boid.getPosition()
        is_neighbour=((boid_pos['x']-self._x_pos)**2 + (boid_pos['y']-self._y_pos)**2) < 100
        if is_neighbour:
            new_x_vel=self._x_vel+(self._x_pos-boid_pos['x'])
            new_y_vel=self._y_vel+(self._y_pos-boid_pos['y'])
            self.setVelocity(new_x_vel,new_y_vel)

    def matchSpeedOfNeighbour(self,boid,num_boids):
        '''
        If a boid is close(ish) then try then make velocity similar to the boid's
        :param boid: another boid object
        :param num_boids: number of boids in the flock
        '''
        boid_pos=boid.getPosition()
        boid_vel=boid.getVelocity()
        is_neighbour=((boid_pos['x']-self._x_pos)**2 + (boid_pos['y']-self._y_pos)**2) < 10000
        if is_neighbour:
            new_x_vel=self._x_vel+(boid_vel['x']-self._x_vel)*0.125/num_boids
            new_y_vel=self._y_vel+(boid_vel['y']-self._y_vel)*0.125/num_boids
            self.setVelocity(new_x_vel,new_y_vel)

    def move(self):
        '''
        update position based on the velocity
        '''
        new_x_pos=self._x_pos+self._x_vel
        new_y_pos=self._y_pos+self._y_vel
        self.setPosition(new_x_pos,new_y_pos)