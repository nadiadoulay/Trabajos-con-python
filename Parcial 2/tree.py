
from typing import Any, Optional

from queue_ import Queue
class Node():

    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0
    
    def __str__(self):
        return self.value


class BinaryTree():

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height
    
    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def insert_node(self, value: Any, other_value=None) -> None:

        def __insert_node(root, value, other_value=None):
            if root is None:
                # print(f'lugar vacio insertar {value}')
                root = Node(value, other_value)
            elif value < root.value:
                # print(f'ir a la izquierda de {root.value}')
                root.left = __insert_node(root.left, value, other_value)
            else:
                # print(f'ir a la derecha de {root.value}')
                root.right = __insert_node(root.right, value, other_value)
            
            root = self.auto_balance(root)
            self.update_height(root)
            return root
            
        self.root = __insert_node(self.root, value, other_value)

    def delete_node(self, value: Any) -> Optional[Any]:
        def __replace(root):
            # print(root.value)
            aux = None
            if root.right is None:
                # print('mayor encontrado')
                return root.left, root
            else:
                # print('segui buscando a la derecha')
                root.right, aux = __replace(root.right)
            return root, aux

        def __delete_node(root, value):
            x = None
            other_value = None
            if root is not None:
                if value < root.value:
                    # print('ir a la izq')
                    # input()
                    root.left, x, other_value = __delete_node(root.left,value)
                elif value > root.value:
                    # print('ir a la derecha')
                    # input()
                    root.right, x, other_value = __delete_node(root.right, value)
                else:
                    # print('valor encontrado')
                    # input()
                    x = root.value
                    other_value = root.other_values
                    aux = None
                    if root.left is None:
                        # print('no tiene hijo izquierdo')
                        # input()
                        return root.right, x, other_value
                    elif root.right is None:
                        # print('no tiene hijo derecho')
                        # input()
                        return root.left, x, other_value
                    else:
                        # print('buscar remplazo')
                        # input()
                        root.left, aux = __replace(root.left)
                        root.value = aux.value
                        root.other_values = aux.other_values
            return root, x, other_value

        other_value = None
        self.root, x, other_value = __delete_node(self.root, value)

        return x, other_value

    def search(self, value) -> Optional[Any]:
        def __search(root, value):
            aux = None
            if root is not None:
            
                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                elif value > root.value:
                    aux = __search(root.right, value)

            return aux


        node = __search(self.root, value)
        
        return node 
    
    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def simple_rotation(self, root, control):
        if control: # rotaicon hacia la derecha
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # rotacion hacia la izquierda
            aux = root.right
            root.right = aux.left
            aux.left = root
        
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root
    
    def double_rotation(self, root, control):
        if control: # rotacion doble a la derecha
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else: # rotacion doble izquierda
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def inorden(self) -> None:
        
        def __inorden(root):
            if root.left is not None:
                # print(f'anda a la izquierda de {root.value}')
                __inorden(root.left)
            # print(f'procesa nodo actual')
            print(root.value, root.height)
            if root.right is not None:
                # print(f'anda a a derecha de {root.value}')
                __inorden(root.right)

        __inorden(self.root)
    
    def postorden(self) -> None:
        
        def __postorden(root):
            if root.right is not None:
                __postorden(root.right)
            print(root.value)
            if root.left is not None:
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self) -> None:
        def __preorden(root):
            print(root.value)
            if root.left is not None:
                __preorden(root.left)
            if root.right is not None:
                __preorden(root.right)

        __preorden(self.root)

    def by_level(self) -> None:

        pendings = Queue()

        if self.root is not None:
            pendings.arrive(self.root)
            # print(f'queue')
            # pendings.show()
            # input()
            while pendings.size() > 0:
                node = pendings.attention()
                print(node.value)
                # input()
                if node.left is not None:
                    pendings.arrive(node.left)
                if node.right is not None:
                    pendings.arrive(node.right)
                # print(f'queue ')
                # pendings.show()
                # input()

    def inorden_villain(self) -> None:
        
        def __inorden_villain(root):
            if root.left is not None:
                __inorden_villain(root.left)
            if root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_villain(root.right)
        __inorden_villain(self.root)

    def postorden_hero(self):
    
        def __postorden_hero(root):
            if root.right is not None:
                __postorden_hero(root.right)
            if not root.other_values['is_villain']:
                print(root.value)
            if root.left is not None:
                __postorden_hero(root.left)

        __postorden_hero(self.root)

    def inorden_hero_star_with(self, prefix: str) -> None:
        
        def __inorden_hero_star_with(root, prefix):
            if root.left is not None:
                __inorden_hero_star_with(root.left, prefix)
            if root.value.startswith(prefix) and not root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_hero_star_with(root.right, prefix)

        __inorden_hero_star_with(self.root, prefix)

    def proxy_search(self, prefix: str) -> None:

        def __proxy_search(root, prefix):
            if root.left is not None:
                __proxy_search(root.left, prefix)

            if prefix.lower() in root.value.lower():
                print(root.value)
                nuevo_nombre = input("Ingrese el nombre correcto: ")
                root.value = nuevo_nombre

            if root.right is not None:
                __proxy_search(root.right, prefix)

        __proxy_search(self.root, prefix)

    def count_heroes(self) -> None:
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.left is not None:
                    count += __count_heroes(root.left)
                if not root.other_values['is_villain']:
                    count += 1
                if root.right is not None:
                    count += __count_heroes(root.right)
            return count

        count = __count_heroes(self.root)
        return count


    def count_nodes(self) -> int:

        def __count_nodes(root):
         count = 0

         if root is not None:
            count += 1
            count += __count_nodes(root.left)
            count += __count_nodes(root.right)

         return count

        return __count_nodes(self.root)

    def split_tree(self, heroes_tree, villains_tree) -> None:

        def __split_tree(root):
            if root is not None:
                if root.other_values['is_villain']:
                    villains_tree.insert_node(root.value, root.other_values)
                else:
                    heroes_tree.insert_node(root.value, root.other_values)
                __split_tree(root.left)
                __split_tree(root.right)

        __split_tree(self.root)


    def cargar_descripcion(self):

        nombre = input("Ingrese el nombre de la criatura: ")
        criatura = self.search(nombre)

        if criatura is not None:
            descripcion = input("Ingrese una breve descripcion: ")
            criatura.other_values["descripcion"] = descripcion
            print("Descripcion cargada correctamente.")
        else:
            print("No se encontro la criatura.")


    def show_creature(self, nombre):

        criatura = self.search(nombre)

        if criatura is not None:
            print("Nombre:", criatura.value)
            print("Derrotado por:", criatura.other_values["derrotado_por"])
            print("Descripcion:", criatura.other_values["descripcion"])
            print("Capturada por:", criatura.other_values["capturada"])
        else:
            print("No se encontro la criatura.")


    def top_defeaters(self):

        derrotas = {}

        def __top_defeaters(root):
            if root is not None:
                __top_defeaters(root.left)

                for heroe in root.other_values["derrotado_por"]:
                    if heroe not in derrotas:
                        derrotas[heroe] = 1
                    else:
                        derrotas[heroe] += 1

                __top_defeaters(root.right)

        __top_defeaters(self.root)

        ordenados = sorted(derrotas.items(), key=lambda x: x[1], reverse=True)

        print("Los 3 heroes o dioses que derrotaron mas criaturas son:")

        for heroe, cantidad in ordenados[:3]:
            print(heroe, "-", cantidad, "criaturas")


    def creatures_defeated_by(self, heroe):

        def __creatures_defeated_by(root):
            if root is not None:
                __creatures_defeated_by(root.left)

                if heroe in root.other_values["derrotado_por"]:
                    print(root.value)

                __creatures_defeated_by(root.right)

        __creatures_defeated_by(self.root)

    def creatures_not_defeated(self):

        def __creatures_not_defeated(root):
            if root is not None:
                __creatures_not_defeated(root.left)

                if len(root.other_values["derrotado_por"]) == 0:
                    print(root.value)

                __creatures_not_defeated(root.right)

        __creatures_not_defeated(self.root)

    def capture_creature(self, nombre, heroe):

        criatura = self.search(nombre)

        if criatura is not None:
            criatura.other_values["capturada"] = heroe
            print(nombre, "fue capturada por", heroe)
        else:
            print("No se encontro la criatura")

    
    def creatures_captured_by(self, heroe):

        def __creatures_captured_by(root):
            if root is not None:
                __creatures_captured_by(root.left)

                if root.other_values["capturada"] == heroe:
                    print(root.value)

                __creatures_captured_by(root.right)

        __creatures_captured_by(self.root)

    def search_coincidence(self, prefix: str) -> None:
        def __search_coincidence(root, prefix):
            if root is not None:
                __search_coincidence(root.left, prefix)

                if prefix.lower() in root.value.lower():
                    print(root.other_values)

                __search_coincidence(root.right, prefix)

        __search_coincidence(self.root, prefix)

    def inorden_creatures(self):

        def __inorden_creatures(root):
            if root is not None:
                __inorden_creatures(root.left)

                derrotadores = ", ".join(root.other_values["derrotado_por"]) or "-"
                print(root.value, "- derrotada por:", derrotadores)

                __inorden_creatures(root.right)

        __inorden_creatures(self.root)

    def names_by_type(self, tipo):

        def __names_by_type(root):
            if root is not None:
                __names_by_type(root.left)

                if root.value == tipo:
                    print(root.other_values["nombre"])

                __names_by_type(root.right)

        __names_by_type(self.root)

    def search_weakness(self, tipo: str) -> None:
        def __search_weakness(root, tipo):
            if root is not None:
                __search_weakness(root.left, tipo)

                if tipo in root.other_values["debilidad"]and root.other_values["nombre"] != "Tyrantrum":
                    print(root.other_values["nombre"])

                __search_weakness(root.right, tipo)

        __search_weakness(self.root, tipo)

    def count_by_type(self):

        cantidades = {}

        def __count_by_type(root):
            if root is not None:
                __count_by_type(root.left)

                if root.value not in cantidades:
                    cantidades[root.value] = 1
                else:
                    cantidades[root.value] += 1

                __count_by_type(root.right)

        __count_by_type(self.root)

        for tipo, cantidad in cantidades.items():
            print(tipo, "-", cantidad, "pokemons")

    def count_flag(self, clave):

        def __count_flag(root):
            count = 0
            if root is not None:
                count += __count_flag(root.left)
                if root.other_values[clave]:
                    count += 1
                count += __count_flag(root.right)
            return count

        return __count_flag(self.root)