import os

def generate_flask_template():
    project_dir = "flask_app_template"
    app_dir = os.path.join(project_dir, "app")
    static_dir = os.path.join(app_dir, "static")
    templates_dir = os.path.join(app_dir, "templates")
    
    app_py = os.path.join(app_dir, "app.py")
    index_html = os.path.join(templates_dir, "index.html")
    style_css = os.path.join(static_dir, "style.css")
    main_js = os.path.join(static_dir, "main.js")
    readme_md = os.path.join(project_dir, "README.md")
    requirements_txt = os.path.join(project_dir, "requirements.txt")

    os.makedirs(static_dir, exist_ok=True)
    os.makedirs(templates_dir, exist_ok=True)

    app_py_content = """from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
"""

    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Welcome to My Flask App</h1>
    <p>This is a basic Flask app template.</p>
    <script src="{{ url_for('static', filename='main.js') }}"></script>
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
    console.log('JavaScript Loaded for Flask App');
});
"""

    readme_content = """# Flask App Template

This is a basic Flask project template consisting of:

- `app/app.py`: The main Flask app file
- `app/templates/index.html`: The HTML template
- `app/static/style.css`: The stylesheet for the HTML
- `app/static/main.js`: The JavaScript file
- `requirements.txt`: List of Python packages required
"""

    requirements_content = """Flask==2.1.1
"""

    with open(app_py, 'w') as file:
        file.write(app_py_content)

    with open(index_html, 'w') as file:
        file.write(html_content)

    with open(style_css, 'w') as file:
        file.write(css_content)

    with open(main_js, 'w') as file:
        file.write(js_content)

    with open(readme_md, 'w') as file:
        file.write(readme_content)

    with open(requirements_txt, 'w') as file:
        file.write(requirements_content)

    print(f"Flask project template created in '{project_dir}'")

generate_flask_template()
