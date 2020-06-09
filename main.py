# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#
# TicTacToe Program
# Elvira Konovalov
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Library import
import kivy
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.popup import Popup

#from twoPlayer import TwoPlayerScreen
from onePlayer import OnePlayerScreen

Builder.load_string("""

<MenuScreen>:
    FloatLayout:
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'Vector Seamless Modern Shapes Pattern Colorful-01.jpg' # Background: https://onlyvectorbackgrounds.com/modern-shapes-pattern-colorful/
        Image:
            pos_hint: {'x':0, 'y':.1}
            source: 'TTTlogo.png'
            size: self.texture_size
        
        Button:
            pos_hint: {'x': 0, 'y': -0.25}
            # size: self.texture_size
            background_color: 0, 0, 0, 0
            text: 'Player vs Player'
            font_size: 85
            # text_size: self.size
            #on_press: root.manager.current = 'second'
        
        Button:
            pos_hint: {'x': 0, 'y': -0.35}
            # size: self.texture_size
            background_color: 0, 0, 0, 0
            text: 'Player vs Computer'
            font_size: 85
            # text_size: self.size
            on_press: root.manager.current = 'third'
            
<TwoPlayerScreen>
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'Vector Seamless Modern Shapes Pattern Colorful-01.jpg'
            
<OnePlayerScreen>
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'Vector Seamless Modern Shapes Pattern Colorful-01.jpg'

""")


# Declare both screens
class MenuScreen(Screen):
    pass


class TestApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='first'))
        #sm.add_widget(TwoPlayerScreen(name='second'))
        sm.add_widget(OnePlayerScreen(name='third'))
        Window.minimum_width = 640
        Window.minimum_height = 360
        return sm


if __name__ == '__main__':
    TestApp().run()
