from interface.menu import Menu


def main():
    ''' Application initializer. '''
    menu: Menu = Menu()
    menu.display(14, 14)


if __name__ == '__main__':
    main()
