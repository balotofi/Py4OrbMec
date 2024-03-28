#--------------------------------------------------------------------------------
# Husseinat Etti-Balogun
# 28/03/2024
#--------------------------------------------------------------------------------
import math as m



def Kepler(E, args):
    # defines the function of Kepler's equation
    return ( E + (args[0] * m.sin(E) - args[1]))

def KeplerDeriv (E, args):
    #defines the derivative function of Kepler's equation
    return ( 1 - args[0] * m.cos(E))

def NewtonsAlgotrithm (f, f_prime, current_guess, args, tolerance=0.01):
    # newtons method of root solving variable functions
    step = 1 # step counter

    delta_f = f(current_guess, args) / f_prime(current_guess, args) # calculate the ratio of function and derivative

    # start loop and break when absolute of delta_f is less than tolerance
    while abs( delta_f ) > tolerance:

        current_guess -= delta_f # calculate next current guess

        delta_f = f(current_guess, args) / f_prime(current_guess, args) # calculate new delta_f

        step += 1 # increment step

    return current_guess, step


def TrueAnomaly():
    eccAnom, steps = NewtonsAlgotrithm(Kepler, KeplerDeriv, E0, args )
    eccFrac = ( 1 - e ) / ( 1 + e )
    halfEccAnom = eccAnom / 2
    nu = 2 * m.atan( m.sqrt( eccFrac * m.tan(halfEccAnom )) )
    return nu 

def polarEqn():
    # return radial value of position of rocket
    p = a * ( 1 - e**2)
    newDeriv = 1 + e * m.cos(TrueAnomaly())
    r = p / newDeriv
    return r

def visViva():
    #return velocity at elapsed time
    r = polarEqn()
    v = m.sqrt(mu * ( ( 2 / r ) - ( 1 / a )))
    return v