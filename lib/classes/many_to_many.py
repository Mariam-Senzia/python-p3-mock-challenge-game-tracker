class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str) or not len(title) > 0:
            raise Exception("Invalid input")
        if hasattr(self, "_title"): 
            raise Exception("Title is immutable")
        self._title = title

    def results(self):
        #returns all results for the game
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set(result.player for result in self.results()))

    def average_score(self, player):
        total_score = 0
        num_of_results = 0
        for result in self.results():
            if result.player == player and result.game == self:
                total_score += result.score
                num_of_results += 1
        if num_of_results > 0:
            return total_score / num_of_results


class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self , username):
        if not isinstance(username, str) or not 2 <= len(username) <= 16 :
            raise Exception("Invalid input")
        self._username = username

    def results(self):
        #returns list of all players
        return [result for result in Result.all if result.player == self ]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        for result in self.results():
            if result.game == game:
                return True
        return False

    def num_times_played(self, game):
        count = 0
        for result in self.results():
            if result.game == game:
                count += 1
        return count

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if not isinstance(score, int) or not 1 <= score <= 5000 :
            raise Exception("Invalid Input")
        if hasattr(self, "_score"):
            raise Exception("Score is immutable")
        self._score = score

    def player(self):
        return [result for result in Result.all if result.player == self]
    
    def game(self):
        return [result for result in Result.all if result.game == self]