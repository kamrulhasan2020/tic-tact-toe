from .models import Game
from django.utils.crypto import get_random_string


def create_a_new_game_code():
    while True:
        unique_code = get_random_string(8)
        try:
            obj = Game.objects.get(code=unique_code)
            if not obj.active:
                obj.delete()
                return unique_code
        except Game.DoesNotExist:
            return unique_code




