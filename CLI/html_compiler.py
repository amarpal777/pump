import glob
import os
import json
from custom_logger import cp, bcolors
from const import BREADCRUMB_HTML, CATEGORY_HTML

all_json_files = glob.glob("data/*.json")
all_json_files.sort(key=os.path.getmtime)
cp(f"Found {len(all_json_files)} file(s)", bcolors.OKGREEN)

# Getting ALl categories
categories = []

# So there will categories inside categories like cat1/cat2/cat3
# So we will split the category by / and then add it to the categories list
for file in all_json_files:
    with open(file) as f:
        data = json.load(f)
        categories.append(data["category"].split("/"))


for cat in categories:
    cat = list(set(cat))
    cp(f"Category: {cat}", bcolors.OKGREEN)
    if not os.path.exists("out/" + "/".join(cat)):
        os.makedirs("out/" + "/".join(cat))
    for index, subcat in enumerate(cat[::-1]):
        cp(f"Current Sub Category: {subcat}", bcolors.OKGREEN)
        breadcrumbs_list = cat[::-1][index:]
        breadcrumbs_html = ""
        print("--------------------------------")
        for i in breadcrumbs_list:
            breadcrumbs_html += BREADCRUMB_HTML.replace(
                "{{{BREADCRUMB_NAME}}}", i
            ).replace("{{{BREADCRUMB_URL}}}", f"/{i}")

        category_html = open("static/category.html").read();
        category_html = category_html.replace("{{{BREADCRUMB_LIST}}}", breadcrumbs_html)
        category_html = category_html.replace("{{{CATEGORY_NAME}}}", subcat)

        cats_under_this = cat[::-1][index + 1 :]
        cats_under_this_list = []
        for i in cats_under_this:
            f = CATEGORY_HTML.replace("{{{PRODUCT_NAME}}}", i)
            f = f.replace("{{{PRODUCT_URL}}}", f"/{i}")
            cats_under_this_list.append(f)
            
        category_html.replace("{{{CATEGORY_LIST}}}", "".join(cats_under_this_list))
        open("out/" + "/".join(cat) + f"/{subcat}.html", "w").write(category_html)
        cp(f"Created: out/" + "/".join(cat) + f"/{subcat}.html", bcolors.OKGREEN)



        print("--------------------------------")
