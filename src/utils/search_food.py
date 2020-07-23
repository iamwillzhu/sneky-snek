from src.models.point import Point
from src.models.battlesnake import Battlesnake

FOOD = 5
HEAD = 2
BODY = 1
EMPTY_SPACE = 0 


def construct_food_snake_matrix(food, board, battlesnake):
    matrix = [[EMPTY_SPACE for _ in range(board.width)] for _ in range(board.height)]

    matrix[board.height - 1 - food.y][food.x] = FOOD

    for body in battlesnake.body:
        matrix[board.height - 1 - body.y][body.x] = BODY

    matrix[board.height - 1 - battlesnake.head.y][battlesnake.head.x] = HEAD

    return tuple(tuple(row) for row in matrix)

def find_closest_food_to_snake(board, battlesnake):
    min_distance_food_to_snake = float('inf')
    closest_food = None

    for food in board.food:
        distance_food_to_snake = abs(food.x - battlesnake.head.x) + abs(food.y - battlesnake.head.y)
        if distance_food_to_snake < min_distance_food_to_snake:
            min_distance_food_to_snake = distance_food_to_snake
            closest_food = food

    return closest_food

def get_successors(matrix, board, battlesnake):
    successors = []
    for i in range(board.height):
        for j in range(board.width):
            if matrix[i][j] == HEAD:
                if i > 0 and matrix[i-1][j] != BODY:
                    head = Point(
                            x=j,
                            y=board.height - 1 - (i-1))
                    successors.append(
                            Battlesnake(
                                id=battlesnake.id,
                                name=battlesnake.name,
                                body=(head,) + battlesnake.body[:battlesnake.length - 1],
                                head=head,
                                health=battlesnake.health,
                                length=battlesnake.length,
                                shout=battlesnake.shout))
                if i + 1 < board.height and matrix[i+1][j] != BODY:
                    head = Point(
                            x=j,
                            y=board.height - 1 - (i+1))
                    successors.append(
                            Battlesnake(
                                id=battlesnake.id,
                                name=battlesnake.name,
                                body=(head,) + battlesnake.body[:battlesnake.length - 1],
                                head=head,
                                health=battlesnake.health,
                                length=battlesnake.length,
                                shout=battlesnake.shout))
                if j > 0 and matrix[i][j-1] != BODY:
                    head = Point(
                            x=j-1,
                            y=board.height - 1 - i)
                    successors.append(
                            Battlesnake(
                                id=battlesnake.id,
                                name=battlesnake.name,
                                body=(head,) + battlesnake.body[:battlesnake.length - 1],
                                head=head,
                                health=battlesnake.health,
                                length=battlesnake.length,
                                shout=battlesnake.shout))
                if j + 1 < board.width and matrix[i][j+1] != BODY:
                    head = Point(
                            x=j+1,
                            y=board.height - 1 - i)
                    successors.append(
                            Battlesnake(
                                id=battlesnake.id,
                                name=battlesnake.name,
                                body=(head,) + battlesnake.body[:battlesnake.length - 1],
                                head=head,
                                health=battlesnake.health,
                                length=battlesnake.length,
                                shout=battlesnake.shout))
    return successors



                    
