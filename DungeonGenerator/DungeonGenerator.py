from Generator import Generator

width = 40
height = 20

if __name__ == '__main__':
    gen = Generator()
    gen.Initialise(width, height)
    gen.Run()
    gen.Draw()

    input()