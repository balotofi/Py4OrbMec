'''
Py4OrbMec | Python for Orbital Mechanics by Husseinat Etti-Balogun
https://github.com/balotofi/py4orbmec

Universe Class Definition ans Simulation
02/03/2024
'''

#-----------------------------------------------------------------------
# Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero.
# Last updated: Fri Oct 20 20:45:16 EDT 2017.
#-----------------------------------------------------------------------

import sys
import stdlib.stddraw as stddraw
import stdlib.stdarray as stdarray
from stdlib.instream import InStream
from stdlib.vector import Vector
from stdlib.color import DARK_RED, PINK, BOOK_LIGHT_BLUE
from body import Body

class Universe:

    def __init__(self, filename):
        instream = InStream(filename)
        n = instream.readInt()
        radius = instream.readFloat()
        stddraw.setXscale(-radius, +radius)
        stddraw.setYscale(-radius, +radius)
        self._bodies = stdarray.create1D(n)
        for i in range (n):
            rx = instream.readFloat()
            ry = instream.readFloat()
            vx = instream.readFloat()
            vy = instream.readFloat()
            mass = instream.readFloat()
            r = Vector([rx, ry])
            v = Vector([vx, vy])
            self._bodies[i] = Body(r, v, mass)

    def increaseTime(self, dt):
        n = len(self._bodies)
        f = stdarray.create1D(n, Vector([0, 0]))
        for i in range(n):
            for j in range(n):
                if i != j:
                    bodyi = self._bodies[i]
                    bodyj = self._bodies[j]
                    f[i] = f[i] + bodyi.forceFrom(bodyj)
        for i in range(n):
            self._bodies[i].move(f[i], dt)

    def draw(self):
        # for body in self._bodies:
        #     body.draw()
        n = len(self._bodies)
        for i in range(n):
            self._bodies[i].draw(0.0125, BOOK_LIGHT_BLUE)
            for j in range(n):
                    self._bodies[j].draw(0.05, DARK_RED)

# ------------ to run the file

def main():
    filename = sys.argv[1]
    dt = float(sys.argv[2])
    universe = Universe(filename)
    while True:
        universe.increaseTime(dt)
        stddraw.clear(PINK)
        universe.draw()
        stddraw.show(10)

if __name__ == '__main__':
    main()