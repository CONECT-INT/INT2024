import pandas as pd
from jinja2 import Template
import os

print("inside generate_html.py")
print(os.getcwd())

# Load the XLSX file
df = pd.read_excel('assets/data/speakers.xlsx')

# Read the HTML template
with open('assets/scripts/session_template.html', 'r') as file:
    template = Template(file.read())

# Generate HTML files for each speaker
for index, row in df.iterrows():
    html_content = template.render(
        Name=row['Name'],
        Path_to_Photo=row['Path_to_Photo'],
        Affiliation=row['Affiliation'],
        URL_Homepage=row['URL_homepage'],
        Bio=row['Short_Bio'],
        Abstract=row['Abstract']
    )

    file_path = row['HTML_file']
    # Write the HTML file
    with open(file_path, 'w') as file:
        file.write(html_content)