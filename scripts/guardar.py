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
import time
import threading
import baxter_interface
import roslib; roslib.load_manifest("moveit_python")
from moveit_python import PlanningSceneInterface, MoveGroupInterface
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
rospy.init_node('Mover')
import sys


#numero = 0.00

def moveToZero():
	limb_right = baxter_interface.Limb('right')
	limb_left = baxter_interface.Limb('left')

	right = {'right_s0': 0.00, 'right_s1': 0.00, 'right_w0': 0.00, 'right_w1': 0.00, 'right_w2': 0.00, 'right_e0': 0.00, 'right_e1': 0.00}
	left = {'left_s0': 0.00, 'left_s1': 0.00, 'left_w0': 0.00, 'left_w1': 0.00, 'left_w2': 0.00, 'left_e0': 0.00, 'left_e1': 0.00}

	hilo1 = threading.Thread(target=limb_right.move_to_joint_positions, args=(right,5))
	hilo2 = threading.Thread(target=limb_left.move_to_joint_positions, args=(left,5))
	hilo1.start()
	hilo2.start()

	hilo1.join()
	hilo2.join()


def moveToArriba():
	limb_right = baxter_interface.Limb('right')
	limb_left = baxter_interface.Limb('left')

	left = {'left_s0': -0.0624913498759, 'left_s1': 0.122212305665, 'left_w0': 0.2340901196, 'left_w1': 0.00, 'left_w2': 0.00, 'left_e0': -2.36234736443, 'left_e1': 1.48204886913}
	right = {'right_s0': -0.684391975403, 'right_s1': 0.0993161052465, 'right_w0': 5.70570516586, 'right_w1': 0.00, 'right_w2': 0.00, 'right_e0': -3.06823801994, 'right_e1': 1.69943296909}

	hilo1 = threading.Thread(target=limb_right.move_to_joint_positions, args=(right,5))
	hilo2 = threading.Thread(target=limb_left.move_to_joint_positions, args=(left,5))
	hilo1.start()
	hilo2.start()

	hilo1.join()
	hilo2.join()

def moveToAbajo():
	limb_left = baxter_interface.Limb('left')
	limb_right = baxter_interface.Limb('right')

	left = {'left_s0': 0.00, 'left_s1': 0.00, 'left_w0': 0.00, 'left_w1': 0.00, 'left_w2': 0.00, 'left_e0': 0.00, 'left_e1': 0.00}
	right = {'right_s0': 0.00, 'right_s1': 0.00, 'right_w0': 0.00, 'right_w1': 0.00, 'right_w2': 0.00, 'right_e0': 0.00, 'right_e1': 0.00}

	hilo1 = threading.Thread(target=limb_left.move_to_joint_positions, args=(left,5))
	hilo2 = threading.Thread(target=limb_right.move_to_joint_positions, args=(right,5))
	hilo1.start()
	hilo2.start()

	hilo1.join()
	hilo2.join()

def moveToCubo():
	limb_left = baxter_interface.Limb('left')
	limb_right = baxter_interface.Limb('right')

	left = {'left_s0': 0.00, 'left_s1': 0.00, 'left_w0': 0.00, 'left_w1': 0.00, 'left_w2': 0.00, 'left_e0': 0.00, 'left_e1': 0.00}
	right = {'right_s0': 0.00, 'right_s1': 0.00, 'right_w0': 0.00, 'right_w1': 0.00, 'right_w2': 0.00, 'right_e0': 0.00, 'right_e1': 0.00}

	hilo1 = threading.Thread(target=limb_left.move_to_joint_positions, args=(left,5))
	hilo2 = threading.Thread(target=limb_right.move_to_joint_positions, args=(right,5))
	hilo1.start()
	hilo2.start()

	hilo1.join()
	hilo2.join()


def moveTo(name, post):
	limb = baxter_interface.Limb(name)
	if name == 'left':
		moving = {'left_s0': post[0], 'left_s1': post[1], 'left_w0': post[2], 'left_w1': post[3], 'left_w2': post[4], 'left_e0': post[5], 'left_e1': post[6]}
	else:
		moving = {'right_s0': post[0], 'right_s1': post[1], 'right_w0': post[2], 'right_w1': post[3], 'right_w2': post[4], 'right_e0': post[5], 'right_e1': post[6]}

	limb.move_to_joint_positions(moving,3)

