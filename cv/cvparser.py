from datetime import date
from pathlib import Path
from typing import Any, Dict

from jinja2 import Environment, select_autoescape, FileSystemLoader

import yaml


def to_template_date(date: date) -> str:
    return date.strftime("%b %Y")


def yaml_to_template(cv_yaml: Dict[str, Any]) -> Dict[str, Any]:
    for experience in cv_yaml["Experiences"]:
        start_date = experience["start"]
        end_date = experience.get("end")

        start_date_str = to_template_date(start_date)
        if end_date:
            end_date_str = to_template_date(end_date)
            years = (end_date - start_date).days / 365.25
            duration = f" ({years:.1f} years)"
        else:
            end_date_str = "Current"
            duration = ""
        experience["dates"] = f"{start_date_str} - {end_date_str} {duration}"
    return cv_yaml


folder = Path(__file__).parent
file_path = folder / "cv.yaml"
with open(file_path) as file:
    cv_text = file.read()

cv_yaml_data = yaml.safe_load(cv_text)
cv_template_data = yaml_to_template(cv_yaml_data)

env = Environment(
    loader=FileSystemLoader(searchpath=folder),
    autoescape=select_autoescape()
)

template = env.get_template("template/cv.html.j2")
cv_rendered = template.render(**cv_yaml_data)

print(cv_rendered)
