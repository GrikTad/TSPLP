import networkx as nx
import matplotlib.pyplot as plt

#

G=nx.Graph()
G.add_node('C',pos=(2,1))
G.add_node('E',pos=(2,-1))
G.add_node('B',pos=(-2,1))
G.add_node('F',pos=(-2,-1))
G.add_node('A',pos=(-4,0))
G.add_node('D',pos=(4,0))

G.add_edge('B','C')
G.add_edge('C','E',weight='P3')
G.add_edge('E','F')
G.add_edge('F','B',weight='P1')
G.add_edge('B','E',weight='P2')

G.add_edge('A','B')
G.add_edge('A','F')
G.add_edge('C','D')
G.add_edge('D','E')

add1=('C','E')
add2=('F','B')
add3=('B','E')
add4=('E','C')
add5=('B','F')
add6=('C','E')
fail_pl=[]
fail_pl.append(add1)
fail_pl.append(add2)
fail_pl.append(add3)
fail_pl.append(add4)
fail_pl.append(add5)
fail_pl.append(add6)
print('Failed physical links:',fail_pl)

pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, width=4)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels, label_pos=0.3)

x,y=pos['A']
plt.text(x-0.5,y+0.1,s='P0(start)', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
x,y=pos['B']
plt.text(x-0.5,y+0.1,s='(b1,b2)', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
x,y=pos['C']
plt.text(x-0.5,y+0.1,s='(c2,c3)', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
x,y=pos['D']
plt.text(x+0.5,y,s='(d3)', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
x,y=pos['E']
plt.text(x-1,y-0.1,s='(e1, e2, e3)', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
x,y=pos['F']
plt.text(x-0.5,y-0.1,s='(f1)', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')

print('Physical Network')

#virtual network-1
G = nx.Graph()
G.add_edge('f1','e1',color='black',weight=2)
G.add_edge('e1','b1',color='r',weight=4)
G.add_edge('b1','f1',color='r',weight=4)

colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()

pos = nx.circular_layout(G)
nx.draw(G, pos, 
        edge_color=colors, 
        width=list(weights),
        with_labels=True,
        node_color='yellow',node_size=700)
print('Black and red edge is virtual link & red edge denotes failure')

#virtual network-2
G = nx.Graph()
G.add_edge('e2','c2',color='r',weight=4)
G.add_edge('c2','b2',color='black',weight=2)
G.add_edge('b2','e2',color='r',weight=4)

colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()

pos = nx.circular_layout(G)
nx.draw(G, pos, 
        edge_color=colors, 
        width=list(weights),
        with_labels=True,
        node_color='yellow',node_size=700)
print('Black and red edge is virtual link & red edge denotes failure')

#virtual network-3
G = nx.Graph()
G.add_edge('c3','d3',color='black',weight=2)
G.add_edge('d3','e3',color='black',weight=2)
G.add_edge('e3','c3',color='r',weight=4)

colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()

pos = nx.circular_layout(G)
nx.draw(G, pos, 
        edge_color=colors, 
        width=list(weights),
        with_labels=True,
        node_color='yellow',node_size=700)
print('Black and red edge is virtual link & red edge denotes failure')

#virtual links

fail_vl=[]
virtual_links=[]
add1=('f1','b1')
add2=('b1','e1')
add3=('e1','f1')
add4=('b2','e2')
add5=('e2','c2')
add6=('c2','b2')
add7=('c3','e3')
add8=('e3','d3')
add9=('d3','c3')

fail_vl.append(add1)
fail_vl.append(add2)
fail_vl.append(add4)
fail_vl.append(add5)
fail_vl.append(add7)


virtual_links.append(add1)
virtual_links.append(add2)
virtual_links.append(add3)
virtual_links.append(add4)
virtual_links.append(add5)
virtual_links.append(add6)
virtual_links.append(add7)
virtual_links.append(add8)
virtual_links.append(add9)
loc=['P1','P2','P2','P3','P3']
print('All virtual links:',virtual_links)
print('All failed virtual links:',fail_vl)
print('Failure locations according to the above failed virtual links are:',loc)


G=nx.DiGraph()
G.add_node('P1',pos=(2,2))
G.add_node('P2',pos=(2,-2))
G.add_node('P0',pos=(-2,2))
G.add_node('P3',pos=(-2,-2))
G.add_edge('P0','P1',weight=3.7)
G.add_edge('P1','P2',weight=3.6)
G.add_edge('P2','P1',weight=3.4)
G.add_edge('P3','P1',weight=4.4)
G.add_edge('P1','P3',weight=4.2)
G.add_edge('P0','P2',weight=4.2)
G.add_edge('P2','P3',weight=4.0)
G.add_edge('P3','P2',weight=4.4)
G.add_edge('P0','P3',weight=4.8)

pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, width=4)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels, label_pos=0.3)

l1=[]
w=[]
n=[]
Na=[]
for u,v,a in G.edges(data=True):
  n.append(u)
  n.append(v)
  n.append(list(a.values())[0])
  Na.append(v)
  l1.append(n)
l1=l1[0]
print(l1)
print('Node P0 is the office of the Repairman')



M=10**5
K=3
phik=[]
ck=0
si_k=['P0']
phi00=1
S=3
alpha=3.7
beta=3.6
gamma=4.0
tt={'P1':1.5,'P2':1.2,'P3':2.0}
tr={'P1':2.2,'P2':2.4,'P3':2.0}
wDVN={'P1':2,'P2':1,'P3':0}


def piav(u,s):
  if(u==1 and s==1):
    pi=1
  elif(u==2 and (s==2 or s==4)):
    pi=1
  elif(u==3 and (s==5 or s==7)):
    pi=1
  else:
    pi=0
  return pi

def phiuk(u,k):
  if(u==0 and k==0):
    phiAuk=1
  elif(k>=0 and k<K+1):
    if(u>0 and u<4):
      phiAuk=1   
  elif(u>0 and u<4):
    if(k>=0 and k<K+1):
      phiAuk=1
  else:
      phiAuk=0
  return phiAuk

def huk(u,k):
  h=0
  if(u>=0 and u<4):
    if(k>=0 and k<=K):
      for l in range(0,k+1):
        h=phiuk(u,l)
  return h

def nijsk(u,s,k):
  if(u>=0 and u<4):
      if(k>0 and k<k+1):
        if(s>0 and s<S+1):
          n=(1-huk(u,k))*(piav(u,s))
  return n


def ckDVN(k,Pv):
  tTk=0
  tRk=0
  omega=0
  for i in tt:
    if(i==Pv):
      tTk=tt[i]
  for i in tr:
    if(i==Pv):
      tRk=tr[i]
  for i in wDVN:
    if(i==Pv):
      omega=wDVN[i]
  cDVN=omega*(tTk+tRk)
  return cDVN

def ckFVL(k,Pv):
  #NNa=['P1','P2','P3']
  wFVL=loc.count(Pv)
  tTk=0
  tRk=0
  for i in tt:
    if(i==Pv):
      tTk=tt[i]
  for i in tr:
    if(i==Pv):
      tRk=tr[i]
  #tTk=tt[k]
  #tRk=tr[k]
  cFVL=wFVL*(tTk+tRk)
  return cFVL

def ckFPL(k,Pv):
  tTk=0
  tRk=0
  for i in tt:
    if(i==Pv):
      tTk=tt[i]
  for i in tr:
    if(i==Pv):
      tRk=tr[i]
  #tTk=tt[k]
  #tRk=tr[k]
  cFPL=1*(tTk+tRk)
  return cFPL


fvl=[]
fpl=[]
for k in range(1,K+1):
  ck=M
  phik=''
  for Pv in Na:
    ckv=alpha*ckDVN(k,Pv)+beta*ckFVL(k,Pv)+gamma*ckFPL(k,Pv)
    if(ckFVL(k,Pv) not in fvl):
      fvl.append(ckFVL(k,Pv))
    if(ckFPL(k,Pv) not in fpl):
      fpl.append(ckFPL(k,Pv))
    if(ckv<ck):
      phik=Pv
      ck=ckv

  si_k.append(si_k[k-1]+" "+phik)
  Na.remove(phik)
  #print(Na) 

print(si_k)

l1=['1','2','3']
plt.xlabel('FAILED VIRTUAL LINKS')
plt.ylabel('TOTAL DAMAGE CAUSED BY FVL')
plt.plot(l1,fvl)
plt.show()

plt.xlabel('FAILED PHYSICAL LINKS')
plt.ylabel('TOTAL DAMAGE CAUSED BY FPL')
plt.plot(l1,fpl)
plt.show()


sik=['P0']
si=[]
#phik=[]
m=10**5
MC=[]
Na=['P1','P2','P3']
tt={'P1':1.5,'P2':1.2,'P3':2.0}
tr={'P1':2.2,'P2':2.4,'P3':2.0}
wDVN={'P1':2,'P2':1,'P3':0}



def ckDVN(k,Pv):
  tTk=0
  tRk=0
  omega=0
  for i in tt:
    if(i==k):
      tTk=tt[i]
  for i in tr:
    if(i==k):
      tRk=tr[i]
  for i in wDVN:
    if(i==k):
      omega=wDVN[i]
  cDVN=omega*(tTk+tRk)
  return cDVN

def ckFVL(k,Pv):
  tTk=0
  tRk=0
  wFVL=loc.count(k)
  for i in tt:
    if(i==k):
      tTk=tt[i]
  for i in tr:
    if(i==k):
      tRk=tr[i]
  cFVL=wFVL*(tTk+tRk)
  return cFVL

def ckFPL(k,Pv):
  tTk=0
  tRk=0
  for i in tt:
    if(i==k):
      tTk=tt[i]
  for i in tr:
    if(i==k):
      tRk=tr[i]
  cFPL=1*(tTk+tRk)
  return cFPL

dm=[]
mck={}

def MC(Pu,phi):
  cu0=alpha*ckDVN(Pu,0)+beta*ckFVL(Pu,0)+gamma*ckFPL(Pu,0)
  return cu0

seq=[]
for u in range(len(Na)):
  Pu=Na[u]
  cu0=alpha*ckDVN(Pu,0)+beta*ckFVL(Pu,0)+gamma*ckFPL(Pu,0)
  mck[Pu,'P0']=cu0
  seq.append('P0')
  
dm.append(mck)
si.append(seq)
m=10**5
mck={}
mc2={}
seq=[]
for u in range(len(Na)):
  Pu=Na[u]
  N_Na=Na
  N_Na.remove(Pu)
  Na=['P1','P2','P3']
  for v in range(len(N_Na)):
    Pv=N_Na[v]
    cuv=alpha*ckDVN(Pu,Pv)+beta*ckFVL(Pu,Pv)+gamma*ckFPL(Pu,Pv)
    mc2[Pu,Pv]=MC(Pv,0)+cuv
    seq.append(Pv)
    for i in dm:
      for j in i:
        if(j==(Pv,'P0')):
          #print(Na[Pu],N_Na[Pv])
          mck[Pu,Pv]=i[j]+cuv

  
dm.append(mc2)
si.append(seq)
mck={}
m=10**5
for k in range(3,K+1):
  for u in range(len(Na)):
    Pu=Na[u]
    N_Na=Na
    N_Na.remove(Pu)
    Na=['P1','P2','P3']
    for v in range(len(N_Na)):
      Pv=N_Na[v]
      cuv=alpha*ckDVN(Pu,Pv)+beta*ckFVL(Pu,Pv)+gamma*ckFPL(Pu,Pv)
      for k in range(1,K):
        for i in dm:
          for j in i:
            cdu=alpha*ckDVN(j[1],Pu)+beta*ckFVL(j[1],Pu)+gamma*ckFPL(j[1],Pu)
            mck[j]=i[j]+cdu
si_k=['P0']
d1=''
minimum=10**5
for i in mck:
  if(mck[i]<minimum):
    minimum=mck[i]
    d1=i[0]
sik.append(d1)
si_k.append(d1)
for i in mck:
  if(sik[1]!=i[0] and sik[1]!=i[1] and i[1]!='P0'):
    if(mck[i]<m):
      m=mck[i]
      d1=i
si_k.append(d1[0])
si_k.append(d1[1])
dm.append(mck)
pdm=[]
pdm.append(dm[1])
pdm.append(dm[2])
ix=1
for i in pdm:
  min=10**5
  for j in i:
    if(j[0]==sik[ix] and sik.count(j[1])==0 ):
      if(i[j]<min):
        min=i[j]
        idx=j[1]
  sik.append(idx)
  ix+=1
print(dm)
print(sik)

#Simulated Annealing Algorithm
import random
import math

sik=['P0']
Na=['P1','P2','P3']
C_initial=[55.5,53.6,44.8]
si_initial=['P1','P2','P3']
lamda=0.9

def ckDVN(k):
  tTk=0
  tRk=0
  omega=0
  for i in tt:
    if(i==k):
      tTk=tt[i]
  for i in tr:
    if(i==k):
      tRk=tr[i]
  for i in wDVN:
    if(i==k):
      omega=wDVN[i]
  cDVN=omega*(tTk+tRk)
  return cDVN

def ckFVL(k):
  tTk=0
  tRk=0
  wFVL=loc.count(k)
  for i in tt:
    if(i==k):
      tTk=tt[i]
  for i in tr:
    if(i==k):
      tRk=tr[i]
  cFVL=wFVL*(tTk+tRk)
  return cFVL

def ckFPL(k):
  tTk=0
  tRk=0
  for i in tt:
    if(i==k):
      tTk=tt[i]
  for i in tr:
    if(i==k):
      tRk=tr[i]
  cFPL=1*(tTk+tRk)
  return cFPL

w_ex_stop=2
C_new=0
w_in_stop=2
theta_stop=0
C_temp=0
theta_temp=0
S_si=[]
w_ex=0
w_in=0

si_temp=['P1','P2','P3']
si_new=[]
while(theta_temp>theta_stop or w_ex<w_ex_stop):
  w_in=0
  F_ex=True
  while(w_in<w_in_stop):
    phi_m=random.choice(si_temp)
    phi_n=random.choice(si_temp)
    si_new.append(phi_m)
    si_new.append(phi_n)
    for i in si_new:
      C_new+=alpha*ckDVN(i)+beta*ckFVL(i)+gamma*ckFPL(i)
    for i in si_temp:
      C_temp+=alpha*ckDVN(i)+beta*ckFVL(i)+gamma*ckFPL(i)
    delta_C=C_new-C_temp
    AP=0
    if(delta_C>0):
      AP=math.exp(-delta_temp/theta_temp)
    else:
      AP=1
    if(delta_C<=0 or AP>random.random()):
      S_si.append(si_new)
      si_temp=si_new
      C_temp=C_new
      w_in=0
      w_ex=0
      F_ex=False
    else:
      w_in+=1
  if(F_ex==True):
    w_ex+=1
  theta_temp=lamda*theta_temp

for i in S_si:
  sik.append(i)

print(sik)

dis1=['DE','EF','EG','GH','GJ']
dis2=['AC','BC','CD','CF','EF','FJ']
dis3=['FJ','GJ','IJ','JN','MN']
Na=['DE','EF','EG','GH','GJ','AC','BC','CD','CF','EF','FJ','GJ','IJ','JN','MN']

import networkx as nx
import matplotlib.pyplot as plt

#Auxiliary graph 
dis1=['DE','EF','EG','GH','GJ']
G=nx.DiGraph()
G.add_node('A',pos=(-6,4))
G.add_node('B',pos=(-7,-1))
G.add_node('C',pos=(-5,-4))
G.add_node('D',pos=(-4,1))
G.add_node('E',pos=(-2,0))
G.add_node('F',pos=(-1,-5))
G.add_node('G',pos=(0,0))
G.add_node('H',pos=(2,1))
G.add_node('I',pos=(4,-1))
G.add_node('J',pos=(3,-4))
G.add_node('K',pos=(4,4))
G.add_node('L',pos=(5,2))
G.add_node('M',pos=(6,0))
G.add_node('N',pos=(5,-3))
G.add_edge('A','B',weight=2.0)
G.add_edge('A','C',weight=2.5)
G.add_edge('A','H',weight=3.0)
G.add_edge('B','C',weight=5.5)
G.add_edge('C','D',weight=4.0)
G.add_edge('C','F',weight=4.5)
G.add_edge('D','E',weight=7.0)
G.add_edge('E','F',weight=5.5)
G.add_edge('E','G',weight=3.0)
G.add_edge('F','J',weight=6.5)
G.add_edge('G','H',weight=2.0)
G.add_edge('G','J',weight=7.5)
G.add_edge('H','I',weight=8.0)
G.add_edge('H','K',weight=2.5)
G.add_edge('I','J',weight=3.2)
G.add_edge('I','M',weight=4.0)
G.add_edge('J','N',weight=4.4)
G.add_edge('K','L',weight=4.8)
G.add_edge('L','M',weight=5.4)
G.add_edge('M','N',weight=6.8)

pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")
nx.draw_networkx_nodes(G, pos, node_size=200)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, width=4)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels, label_pos=0.3)

l1=[]
w=[]
n=[]
Na=[]
print('disaster-1:',dis1)

import random

prob=[1,2,3,4,5,6,7,8,9,10]
#print(random.choice(prob)>3)
#print(random.randint(1,3))
disaster1=['D','E','F','G','H','J']
nodes=[]
vir={}
for i in range(len(disaster1)):
  val=random.randint(1,3)
  vir[disaster1[i]]=val
  nodes.append(val)
print(vir)


K=5


Na=['P1','P2','P3','P4','P5']
tt={'P1':7.5,'P2':3.0,'P3':2.0,'P4':6.0,'P5':4.0}
tr={'P1':2.2,'P2':2.4,'P3':2.0,'P4':2.0,'P5':2.5}

tk=[]
Cfpl=0
l1=[]
for i in range(1,K+1):
  v=0
  for j in tt:
    for k in tr:
      v+=tt[j]+tr[k]
  tk.append(v)
      
for i in range(1,K+1):
  #print(Cfpl)
  for Pu in range(len(Na)):
    Cfpl+=1*tk[i-1]
  l1.append(round(Cfpl,2))
print(l1)

import matplotlib.pyplot as plt
k1=[1,2,3,4,5]
plt.xlabel('FAILED PHYSICAL LINKS')
plt.ylabel('TOTAL DAMAGE CAUSED BY FPL')
plt.plot(k1,l1)
plt.show()

import matplotlib.pyplot as plt
k1=[1,2,3,4,5]
plt.xlabel('FAILED PHYSICAL LINKS')
plt.ylabel('TOTAL DAMAGE CAUSED BY FPL')
plt.plot(k1,l1)
plt.show()

K=3
Na=['P1','P2','P3']
tt={'P1':1.5,'P2':1.2,'P3':2.0}
tr={'P1':2.2,'P2':2.4,'P3':2.0}


tk=[]
Cfpl=0
l1=[]
for i in range(1,K+1):
  v=0
  for j in tt:
    for k in tr:
      v+=tt[j]+tr[k]
  tk.append(v)
    
for i in range(1,K+1):
  
  for Pu in range(len(Na)):
    Cfpl+=1*tk[i-1]
  l1.append(round(Cfpl,2))
print(l1)

k1=[1,2,3]
plt.xlabel('FAILED PHYSICAL LINKS')
plt.ylabel('TOTAL DAMAGE CAUSED BY FPL')
plt.plot(k1,l1)
plt.show()

