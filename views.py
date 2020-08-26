from django.shortcuts import render
from django.http import HttpResponse
import math
import random
# Create your views here.
def index(request):
    return render(request,'index.html')
def rec(request):
    return render(request,'rec.html')

def receiver(request):
    #defining gcd function for further use.
    
    def gcd(a,b): 
        if b==0: 
            return a 
        else: 
            return gcd(b,a%b)

    s=[]
    x=0
    v=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!@#$%^&*()=-+_*/{?}"
    #taking two large prime numbers from ram:
    p=int(request.POST['p1'])
    q=int(request.POST['q'])
    n=p*q
    
    #taking phi function as f.As p and q are prime numbers f=(p-1)*(q-1): 
    f=(p-1)*(q-1)
    #finding suitable e as 1<e<f and e should be coprime with f:
    for e in range(2,f): 
        if gcd(e,f)== 1: 
            break
    return render(request, 'receiver.html',{'e':e,'n':n,'f':f})
    
    #print('The public key is: ',e)
    #taking the cipher text from ram which is provided by shyam;
    #c=input('Enter the cipher text: ')
def gen(request):
    k=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599]
    val1=random.randint(0,len(k))
    val2=random.randint(0,len(k))
    return render(request,'rec.html',{'val1':k[val1],'val2':k[val2]})
def ty(request):
    e=int(request.POST['pk'])
    f=int(request.POST['f'])
    n=int(request.POST['n'])
    return render(request, '2.html',{'n':n,'e':e,'f':f})
def receive(request):
    return render(request,'receive.html') 
def r(request):
    c=request.POST['d']
    e=int(request.POST['e'])
    f=int(request.POST['f'])
    n=int(request.POST['n'])
    l=(c.split())
    v=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!@#$%^&*()=-+_*/{?}"
    #finding the private key-d.
    for i in range(1,10): 
        x = 1 + i*f 
        if x % e == 0: 
            d = int(x/e)
            break
    #print('private key is: ',d)

    w=[]
    k=[]
    u=''
    for i in l:
        m=(int(i)**d)%n
        k.append(m)

    for i in k:
        for j in range(len(v)):
            if i==j:
                u=u+v[j]
    #print(u)'''
    return render(request,'wait.html',{'u':u})
        

   


def send(request):
    
    #taking input message in string form from the Shyam.
    msg=request.POST['msg']
    
    s=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!@#$%^&*()=-+_*/{?}"
    #x=[]
    d=[]
    enctxt=""
    #comparing the msg with string s and converting it's each character into number form and storing it in a list-d.

    for j in range(len(msg)):
            if msg[j] in s:
                q=s.index(msg[j])
                d.append(q)
    #taking values of public key and N from ram:
    e=int(request.POST['pk'])
    f=int(request.POST['f'])
    n=int(request.POST['n'])
    #printing decrypted text-cipher text-C
    
    for i in d:
        enctxt+=str((i**e)%n)
        enctxt+=' '
    
    return render(request, '3.html',{'d':enctxt,'n':n,'e':e,'f':f})
   
    

