# astro-sample
sample python code using astropy. development environment provided by vscode devcontainer and poetry.

## poetry
- generate or regenerate the poetry lock file:
```
poetry lock
```

- install the dependencies managed by poetry:
```
poetry install
```

- use poetry environment to run get_gsr_from_name.py:
```
poetry run python get_gsr_from_name.py --query "HD 155967"
```

- run astropy tests:
```
poetry run python astropy_test.py
```

## vscode
- if imports are not resolving select the poetry python interpreter:
    - `cmd+shift+p`
    - `Python: Select Interpreter`
    - select the appropriate poetry interpreter
