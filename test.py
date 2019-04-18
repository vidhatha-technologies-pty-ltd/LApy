import LA
mm = LA.Make_Matrix()
mo = LA.Matrix_Operations()
vo = LA.Vector_Operations()

a = mm.make_random_matrix(3, 1)
b = mm.make_random_matrix(3, 1)
c = mm.make_random_matrix(3, 1)
d = mm.make_random_matrix(2, 1)
mo.print_matrix(a, b, c, d)
r1 = vo.vector_dot_product(a, b)
r2 = vo.vector_cross_product(a, b)
r3 = vo.scalar_triple_product(a, b, c)
r4 = vo.get_angle_between(a, b)
r5 = vo.get_angle_between_horizontal(d)
print("Dot product of a.b: {}\nCross product of a x b: {}\nScalar triple product a, b, c: {}\nAngle between a b: {}\nAngle between horizontal and d: {}".format(r1, r2, r3, r4, r5))
