import tkinter, os

IMG_PATH= 'nums'

main_window = tkinter.Tk()
main_window.title('GAME 15')

files_list = os.listdir(IMG_PATH)

images_path=[]
for file in files_list:
    images_path.append(os.path.join(IMG_PATH,file))

images_list=[]
for file in files_list:
    _image = tkinter.PhotoImage(file=images_path)
    images_list.append(_image)
#print(images_list)

label_list = []
for image in images_list:
    _label = tkinter.Label(main_window, image=image)
    _label.grid()

    labels_list.append(_label)
#print label_list


# image_1=tkinter.PhotoImage(file=images_path[7])
# print(image_1)
# label_2=tkinter.Label(main_window,image=image_1)
# label_2.grid(row=1,column=0)


main_window.mainloop()