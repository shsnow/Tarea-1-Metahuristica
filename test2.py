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

    def forward_checking(self, project, selected_projects):
        if project >= len(self.tasks):
            return False
        
        for task in range(self.n):
            if self.tasks[project][task] == 1:
                for p in selected_projects:
                    if p < len(self.tasks) and self.tasks[p][task] == 1:
                        return False
        return True

    ''' 
    def forward_checking(self, task, selected_projects):
        #print("task", task)
        #print("selected_projects", selected_projects)
        for p in selected_projects:
            if self.tasks[p][task] == 1:
                return False
        return True
    '''
    def mfc_search(self, selected_projects=[], current_profit=0):
        if len(selected_projects) == self.m:
            if current_profit > self.best_profit:
                self.best_solution = selected_projects[:]
                self.best_profit = current_profit
            return

        next_project = len(selected_projects)
        for value in [0, 1]:
            if value == 1 and sum(self.costs[task] for task in range(self.n) if self.tasks[next_project][task] == 1) > self.B:
                #print("Costo excedido")
                continue
            if value == 1 and not self.forward_checking(next_project, selected_projects):
                #print("Forward checking fallido")
                continue
            #print("Proyecto", next_project+1, "Valor", value)
            selected_projects.append(next_project)
            new_profit = current_profit + value * self.profits[next_project]
            self.mfc_search(selected_projects, new_profit)
            selected_projects.pop()

def main():
    # Leer datos del archivo y crear instancia de ProjectSelection
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
    
    print("Mejor combinación de proyectos:", project_selection.best_solution)
    print("Largo combinación de proyectos:", len(project_selection.best_solution))
    print("Ganancia total:", project_selection.best_profit)

if __name__ == "__main__":
    main()
