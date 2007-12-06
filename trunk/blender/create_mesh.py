from Blender import NMesh, Redraw
from math import sqrt
me = NMesh.GetRaw()
i = 0
j = 0
vertices = 9
n = sqrt(vertices)
for i in range(0, n, 1):
    for j in range(0, n, 1):
        v = NMesh.Vert(j, i, 0.0)
        me.verts.append(v)
NMesh.PutRaw(me, "plane", 1)
Redraw()
