import pytest

from src.models.battlesnake import Battlesnake
from src.models.point import Point

@pytest.fixture
def json():
    return {
      "game": {
        "id": "game-00fe20da-94ad-11ea-bb37",
        "timeout": 500
      },
      "turn": 14,
      "board": {
        "height": 11,
        "width": 11,
        "food": [
          {"x": 5, "y": 5}, 
          {"x": 9, "y": 0}, 
          {"x": 2, "y": 6}
        ],
        "snakes": [
          {
            "id": "snake-508e96ac-94ad-11ea-bb37",
            "name": "My Snake",
            "health": 54,
            "body": [
              {"x": 0, "y": 0}, 
              {"x": 1, "y": 0}, 
              {"x": 2, "y": 0}
            ],
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??"
          }, 
          {
            "id": "snake-b67f4906-94ae-11ea-bb37",
            "name": "Another Snake",
            "health": 16,
            "body": [
              {"x": 5, "y": 4}, 
              {"x": 5, "y": 3}, 
              {"x": 6, "y": 3},
              {"x": 6, "y": 2}
            ],
            "head": {"x": 5, "y": 4},
            "length": 4,
            "shout": "I'm not really sure..."
          }
        ]
      },
      "you": {
        "id": "snake-508e96ac-94ad-11ea-bb37",
        "name": "My Snake",
        "health": 54,
        "body": [
          {"x": 0, "y": 0}, 
          {"x": 1, "y": 0}, 
          {"x": 2, "y": 0}
        ],
        "head": {"x": 0, "y": 0},
        "length": 3,
        "shout": "why are we shouting??"
      }
    }

@pytest.fixture
def battlesnake():
    return Battlesnake(
            id="snake-508e96ac-94ad-11ea-bb37",
            name="My Snake",
            health=54,
            body=(
                Point(x=0,y=0),
                Point(x=1,y=0),
                Point(x=2,y=0)),
            head=Point(x=0,y=0),
            length=3,
            shout="why are we shouting??")

@pytest.fixture
def battlesnake_successors():
    return [
            Battlesnake(
                id="snake-508e96ac-94ad-11ea-bb37",
                name="My Snake",
                health=54,
                body=(
                    Point(x=0,y=1),
                    Point(x=0,y=0),
                    Point(x=1,y=0)),
                head=Point(x=0,y=1),
                length=3,
                shout="why are we shouting??")
            ]


