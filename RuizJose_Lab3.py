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
        __init__(self, numero_de_nodos, dirigido=True):
        añadir_nodo(self, nodo1, nodo2, peso=1):
        mostrar_lista_adyacencia(self):
        def dfs(self, nodo_de_inicio, objetivo, camino = [], visitado = set()):
    '''
    def __init__(self, numero_de_nodos, dirigido=True):

        '''
        Parametros:
            numero_de_nodos: int
            dirigido: bool
        Retorna:
            nada
        '''
        #Designando el numero de nodos a cada nodo recibido por parámetro
        self.m_numero_de_nodos = numero_de_nodos 
        #Mide el rango de nodos
        self.m_nodos = range(self.m_numero_de_nodos) 
        #Dirigido o No Dirigido
        self.m_dirigido = dirigido
        #asigna la creación de un diccionario de datos
        #determina el espacio en donde se almacenarán los nodos
        self.m_adyacencia_lista = {self: set() for self in self.m_nodos} 