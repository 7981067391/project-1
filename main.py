from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None
        self.result = ''
        layout = BoxLayout(orientation='vertical')

        self.display = Button(text="0", font_size=32, height=200, size_hint_y=None)
        self.display.bind(on_press=self.on_display_button_press)
        layout.add_widget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        equals_button = Button(text="=", pos_hint={'center_x': 0.5, 'center_y': 0.5})
        equals_button.bind(on_press=self.on_solution_button_press)
        layout.add_widget(equals_button)

        return layout

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        if button_text == 'C':
            self.display.text = '0'
        else:
            if current == '0':
                self.display.text = ''
            self.display.text += button_text

    def on_display_button_press(self, instance):
        current = self.display.text
        if current and current[-1] in self.operators:
            return
        if self.last_was_operator:
            return
        self.display.text += ' '

    def on_solution_button_press(self, instance):
        text = self.display.text
        try:
            solution = str(eval(text))
            self.display.text = solution
        except:
            self.display.text = 'Error'

    def on_operator_button_press(self, instance):
        button_text = instance.text
        current = self.display.text

        if current and current[-1] in self.operators:
            return
        if current == '' and button_text == '-':
            self.display.text += button_text
        elif current == '' or current[-1] in self.operators:
            return
        else:
            self.display.text += button_text

    def on_operator_button_release(self, instance):
        self.last_was_operator = True

CalculatorApp().run()
