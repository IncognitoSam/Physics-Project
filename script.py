from math import *
from vpython import *

g = vector(0,9.8,0)

m1 = 5
m2 = 5 

k1 = 10
k2 = 10

equil1 = vector(0,-5,0)
equil2 = vector(0,-10,0) 

mass1 = box(pos=equil1,size=vector(5,5,5),color=color.green)
mass2 = box(pos=equil2*2,size=vector(5,5,5),color=color.red)
ceiling = box(pos=vector(0,0,0),size=vector(5,1,5))

spring1 = helix(pos=ceiling.pos,axis=mass1.pos,length=-(mass1.pos.y-ceiling.pos.y),radius=1)
spring2 = helix(pos=mass1.pos,axis=mass2.pos,length=-(mass2.pos.y-mass1.pos.y),radius=1)

mass1.mass = m1
mass2.mass = m2

mass1.momentum = vector(0,0,0)
mass2.momentum = vector(0,0,0)

mass1.force = vector(0,0,0)
mass2.force = vector(0,0,0)

time_limit = 100
dt = .001
time = 0

while time < time_limit:
	rate(1000)

	time += dt

	mass1.force = -mass1.mass*g-(k1*((mass1.pos-ceiling.pos)-equil1))+(k2*((mass2.pos-mass1.pos)-equil2))
	mass2.force = -mass2.mass*g-(k2*((mass2.pos-mass1.pos)-equil2))

	mass1.momentum += mass1.force*dt
	mass2.momentum += mass2.force*dt

	mass1.pos += mass1.momentum*dt/mass1.mass
	mass2.pos += mass2.momentum*dt/mass2.mass
	
	spring2.pos=mass1.pos
	
	spring1.length=mag(mass1.pos-ceiling.pos)
	spring2.length=mag(mass2.pos-mass1.pos)	

	KE = .5*mass1.mass*mag2(mass1.momentum/mass1.mass)+.5*mass2.mass*mag2(mass2.momentum/mass2.mass)
	GPE = mass1.mass*mag(g)*(mass1.pos.y-ceiling.pos.y)+mass2.mass*mag(g)*(mass2.pos.y-ceiling.pos.y)
	SPE = .5*k1*mag2(mass1.pos-equil1)+.5*k2*mag2((mass2.pos-mass1.pos)-equil2)

	print(KE+GPE+SPE)


