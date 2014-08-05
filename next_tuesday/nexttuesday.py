import re
import os
import random


class NextTuesday(object):
	re_split = re.compile(r'(\s|...|--)+')
	re_sanitize = re.compile(r'^[\.,;?:<>{}()\[\]]+|[\.,;?:<>{}()\[\]]+$')

	def __init__(self, text=None):
		self.next_words = {}
		self.words_beginning_with = {}

		if text:
			self.compile(text)

	def compile(self, text):
		words = (
			word
			for words in (
				self.re_sanitize.sub(' ', word)
				for word in self.re_split.split(text)
			)
			for word in words.split(' ')
		)

		prev = None
		for word in words:
			if prev:
				self.next_words.setdefault(prev, set()).add(word)
			else:
				prev = word

		for word in self.next_words:
			letter = word[0]
			self.words_beginning_with.setdefault(letter, []).append(word)

	def get_random_word(self, words):
		if not words:
			return None

		return words[random.randint(0, len(words))]

	def get_random_word_beginning_with(self, letter):
		words = self.words_beginning_with.get(letter)
		return self.get_random_word(words)

	def get_next_random_word_beginning_with(self, previous, letter):
		words = set(self.next_words.get(previous, [])) & set(self.words_beginning_with.get(letter, []))
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
