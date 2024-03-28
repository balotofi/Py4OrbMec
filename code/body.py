'''
Py4OrbMec | Python for Orbital Mechanics by Husseinat Etti-Balogun
https://github.com/balotofi/py4orbmec

Orbital Body Class Definition
02/03/2024
'''

#-----------------------------------------------------------------------
# Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero.
# Last updated: Fri Oct 20 20:45:16 EDT 2017.
#-----------------------------------------------------------------------

#---------------------------- IMPORTS ----------------------------------------------------

import sys

from stdlib.color import BLACK
import stdlib.stddraw as stddraw

#-----------------------------------------------------------------------------------------
class Body:
    AU = 149.6e6 * 1000
	G = 6.67428e-11
	SCALE = 250 / AU  # 1AU = 100 pixels
	TIMESTEP = 3600*24 # 1 day

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
    
    def attraction(self, other):
		other_x, other_y = other.x, other.y
		distance_x = other_x - self.x
		distance_y = other_y - self.y
		distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

		if other.sun:
			self.distance_to_sun = distance

		force = self.G * self.mass * other.mass / distance**2
		theta = math.atan2(distance_y, distance_x)
		force_x = math.cos(theta) * force
		force_y = math.sin(theta) * force
		return force_x, force_y

	def update_position(self, planets):
		total_fx = total_fy = 0
		for planet in planets:
			if self == planet:
				continue

			fx, fy = self.attraction(planet)
			total_fx += fx
			total_fy += fy

		self.x_vel += total_fx / self.mass * self.TIMESTEP
		self.y_vel += total_fy / self.mass * self.TIMESTEP

		self.x += self.x_vel * self.TIMESTEP
		self.y += self.y_vel * self.TIMESTEP
		self.orbit.append((self.x, self.y))


    def draw(self, size=0.0125, color=BLACK):
        stddraw.setPenRadius(size)
        stddraw.setPenColor(color)
        stddraw.point(self._r[0], self._r[1])