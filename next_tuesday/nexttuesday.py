import re
import os
import random


class NextTuesday(object):
	re_split = re.compile(r'(\s|\.\.\.|--)+')
	re_sanitize = re.compile(r'^[\.\'",;!?&:<>{}()\[\]\s]+|[\.\'",;!?&:<>{}()\[\]\s]+$')
	MIN_WORD_LENGTH = 4

	def __init__(self, text=None):
		self.next_words = {}
		self.words_beginning_with = {}

		if text:
			self.compile(text)

	def compile(self, text):
		words = (
			word
			for words in (
				self.re_sanitize.sub(' ', word.lower())
				for word in self.re_split.split(text)
			)
			for word in words.split(' ')
		)

		prev = None
		for word in words:
			# Ignore empty words
			if not word:
				continue
			# Ignore small words
			if len(word) < self.MIN_WORD_LENGTH:
				continue
			if prev:
				self.next_words.setdefault(prev, set()).add(word)
			prev = word

		for word in self.next_words:
			letter = word[0]
			self.words_beginning_with.setdefault(letter, []).append(word)

	def get_random_word(self, words):
		if not words:
			return None

		return words[random.randint(0, len(words) - 1)]

	def get_random_word_beginning_with(self, letter):
		words = self.words_beginning_with.get(letter)
		return self.get_random_word(words)

	def get_next_random_word_beginning_with(self, previous, letter):
		nexts = set(self.next_words.get(previous, []))
		beginning = set(self.words_beginning_with.get(letter, []))
		words = list(nexts & beginning)
		return self.get_random_word(words)

	def try_create_phrase(self, word):
		words = []
		letter = word[0]
		letter_word = self.get_random_word_beginning_with(letter)
		if not letter_word:
			return None
		words.append(letter_word)

		for letter in word[1:]:
			letter_word = self.get_next_random_word_beginning_with(letter_word, letter)
			if not letter_word:
				return None
			words.append(letter_word)

		if len(word) != len(words):
			return None

		return ' '.join(words)

	def create_phrase(self, word='cunt'):
		for _ in xrange(50):
			phrase = self.try_create_phrase(word)
			if phrase:
				return phrase
