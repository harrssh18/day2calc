from django.shortcuts import render, redirect 
from .forms import LCMForm
import math
from datetime import datetime
# Create your views here.
def home(request):
    return redirect('/lcm-calculator/')

def lcm1(request):
    try:
        if request.method == "POST":
            fm = LCMForm(request.POST)
            if fm.is_valid():
                num1 = fm.cleaned_data['num1']
                num2 = fm.cleaned_data['num2']
                def Prime_factor(num):
                    l = []
                    if num%2==0:
                        l.append(2)
                        num=num//2
                    for i in range(3,int(math.sqrt(num))+1,2):
                        while num % i== 0:
                            l.append(i)
                            num = num / i
                    if num > 2:
                        l.append(num)
                    return l
                def list_mul(l):
                    result = 1
                    for i in l:
                        result = result * i
                    return result
                gcf = math.gcd(num1,num2)
                mul = num1*num2
                lcm = mul//gcf
                prime_fact1 = Prime_factor(num1)
                prime_fact2 = Prime_factor(num2)
                prime_fact1.sort()
                prime_fact1 = [str(i) for i in prime_fact1]
                prime_fact111 = ','.join(prime_fact1)
                prime_fact11 = ' * '.join(prime_fact1)
                prime_fact2.sort()
                prime1_mul = list_mul(prime_fact1)
                prime2_mul = list_mul(prime_fact2)
                prime_fact2 = [str(i) for i in prime_fact2]
                prime_fact222 = ','.join(prime_fact2)
                prime_fact22 = ' * '.join(prime_fact2)
                l = []
                re=True
                for i in prime_fact1:
                    if i not in prime_fact2:
                        l.append(i)
                for i in prime_fact2:
                    l.append(i)
                l = [str(i) for i in l]
                l = ' * '.join(l)
                context = {'prime_fact1':prime_fact111,'prime_fact2':prime_fact222,'gcf':gcf,'mul':mul,'lcm':lcm,'l':l,'prime_fact11':prime_fact11,'prime_fact22':prime_fact22,'num1':num1,'num2':num2,'forms':fm,'re':re,'prime1_mul':prime1_mul,'prime2_mul':prime2_mul}
                return render(request,'calc/lcm.html',context)
                
        else:
            re = False
            fm= LCMForm()
        return render(request,'calc/lcm.html',{'forms':fm})
    except:
        return redirect('/lcm-calculator/')