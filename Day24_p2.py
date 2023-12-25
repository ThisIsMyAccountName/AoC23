import z3
storms = []
for line in open("inputs/day24.txt"):
	cords, vel = line.split(" @ ")
	cords = cords.split(", ")
	vel = vel.split(", ")
	storm = (tuple(map(int, cords)), tuple(map(int, vel)))
	storms.append(storm)
	
x,y,z,vx,vy,vz = z3.Reals("x y z vx vy vz")

math_thingy = z3.Solver()

for i in range(len(storms)):
	(x1, y1, z1), (vx1, vy1, vz1) = storms[i]
	t = z3.Real(f"t{i}")
	math_thingy.add(t >= 0)
	math_thingy.add(x + vx * t == x1 + vx1 * t)
	math_thingy.add(y + vy * t == y1 + vy1 * t)
	math_thingy.add(z + vz * t == z1 + vz1 * t)

math_thingy.check()
result_thingy = math_thingy.model()
print(sum(result_thingy.eval(x).as_long() for x in (x,y,z)))