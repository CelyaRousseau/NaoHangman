# -*- coding: utf-8 -*-

class NovicePlayer:
    def get_letter(self, game):
        raise NotImplementedError

    def game_won(self, game):
        raise NotImplementedError

    def game_lost(self, game):
        raise NotImplementedError