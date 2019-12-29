from commitizen.cz.base import BaseCommitizen


class {{cookiecutter.cz_name | capitalize}}Cz(BaseCommitizen):
    def questions(self) -> list:
        raise NotImplementedError("Not Implemented yet")

    def message(self, answers: dict) -> str:
        raise NotImplementedError("Not Implemented yet")


discover_this = {{cookiecutter.cz_name | capitalize}}Cz