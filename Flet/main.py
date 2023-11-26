import flet as ft


tracker_style:  dict = {
    "main": {
        "expand": True, 
        "bgcolor": "#17181d",
        "border_radius": 10,
    },
}

out_style: dict= {
    "expand": 1, 
    "bgcolor": "#17181d",
    "border_radius": 10,
    "padding": 30,
}


in_style: dict= {
    "expand": 1, 
    "bgcolor": "#17181d",
    "border_radius": 10,
    "padding": 30,
}


class GraphIn(ft.Container):
    def __init__(self) -> None:
        super().__init__(**in_style)


class GraphOut(ft.Container):
    def __init__(self) -> None:
        super().__init__(**out_style)


        
class Tracker(ft.Container):
    def __init__(self) -> None:
        super().__init__(tracker_style.get("main"))


def main(page: ft.Page) -> None:
    page.padding= 30
    page.bgcolor = "#1f2128"

    graph_in: ft.Container = GraphIn()
    graph_out: ft.Container = GraphOut()
    tracker: ft.Container = Tracker()

    page.add(
        ft.Row(
            expand=True, 
            controls=[
                tracker,
                ft.Column(
                    expand=True,
                    controls=[graph_in, graph_out],
                ),

            ],
        )
    )


    page.update()
    

        


if __name__ == "__main__":
    ft.app(target=main)
