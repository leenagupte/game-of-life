import unittest

from hamcrest import equal_to, assert_that
from mock import patch

from game_of_life import get_cell_state, set_cell_state, get_next_day_universe, get_number_of_alive_neighbours


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

        assert_that(get_cell_state(universe, 0, 4), equal_to(1))

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

        assert_that(get_next_day_universe(yesterdays_universe),
                    equal_to(expected_universe))


    @patch('game_of_life.get_cell_state')
    def test_get_state_of_neighbour(self, get_cell_state_mock):
        universe = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        number_alive_neighbours = \
            get_number_of_alive_neighbours(universe, 1, 1)

        assert_that(get_cell_state_mock.called)

        assert_that(get_cell_state_mock.call_count, equal_to(8))

        get_cell_state_mock.assert_any_call(universe, 0, 0)
        get_cell_state_mock.assert_any_call(universe, 0, 1)
        get_cell_state_mock.assert_any_call(universe, 0, 2)
        get_cell_state_mock.assert_any_call(universe, 1, 0)
        get_cell_state_mock.assert_any_call(universe, 1, 2)
        get_cell_state_mock.assert_any_call(universe, 2, 0)
        get_cell_state_mock.assert_any_call(universe, 2, 1)
        get_cell_state_mock.assert_any_call(universe, 2, 2)


    def test_number_of_alive_neighbours(self):
        universe = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        number_alive_neighbours = \
            get_number_of_alive_neighbours(universe, 1, 1)

        assert_that(number_alive_neighbours, equal_to(0))

    def test_number_of_alive_neighbours_is_two(self):
        universe = [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0]
        ]

        number_alive_neighbours = \
            get_number_of_alive_neighbours(universe, 1, 1)

        assert_that(number_alive_neighbours, equal_to(2))

    def test_cell_dies_when_no_living_neighbours(self):
        yesterdays_universe = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
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

        assert_that(get_next_day_universe(yesterdays_universe),
                    equal_to(expected_universe))

    def test_cell_dies_when_more_than_three_alive_neighbours(self):
        yesterdays_universe = [
            [1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        expected_universe = [
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        assert_that(get_next_day_universe(yesterdays_universe),
                    equal_to(expected_universe))


    def test_dead_cell_with_exactly_three_alive_neighbours_is_reborn(self):
        yesterdays_universe = [
            [1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        expected_universe = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        assert_that(get_next_day_universe(yesterdays_universe),
                    equal_to(expected_universe))
