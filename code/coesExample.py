#--------------------------------------------------------------------------------
# Husseinat Etti-Balogun
# 09/03/2024
#--------------------------------------------------------------------------------
import math as m
import stdlib.stdtools as st

#---------------------------- CONSTANTS ----------------------------------------------------

a = 2160000 #semi major axis in meters
Kerbin_mass = 5.29e22 # mass of the body in kg
e = 0.832 # eccentricity
t = 900 # time elapsed in seconds
G = 6.67e-11 # universal constant of gravitation
mu = G * Kerbin_mass # kerbin grav const 
T = 2 * m.pi * m.sqrt( (a**3) / mu ) # the orbital period of rocket around Kerbin in days
n = ( 2 * m.pi ) / T # mean motion of the rocket rad/sec

#---------------------------- MAIN CODE ----------------------------------------------------

if __name__ == '__main__':
    # solve for trueanom, get position and velocity
    st.TrueAnomaly()
    position = st.polarEqn()
    velocity = st.visViva()
    print('\nposition is %.10f m and velocity is %.10f m/s' % (position, velocity))