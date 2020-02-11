from big_ol_pile_of_manim_imports import *
import numpy as np
import itertools as it
from manimlib.constants import *
from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Polygon


ac= RED_D
bc = BLUE
cc = PURPLE_A
tc = YELLOW_D

pts = np.array([[0, -2, 0],[0, 1, 0],[-1, -2, 0],[0, -3, 0],[-1, -3, 0],[3, -2, 0],[3, 1, 0],[-4, -1, 0],[-3, 2, 0],[-2, -1, 0],[-2, 3, 0],[-6, 3, 0],[-6, -1, 0],[-2/3, 1, 0],[-7/3, -3, 0],[7/3, -3, 0],[-1/3, -5/3, 0],[-1/3, -3, 0],[-61/39, -15/13, 0],[11/15, -13/15, 0],])
d = np.array([[3, 2, 0],[-2, 1, 0],[-2, 2, 0],[2, 2, 0],[0, 1, 0],[-1, 1, 0],[10.5*0.25, 0, 0],[1, 0, 0]])

def Triangle(**kwargs):
	return Polygon(*pts[[1, 0, 2]], color = tc, **kwargs, fill_color = tc, fill_opacity = 0.7)

def a_square(**kwargs):
    return Polygon(*pts[[0, 2, 4, 3]], color = ac, **kwargs, fill_color = ac, fill_opacity = 0.7)

def b_square(**kwargs):
    return Polygon(*pts[[1, 0, 5, 6]], color = bc, **kwargs, fill_color = bc, fill_opacity = 0.7)

def c_square(**kwargs):
    return Polygon(*pts[[2, 1, 8, 7]], color = cc, **kwargs, fill_color = cc, fill_opacity = 0.7)

def big_square(**kwargs):
	return Polygon(*pts[[9, 10, 11, 12]], color = WHITE, **kwargs, fill_color = WHITE, fill_opacity = 0)

class pythagoras(Scene):
	def construct(self):
		#Topic Block
		text = TextMobject("Pythagoras Theorem Animation With Python-Manim ")
		text.shift(2.5*UP)
		text.scale(.7)
		self.play(Write(text), run_time = 1)
		self.wait()
		
		text1 = TextMobject("By Ayush19 for GCI 2019")
		text1.shift(1.8*UP)
		text1.scale(.5)
		self.play(Write(text1), run_time = 1)
		self.wait()
		#Triangle Formation Block	
			
		tri = Triangle()
		self.play(ShowCreation(tri), run_time = 1)
		a = a_square()
		b = b_square()
		c = c_square()
		side_a = TextMobject("$a$", color = ac).shift(2.2*DOWN+0.5*LEFT)
		side_b = TextMobject("$b$", color = bc).shift(0.5*DOWN+0.2*RIGHT)
		side_c = TextMobject("$c$", color = cc).shift(0.5*DOWN+ 0.7*LEFT)
		self.play(FadeInFromDown(side_a),FadeInFrom(side_b, RIGHT),FadeInFrom(side_c, LEFT),)
		self.wait()
		area_a = TextMobject("$a^2$", color = ac).shift((pts[0]+pts[2]+pts[4]+pts[3])/4)
		area_b = TextMobject("$b^2$", color = bc).shift((pts[1]+pts[0]+pts[5]+pts[6])/4)
		area_c = TextMobject("$c^2$", color = cc).shift((pts[2]+pts[1]+pts[8]+pts[7])/4)
		self.play(ShowCreation(a),ShowCreation(b),ShowCreation(c),Transform(side_a, area_a),Transform(side_b, area_b),Transform(side_c, area_c),run_time = 3,)
		self.wait(1)
		
		#Removing TRiangle Block
		tri2 = Triangle()
		self.add(tri2)
		x = 3
		y = 4
		z = 1
		self.play(side_a.shift, d[0],side_b.shift, d[0],tri.shift, d[0],a.shift, d[0],b.shift, d[0],side_c.shift, d[1],tri2.shift, d[1],c.shift, d[1],FadeOut(text),run_time = 2,)
		tri3 = Triangle().move_to(tri2)
		tri4 = Triangle().move_to(tri2)
		tri5 = Triangle().move_to(tri2)
		tri6 = Triangle().move_to(tri)
		tri7 = Triangle().move_to(tri)
		tri8 = Triangle().move_to(tri)
		self.play(tri3.shift, 3*LEFT+UP,tri3.rotate, PI,tri4.shift, LEFT+2*UP,tri4.rotate, PI/2,tri5.shift, DOWN+2*LEFT,tri5.rotate, -PI/2,tri6.rotate, PI,tri7.shift, 2*RIGHT+2*DOWN,tri7.rotate, PI/2,tri8.shift, 2*DOWN+2*RIGHT,tri8.rotate, -PI/2,FadeOut(text1),run_time = 2)
		big = big_square()
		self.play(ShowCreation(big),run_time = 2,)
		big2 = big_square()
		self.play(big2.shift, 8*RIGHT,run_time = 2,)
		
		#Final Result
		
		self.play(FadeOut(tri),FadeOut(tri2),FadeOut(tri3),FadeOut(tri4),FadeOut(tri5),FadeOut(tri6),FadeOut(tri7),FadeOut(tri8),)
		equal = TextMobject("$=$").shift(0.3*RIGHT+2.2*DOWN)
		plus = TextMobject("$+$").shift(3.1*LEFT+2*DOWN)
		self.play(Write(equal),Write(plus),side_c.move_to, 2.4*RIGHT+2*DOWN,side_a.move_to, 4.8*LEFT+2*DOWN,side_b.move_to, 1.8*LEFT+2*DOWN,run_time = 2,)
		self.play(side_c.scale, 2,side_b.scale, 2,side_a.scale, 2,equal.scale, 2,plus.scale, 2,)
		self.wait()
	
