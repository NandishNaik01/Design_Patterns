from abc import ABC, abstractmethod


# 1. Component
class FileSystemItem(ABC):

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def display(self, indent: int = 0):
        pass


# 2. Leaf
class File(FileSystemItem):

    def __init__(self, name: str, size: int):
        self.name = name
        self._size = size

    def size(self) -> int:
        return self._size

    def display(self, indent: int = 0):
        print(" " * indent + f"- File: {self.name} ({self._size} KB)")


# 3. Composite
class Folder(FileSystemItem):

    def __init__(self, name: str):
        self.name = name
        self.children: list[FileSystemItem] = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def size(self) -> int:
        # Composite delegates work to children
        return sum(child.size() for child in self.children)

    def display(self, indent: int = 0):
        print(" " * indent + f"+ Folder: {self.name}")
        for child in self.children:
            child.display(indent + 2)


# 4. Client
def main():
    # Leaf objects
    file1 = File("resume.pdf", 120)
    file2 = File("photo.jpg", 350)
    file3 = File("notes.txt", 30)

    # Composite objects
    documents = Folder("Documents")
    pictures = Folder("Pictures")
    root = Folder("Root")

    # Build tree
    documents.add(file1)
    documents.add(file3)

    pictures.add(file2)

    root.add(documents)
    root.add(pictures)

    # Client treats everything uniformly
    root.display()
    print("\nTotal size:", root.size(), "KB")


if __name__ == "__main__":
    main()
