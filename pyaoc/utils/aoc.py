from os import environ
import pathlib
from typing import TypeVar

T = TypeVar("T", bound=type)


def get_input(day: int, year) -> str:
    path = pathlib.Path.joinpath(pathlib.Path("inputs"), str(year), f"{day:02}.txt")
    if path.exists():
        return read_file(path)

    session_cookie = environ.get("AOC_SESSION_COOKIE")
    import requests

    r = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers={"Cookie": f"session={session_cookie}"},
        verify=False,
    )
    r.raise_for_status()
    write_file(path, r.text)
    return r.text


def get_input_class(day: int, year, cls: T) -> T:
    return cls(get_input(day, year))


def get_input_array(day: int, year, sep=",") -> list[str]:
    return [x for x in get_input(day, year).split(sep) if x]


def get_input_array_int(day: int, year, sep=",") -> list[int]:
    return [int(x) for x in get_input_array(day, year, sep)]


def get_input_array_class(day: int, year, cls: T, sep=",", args=None) -> list[T]:
    if not args:
        args = {}
    return [cls(x, **args) for x in get_input_array(day, year, sep)]


def read_file(path: pathlib.Path) -> str:
    with open(path, "r", encoding="UTF8") as f:
        return f.read()


def write_file(path: pathlib.Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="UTF8") as f:
        return f.write(data)


if __name__ == "__main__":
    print(get_input_array_int(2, 2019))
