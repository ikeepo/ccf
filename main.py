from nicegui import ui
from nicegui.events import ValueChangeEventArguments
import plotly.graph_objects as go
import asyncio
from random import random, uniform

with ui.row().classes('w-full items-center justify-center'):
    ui.label('Crypto Currency Flow').classes('text-2xl font-bold')
    ui.space()
    ui.link('Github', 'https://github.com/ikeepo/ccf').classes('mt-18')
    ui.space()
    ui.chat_message('Hi, This is a demo for job hunting',
                    name='ikeepo',
                    stamp='now',
                    avatar='https://robohash.org/ui')
ui.space()
ui.separator().classes('w-full border-t-5 border-gray-300 col-span-2')
ui.space()
with ui.row().classes("w-full items-center justify-center"):
    input = ui.input(
        label='Input addr which you want to check', 
        placeholder='start typing',
        value='dafagaadgagaerhgerahrhrahahg',
        validation={'Input too short': lambda value: len(value) > 15},
        ).props("clearable")
    # ui.label().bind_text_from(input, 'value')
    # 调整窗口长度
    input.classes('w-1/2 items-center justify-center')

    button = ui.button(
        'Button', 
        # on_click=lambda: ui.notify(input.value),
        on_click=lambda: update_image(input.value)
        )
ui.separator().classes('w-full border-t-5 border-gray-300 col-span-2')
# def show(event: ValueChangeEventArguments):
#     name = type(event.sender).__name__
#     ui.notify(f'{name}: {event.value}')
## 生成图片
fig = go.Figure(go.Line(
        x=[uniform(1,5) for _ in range(3)], 
        y=[uniform(1,5) for _ in range(3)]
        ))
fig.update_layout(
    margin=dict(l=0, r=0, t=50, b=0),
    title='This is a demo flow'
    )
plot = ui.plotly(fig).classes('w-full')

def update_image(addr: str):
    fig = go.Figure(go.Line(
        x=[uniform(1,5) for _ in range(3)], 
        y=[uniform(1,5) for _ in range(3)]
        ))
    fig.update_layout(
        margin=dict(l=0, r=0, t=50, b=0),
        title=addr
        )
    plot.update_figure(fig)





ui.run()