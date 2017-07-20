import tkinter, os

IMG_PATH= 'nums'

main_window = tkinter.Tk()
main_window.title('GAME 15')

files_list = os.listdir(IMG_PATH)

images_path=[]
for file in files_list:
    images_path.append(os.path.join(IMG_PATH,file))

images_list=[]
for image_path in images_path:
    _image = tkinter.PhotoImage(file=image_path)
    images_list.append(_image)
#print(images_list)

labels_list = []
SIZE=4
for i in range(SIZE):
    for j in range(SIZE):
        x=i*SIZE+j
        _label = tkinter.Label(main_window, image=images_list[x])
        _label.grid(row=i, column=j)
        #dopattributi
        _label.x=x
        _label.row=i
        _label.column=j


        labels_list.append(_label)
curr=labels_list[-1]
#print label_list



# image_1=tkinter.PhotoImage(file=images_path[7])
# print(image_1)
# label_2=tkinter.Label(main_window,image=image_1)
# label_2.grid(row=1,column=0)


main_window.mainloop()