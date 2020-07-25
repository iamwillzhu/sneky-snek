from dataclasses import dataclass

from src.algorithms.search_food import search_food_bfs
from src.models.board import Board
from src.models.battlesnake import Battlesnake

@dataclass(frozen=True)
class Strategy:
    game_id: str
    turn: int
    board: Board
    you: Battlesnake


    def find_food(self):
        return search_food_bfs(self.board, self.you)


    @classmethod
    def from_json_input(cls, json):
        game_id = json["game"]["id"]
        turn = json["turn"]
        board = Board.from_json_input(json)
        you = Battlesnake.from_json_input(json)

        return cls(
                game_id=game_id,
                turn=turn,
                board=board,
                you=you)