def moveTo2(postL,postR):
	limb_left = baxter_interface.Limb('left')
	limb_right = baxter_interface.Limb('right')

	left = {'left_s0': postL[0], 'left_s1': postL[1], 'left_w0': postL[2], 'left_w1': postL[3], 'left_w2': postL[4], 'left_e0': postL[5], 'left_e1': postL[6]}
	right = {'right_s0': postR[0], 'right_s1': postR[1], 'right_w0': postR[2], 'right_w1': postR[3], 'right_w2': postR[4], 'right_e0': postR[5], 'right_e1': postR[6]}

	hilo3 = threading.Thread(target=limb_right.move_to_joint_positions, args=(right,1))
	hilo4 = threading.Thread(target=limb_left.move_to_joint_positions, args=(left,1))
	hilo3.start()
	hilo4.start()
	hilo3.join()
	hilo4.join()

def moverArchivo(array):
	limb_left = baxter_interface.Limb('left')
	limb_right = baxter_interface.Limb('right')

	left = {'left_s0': array[0], 'left_s1': array[1], 'left_w0': array[2], 'left_w1': array[3], 'left_w2': array[4], 'left_e0': array[5], 'left_e1': array[6]}
	right = {'right_s0': array[7], 'right_s1': array[8], 'right_w0': array[9], 'right_w1': array[10], 'right_w2': array[11], 'right_e0': array[12], 'right_e1': array[13]}

	hilo3 = threading.Thread(target=limb_right.move_to_joint_positions, args=(right,1))
	hilo4 = threading.Thread(target=limb_left.move_to_joint_positions, args=(left,1))

	hilo3.start()
	hilo4.start()
	hilo3.join()
	hilo4.join()

def grabar(nom,posL,posR):
	outfile = open(nom, 'a') # Indicamos el valor 'w'.
	for i in range(len(posL)):
		outfile.write(str(posL[i]))
		if (i != 6):
			outfile.write(',')
	for i in range(len(posR)):
		outfile.write(','+str(posR[i]))
	outfile.write('\n')
	outfile.close()

def leer(cosa):
	file=open(cosa,'r')
	data=file.readlines()
	file.close()
	#contador=0
	array=[]
	for linea in data:
	    for numero in linea.split(','):
			array.append(float(numero))

	return array


def mover(array):
	posRecord=[]
	for i in range(0,len(arr),14):
		#print i
		for j in range(14):
			posRecord.append(arr[i+j])
		#print posRecord
		moverArchivo(posRecord)
		posRecord = []




#moveToArriba()
moveToZero()
#arr = leer(sys.argv[1])
#mover(arr)

#"""

while True:
	temp = rospy.wait_for_message("chatter", Float64MultiArray)
	#print temp.data[1]
	#radi1 = 3.14 - radi1
	posL = [temp.data[0], temp.data[1], temp.data[4], 0.0, 0.0, temp.data[2], temp.data[3]]
	#pos1 = [1, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]

	posR = [temp.data[6], temp.data[7], temp.data[10], 0.0, 0.0, temp.data[8], temp.data[9]]
	#grabar(sys.argv[1],posL,posR)

	#pos13 = [radi3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	#pos2 = [-1.441426162661994, 0.8389151064712133, 0.14240920034028015, -0.14501001475655606, -1.7630090377446503, -1.5706376573674472, 1.59225918246029519]
	#lpos1 = [-1.441426162661994, 0.8389151064712133, 0.14240920034028015, -0.14501001475655606, -1.7630090377446503, -1.5706376573674472, 0.09225918246029519]

	#rpos1 = [1.8342575250183106, 1.8668546167236328, -0.45674277907104494, -0.21667478604125978, -1.2712865765075685, 1.7472041154052735, -2.4582042097778323]
	#lpos2 = [-0.949534106616211, 1.4994662184448244, -0.6036214393432617, -0.7869321432861328, -2.4735440176391603, -1.212228316241455, -0.8690001153442384]

	#moveToZero()
	#moveTo('right', posR)
	#moveTo('left', posL)
	moveTo2(posL,posR)
#"""

quit()
