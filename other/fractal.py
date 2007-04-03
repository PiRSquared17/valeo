#
# fractal by Ricardo Bittencourt and Nilton Volpato
#

from Tkinter import*
r=Tk();k=256;p=PhotoImage(w=k,h=k)
m=lambda z,i,n:(abs(z)>2 or n>1)and(z,i,n)or m(z*z+complex(i/k/1e2-2,(i%k-128)/1e2),i,n+0.03)
[p.put("#00%02x00"%(a[2]**0.7*k),divmod(a[1],k))for a in[m(0,i,0)for i in range(k*k)]if a[2]<1]
Label(r,i=p,bg="white").pack()
r.mainloop()

from Tkinter import*
Tk();k=256;p=PhotoImage(w=k,h=k)
m=lambda z,i,n:(abs(z)>2or n>1)and(z,i,n)or m(z*z+(i/k/1e2-2+(128-i%k)/1e2j),i,n+.03)
[p.put("#00%02x00"%(b**.7*k),(a/k,a%k))for(_,a,b)in[m(0,i,0)for i in range(k*k)]if b<1]
Label(i=p,bg="white").pack()
mainloop()

from Tkinter import*
Tk();k=256;p=PhotoImage(w=k,h=k)
m=lambda z,i,n:(abs(z)>2or n>1)and(z,i,n)or m(z*z+(i/k/1e2-2+(128-i%k)/1e2j),i,n+.03)
[p.put("#00%02x00"%(b**.7*k),(a/k,a%k))for(_,a,b)in[m(0,i,0)for i in range(k*k)]if b<1]
Label(i=p).pack();mainloop()
