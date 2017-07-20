import tkinter, os

IMG_PATH = 'nums'
SIZE = 4

main_window = tkinter.Tk()
main_window.title('GAME 15')

files_list = os.listdir(IMG_PATH)

images_path = []
for file in files_list:
    images_path.append(os.path.join(IMG_PATH, file))

images_list = []
for image_path in images_path:
    _image = tkinter.PhotoImage(file=image_path)
    images_list.append(_image)

labels_list = []

for i in range(SIZE):
    for j in range(SIZE):
        x = i * SIZE + j
        _label = tkinter.Label(main_window, image=images_list[x])
        _label.grid(row=i, column=j)
        # dopattributi
        _label.x = x
        _label.row = i
        _label.column = j

labels_list.append(_label)
curr = labels_list[-1]

print(curr.x, curr.row, curr.column)


def leftItem(arg):
    return labels_list[arg.row * SIZE + arg.column - 1]


def rightItem(arg):
    return labels_list[arg.row * SIZE + arg.column + 1]


def upItem(arg):
    return labels_list[(arg.row - 1) * SIZE + arg.column]


def downItem(arg):
    return labels_list[(arg.row + 1) * SIZE + arg.column]


def exchangeItems(arg):
    x1 = curr.row * SIZE + curr.column
    x2 = arg.row * SIZE + arg.column
    curr.row, arg.row = arg.row, curr.row
    curr.column, arg.column = arg.column, curr.column
    labels_list[x1], labels_list[x2]=labels_list[x2],labels_list[x1]

def renderItem(arg):
    arg.grid(row=ar.row, column=arg.column)


def keyPress(arg):
    print(arg)
    near = None
    if arg == 'r' and curr.column < SIZE - 1:
        near = rightItem(curr)
    elif arg == 'l' and curr.column > 0:
        near = leftItem(curr)
    elif arg == 'u' and curr.row > 0:
        near = upItem(curr)
    elif arg == 'd' and curr.row < SIZE - 1:
        near = downItem(curr)

    if near:
        exchangeItems(near)
        renderItem(curr)
        renderItem(near)
        #print(near.x)


def gameExit(arg):
    exit(0)


main_window.bind('<Up>', lambda x: keyPress('u'))
main_window.bind('<Down>', lambda x: keyPress('d'))
main_window.bind('<Left>', lambda x: keyPress('l'))
main_window.bind('<Right>', lambda x: keyPress('r'))
main_window.bind('<q>', gameExit)

main_window.mainloop()
