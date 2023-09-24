<p align="center">
  <img src="assets/python.png" alt="Python"/>
</p>
<p align="center"><a href="https://www.flaticon.com/free-icons/python-file">Icon by Flat Icons</a></p>
<h1 align="center">Python project scratch</h1>

> This project contain a basic architectural definition for to initializing a Python application. It considers tools that I know personally, so if you think something should be improved, fell free to make suggestions.

<br />

## Table of contents
- [Tools](#tools)
- [Folder and file structures](#folder-and-file-structures)
- [Environment configuring](#environment-configuring)
- [How to use](#how-to-use)

## Tools
- Environment manager
  - [x] [poetry](https://python-poetry.org/)
  - [ ] [hatch](https://hatch.pypa.io/latest/)
- Task execution
  - [x] [taskipy](https://github.com/taskipy/taskipy)
- Tests
  - [x] [pytest](https://docs.pytest.org/en/7.4.x/)
- Code formatting
  - [x] To remove not used variables: [autoflake](https://github.com/PyCQA/autoflake)
  - [x] Code formatting: [blue](https://blue.readthedocs.io/en/latest/)
  - [x] Importing ordering: [isort](https://pycqa.github.io/isort/index.html)
- Clis development
  - [x] [click](https://click.palletsprojects.com/en/8.1.x/)
  - [ ] [typer](https://typer.tiangolo.com/)
- Task scheduling
  - [x] [celery](https://typer.tiangolo.com/)
  - [ ] [schedule](https://schedule.readthedocs.io/en/stable/)
  - [ ] [python-crontab](https://gitlab.com/doctormo/python-crontab/)
- Database
  - [x] Relational orm: [sqlAlchemy](https://www.sqlalchemy.org/)
  - [x] Mongodb orm: [pymongo](https://pymongo.readthedocs.io/en/stable/)
  - [x] Migrations manager: [alembic](https://alembic.sqlalchemy.org/en/latest/)
- Wsgi server
  - [x] Linux: [gunicorn](https://gunicorn.org/)
- Api
  - [x] Flask

## Folder and file structures
```

|- assets
|- docs
|- project
    |- cli
        |- __init__.py
    |- resources
        |- __init__.py
    |- __init__.py
    |- .env
    |- cli.py
    |- config.py
    |- wsgi.py
|- tests
    |- __init__.py
|- var
|- .editorconfig
|- .gitignore
|- docker-compose.yml
|- pyproject.toml
|- README.md
```
- assets: media, png, pdf etc files;
- docs: markdown files with system documentation
- project: application source code
  - cli: cli source code
  - resource: implementation source code
  - .env: environment variables
  - cli.py: cli source code entrypoint
  - config.py: general configurations
  - wsgi.py: configuration to wsgi servers
- tests: tests source code
- var: temporary files (not commited)
- .editorconfig: some basic settings of formatting
- .gitignore: files that should not be considered for versioning
- pyproject.toml: project configuration

## Environment configuring
Installing dependecies
```shell
pip install poetry

# The next steps must be performed within the project directory

# To activate the environment
poetry shell

# Configures the .venv folder in project root
# This folder will contain the external dependencies
poetry config virtualenvs.in-project true

# Install the other libraries
poetry add --group dev blue
poetry add --group dev isort
poetry add --group dev taskipy
poetry add --group dev autoflake

poetry add --group dev pytest
```

To configure isort
```yml
# Change the pyproject.toml file and add the configuration below
[tool.isort]
profile = "black"
line_length = 79
```

To configure taskipy
```yml
# Change the pyproject.toml file and add the configuration below
[tool.taskipy.tasks]
lint = "autoflake --in-place --exclude=*/migrations/* --remove-all-unused-imports -r . && blue . && isort ."
```

## How to use
- Activating the environment
```shell
poetry shell
```

- Executing a task
```shell
# To execute a task, you just need to type the command "task" followed by its name
task lint
```

- Executing a cli command
```shell
python project/cli.py --help
```