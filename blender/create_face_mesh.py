import Blender
from Blender import NMesh
from math import sqrt
me=NMesh.GetRaw()
i = 0
j = 0
vertices = 9
n = sqrt(vertices)
n0=int(n)
for i in range(0, n-1):
    for j in range(0, n-1):
        f=NMesh.Face()
        f.v.append(me.verts[i*n0+j ])
        f.v.append(me.verts[i*n0+j+1 ])
        f.v.append(me.verts[(i+1)*n0+j+1 ])
        f.v.append(me.verts[(i+1)*n0+j ])
        me.faces.append(f)
NMesh.PutRaw(me, "plane", 1)
Blender.Redraw()
