'''
Py4OrbMec | Python for Orbital Mechanics by Husseinat Etti-Balogun
https://github.com/balotofi/py4orbmec

Coordinate Frame Rotation Visualisation Example
19/03/2024
'''

#---------------------------- IMPORTS ------------------------------------------------------

import math
import matplotlib.pyplot as plt
import numpy as np
import stdlib.orbittools as st 
#--------------------------------------------------------------------------------

np.matmul
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

v1 = np.array([1, 2, 3])
v2 = np.array([-2, 1, 4])
v3 = np.array([-2, -1, -4])

#VECTOR 1
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', arrow_length_ratio=0.1)
#VECTOR 2
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', arrow_length_ratio=0.1)
#VECTOR 3
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='g', arrow_length_ratio=0.1)


ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Vector Plot')

# plt.show()
#---------------------------- MAIN CODE ------------------------------------------

if __name__ == '__main__':
	angle = 70 * d2r
	z_rotation = Cz(angle)
	
    plot_config = {
          'frame_labels': [ 'Z' ],
		'frame_colours': [ 'b' ],
		'filename' : fn 
		'show' : True
	}
		
    plot_reference_frames( [ z_rotation ], plot_config)