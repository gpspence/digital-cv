import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# Load JSON portfolio data
with Path("portfolio.json").open(encoding="utf-8") as f:
    data = json.load(f)

# Set up Jinja environment
env = Environment(loader=FileSystemLoader("."), autoescape=True)
index_template = env.get_template("index_template.html")

# Render the template with the data
html_output = index_template.render(**data)

# Write the output to an HTML file
with Path("index.html").open("w", encoding="utf-8") as f:
    f.write(html_output)
