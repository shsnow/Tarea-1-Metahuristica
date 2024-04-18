class Variable:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
        self.next = None

class MFC:
    def __init__(self):
        self.variables = None
        self.restricciones = []  # Lista de restricciones específicas del problema

    def add_variable(self, name, domain):
        new_variable = Variable(name, domain)
        new_variable.next = self.variables
        self.variables = new_variable

    def add_restriccion(self, var1, var2):
        self.restricciones.append((var1, var2))

    def search_solution(self):
        return self._search_solution({})

    def _search_solution(self, asigns):
        if len(asigns) == self._num_variables():
            return asigns

        variable_actual = self._select_variable_without_assign(asigns)
        for value in variable_actual.domain:
            if self._is_value_consistent(value, variable_actual, asigns):
                asigns[variable_actual.name] = value
                result = self._search_solution(asigns)
                if result is not None:
                    return result
                del asigns[variable_actual.name]
        return None

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
        for restriccion in self.restricciones:
            if restriccion[0] == variable.name:
                otra_variable = restriccion[1]
                if otra_variable in asigns and asigns[otra_variable] == value:
                    return False
            elif restriccion[1] == variable.name:
                otra_variable = restriccion[0]
                if otra_variable in asigns and asigns[otra_variable] == value:
                    return False

        # Restricción de Realización Única de Tareas
        tareas_asignadas = [asigns[var] for var in asigns if var.startswith('Tarea')]
        if value in tareas_asignadas:
            return False

        return True
# Ejemplo de uso
mfc = MFC()
mfc.add_variable('A', [1, 2, 3])
mfc.add_variable('B', [1, 2])
mfc.add_variable('C', [2, 3])
mfc.add_restriccion('A', 'B')  # Ejemplo de restricción entre variables A y B
solucion = mfc.search_solution()
print(solucion)