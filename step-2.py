#https://yadi.sk/d/bhwJI7M03JFmij
#https://yadi.sk/i/cwbB1zai3JdmDC

import tkinter, os
#from tkinter import Tk

IMG_PATH= 'nums'

main_window = tkinter.Tk()
#main_window=Tk()
main_window.title('GAME 15')

label_1=tkinter.Label(main_window, text='Hello, World!')
#label_1=tkinter.Label(main_window, textvar='Hello, World!')
#label_1.pack()
label_1.grid(row=0, column=0)

files_list = os.listdir(IMG_PATH)
print(files_list)

#GENERATOR!

images_path=[]
for file in files_list:
    images_path.append(os.path.join(IMG_PATH,file))
    # IMG_PATH + '\' + file
print(images_path[5])

image_1=tkinter.PhotoImage(file=images_path[7])
print(image_1)
label_2=tkinter.Label(main_window,image=image_1)
label_2.grid(row=1,column=0)


main_window.mainloop()