import tkinter, os

IMG_PATH = 'nums'
SIZE=4

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

def keyPress(arg):
    print(arg)
def gameExit(arg):
    exit(0)

main_window.bind('<Up>', keyPress)
main_window.bind('<Down>', keyPress)
main_window.bind('<Left>', keyPress)
main_window.bind('<Right>', keyPress)
main_window.bind('<q>', gameExit)

main_window.mainloop()