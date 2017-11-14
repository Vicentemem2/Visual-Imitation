#!/usr/bin/env python
#codo izquierdo: 1. (-356.45, 258.70, 1951.21) //(x',y',z')
#codo izquierdo: 2. (-400.44, 248.07, 2224.67)
#hombro izquierdo: 1. (-170.53, 222.65, 2102.93)


#codo izquierdo: 3. (-89.26, 121.40, 2202.82)
######################################################################################################
#hombro izquierdo: 1. (-241.99, 61.72, 2431.81)
#codo izquierdo: 1. (-298.11, 26.22, 2633.05)

#radi1= math.atan2(2431.81-2633.05,-241.99+298.11)

#hombro izquierdo: 2. (-199.86, 89.15, 2156.93)
#codo izquierdo: 2. (-375.93, 153.48, 2019.42)

#hombro izquierdo: 1. (-200.80, 77.07, 2320.52)
#codo izquierdo: 1. (-332.16, 60.62, 2302.84)
######################################################################################################
import rospy
import math
import baxter_interface
from std_msgs.msg import String
rospy.init_node('Mover')

#numero = 0.00

def moveToZero():
	limb_right = baxter_interface.Limb('right')
	limb_left = baxter_interface.Limb('left')

	right = {'right_s0': 0.00, 'right_s1': 0.00, 'right_w0': 0.00, 'right_w1': 0.00, 'right_w2': 0.00, 'right_e0': 0.00, 'right_e1': 0.00}
	left = {'left_s0': 0.00, 'left_s1': 0.00, 'left_w0': 0.00, 'left_w1': 0.00, 'left_w2': 0.00, 'left_e0': 0.00, 'left_e1': 0.00}

	limb_right.move_to_joint_positions(right,5)
	limb_left.move_to_joint_positions(left,5)

def moveTo(name, post):
	limb = baxter_interface.Limb(name)
	if name == 'left':	
		moving = {'left_s0': post[0], 'left_s1': post[1], 'left_w0': post[2], 'left_w1': post[3], 'left_w2': post[4], 'left_e0': post[5], 'left_e1': post[6]}
	else:
		moving = {'right_s0': post[0], 'right_s1': post[1], 'right_w0': post[2], 'right_w1': post[3], 'right_w2': post[4], 'right_e0': post[5], 'right_e1': post[6]}		
	
	limb.move_to_joint_positions(moving,5)


radi1= math.atan2(2431.81-2633.05,-241.99+298.11)

radi2= math.atan2(2320.52-2302.84,-200.80+332.16)

radi3= math.atan2(2102.93-2202.82,-89.26-170.53)

print radi1
print radi2
print radi3

#radi1 = 3.14 - radi1
pos1 = [radi1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
pos12 = [radi2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#pos13 = [radi3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
pos2 = [-1.441426162661994, 0.8389151064712133, 0.14240920034028015, -0.14501001475655606, -1.7630090377446503, -1.5706376573674472, 1.59225918246029519]
lpos1 = [-1.441426162661994, 0.8389151064712133, 0.14240920034028015, -0.14501001475655606, -1.7630090377446503, -1.5706376573674472, 0.09225918246029519]

rpos1 = [1.8342575250183106, 1.8668546167236328, -0.45674277907104494, -0.21667478604125978, -1.2712865765075685, 1.7472041154052735, -2.4582042097778323]
lpos2 = [-0.949534106616211, 1.4994662184448244, -0.6036214393432617, -0.7869321432861328, -2.4735440176391603, -1.212228316241455, -0.8690001153442384]

#moveToZero()
moveTo('right', pos1)
moveTo('right', pos12)
#moveTo('right', pos13)

#moveTo('left', lpos1)


quit()
