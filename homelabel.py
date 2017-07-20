import tkinter, os, random

IMG_PATH = 'nums'
SIZE = 4

main_window = tkinter.Tk()
main_window.title('GAME 15')

# counter = 0
# label_1 = tkinter.Label(main_window, text=counter)
# label_1.grid(row=5, column=4)
# counter+=1
# print (counter)

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
    labels_list[x1], labels_list[x2] = labels_list[x2], labels_list[x1]


def renderItem(arg):
    arg.grid(row=arg.row, column=arg.column)


counter = [0,]


def keyPress(arg):
    # print(arg)
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
        # print(near.x)
    counter[0] = counter[0] + 1
    print(counter[0])


def gameExit(arg):
    exit(0)


def shuffleGame():
    actions = ['r', 'l', 'u', 'd']
    for step in range(100):
        random_action = random.sample(actions, 1)[0]
        # print(random_action)
        keyPress(random_action)



main_window.bind('<Up>', lambda x: keyPress('u'))
main_window.bind('<Down>', lambda x: keyPress('d'))
main_window.bind('<Left>', lambda x: keyPress('l'))
main_window.bind('<Right>', lambda x: keyPress('r'))
main_window.bind('<q>', gameExit)

label_1 = tkinter.Label(main_window, text=counter[0])
label_1.grid(row=5, column=4)

main_window.after(2000, shuffleGame)
main_window.mainloop()
