# 2ta number moddhe Highest common factor (HCF) small number er theke kokhonoi boro hoy nah

def hcf(a,b):
    if a>b:
        smaller = b
    else:
        smaller = a

    for i in range(1,smaller+1):
        if a%i==0 and b%i==0:
            ans=i
            print(i,end='')
            if i<smaller:
                print(',',end='')

    print('')
    print('So the HCF= '+str(ans)+'.')

a=int(input('Input a-\n'))
b=int(input('Input b-\n'))
hcf(a,b)
