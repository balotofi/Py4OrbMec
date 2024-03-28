'''
Py4OrbMec | Python for Orbital Mechanics by Husseinat Etti-Balogun
https://github.com/balotofi/py4orbmec

COES Example
09/03/2024
'''

#---------------------------- IMPORTS ----------------------------------------------------

import stdlib.orbittools as st

#---------------------------- MAIN CODE ----------------------------------------------------

if __name__ == '__main__':
    # solve for trueanom, get position and velocity
    st.TrueAnomaly()
    position = st.polarEqn()
    velocity = st.visViva()
    print('\nposition is %.10f m and velocity is %.10f m/s' % (position, velocity))