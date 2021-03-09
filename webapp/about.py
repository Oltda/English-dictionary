import justpy as jp
from webapp import layout
from webapp import page

class About(page.Page):
    path = "/about"
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page!", classes="text-4xl m-2")
        jp.Div(a=div, text=""" 
            iuhuih ihiusd uaih duasihdiuashd iusah diuhas da
            iushdiua sdiuhs auidh asihd iuahd auhd 
            dsiuahd iusah duihas uidhasuihd iuashd iuash d
            sudhiuadh iuashdiuash duihasiudhasuidh iu
        """, classes="text-lg")
        return wp


