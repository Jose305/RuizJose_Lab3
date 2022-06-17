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
    