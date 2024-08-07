from brain_games.core import run
from brain_games.games.progression import get_exercise, TASK
"""
Модуль для запуска игры "Прогрессия".
"""


def main():
    """
    Запускаем игру "Прогрессия".
    """
    run(get_exercise, TASK)


if __name__ == "__main__":
    main()
