from dataclasses import dataclass
from typing import Tuple

from src.models.point import Point

@dataclass(frozen=True)
class Battlesnake:
    id: str
    name: str
    health: int
    body: Tuple[Point, ...]
    head: Point
    length: int
    shout: str

    @classmethod
    def from_json_input(cls, json):
        id = json["you"]["id"]
        name = json["you"]["name"]
        health = json["you"]["health"]
        body = tuple([
            Point(
                x=body_json["x"],
                y=body_json["y"])
            for body_json in json["you"]["body"]])

        head = Point(x=json["you"]["head"]["x"], y=json["you"]["head"]["y"])
        length = json["you"]["length"]
        shout = json["you"]["shout"]

        return cls(
                id=id,
                name=name,
                health=health,
                body=body,
                head=head,
                length=length,
                shout=shout)
