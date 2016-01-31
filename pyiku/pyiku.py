from collections import deque
import random

import markov
from syllable_counter import SyllableCounter

PYIKU_PUNCH_LINE_LAST = 1
PYIKU_PUNCH_LINE_FIRST = 2


class Pyiku:
    
    def __init__(self, markov_chain):
        self.mc = markov_chain
        
        
    def generate_pyiku_line(self, syllables, pyiku_text ='', attempt = 0):
        """ Generates a single lin of pyiku
        :param syllables: required number of syllables in the line
        :param pyiku_text: previous lines of pyiku
        :param attempt: number of re-trys (recurrence)
        :return: string of pyiku line
        """

        if attempt > 100:
            return "" # prevent stack overflow - allow only 100 recursive calls

        if pyiku_text.strip() == '':
            seed = random.randint(0, len(self.mc.words) - 3)
            w = deque([self.mc.words[seed], self.mc.words[seed + 1]])
        else:
            w = deque([pyiku_text.split(None)[-2],  # get the last word of already assembled text
                       pyiku_text.split(None)[-1]])
            # generate next words and discard the seeding ones
            w.append(random.choice(self.mc.word_cache[tuple(w)]))
            w.popleft()
            w.append(random.choice(self.mc.word_cache[tuple(w)]))
            w.popleft()

        pyiku_line = '  '
        # loop until correct count of syllables
        line_syllables = 0
        while line_syllables < syllables:
            w.append(random.choice(self.mc.word_cache[tuple(w)]))
            word = w.popleft()
            line_syllables += SyllableCounter(word)
            pyiku_line += word + ' '

        # if it's too short or too long, try again
        if line_syllables != syllables:
            pyiku_line = self.generate_pyiku_line(syllables, pyiku_text, attempt + 1)

        return pyiku_line.strip()
    
    
    def generate_pyiku(self, style=PYIKU_PUNCH_LINE_LAST):

        if style == PYIKU_PUNCH_LINE_LAST:
            pyiku = self.generate_pyiku_line(5)
            pyiku = "".join([pyiku, "\n", self.generate_pyiku_line(7, pyiku)])
            pyiku = "".join([pyiku, ":\n",  self.generate_pyiku_line(5)])
        elif style == PYIKU_PUNCH_LINE_FIRST:
            pyiku = self.generate_pyiku_line(5)
            pyiku = "".join([pyiku, ":\n", self.generate_pyiku_line(7)])
            pyiku = "".join([pyiku, "\n",  self.generate_pyiku_line(5, pyiku)])

        return pyiku