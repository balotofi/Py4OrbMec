import math
import matplotlib.pyplot as plt
import numpy as np


r2d = 180 / np.pi # convert a value in radians to degrees
d2r = 1.0 / r2d # convert a value in degrees to radians

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


def norm( v ):
	'''
	Returns the norm of a vector v
	'''
	return np.linalg.norm( v )

def normed( v ):
	'''
	Returns the normed vector of a vector v
	'''
	return v / np.linalg.norm( v )

def rotZ( a ):
	'''
	Returns reference Z axis rotation by multiplying rotation matrix by an angle a in radians
	'''
	return np.array( [ 
		[ math.cos( a ), -math.sin( a ), 0 ],
		[ math.sin( a ),  math.cos( a ), 0 ],
		[        0,             0,       1 ]
	] )

def rotX( a ):
	'''
	Returns reference X axis rotation by multiplying rotation matrix by an angle a in radians
	'''
	return np.array( [ 
		[ 1,              0,             0 ],
		[ 0, math.cos( a ), -math.sin( a ) ],
		[ 0, math.sin( a ),  math.cos( a ) ]
	] )

def rotY( a ):
	'''
	Returns reference Y axis rotation by multiplying rotation matrix by an angle a in radians
	'''
	return np.array( [ 
		[ math.cos( a ), 0, math.sin( a ) ],
		[ 0,             1,             0 ],
		[ -math.sin( a ),0, math.cos( a ) ]
	] )


def plot_reference_frames( frames, args ):
	_args = {
		'figsize'        : ( 12, 12 ),
		'frame_labels'   : [ '' ] * len( frames),
		'xlabel'         : "X",
		'ylabel'         : "Y",
		'zlabel'         : "Z",
		'xlim'           : 1,
		'ylim'           : 1,
		'zlim'           : 1
    }
    for key in args.keys():
	    _args[ key ] = args[ key ]
		
    fig     = plt.figure( figsize = _args[ 'figsize' ])
    ax      = fig.add_subplot( 111, projection=)
	




ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Vector Plot')

# plt.show()

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