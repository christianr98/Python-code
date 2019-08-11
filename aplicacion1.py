#|||||||||||||||||Implementación de
#|||||||||||||||||||Árbol Binario
#||||||||||||||||||||en Python3
class ArbolBin:
    def __init__(self,valor=None, izq=None, der=None):
        if valor is None:
            self.valor=None
        else:
            self.valor=valor
            self.izq=izq
            self.der=der

    def hijo_izq(self):
        return self.izq

    def hijo_der(self):
        return self.der

    def raiz(self):
        return self.valor

    def es_arbol_vacio(self):
        return self.valor is None

#Extensiones
    def altura(self):
        if self.es_arbol_vacio():
            return 0
        alt_izq=0 if self.izq is None else self.izq.altura()
        alt_der=0 if self.der is None else self.der.altura()

        return 1 + max(alt_izq,alt_der)

    def num_nodos(self):
        if self.es_arbol_vacio():
            return 0
        num_nodos_izq=0 if self.izq is None else self.izq.num_nodos()
        num_nodos_der=0 if self.der is None else self.der.num_nodos()

        return 1 + num_nodos_izq + num_nodos_der

    def num_hojas(self):
        if self.es_arbol_vacio():
            return 0
        if self.izq is None and self.der is None:
            return 1
        hoja_izq=0 if self.izq is None else self.izq.num_hojas()
        hoja_der=0 if self.der is None else self.der.num_hojas()

        return hoja_izq + hoja_der

def preguntar(arbol):    
    print(arbol.raiz())
    if arbol.izq is not None:
        var = input()
        if var == "si":
            preguntar(arbol.izq)
        else:
            if var =="no":
                preguntar(arbol.der)

def main():
    #Datos
    a14=ArbolBin('¡Es Koopa Troopa!')
    a13=ArbolBin('¡Es Browser!')
    a12=ArbolBin('¡Es Yoshi!')
    a11=ArbolBin('¡Es Luigi!')
    a10=ArbolBin('¡Es Toad!')
    a9=ArbolBin('¡Es Mario!')
    a8=ArbolBin('¡Es Donkey Kong!')
    a7=ArbolBin('¿Es grande?',a13,a14)
    a6=ArbolBin('¿Es humano?',a11,a12)
    a5=ArbolBin('¿Su nombre lleva una "M"?',a9,a10)
    a4=ArbolBin('¿Tiene caparazon?',a7,a8)
    a3=ArbolBin('¿Viste de rojo?',a5,a6)
    a2=ArbolBin('¡Es Peach!')
    a1=ArbolBin('¿Es bueno?',a3,a4)
    a0=ArbolBin('¿Es hombre?',a1,a2)
    #                 ao
    #               /    \
    #             a1       2(Peach)
    #           /     \      
    #         a3        a4 
    #        / \        /   \
    #      a5   a6     a7    8
    #     / \   / \   / \   
    #     9 10 11 12 13 14
    #
    #Que comience el juego
    print("¡Hola! ¿Quiéres jugar Adivina Quién? Versión Mario?")
    ##print(a0.raiz())
    resp=input("Responde si o no: ")
    if resp == 'si':
        preguntar(a0)


if __name__ == '__main__':
    main()
