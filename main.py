from controller import Controller
from display import Display

def main():
    display = Display()
    controller = Controller(display)

    controller.run('./storage/input.txt')

if __name__ == '__main__':
    main()