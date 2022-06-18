'''
    Universidad de las Fuerzas Armadas ESPE Sede Santo Domingo de los Colorados
    Ciencias de la Computación
    Ingeniería en Tecnologías de la Información
    Autor: José Ruiz
    Materia: Inteligencia artificial
'''
#Importamos la libreria Queue
from queue import Queue

class Grafo():
    '''
    Atributos:
        m_numero_de_nodos: int
        m_nodos: int
        m_dirigido: bool
        m_adyacencia_lista: dict 
    Métodos:
        mostrar_lista_adyacencia(self)
        def dfs(self, nodo_de_inicio, objetivo, camino = [], visitado = set())
    '''
    def __init__(self, numero_de_nodos, dirigido=True):

        '''
        Parametros:
            numero_de_nodos: int
            dirigido: bool
        Retorna:
            nada
        '''
        #Numero de nodos a nodo recibido por parámetro
        self.m_numero_de_nodos = numero_de_nodos 
        #Rango de nodos
        self.m_nodos = range(self.m_numero_de_nodos) 
        #Dirigido o No Dirigido
        self.m_dirigido = dirigido
        self.m_adyacencia_lista = {self: set() for self in self.m_nodos}     

    #Añade un nodo al grafo
    def añadir_nodo(self, nodo1, nodo2, peso=1):
         #Ingreso del nodo2 a la lista de adyacencia del nodo1
        self.m_adyacencia_lista[nodo1].add((nodo2, peso))
        #Estructura condicional en caso de que no sea dirigido
        if not self.m_dirigido: 
            #Ingreso del nodo1 a la lista de adyacencia del nodo2
            self.m_adyacencia_lista[nodo2].add((nodo1, peso)) 

    # Imprime la representación del grafo
    def mostrar_lista_adyacencia(self):
        #Generacion del ciclo for que permite recorrer el tamaño del nodo
        for clave in self.m_adyacencia_lista.keys(): 
            #Muestra en la terminal el grafo
            print("Nodo", clave, ": ", self.m_adyacencia_lista[clave]) 

    #Recorrido en amplitud
    def dfs(self, inicio, objetivo, ruta = [], visitado = set()):
        """
        Parametros:
            ruta: lista
            visitado: diccionario
        Retorna:
            nada
        """
        #Se añade a la ruta el nodo inicial
        ruta.append(inicio) 
        #Se añade a la la lista de nodos visitados el nodo inicial
        visitado.add(inicio) 
        if inicio == objetivo: 
            return ruta 
        for(vecino, peso) in self.m_adyacencia_lista[inicio]: 
            if vecino not in visitado:  
                #Si el vecino no se encuentra en el diccionario de nodos visitados
                resultado = self.dfs(vecino, objetivo, ruta, visitado) 
                #Si la lista resultado no esta vacio
                if resultado is not None: 
                    return resultado #Retorna resultado
                    
        
        ruta.pop() 
        # Elimina y retorna a la ruta
        return None 

if __name__ == "__main__":
    #Creación del grafo
    print("\n CASO DE PRUEBA 3")
    grafo1 = Grafo(3, dirigido=True)
    #Añade los nodos
    grafo1.añadir_nodo(0, 2, 1)
    grafo1.añadir_nodo(0, 1, 2)
    grafo1.añadir_nodo(1, 0, 3)
    grafo1.añadir_nodo(1, 2, 4)
    #Impresión de la lista adyacente
    grafo1.mostrar_lista_adyacencia()
    #Generar la ruta transversal
    ruta_transversal3 = []
    ruta_transversal3 = grafo1.dfs(0, 2)
    print(f" La ruta trasversal desde el nodo 0 hasta el nodo 2 es {ruta_transversal3}")