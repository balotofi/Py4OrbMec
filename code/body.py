
from stdlib.color import BLACK
import stdlib.stddraw as stddraw

class Body:

    def __init__(self, r, v, mass):
        self._r = r # position
        self._v = v # velocity
        self._mass = mass  # mass

    def move(self, f, dt):
        a = f.scale(1 / self._mass)
        self._v = self._v + (a.scale(dt))
        self._r = self._r + self._v.scale(dt)

    def forceFrom(self, other):
        G = 6.67e-11
        delta = other._r - self._r
        dist = abs(delta)
        magnitude = (G * self._mass * other._mass) / (dist * dist)
        return delta.direction().scale(magnitude)

    def draw(self, size=0.0125, color=BLACK):
        stddraw.setPenRadius(size)
        stddraw.setPenColor(color)
        stddraw.point(self._r[0], self._r[1])