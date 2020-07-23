from src.models.board import Board

from fixtures.models.board import json, board
from fixtures.models.battlesnake import battlesnake

class TestBoard:
    def test_from_json_input(self, json, board):
        assert(Board.from_json_input(json) == board)

    def test_battlesnakes_equal(self, board, battlesnake):
        assert(battlesnake in board.snakes)
