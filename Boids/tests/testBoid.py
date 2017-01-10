from ..boid import Boid
from nose.tools import assert_equal, assert_raises
import yaml
import os
import sys

def test_constructor():
    #should work
    test_boid=Boid(-100,500,2,5)
    assert_equal(test_boid._x_pos,-100)
    assert_equal(test_boid._y_pos,500)
    assert_equal(test_boid._x_vel,2)
    assert_equal(test_boid._y_vel,5)

    #not enough arguments
    assert_raises(ValueError,Boid,((-100,500,2)))
    #too many arguments
    assert_raises(ValueError,Boid,((-100,500,2,5,10)))
    #outside of bounds
    assert_raises(ValueError,Boid,((-1000,500,2,5)))
    assert_raises(ValueError,Boid,((-100,5000,2,5)))
    assert_raises(ValueError,Boid,((-100,500,200,5)))
    assert_raises(ValueError,Boid,((-100,500,2,50)))


def test_getPosition():
    test_boid=Boid()
    expected_position={'x':test_boid._x_pos,'y':test_boid._y_pos}
    assert_equal(test_boid.getPosition(),expected_position)

def test_getVelocity():
    test_boid=Boid()
    expected_velocity={'x':test_boid._x_vel,'y':test_boid._y_vel}
    assert_equal(test_boid.getVelocity(),expected_velocity)

def test_setPosition():
    test_boid=Boid()
    #positions within boundries
    x=-100
    y=500
    test_boid.setPosition(x,y)
    assert_equal(test_boid._x_pos,x)
    assert_equal(test_boid._y_pos,y)
    #x outside boundries
    #assert_raises(ValueError,test_boid.setPosition,-1000,500)
    #assert_raises(ValueError,test_boid.setPosition,1000,400)
    #y outside boundries
    #assert_raises(ValueError,test_boid.setPosition,-100,200)
    #assert_raises(ValueError,test_boid.setPosition,10,601)


def test_setVelocity():
    test_boid=Boid()
    #positions within boundries
    x=5
    y=10
    test_boid.setVelocity(x,y)
    assert_equal(test_boid._x_vel,x)
    assert_equal(test_boid._y_vel,y)
    #x outside boundries
    #assert_raises(ValueError,test_boid.setVelocity,-1000,10)
    #assert_raises(ValueError,test_boid.setVelocity,1000,9)
    #y outside boundries
    #assert_raises(ValueError,test_boid.setPosition,6,30)
    #assert_raises(ValueError,test_boid.setPosition,7,-40)

def test_towardsMiddle():
    with open(os.path.join(os.path.dirname(__file__),'fixtures','fixture_data.yaml'), 'r') as stream:
        fixture=yaml.load(stream)
        neighbours=fixture['neighbours']
        expected_result=fixture['move_towards_expected_velocity']
        num_boids=fixture['num_boids']
        tst_boid_init_conds=fixture['test_boid']

        boids=[Boid(*coord) for coord in neighbours]
        i=0
        for boid in boids:
            test_boid=Boid(*tst_boid_init_conds)
            test_boid.towardsMiddle(boid,num_boids)
            test_boid_vel=test_boid.getVelocity()
            print((test_boid_vel['x'],expected_result[i][0]))
            assert_equal(test_boid_vel['x'],expected_result[i][0])
            i+=1


