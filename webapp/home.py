import justpy as jp
from webapp import layout

class Home:
    path = "/home"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")

        jp.Div(a=div, text="This is the home page!", classes="text-4xl m-2")
        jp.Div(a=div, text=""" 
             iuhuih ihiusd uaih duasihdiuashd iusah diuhas da
             iushdiua sdiuhs auidh asihd iuahd auhd 
             dsiuahd iusah duihas uidhasuihd iuashd iuash d
             sudhiuadh iuashdiuash duihasiudhasuidh iu
         """, classes="text-lg")
        return wp




