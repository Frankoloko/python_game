class Text:
    def __init__(self, screen, font, position):
        self.font = font
        self.screen = screen
        self.position = position

        self.color = (242, 242, 242)

    # PUBLIC FUNCTIONS

    def draw(self, text):
        text = self.font.render(text, True, self.color )
        self.screen.blit(text, self.position)
