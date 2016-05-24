from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        """
        Has the title of the file
        Loads the kivygreet.kv
        """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('kivygreet.kv')
        return self.root

    def handle_greet(self):
        """
        When the user clicks the greet button, it prints out Hello, name in the label.
        """
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        """
        When the user clicks clear button, it clears the text field and the label.
        """
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

"""
Runs the BoxLayoutDemo class which loads kivy.app
"""
BoxLayoutDemo().run()
