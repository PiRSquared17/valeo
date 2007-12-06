from Blender.Draw import Register, PushButton, QKEY, ESCKEY, Exit

def draw():
    PushButton("Hello blender!", 400, 100, 300, 100, 80, "Hello blender!!")
    PushButton("Exit", 400, 100, 270, 100, 20, "Q or ESC to exit")

def event(evt, val):
    if (evt == QKEY and not val) or (evt == ESCKEY):
        Exit()

if __name__ == '__main__':
    Register(draw, event)
