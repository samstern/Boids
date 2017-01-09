import random
class Boid:

    #random initialisation
    def __init__(self):
        #boundries that the boids position and velocity must be between
        self._x_pos_boundaries = {'low':-450,'high':50.0}
        self._y_pos_boundaries = {'low':300.0,'high':600.0}
        self._x_vel_boundaries = {'low':0,'high':10.0}
        self._y_vel_boundaries = {'low':-20.0,'high':20.0}

        #initialising boids position and velocity
        self._x_pos=random.uniform(self._x_pos_boundaries['low'],self._x_pos_boundaries['high'])
        self._y_pos=random.uniform(self._y_pos_boundaries['low'],self._y_pos_boundaries['high'])
        self._x_vel=random.uniform(self._x_vel_boundaries['low'],self._x_vel_boundaries['high'])
        self._y_vel=random.uniform(self._y_vel_boundaries['low'],self._y_vel_boundaries['high'])

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

        x_outside_boundary = x<self._x_pos_boundaries['low'] or x>self._s_pos_boundaries['high']
        y_outside_boundary = y<self._y_pos_boundaries['low'] or y>self._s_pos_boundaries['high']
        if x_outside_boundary:
            raise ValueError('x position coordinate outside boundary')
        elif y_outside_boundary:
            raise ValueError('y position coordinate outside boundary')
        else:
            self._x_pos=x
            self._y_pos=y

    def setVelocity(self,x,y):
        '''
        set the velocity of a boid in 2D cartesian space
        :param x: x position
        :param y: y position
        '''
        x_outside_boundary = x<self._x_vel_boundaries['low'] or x>self._s_vel_boundaries['high']
        y_outside_boundary = y<self._y_vel_boundaries['low'] or y>self._s_vel_boundaries['high']
        if x_outside_boundary:
            raise ValueError('x velocity coordinate outside boundary')
        elif y_outside_boundary:
            raise ValueError('y velocity coordinate outside boundary')
        else:
            self._x_vel=x
            self._y_vel=y