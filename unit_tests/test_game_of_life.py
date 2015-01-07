import unittest
from hamcrest import equal_to, assert_that


class TestGameOfLife(unittest.TestCase):
    def test_universe_dimension(self):
        universe = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        # column length is 5
        assert_that(len(universe), equal_to(5))

        for row in universe:
            assert_that(len(row), equal_to(5))

    def test_cell_is_alive(self):
        universe = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0]
        ]

        assert_that(get_cell_state(universe, 4, 0), equal_to(1))

    def test_cell_state_changes(self):
        # arrange
        universe = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        # act
        set_cell_state(universe, 4, 0, 1)

        #assert
        assert_that(get_cell_state(universe, 4, 0), equal_to(1))

    def test_todays_universe_is_dead_when_yesterdays_is_dead(self):
        yesterdays_universe = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        expected_universe = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        assert_that(get_todays_universe(yesterdays_universe),
                    equal_to(expected_universe))




def get_cell_state(universe, position_y, position_x):

    state = universe[position_y][position_x]

    return state


def set_cell_state(universe, position_y, position_x, state):
    universe[position_y][position_x] = state

def get_todays_universe(yesterdays_universe):

    todays_universe = yesterdays_universe

    return todays_universe


if __name__ == "__main__":
    unittest.main()
