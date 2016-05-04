# -*- coding: utf-8 -*-
import sys
import random

class GeniusPlayer:
	
	def pick_up_a_word(self):
		raise NotImplementedError

	def game_won(self, game):
		raise NotImplementedError

	def game_lost(self, game):
		raise NotImplementedError