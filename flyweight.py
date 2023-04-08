class Character:
    def __init__(self, char, formatting):
        self.char = char
        self.formatting = formatting

    def render(self):
        print(f"Rendering '{self.char}' with {self.formatting}")

class FormattingFlyweight:
    def __init__(self, font, size, color):
        self.font = font
        self.size = size
        self.color = color

    def __str__(self):
        return f"font: {self.font}, size: {self.size}, color: {self.color}"

class FormattingFlyweightFactory:
    def __init__(self):
        self._formatting_flyweights = {}

    def get_flyweight(self, font, size, color):
        key = (font, size, color)
        if key not in self._formatting_flyweights:
            self._formatting_flyweights[key] = FormattingFlyweight(font, size, color)
        return self._formatting_flyweights[key]

class TextEditor:
    def __init__(self):
        self._characters = []
        self._formatting_factory = FormattingFlyweightFactory()

    def add_character(self, char, font, size, color):
        formatting = self._formatting_factory.get_flyweight(font, size, color)
        character = Character(char, formatting)
        self._characters.append(character)

    def render(self):
        for character in self._characters:
            character.render()

# Example usage
editor = TextEditor()

# Adding some characters with different formatting
editor.add_character('H', 'Arial', 12, 'black')
editor.add_character('e', 'Arial', 12, 'black')
editor.add_character('l', 'Arial', 12, 'black')
editor.add_character('l', 'Arial', 12, 'black')
editor.add_character('o', 'Arial', 12, 'black')
editor.add_character('!', 'Arial', 12, 'red')

# Render the characters
editor.render()
