#abstraction code-2


from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class VsCode(Editor):

    def open(self):
        print("vscode open method")

    def write(self):
        print("VS Code write method")

    def debug(self):
        print("VS Code debug method")

    def execute(self):
        print("VS Code execute method")

vscode_instance=VsCode()

vscode_instance.open()

vscode_instance.write()  

vscode_instance.debug()  

vscode_instance.execute()  