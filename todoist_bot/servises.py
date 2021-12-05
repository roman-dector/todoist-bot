from todoist import TodoistAPI
from loguru import logger as log


def improve_structure(api: TodoistAPI):
    static_projects = ["Team Inbox", "Inbox", "ToDo", "Someday", "Notions"]

    api.sync()

    for project in api.state["projects"]:

        if project["name"] == "ToDo":
            for item in api.projects.get_data(project["id"])["items"]:
                api.items.get_by_id(item["id"]).update(labels=[2159063863])


        if not (project["name"] in static_projects) and isinstance(project["id"], int):

            if project["color"] == 47:
                api.templates.import_into_project(project["id"], "project.csv")

            content = api.projects.get_data(project["id"])

            first_step = content["sections"][0]
            items = content["items"]

            for item in items:
                if item["section_id"] == first_step["id"]:
                    project.update(color=36)
                    break
                
                project.update(color=46)
                

    api.commit()


def run_polling(api: TodoistAPI):
    log.info("Bot started in polling mod!")
    
    while True:
        improve_structure(api)
   
