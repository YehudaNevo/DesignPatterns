from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self, indent=0):
        pass

class File(FileSystemComponent):
    def display(self, indent=0):
        print(' ' * indent + self.name)

class Directory(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self, indent=0):
        print(' ' * indent + self.name)
        for child in self.children:
            child.display(indent + 2)

# Client code

root = Directory("root")
documents = Directory("documents")
pictures = Directory("pictures")

root.add(documents)
root.add(pictures)

documents.add(File("file1.txt"))
documents.add(File("file2.docx"))

pictures.add(File("image1.jpg"))
pictures.add(File("image2.png"))

root.display()
