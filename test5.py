class ProjectSelection:
    def __init__(self, m, n, B, profits, costs, tasks):
        self.m = m
        self.n = n
        self.B = B
        self.profits = profits
        self.costs = costs
        self.tasks = tasks
        self.selected_projects = []
        self.best_solution = None
        self.best_profit = 0
        self.taskDone = [0 for _ in range(n)]

    def restrictions(self, project, tasks, costs):
        # Vector filtrado de tareas
        # Restricciones
        for i in range(len(tasks)):
            # Revisión de si la tarea es 1 y si no se ha hecho
            if tasks[i] == 1 and self.taskDone[i] == 0:
                # Si el costo de la tarea es menor al presupuesto
                if self.B - costs[i] >= 0:
                    self.B -= costs[i]
                    self.taskDone[i] = 1
                    self.best_profit += costs[i]
                    #imprimir tareas realizadas
                    print("Tarea", i+1, "del proyecto", project+1, "realizada")
                    # Revisar si se hicieron todas las tareas del proyecto comparando los 1 de tasks con los 1 de taskDone
                    if self.comparate(tasks, self.taskDone):
                        print("Proyecto", project+1, "completado")
                        self.selected_projects.append(project)
                        return True
                    else:
                        continue
                else:
                    return False
            else:
                # Revisar si ya se hicieron las tareas del proyecto (en iteraciones anteriores)
                if self.comparate(tasks, self.taskDone):
                    # Revisar si ya se seleccionó el proyecto
                    if project not in self.selected_projects:
                        self.selected_projects.append(project)
                        return True
                else:
                    continue
                continue

    def comparate(self, tasks, taskDone):
        '''
        Función que compara si las tareas de un proyecto ya se hicieron
        '''
        for i in range(len(tasks)):
            if tasks[i] == 1 and taskDone[i] == 0:
                return False
        return True

    def mfc_search(self):
        # Crear una lista de tuplas que contengan la ganancia del proyecto y su índice
        project_gains = [(self.profits[i], i) for i in range(self.m)]
        # Ordenar la lista de proyectos por ganancia en orden descendente
        project_gains.sort(reverse=True)
        
        # Recorremos los proyectos ordenados por ganancia
        for gain, project in project_gains:
            # Verificamos si las restricciones permiten seleccionar el proyecto
            if self.restrictions(project, self.tasks[project], self.costs):
                # Si es posible, seleccionamos el proyecto y continuamos con la búsqueda
                continue

            # Si no es posible seleccionar el proyecto, pasamos al siguiente en la lista
            else:
                continue



def main():
    # Leer datos del archivo y crear instancia de ProjectSelection
    '''
    Ejemplo del problema
    tareas = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]
    costos = [2, 3, 4, 5, 6] #costos de cada tarea
    ganancias = [10, 20, 30] #ganancias de cada proyecto
    B = 10 #presupuesto
    m = 3 #numero de proyectos
    n = 5 #numero de tareas
        
    project_selection = ProjectSelection(m, n, B, ganancias, costos, Atareas)
    project_selection.mfc_search()        
    '''
    with open("1-2024.txt", "r") as file:
        m = int(file.readline().strip())
        n = int(file.readline().strip())
        B = int(file.readline().strip())
        profits = list(map(int, file.readline().strip().split()))
        costs = list(map(int, file.readline().strip().split()))
        tasks = [list(map(int, file.readline().strip().split())) for _ in range(m)]
    #print(m, n, B, profits, costs, tasks)
    #for i in range(len(tasks)):
    #    print("Proyecto", i+1)
    #    print(len(tasks[i]))
        
    project_selection = ProjectSelection(m, n, B, profits, costs, tasks)
    project_selection.mfc_search()        
    print("Mejor combinación de proyectos:", project_selection.selected_projects)
    print("Ganancia total:", project_selection.best_profit)
    print("Tareas realizadas:", project_selection.taskDone)
    print("cantidad tareas realizadas", sum(project_selection.taskDone))
    #Falta la parte de la ganancia total


if __name__ == "__main__":
    main()
