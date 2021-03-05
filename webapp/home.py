import justpy as jp

class Home:
    path = "/home"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the home page!", classes="text-4xl m-2")
        jp.Div(a=div, text=""" 
             iuhuih ihiusd uaih duasihdiuashd iusah diuhas da
             iushdiua sdiuhs auidh asihd iuahd auhd 
             dsiuahd iusah duihas uidhasuihd iuashd iuash d
             sudhiuadh iuashdiuash duihasiudhasuidh iu
         """, classes="text-lg")
        return wp


