from dataclasses import dataclass
from typing import Tuple
from src.models.point import Point
from src.models.battlesnake import Battlesnake

@dataclass(frozen=True)
class Board:
    height: int
    width: int
    food: Tuple[Point, ...]
    snakes: Tuple[Battlesnake, ...]

    @classmethod
    def from_json_input(cls, json):
        height = json["board"]["height"]
        width = json["board"]["width"]
        food = tuple([
            Point(
                x=food_json["x"],
                y=food_json["y"])
            for food_json in json["board"]["food"]])
        snakes = tuple([
            Battlesnake(
                id=snake_json["id"],
                name=snake_json["name"],
                health=snake_json["health"],
                body=tuple([
                    Point(
                        x=body_json["x"],
                        y=body_json["y"])
                    for body_json in snake_json["body"]]),
                head=Point(
                    x=snake_json["head"]["x"],
                    y=snake_json["head"]["y"]),
                length=snake_json["length"],
                shout=snake_json["shout"]) 
            for snake_json in json["board"]["snakes"]])

        return cls(
                height=height,
                width=width,
                food=food,
                snakes=snakes)
