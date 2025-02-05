uv init --package project1 to create a uv project with src directory. src coming from --package
uv v to create a .venv file and that one line to copy/paste to create virtual env.
uv run project1 to run the project with default .py file which is __init__.
.toml file for configs. there:
[project.scripts]
project1 = "project1:main"
points to default python file to excecute with uv run command.