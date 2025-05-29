import importlib
import pkgutil


def import_models():
    """Автоматический импорт всех моделей"""
    for module_info in pkgutil.iter_modules(["src"]):
        if module_info.ispkg:
            for submodule_info in pkgutil.iter_modules([f"src\\{module_info.name}"]):
                if submodule_info.name == "models":
                    importlib.import_module(f"src.{module_info.name}.models")
