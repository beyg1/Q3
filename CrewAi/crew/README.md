ms build tools with Microsoft C++ Build Tool are required to run crewai. 
crewai does install without it and with pth 3.11 but doesnt run properly.
create virtual env with uv. uv init --package project-name, then initialize venv
uv add crewai then start working in new main.py files with python decorators, importing Flow and others from crewai.
update scripts in .toml file, then run through uv. uv run project-name.
up until main function, we have made our first crewai flow, a pretty basic one.

