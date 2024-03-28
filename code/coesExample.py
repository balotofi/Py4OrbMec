#--------------------------------------------------------------------------------
# Husseinat Etti-Balogun
# 09/03/2024
#--------------------------------------------------------------------------------
import math as m
import stdlib.stdtools as st

#---------------------------- MAIN CODE ----------------------------------------------------

if __name__ == '__main__':
    # solve for trueanom, get position and velocity
    st.TrueAnomaly()
    position = st.polarEqn()
    velocity = st.visViva()
    print('\nposition is %.10f m and velocity is %.10f m/s' % (position, velocity))