from src.utils.search_food import (
        construct_food_snake_matrix,
        find_closest_food_to_snake,
        get_successors)

from src.models.point import Point
from fixtures.models.board import board, one_food_board
from fixtures.models.battlesnake import battlesnake, battlesnake_successors

import pytest

@pytest.fixture
def food():
    return Point(x=2,y=6)

@pytest.fixture
def matrix():
    return (
            (0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0),
            (0,0,5,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0),
            (2,1,1,0,0,0,0,0,0,0,0))

class TestFindClosestFoodToSnake:
    def test_only_one_food_on_board(self, one_food_board, battlesnake):
        assert(find_closest_food_to_snake(one_food_board, battlesnake) == one_food_board.food[0])

    def test_closest_food_on_board(self, board, battlesnake):
        assert(find_closest_food_to_snake(board, battlesnake) == board.food[2])

    
class TestConstructFoodSnakeMatrix:
    def test_construct_food_snake_matrix(self, food, board, battlesnake, matrix):
        assert(construct_food_snake_matrix(food, board, battlesnake) == matrix)

class TestGetSuccessors:
    def test_battlesnake_successors(self, matrix, board, battlesnake, battlesnake_successors):
        assert(get_successors(matrix, board, battlesnake) == battlesnake_successors)
