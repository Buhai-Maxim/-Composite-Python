from abc import ABC, abstractmethod
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Component(ABC):
    # Спільні методи для файлу і папки
    @abstractmethod
    def show(self, level=0):
        pass

    @abstractmethod
    def get_size(self):
        pass


class File(Component):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show(self, level=0):
        return "  " * level + "Файл: " + self.name

    def get_size(self):
        return self.size


class Folder(Component):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def show(self, level=0):
        result = "  " * level + "Папка: " + self.name

        for item in self.items:
            result += "\n" + item.show(level + 1)

        return result

    def get_size(self):
        total = 0
        for item in self.items:
            total += item.get_size()
        return total


def make_project():
    # Створюємо звичайну структуру папок і файлів
    source = Folder("source")
    source.add(File("main.py", 2400))
    source.add(File("composite.py", 5100))

    docs = Folder("docs")
    docs.add(File("README.md", 1800))

    project = Folder("my_project")
    project.add(source)
    project.add(docs)
    project.add(File("requirements.txt", 320))

    return project


project = make_project()

print("Приклад патерну Composite")
print("-" * 28)
print(project.show())
print("\nРозмір усіх файлів:", project.get_size(), "байт")

# Порівняння: окремий файл також має ті самі методи
file = File("notes.txt", 100)
print("\nОкремий файл:")
print(file.show())
print("Розмір:", file.get_size(), "байт")
