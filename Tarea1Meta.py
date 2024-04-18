class Variable:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain  # Lista de valores posibles para la variable
        self.next = None  # Referencia al siguiente nodo en la lista

class MFC:
    def __init__(self):
        self.variables = None  # Cabeza de la lista de variables

    def add_variable(self, name, domain):
        new_variable = Variable(name, domain)
        new_variable.next = self.variables
        self.variables = new_variable

    def search_solution(self):
        return self._search_solution({})

    def _search_solution(self, asigns):  # Forward Checking
        if len(asigns) == self._num_variables():
            return asigns  # Se encontró una solución

        variable_actual = self._select_variable_without_assign(asigns)
        for value in variable_actual.domain:
            if self._is_value_consistent(value, variable_actual, asigns):
                asigns[variable_actual.name] = value
                result = self._search_solution(asigns)
                if result is not None:
                    return result
                del asigns[variable_actual.name]
        return None  # No se encontró solución

    def _num_variables(self):
        count = 0
        current = self.variables
        while current:
            count += 1
            current = current.next
        return count

    def _select_variable_without_assign(self, asigns):
        current = self.variables
        while current:
            if current.name not in asigns:
                return current
            current = current.next
        return None

    def _is_value_consistent(self, value, variable, asigns):
        # Verificar restricciones basadas en una lista de restricciones
        for restriccion in self.restricciones:
            if restriccion[0] == variable.name:  # La restricción involucra a la variable actual
                otra_variable = restriccion[1]
                if otra_variable in asigns and asigns[otra_variable] == value:
                    return False  # Violación de restricción
            elif restriccion[1] == variable.name:  # La restricción involucra a la otra variable
                otra_variable = restriccion[0]
                if otra_variable in asigns and asigns[otra_variable] == value:
                    return False  # Violación de restricción
        return True  # El valor es consistente


# Ejemplo de uso
mfc = MFC()
mfc.add_variable('A', [1, 2, 3])
mfc.add_variable('B', [1, 2])
mfc.add_variable('C', [2, 3])
solucion = mfc.search_solution()
print(solucion)
