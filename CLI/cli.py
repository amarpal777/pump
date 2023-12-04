import os
import PyInquirer as inquirer
import json
from custom_logger import cp, bcolors

print("Pump Questions CLI")


if not os.path.exists("data"):
    os.mkdir("data")
    cp("[*] Created data directory", bcolors.OKGREEN)




questions = [
    {
        "type": "input",
        "name": "category",
        "message": "Enter the path of the category (eg. Allied Products/Motor/Valves...)",
    },
    {
        "type": "input",
        "name": "name",
        "message": "Enter the name of the product",
    },
    {
        "type": "input",
        "name": "small_desc",
        "message": "Enter the small description of the product",
    },
    {
        "type": "editor",
        "name": "long_desc",
        "message": "Enter the long description of the product",
        "eargs": {"editor": "notepad.exe"},
    },
]

def ask_questions():

    answers = inquirer.prompt(questions)
    answers["image"] = "{{{CHANGE_IMGAGE_ME}}}"

    cp(f"Name: {answers['name']}", bcolors.OKCYAN)
    cp(f"Category: {answers['category']}", bcolors.OKCYAN)
    cp(f"Small Description: {answers['small_desc']}", bcolors.OKCYAN)
    cp(f"Long Description: {answers['long_desc']}", bcolors.OKCYAN)
    cp(f"Image: {answers['image']}", bcolors.OKCYAN)
    ok = inquirer.prompt(
        {
            "type": "confirm",
            "name": "ok",
            "message": "Are you sure you want to add this product?",
            "default": False,
        }
    )
    if ok["ok"]:
        with open(f"data/{create_name_id(answers['name'])}.json", "a") as f:
            f.write(json.dumps(answers, indent=4))
        cp("Created Product", bcolors.OKGREEN)

def create_name_id(name):
    return name.lower().replace(" ", "_")

def main():
    while True:
        ask_questions()
        cont = inquirer.prompt(
            {
                "type": "confirm",
                "name": "cont",
                "message": "Do you want to add another product?",
                "default": False,
            }
        )
        if not cont["cont"]:
            break



if __name__ == "__main__":
    main()
