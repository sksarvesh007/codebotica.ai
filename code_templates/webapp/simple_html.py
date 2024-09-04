import os
def simple_html_template():
    with open("root_dir.txt", "r") as file:
        project_dir = file.read()
    index_html = os.path.join(project_dir, "index.html")
    style_css = os.path.join(project_dir, "style.css")
    main_js = os.path.join(project_dir, "main.js")
    readme_md = os.path.join(project_dir, "README.md")

    os.makedirs(project_dir, exist_ok=True)

    html_content = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple HTML Template</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>Welcome to My Simple HTML Template</h1>
        <p>This is a basic template for a website.</p>
        <script src="main.js"></script>
    </body>
    </html>
    """

    css_content = """body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f0f0f0;
    }

    h1 {
        color: #333;
        text-align: center;
        margin-top: 50px;
    }
    """

    js_content = """document.addEventListener('DOMContentLoaded', function() {
        console.log('JavaScript Loaded');
    });
    """

    readme_content = """# Simple HTML Template

    This is a basic project template consisting of:

    - `index.html`: The main HTML file
    - `style.css`: The stylesheet for the HTML
    - `main.js`: The JavaScript file
    - `README.md`: This file providing an overview
    """

    with open(index_html, 'w') as file:
        file.write(html_content)

    with open(style_css, 'w') as file:
        file.write(css_content)

    with open(main_js, 'w') as file:
        file.write(js_content)

    with open(readme_md, 'w') as file:
        file.write(readme_content)

    print(f"Project '{project_dir}' created successfully!")
