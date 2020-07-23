from src.models.battlesnake import Battlesnake
from fixtures.models.battlesnake import json, battlesnake

class TestBattlesnake:
    def test_from_json_input(self, json, battlesnake):
        assert(Battlesnake.from_json_input(json) == battlesnake)
