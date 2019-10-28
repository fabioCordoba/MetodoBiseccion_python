import re
import csv
import os
def CalcularIntervalo(temp):
    reemp = (re.sub(r'x',temp,ecuacion))
    #print('\t\t***** Calcular f(x) ****\nReemplazando ', temp , 'en la ecuacion ', ecuacion , ' = ' , reemp , '\n')
    #print('=>',reemp)
    #print('f(x)=',eval(reemp))
    return eval(reemp)
def modxi(A,B):
    ecuacion = 'a+(b-a)/2'
    re1 = (re.sub(r'a',A,ecuacion))
    re2 = (re.sub(r'b',B,re1))
    return eval(re2)
def error(A,B):
    ecuacion = '(b-a)/2'
    re1 = (re.sub(r'a',A,ecuacion))
    re2 = (re.sub(r'b',B,re1))
    #print(re2)
    return eval(re2)
ecuacion = input('Digite su ecuacion \n')
interA = input('Digite el intervalo A \n')
interB = input('Digite el intervalo B \n')
doc = open ("Datos.csv","w",newline="")
doc_csv_w = csv.writer(doc,delimiter=';')
print('\nEntradas: Ecuacion = ' , ecuacion , ' Intervalo A = ' , interA , ' Intervalo B = ' , interB ,'\n')
fa = CalcularIntervalo(interA)
fb = CalcularIntervalo(interB)
print('\nPrueba de Salida: Ecuacion = ' , ecuacion , ' f(a) = ' , fa , '  f(b) = ' , fb ,'\n')
    
if fa * fb < 0:
    i=1
    x=0
    while(i <= 14):
        if(i==1):
            #print('\tse cumple Aplicar La Ecuacion a+(b-a)/2 \n')
            a = float(interA)
            b = float(interB)
            xi = str(a+(b-a)/2)
            #print('xi=',xi,'\n')
            fxi = CalcularIntervalo(xi)
            #print('fxi=',fxi,'\n')
            xii = (b-a)/2;
            #print('xii=',xii,'\n')
            print('\ti\ta\tb\tf(a)\tf(b)\txi\tf(xi)\terror')
            print('\t',i,'\t',a,'\t',b,'\t',fa,'\t',fb,'\t',xi,'\t',fxi,'\t',xii)
            lista = [[i,a,b,fa,fb,xi,fxi,xii]]
            encabezado = [['i','a','b','f(a)','f(b)','xi','f(xi)','error']]
            if x==0:
                for x in encabezado:
                    doc_csv_w.writerow(x)
            for x in lista:
                doc_csv_w.writerow(x)
            i= i+1
        else:
            if fa * fxi < 0:
                a = str(a)
                if fb * fxi < 0:
                    b = str(b)
                else:
                    b = str(xi)
            else:
                a = str(xi)
                if fb * fxi < 0:
                    b = str(b)
                else:
                    b = xi
            fa = CalcularIntervalo(str(a))
            fb = CalcularIntervalo(str(b))
            xi = modxi(a,b)
            fxi = CalcularIntervalo(str(xi))
            xii = error(a,b);
            print('\t',i,'\t',a,'\t',b,'\t',fa,'\t',fb,'\t',xi,'\t',fxi,'\t',xii)
            lista = [[i,a,b,fa,fb,xi,fxi,xii]]
            for x in lista:
                doc_csv_w.writerow(x)
                if i == 14:
                    doc.close()
            i= i+1
    dire=os.popen('chdir').read()
    print("\nPara visualizar mejor los valores Se ha creado en un archivo 'Datos.csv' en =",dire)
    
else:
    print('\tLa Ecuacion o los intervalos No cumplen con los requisitos del Calculo')


    





