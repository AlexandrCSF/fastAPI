from alembic import command
from alembic.config import Config
from src.utils.models import import_models


def run_alembic_autogenerate():
    alembic_cfg = Config("alembic.ini")
    import_models()
    try:
        command.revision(alembic_cfg, autogenerate=True, message="initial migration")
        print("Миграция успешно создана")
    except Exception as e:
        print(f"Ошибка при создании миграции: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    run_alembic_autogenerate()
