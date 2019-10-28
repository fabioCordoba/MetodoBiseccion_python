import re
def CalcularIntervalo(temp):
    reemp = (re.sub(r'x',temp,ecuacion))
    print('\t\t***** Calcular f(x) ****\nReemplazando ', temp , 'en la ecuacion ', ecuacion , ' = ' , reemp , '\n')
    #print('=>',reemp)
    print('f(x)=',eval(reemp))
    return eval(reemp)

ecuacion = input('Digite su ecuacion \n')
interA = input('Digite el intervalo A \n')
interB = input('Digite el intervalo B \n')

print('\nEntradas: Ecuacion = ' , ecuacion , ' Intervalo A = ' , interA , ' Intervalo B = ' , interB ,'\n')
fa = CalcularIntervalo(interA)
fb = CalcularIntervalo(interB)
print('\nPrueba de Salida: Ecuacion = ' , ecuacion , ' f(a) = ' , fa , '  f(b) = ' , fb )
if fa * fb < 0:
    print('\tse cumple Aplicar La Ecuacion a+(b-a)/2')
    a = int(interA)
    b = int(interB)
    xi = (a+(b-a)/2)
    print('xi=',xi,'\n')
else:
    print('\tNo Se Cumple')


    





