from alembic import command
from alembic.config import Config


def apply_migrations():
    """
    Применяет все pending миграции к базе данных
    """
    alembic_cfg = Config("alembic.ini")

    try:
        print("Начинаем применение миграций...")
        command.upgrade(alembic_cfg, "head")
        print("Миграции успешно применены")
    except Exception as e:
        print(f"Ошибка при применении миграций: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    apply_migrations()
