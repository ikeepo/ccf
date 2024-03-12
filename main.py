from nicegui import ui
from nicegui.events import ValueChangeEventArguments
ui.chat_message('Hello This is a demo for find job',
                name='ikeepo',
                stamp='now',
                avatar='https://robohash.org/ui')

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

with ui.row():
    ui.input('addr you want to check', on_change=show)
    ui.button('Button', on_click=lambda: ui.notify('Click'))
ui.link('Github', 'https://github.com/ikeepo/ccf').classes('mt-8')
ui.run()