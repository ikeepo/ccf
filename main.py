from nicegui import ui
import plotly.graph_objects as go
import os
from random import random, uniform
import requests
import json
from graphviz import Digraph, Source

from PIL import Image
# from io import BytesIO
image_widget = None
def update_graph(addr):
    # response = requests.get("http://127.0.0.1:8000")
    response = get_draw_flowmap(addr)
    data = response.json()
    graph_data = data["message"]
    graph = Source(graph_data)
    graph.render(f'graph_{addr}', format='png', cleanup=True) 
    global image_widget
    # Display the image in NiceGUI
    img = Image.open(f"graph_{addr}.png")
    # image_widget = ui.image(img)
    if image_widget is None:
        image_widget = ui.image(img)
        print(f"image_widget is None: {addr}")
    else:
        # image_widget = None
        # image_widget = ui.image(img)
        image_widget.value = img
        # image_widget.source(img)
        # image_widget.bind_from(img)
        # print(dir(image_widget))
        # image_widget.update_image()
        # print(f"image_widget isnot None: {addr}")


def get_draw_flowmap(addr: str):
    url_base = "https://young-chamber-41337-67dbb5d1ef56.herokuapp.com"
    # url_base = "http://127.0.0.1:8004"
    url = f"{url_base}/cash_flow/draw_flowmap/"
    payload = {
        "sender_address": addr,
    }
    response = requests.post(url=url, data=json.dumps(payload))
    return response



with ui.row().classes("w-full items-center justify-center"):
    ui.label("Crypto Currency Flow").classes("text-2xl font-bold")
    ui.space()
    ui.link("Github", "https://github.com/ikeepo/ccf").classes("mt-18")
    ui.space()
    ui.chat_message(
        "Hi, This is a demo for job hunting.\n\nIt don't have enough data to show the the hold flow.",
        name="ikeepo",
        stamp="now",
        avatar="https://robohash.org/ui",
    )
ui.space()
ui.separator().classes("w-full border-t-5 border-gray-300 col-span-2")
ui.space()
with ui.row().classes("w-full items-center justify-center"):
    input = ui.input(
        label="Input addr which you want to check",
        placeholder="start typing",
        value="0x000111",
        validation={"Input too short": lambda value: len(value) > 5},
    ).props("clearable")
    # 调整窗口长度
    input.classes("w-1/2 items-center justify-center")

    button = ui.button(
        "CheckFLow",
        # on_click=lambda: ui.notify(input.value),
        # on_click=lambda: update_image(input.value),
        on_click=lambda: update_graph(input.value),
    )
ui.separator().classes("w-full border-t-5 border-gray-300 col-span-2")
## 生成图片
# fig = go.Figure(
#     go.Line(x=[uniform(1, 5) for _ in range(3)], y=[uniform(1, 5) for _ in range(3)])
# )
# fig.update_layout(margin=dict(l=0, r=0, t=50, b=0), title="This is a demo flow")
# plot = ui.plotly(fig).classes("w-full")


# def update_image(addr: str):
    ## 获取json数据用以表示图片
    # json_data = get_draw_flowmap(addr)
    # json_data = get_flowmap_json_demo(addr)
    # fig = json_data
    # plot.update_figure(fig)


ui.run(title="Crypto Currency Flow", reload="FLY_ALLOC_ID" not in os.environ)
