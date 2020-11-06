from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterprojectapi.models import Game, GameCategory
from django.contrib.auth.models import User


class Games(ViewSet):

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        created_by = request.auth.user

        game = Game()
        game.title = request.data["title"]
        game.description = request.data["description"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.designer = request.data["designer"]
        game.year_released = request.data["year_released"]
        game.time_of_play = request.data["time_of_play"]
        game.recommended_age = request.data["recommended_age"]
        game.created_by = created_by

        try:
            game.save()
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        created_by = request.auth.user

        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.descrition = request.data["maker"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.designer = request.data["designer"]
        game.year_released = request.data["year_released"]
        game.time_of_play = request.data["time_of_play"]
        game.recommended_age = request.data["recommended_age"]
        game.created_by = created_by

        game.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            game = Game.objects.get(pk=pk)
            game.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()

        serializer = GameSerializer(
            games, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['get', 'post', 'delete'], detail=True)
    def addCategory(self, request, pk=None):

        if request.method == "POST":

            game = Game.objects.get(pk=pk)

            try:
                addCategory = GameCategory()
                addCategory.category = category
                addCategory.game = game
                addCategory.save()

                return Response({}, status=status.HTTP_201_CREATED)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', )

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """
    created_by = UserSerializer(many = False)

    class Meta:
        model = Game
        fields = ('id', 'title', 'designer', 'description', 'year_released', 'number_of_players', 'time_of_play', 'recommended_age', 'created_by')
        depth = 1