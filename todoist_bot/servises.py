from todoist import TodoistAPI
from loguru import logger as log


def change_color_if_first_step_assigned(api: TodoistAPI) -> None:
    api.sync()

    list_of_projects = [
        p for p in api.state["projects"]
        if (
            (not isinstance(p["id"], str)) and (p["parent_id"] == 2279765501)
            and (p["color"] != 33)
        )
    ]

    for p in list_of_projects:

        project_data = api.projects.get_data(p["id"])
        first_step = project_data["sections"][0]
        list_of_items = project_data["items"] 
        
        for i in list_of_items:
            if i["section_id"] == first_step["id"]:
                p.update(color=36)
                #p.reorder(child_order=-1)
                break
        else:
            p.update(color=46)
            p.reorder(child_order=1)

    api.commit()


def shape_new_projects(api: TodoistAPI) -> None:
    api.sync()

    list_of_projects = [
        p for p in api.state["projects"]
        if (
            (not isinstance(p["id"], str)) and (p["parent_id"] == 2279765501)
            and (p["color"] == 33)
        )
    ]

    for p in list_of_projects:
        api.templates.import_into_project(p["id"], "todoist_bot/template_project.csv")
        p.update(color=46)

    api.commit()


def run_polling(api: TodoistAPI):
    log.info("Bot started in polling mod!")
    
    while True:
        shape_new_projects(api)
        change_color_if_first_step_assigned(api)

