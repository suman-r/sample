def flames(f,g,b,re,cr,your):
    your=str(your).upper()
    crush=str(g).upper()
    for i in re:
        if i in cr:
            b.remove(i)
            cr.remove(i)
    ans=len(b)+len(cr)
    i=-1
    while len(f)!=1:
        a=-1
        while a!=ans-1:
            i+=1
            a+=1
            x=f[i]
            if i==len(f)-1:
                i=-1
        f.remove(x)
        i=-1
    relation=f[0]
    print(your+' + '+crush+' = '+relation);print("\n\n\n\n\n\n")
    ff = Figlet(font='slant')
    print(ff.renderText(relation));print("\n\n\n\n\n\n")
flag=0
from pyfiglet import Figlet
ss = Figlet(font='slant')
print (ss.renderText('FLAMES'))
while(flag==0):
    print('ENTER 0 TO EXIT');print()
    print('ENTER 7 TO PLAY');print()
    key=input("PLEASE ENTER A VALID KEY: ");print()
    if key=='0':break
    elif key=='7':
        your=input('ENTER YOUR NAME: ').strip().upper();print()
        b=list(your)
        re=list(your)
        g=input('ENTER YOUR CRUSH: ').strip().upper();print();cr=list(g)
        f=['FRIENDS','LOVER','AFFECTION','MARRIAGE','ENEMY','SISTER']
        flames(f,g,b,re,cr,your)
    else:
        print('error:invalid key');print()
        print('if you want to play again'.upper());print()
        print('enter 0');print()
        print('again enter enter a valid key'.upper());print()
        flag=input()
        if flag!='0':break
print(ss.renderText('BYE BYE'));print()
ff= Figlet()
print (ff.renderText('We\'ll play later.....come with new crush'))
