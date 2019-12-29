from setuptools import setup


setup(
    name="{{cookiecutter.package_name}}",
    version="{{cookiecutter.version}}",
    py_modules=["cz_{{cookiecutter.cz_name}}"],
    license="{{cookiecutter.license}}",
    long_description="{{cookiecutter.package_description}}",
    install_requires=["commitizen"],
)
