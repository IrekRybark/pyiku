"""
The MIT License (MIT)

Copyright (c) 2016 Irek Rybark

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Silly little attempt to generate haiku poems based on given corpus of a text.
I call it pyiku to make sure that hypothetical International Association of Haiku Authors does not send mafia after me.

The algorithm is based on gjreda/beer-snob-says attempt to write Twitter bot generating snobby beer reviews.

Credits:
- Markov Chains: gjreda/beer-snob-says
- Syllable counting: M. Emre Aydın (http://eayd.in/?p=232)

"""

from markov import MarkovChain
from pyiku import Pyiku
import pyiku

def main():
    with open("../data/beer_reviews.txt") as f:
        text = [line for line in f]

    mc = MarkovChain(text, num = 3)
    pk = Pyiku(mc)

    # just spit out some pyikus
    for style in range(1,3):
        print("\n\nStyle: %d" % style)
        for i in range(0,10):
            out = pk.generate_pyiku(style)
            print("\n")
            print(out)


if __name__ == '__main__':
    main()
