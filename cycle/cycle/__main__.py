import constants

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point

def main():

    # create the cast
    cast = Cast()
    # cast.add_actor("foods", Food())
    cast.add_actor("cycle1", Cycle(constants.RED, -5 * constants.CELL_SIZE))
    cast.add_actor("cycle2", Cycle(constants.GREEN, 5 * constants.CELL_SIZE))
    cast.add_actor("score1", Score('Player 1', Point(0,0)))
    cast.add_actor("score2", Score('Player 2', Point(765,0)))
    
    

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()