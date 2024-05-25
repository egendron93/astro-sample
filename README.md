# astro-sample
sample python code using astropy. development environment provided by vscode devcontainer and poetry.

## poetry
- Generate or regenerate the poetry lock file.
```
poetry lock
```

- Install the dependencies managed by poetry.
```
poetry install
```

- Use poetry environment to run get_gsr_from_name.py
```
poetry run python get_gsr_from_name.py --query "HD 155967"
```

## vscode
- if imports are not resolving select the poetry python interpreter:
    - `cmd+shift+p`
    - `Python: Select Interpreter`
    - select the appropriate poetry interpreter
