from manim import *
from random import randint
from random import shuffle

class letterGridRandomScene(Scene):
    def construct(self):

        #self.camera.background_color = WHITE

        def make_random_text() -> Text:
            #colors = [RED, GREEN, BLUE, TEAL, PURPLE, ORANGE]
            #color = colors[randint(0,len(colors)-1)]
            #size = randint(30,75)
            return Text(f"{'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[randint(0,24)]}", font_size=50, color=GRAY, font="Nexus Serif Pro")
        group = VGroup()
        for i in range(12):
            for j in range(6):
                shape = make_random_text().set_x(i).set_y(j)
                group.add(shape)
        group.set_x(0).set_y(0) 

        animations = [FadeIn(item, scale=0.5) for item in group]

        self.play(LaggedStart(*animations, lag_ratio=0.05))

        mix_it_up = [item.animate.scale(randint(100,200)/150).set_color([RED, GREEN, BLUE, TEAL, PURPLE, ORANGE][randint(0,5)]) for item in group]

        self.play(LaggedStart(*mix_it_up, lag_ratio=0))

        self.wait()

        text = Text("WPSNJ Art Show", font="Nexus Serif Pro", color=WHITE).scale(1.25)

        self.play(Transform(group, text))
