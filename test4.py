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
        self.taskDone = [0 for i in range(n)]

    def restrictions(self, project, tasks, costs):
        #vector filtrado de tareas
        costFiltered = []
        for i in enumerate(tasks):
            if tasks[i] == 1:
                costFiltered.append(costs[i])
        #print(costFiltered)
        #-----------------
        #restricciones
        for i in enumerate(tasks):
            #revision de si la tarea es 1 y si no se ha hecho
            if tasks[i] == 1 and self.taskDone[i] == 0:
                #si el costo de la tarea es menor al presupuesto
                if self.B - costFiltered[i] >= 0:
                    self.B -= costFiltered[i]
                    self.taskDone[i] = 1
                    self.best_profit += costFiltered[i]
                    #revisar si se hicieron todas las tareas del proyecto comparando los 1 de tasks con los 1 de taskDone
                    if self.comparate(tasks, self.taskDone):
                        self.selected_projects.append(project)
                        return True
                    else:
                        continue
                else:
                    return False

            else:
                #revisar si ya se hicieron las tareas del proyecto (en iteraciones anteriores)
                if self.comparate(tasks, self.taskDone):
                    #revisar si ya se selecciono el proyecto
                    if project not in self.selected_projects:
                        self.selected_projects.append(project) 
                        return True
                else:
                    continue
                continue

    def comparate(self,tasks, taskDone):
        '''
        Funcion que compara si las tareas de un proyecto ya se hicieron
        '''
        for i in enumerate(tasks):
            if tasks[i] == 1 and taskDone[i] == 0:
                return False
        return True




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
        
        #project_selection = ProjectSelection(m, n, B, profits, costs, tasks)
        #project_selection.mfc_search()
        
        #print("Mejor combinación de proyectos:", project_selection.best_solution)
        #print("Largo combinación de proyectos:", len(project_selection.best_solution))
        #print("Ganancia total:", project_selection.best_profit)

    if __name__ == "__main__":
        main()
