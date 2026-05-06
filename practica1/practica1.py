import reflex as rx

class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def index():
    return rx.center(
        rx.vstack(
            rx.heading("Contador"),
            rx.text(State.count),
            rx.hstack(
                rx.button("-", on_click=State.decrement),
                rx.button("+", on_click=State.increment),
            ),
        )
    )

app = rx.App()
app.add_page(index)