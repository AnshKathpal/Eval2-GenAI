

def allocate_projects(employees,projects):
    assignedProjects = []
    for employee in employees:
        projects = []
        for project in projects:
            required_skills = project["required_skills"]
            employee_skills = employee["skills"]
            if required_skills(employee_skills):
                projects.append(project["name"])
        if projects:
            assignedProjects.append({"name" : employee["name"], project : projects})

    return allocate_projects


employees = [
    {"name" : "John" , "skills" : ["Python","Database"], "current_project" : None},
    {"name" : "Jane" , "skills" : ["Java","Testing"], "current_project" : None},
    {"name" : "John" , "skills" : ["Python","Java"], "current_project" : None}
]

projects = [
    {"name" : "Project A", "required_skills" : ["Python","Database"]},
    {"name" : "Project B", "required_skills" : ["Java","Testing"]},
    {"name" : "Project A", "required_skills" : ["Python","Java"]}, 
]

result = allocate_projects(employees,projects)
print(result)

