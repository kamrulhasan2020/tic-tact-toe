from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from sqlalchemy import null
from .models import Game
from .helpers import create_a_new_game_code


class HomeView(TemplateView):
    template_name = 'main/home.html'


class GameView(TemplateView):
    template_name = 'main/game.html'


def new_game(request):
    code = create_a_new_game_code()
    request.session['code'] = code
    obj = Game(code=code)
    obj.save()
    data = {
        'code': code,
    }
    return JsonResponse(data)


def join_with_code(request):
    code = request.POST['game_code']
    try:
        game = Game.objects.get(code=code)
        request.session['code'] = code
        data = {
            'res': 'ok',
        }
    except Game.DoesNotExist:
        data = {
            'res':'not ok',
        }
    
    return JsonResponse(data)
    

def set_name(request):
    request.session['name'] = request.POST['name']
    try:
        code = request.session['code']
        try:
            game = Game.objects.get(code=code)
            if game.player1 == '':
                game.player1 = request.session['name']
            else:
                game.player2 = request.session['name']
                game.active = True
            game.save()
            data = {
                'status': 'ok',
            }
        except Game.DoesNotExist:
            data = {
                'status': 'game_code_does_not_exist',
            }
    except KeyError:
        data = {
            'status': 'no_game_is_set',
        }
    return JsonResponse(data)


class PaintCell(View):
    def get(self):
        code = self.request.GET['code']
        try:
            game = Game.objects.get(code=code)
        except Game.DoesNotExist:
            data ={
                'status':'0',
            }
            return JsonResponse(data)
        try:
            user_code = self.request.session['code']
        except KeyError:
            data={
                'status':'0',
            }
            return JsonResponse(data)
        if code != user_code:
            data={
                'status':'0',
            }
            return JsonResponse(data)
        cell = self.request.GET['cell']
        board = game.board
        if getattr(board, cell) != '':
            data={
                'status':'0',
            }
            return JsonResponse(data)
        try:
            name = self.request.session['name']
        except KeyError:
            data = {
                'status':'0',
            }
            return JsonResponse(data)
        
        if(board.turn == name or board.turn == null):
        
        