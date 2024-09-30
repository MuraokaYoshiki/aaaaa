import numpy as np
import math
def h(x):
    y = np.array([(math.tanh((a-0.5)*0.5)+1.0)/2.0 for a in x])
    return y
def s(a):
    c=np.max(a)
    exp_a=np.exp(a-c)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return y

A1=np.array([
    [0,0,],
    [0,0,],
])
b1=np.array([[0,0,]])
A2=np.array([
    [0,0,],
    [0,0,],
    [0,0,],
])
b2=np.array([[0,0,0,]])
A=[A1,b1,A2,b2,]

x=[
    np.array([0,0]),
    np.array([0,1]),
    np.array([1,0]),
    np.array([1,1]),
]
ans=[
    np.array([1,0,0,]),
    np.array([0,1,0,]),
    np.array([0,1,0,]),
    np.array([0,0,1,]),
]
lenA=int(len(A)/2)
yki=[]#04
dEdakj=[]#04
dEdaj=np.zeros(np.shape(ans[0]))#04
ukm=[]#05
dukmdvkm=[]#06
dEdrjmk=[]#05
dEdukm=[]#06
dEdvkm=[]#06
dEdrjm=np.zeros(np.shape(A2))#05
dEdcm=np.zeros(np.shape(b1))#06
dEdqmn=np.zeros(np.shape(A1))#07
for nans in range(len(x)):#04
    yki.append([])#04
    dEdakj.append([])#04
    ukm.append([])#05
    dukmdvkm.append([])#06
    dEdukm.append([])#06
    dEdvkm.append([])#06
    dEdrjmk.append([])#05

def add(A,dA):
    a=[]
    global dEdaj,dEdrjm,dEdcm,dEdqmn#07
    dEdaj=0#04
    dEdrjm=0#05
    dEdcm=0#06
    dEdqmn=0#07
    for nans in range(len(x)):
        y=np.array([x[nans][0],x[nans][1]])
        for n in range(lenA-1):
            y=h((A[n*2]+dA[n*2])@y+A[n*2+1][0]+dA[n*2+1][0])
            if n==0:#05
                ukm[nans]=y#05
                dukmdvkm[nans]=y*(1.0-y)#06
        n=lenA-1
        y=s((A[n*2]+dA[n*2])@y+A[n*2+1][0]+dA[n*2+1][0])
        a.append(y)
        yki[nans]=y#04
        dEdakj[nans]=yki[nans]-ans[nans]#04
        dEdaj=dEdaj+dEdakj[nans]#04
        dEdrjmk[nans]=np.outer(dEdakj[nans],ukm[nans])#05
        dEdrjm=dEdrjm+dEdrjmk[nans]#05
        dEdukm[nans]=dEdakj[nans]@A[2]#06
        dEdvkm[nans]=dEdukm[nans]*dukmdvkm[nans]#06
        dEdcm=dEdcm+dEdvkm[nans]#06
        dEdqmn=dEdqmn+np.outer(dEdvkm[nans],x[nans])#07
    return a

def err(a):
    e=0.0
    for n in range(len(a)):
        for k in range(len(a[0])):
            if ans[n][k]==1:
                e=e-math.log(a[n][k])
    return e

gA=[]
for n in range(lenA*2):
    gA.append(np.zeros(np.shape(A[n])))

delta=0.000001
alpha=0.2
epsilon=0.1

for iter in range(2):
    dA=[]
    for n in range(lenA*2):
        dA.append(np.zeros(np.shape(A[n])))
    e=err(add(A,dA))
    print(e)
    if e < epsilon:
        break
    for n in range(lenA*2):
        for i in range(len(A[n])):
            for k in range(len(A[n][0])):
                for m in range(lenA*2):
                    for j in range(len(A[m])):
                        for l in range(len(A[m][0])):
                            if n==m and i==j and k==l:
                                dA[m][j][l]=delta
                            else:
                                dA[m][j][l]=0.0
                gA[n][i][k]=(err(add(A,dA))-e)/delta
    for n in range(lenA*2):
        A[n]=A[n]-gA[n]*alpha
    #print(gA[3][0])#04
    #print(dEdaj)#04
    #print(gA[2])#05
    #print(dEdrjm)#05
    #print(gA[2]-dEdrjm)#05
    #print(gA[1][0])#06
    #print(dEdcm)#06
    #print(dEdcm-gA[1][0])#06
    print(gA[0])#07
    print(dEdqmn)#07
    print(dEdqmn-gA[0])#07

dA=[]
for n in range(lenA*2):
    dA.append(np.zeros(np.shape(A[n])))
for x1 in range(2):
    for x2 in range(2):
        x=[np.array([x1,x2])]
        y=add(A,dA)[0]
        print(x1,x2,np.argmax(y))