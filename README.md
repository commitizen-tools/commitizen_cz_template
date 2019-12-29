# commitizen cz template

cz template for [commitizen](https://github.com/Woile/commitizen)

## Prerequiste
* Python 3.x
* [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
    * `python -m pip install cookiecutter`

## Usage

1. Initialize project through cookiecutter

    ```sh
    cookiecutter gh:Lee-W/commitizen_cz_template
    ```

    Note that you don't need to add cz prefix in your project name and package name.

2. Implement the `questions` and `message` function in your `cz_[cz_name].py`
3. Publish it to [pypi](https://pypi.org/) or install locally through `pip install .`
4. Test through `cz --name cz_[cz_name] [command]`

## Lisence
[MIT](https://opensource.org/licenses/MIT)

## Author
[Lee-W](https://github.com/Lee-W/) (weilee.rx@gmail.com)
