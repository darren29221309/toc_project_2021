from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_hello(self, event):
        text = event.message.text
        return text.lower() == "你好"

    def is_going_to_ugly(self, event):
        text = event.message.text
        return text.lower() == "我帥嗎"

    def on_enter_hello(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "你好")
        self.go_back()

    def on_exit_hello(self):
        print("Leaving hello")

    def on_enter_ugly(self, event):
        print("I'm entering ugly")

        reply_token = event.reply_token
        send_text_message(reply_token, "醜狗")
        self.go_back()

    def on_exit_ugly(self):
        print("Leaving ugly")
