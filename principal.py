import numpy
TEST = "test.csv"
TRAIN = "train.csv"


def calcularDist(elem1,elem2):
    resul = 0
    resta = elem1 - elem2
    for dim in resta:
        resul = resul + dim**2
    return resul**0.5
        


def obtenerDistancias(elem,archivo):
    print 'hola'
    listDistancias = []
    for i in range(10):
        reg = archivo[41990 + i]
        subReg = numpy.delete(reg,0,0)
        dist = calcularDist(elem,subReg)
        listDistancias.append((reg[0],dist))
    listDistancias = sorted(listDistancias,key=lambda tup: tup[1])
    return listDistancias

        

def consultarClase(elem,archivo):
    print 'hola'
    distancias = obtenerDistancias(elem,archivo)
    print distancias
#    vecinos = obtenerVecinos(distancias,k)
#    print clasificar(vecinos)
    
def main():
    print 'Hola KNN'
    train = numpy.genfromtxt(TRAIN,delimiter=',',dtype='int64',skip_header=1)
    test = numpy.genfromtxt(TEST,delimiter=',',dtype='int64',skip_header=1)
    consultarClase(test[0],train)
    
main()