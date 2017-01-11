from ..flock import Flock
from ..boid import Boid
from nose.tools import assert_equal
from mock import patch, call

def test_constructor():
    num_boids=50
    test_flock=Flock(num_boids)
    assert_equal(num_boids,test_flock.num_boids)
    assert_equal(num_boids,len(test_flock.boids))


def test_updateBoids():
    num_boids=50
    with patch.object(Flock,'_update_velocities') as mock_update_velocities:
        with patch.object(Flock,'_update_positions') as mock_update_positions:
            test_flock=Flock(num_boids)
            test_flock.update_boids()
            mock_update_velocities.assert_called_once()
            mock_update_positions.assert_called_once()

def test_update_velocities():
    num_boids=50
    with patch.object(Boid,'towardsMiddle') as mock_towardsMiddle:
        with patch.object(Boid,'awayFromNeighbour') as mock_awayFromNeighbour:
            with patch.object(Boid,'matchSpeedOfNeighbour') as mock_matchSpeedOfNeighbour:
                test_flock=Flock(num_boids)
                test_flock._update_velocities()
                towardsMiddle_call_list=mock_towardsMiddle.call_args_list
                awayFromNeighbour_call_list=mock_awayFromNeighbour.call_args_list
                matchSpeedOfNeighbour_call_list=mock_matchSpeedOfNeighbour.call_args_list
                expected_towardsMiddle=[call(boid,num_boids) for boid in test_flock.boids]
                expected_awayFromNeighbour=[call(boid) for boid in test_flock.boids]
                expected_matchSpeedOfNeighbour=expected_towardsMiddle
                assert(all([exp==call for exp,call in zip(expected_towardsMiddle,towardsMiddle_call_list)])==True)
                assert(all([exp==call for exp,call in zip(expected_awayFromNeighbour,awayFromNeighbour_call_list)])==True)
                assert(all([exp==call for exp,call in zip(expected_matchSpeedOfNeighbour,matchSpeedOfNeighbour_call_list)])==True)

def test_update_positions():
    num_boids=50
    with patch.object(Boid,'move') as mock_move:
        test_flock=Flock(num_boids)
        test_flock._update_positions()
        assert(len(mock_move.call_args_list),50)