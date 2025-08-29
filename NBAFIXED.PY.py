from msilib import Table
from re import search
from this import d, s
import tkinter as tk
from tkinter import BOTH, HORIZONTAL, LEFT, RIGHT, VERTICAL, Y, Button, Canvas, Frame, Label, PhotoImage, Scrollbar, ttk
from PIL import Image, ImageTk
from tkvideo import tkvideo




def switch_image(image_number):
    global current_image
    my_label.configure(image=image_list[image_number])
    current_image = image_number
    status.config(text="Image " + str(current_image + 1) + " of " + str(len(image_list)))

     


def forward():
    global current_image
    if current_image < len(image_list) - 1:
        current_image += 1
        switch_image(current_image)

def back():
    global current_image
    if current_image > 0:
        current_image -= 1
        switch_image(current_image)


def open_lebron():
    lebron_info = tk.Toplevel()
    lbl_lebron= Label(lebron_info, text="Lebron Info")
    lebron_info.configure(bg="#580858")

    # Create a table using Treeview
    table = ttk.Treeview(lebron_info, columns=('Statistic', 'Value'), show='headings', height=4)
    table.heading('Statistic', text='Statistic')
    table.heading('Value', text='Value')

    stats_data = [("Points Scored", "38,652"),
                  ("Dunks", "2,460"),
                  ("Threes", "2,261")]

    for stat, value in stats_data:
        table.insert('', 'end', values=(stat, value))

    table.pack(pady=10, padx=10)
    
    



    #-----------------------------------#
    lebron_video = tkvideo("pythonvideo/lebron.mp4",lbl_lebron,loop=1,size=(1280,720))
    lebron_video.play()





    #----------------------------------------#

    lbl_lebron.pack()


def load_lebron():
    p_bar = tk.Toplevel()

    my_progress = ttk.Progressbar(p_bar, orient='horizontal', length=300, mode='determinate')
    my_progress.pack()

    def load_and_open_lebron():
        my_progress.start(10)
        my_progress.after(1250, my_progress.stop)
        my_progress.after(1400, lambda: [p_bar.destroy(), open_lebron()])

    p_bar.after(100, load_and_open_lebron)

def open_jordan():
    jordan_info = tk.Toplevel()
    lbl_lordan= Label(jordan_info, text="Jordan Info")
    jordan_info.configure(bg="RED")

    # Create a table using Treeview
    table = ttk.Treeview(jordan_info, columns=('Statistic', 'Value'), show='headings', height=4)
    table.heading('Statistic', text='Statistic')
    table.heading('Value', text='Value')

    stats_data = [("Points Scored", "38,652"),
                  ("Dunks", "2,460"),
                  ("Threes", "2,261")]

    for stat, value in stats_data:
        table.insert('', 'end', values=(stat, value))

    table.pack(pady=10, padx=10)

    jordan_video = tkvideo("pythonvideo/jordan.mp4",lbl_lordan,loop=1,size=(1280,720))
    jordan_video.play()

    lbl_lordan.pack()

def load_jordan():
    p_bar = tk.Toplevel()

    my_progress = ttk.Progressbar(p_bar, orient='horizontal', length=300, mode='determinate')
    my_progress.pack()

    def load_and_open_jordan():
        my_progress.start(10)
        my_progress.after(1250, my_progress.stop)
        my_progress.after(1400, lambda: [p_bar.destroy(), open_jordan()])

    p_bar.after(100, load_and_open_jordan)

def open_steph():
    steph_info = tk.Toplevel()
    lbl_steph= Label(steph_info, text="Steph Info")
    steph_info.configure(bg="YELLOW")

    # Create a table using Treeview
    table = ttk.Treeview(steph_info, columns=('Statistic', 'Value'), show='headings', height=4)
    table.heading('Statistic', text='Statistic')
    table.heading('Value', text='Value')

    stats_data = [("Points Scored", "38,652"),
                  ("Dunks", "2,460"),
                  ("Threes", "2,261")]

    for stat, value in stats_data:
        table.insert('', 'end', values=(stat, value))

    table.pack(pady=10, padx=10)
    steph_video = tkvideo("pythonvideo/steph.mp4",lbl_steph,loop=1,size=(1280,720))
    steph_video.play()
    lbl_steph.pack()

def load_steph():
    p_bar = tk.Toplevel()

    my_progress = ttk.Progressbar(p_bar, orient='horizontal', length=300, mode='determinate')
    my_progress.pack()

    def load_and_open_steph():
        my_progress.start(10)
        my_progress.after(1250, my_progress.stop)
        my_progress.after(1400, lambda: [p_bar.destroy(), open_steph()])

    p_bar.after(100, load_and_open_steph)

def open_shaq():
    shaq_info = tk.Toplevel()
    lbl_shaq= Label(shaq_info, text="Shaq Info")
    shaq_info.configure(bg="YELLOW")

    # Create a table using Treeview
    table = ttk.Treeview(shaq_info, columns=('Statistic', 'Value'), show='headings', height=4)
    table.heading('Statistic', text='Statistic')
    table.heading('Value', text='Value')

    stats_data = [("Points Scored", "38,652"),
                  ("Dunks", "2,460"),
                  ("Threes", "2,261")]

    for stat, value in stats_data:
        table.insert('', 'end', values=(stat, value))

    table.pack(pady=10, padx=10)

    shaq_video = tkvideo("pythonvideo/shaq.mp4",lbl_shaq,loop=1,size=(1280,720))
    shaq_video.play()
    lbl_shaq.pack()

def load_shaq():
    p_bar = tk.Toplevel()

    my_progress = ttk.Progressbar(p_bar, orient='horizontal', length=300, mode='determinate')
    my_progress.pack()

    def load_and_open_shaq():
        my_progress.start(10)
        my_progress.after(1250, my_progress.stop)
        my_progress.after(1400, lambda: [p_bar.destroy(), open_shaq()])

    p_bar.after(100, load_and_open_shaq)

def open_kyrie():
    kyrie_info = tk.Toplevel()
    lbl_kyrie= Label(kyrie_info, text="Kyrie Info")
    kyrie_info.configure(bg="BLACK")

    # Create a table using Treeview
    table = ttk.Treeview(kyrie_info, columns=('Statistic', 'Value'), show='headings', height=4)
    table.heading('Statistic', text='Statistic')
    table.heading('Value', text='Value')

    stats_data = [("Points Scored", "38,652"),
                  ("Dunks", "2,460"),
                  ("Threes", "2,261")]

    for stat, value in stats_data:
        table.insert('', 'end', values=(stat, value))

    table.pack(pady=10, padx=10)

    kyrie_video = tkvideo("pythonvideo/kyrie.mp4",lbl_kyrie,loop=1,size=(1280,720))
    kyrie_video.play()

    lbl_kyrie.pack()

def load_kyrie():
    p_bar = tk.Toplevel()

    my_progress = ttk.Progressbar(p_bar, orient='horizontal', length=300, mode='determinate')
    my_progress.pack()

    def load_and_open_kyrie():
        my_progress.start(10)
        my_progress.after(1250, my_progress.stop)
        my_progress.after(1400, lambda: [p_bar.destroy(), open_kyrie()])

    p_bar.after(100, load_and_open_kyrie)

def search_player(event):
    player_name = combo.get().lower()

    if player_name == 'lebron':
        switch_image(0)
    elif player_name == 'jordan':
        switch_image(1)
    elif player_name == 'steph':
        switch_image(2)
    elif player_name == 'shaq':
        switch_image(3)
    elif player_name == 'kyrie':
        switch_image(4)
    else:
        print("Player not found")

def set_completion_list(event):
    search_text = event.widget.get()
    matching_options = [player for player in player_list if player.startswith(search_text)]
    combo['values'] = matching_options

def search_button_clicked():
    player_name = combo.get().lower()
    if player_name == 'lebron':
        switch_image(0)
    elif player_name == 'jordan':
        switch_image(1)
    elif player_name == 'steph':
        switch_image(2)
    elif player_name == 'shaq':
        switch_image(3)
    elif player_name == 'kyrie':
        switch_image(4)
    else:
        print("Player not found")

root = tk.Tk()
root.title('NBA WIKI')

nba_logo = ImageTk.PhotoImage(Image.open("pythonimage/NBA-Logo.png").resize((250,100)))
nba_lbl = tk.Label(root, image=nba_logo)
nba_lbl.grid(row=0,column=0,columnspan=3)

root.configure(bg="#FF6700")

img1 = ImageTk.PhotoImage(Image.open("pythonimage/lebron.png").resize((500, 400), Image.BILINEAR))
img2 = ImageTk.PhotoImage(Image.open("pythonimage/jordan.png").resize((500, 400), Image.BILINEAR))
img3 = ImageTk.PhotoImage(Image.open("pythonimage/steph.webp").resize((500, 400), Image.BILINEAR))
img4 = ImageTk.PhotoImage(Image.open("pythonimage/shaq.webp").resize((500, 400), Image.BILINEAR))
img5 = ImageTk.PhotoImage(Image.open("pythonimage/kyri.png").resize((500, 400), Image.BILINEAR))

image_list = [img1, img2, img3, img4, img5]

status = tk.Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=tk.SUNKEN)

current_image = 0
function_list = [load_lebron, load_jordan, load_steph, load_shaq, load_kyrie]


my_label = tk.Button(root, image=image_list[current_image], command=lambda: function_list[current_image]())
my_label.grid(row=1, column=0, columnspan=3)


#--------------------------------------------#
image1 = Image.open("pythonimage/next.png")
resized_image1 = image1.resize((50, 50))
Image1 = ImageTk.PhotoImage(resized_image1)

canvas = tk.Canvas(root, width=100, height=50, bg="#FF6700", highlightthickness=0)
canvas.place(relx=0.8, rely=0.865, anchor='center')

x, y = 55, 27  # You need to define x and y values

Artist1 = canvas.create_image(x, y, image=Image1)
canvas.tag_bind(Artist1, "<Button-1>", lambda event:forward())

#_-------------------------------------------------#

image2 = Image.open("pythonimage/back.png")
resized_image2 = image2.resize((50, 50))
Image2 = ImageTk.PhotoImage(resized_image2)

canvas2 = tk.Canvas(root, width=100, height=50, bg="#FF6700", highlightthickness=0)
canvas2.place(relx=0.2, rely=0.865, anchor='center')

x1, y1 = 55, 27  # You need to define x and y values

Artist2 = canvas2.create_image(x1, y1, image=Image2)
canvas2.tag_bind(Artist1, "<Button-1>", lambda event:back())

#-------------------------------------------------------#

exit_btn = ImageTk.PhotoImage(Image.open("pythonimage/exit.png").resize((50,50)))
button_exit = tk.Button(root, image=exit_btn, command=root.quit, borderwidth=0,bg="#FF6700")
button_exit.grid(row=2, column=1)

#--------------------------------------------------------#
status.grid(row=3, column=0, columnspan=3, sticky=tk.W+tk.E)



player_list = ['lebron', 'jordan', 'steph', 'shaq', 'kyrie']

combo = ttk.Combobox(root, values=player_list)
combo.grid(row=4, column=1, pady=(10,0))
combo.bind('<<ComboboxSelected>>', search_player)
combo.bind('<KeyRelease>', set_completion_list)

img_search = ImageTk.PhotoImage(Image.open("pythonimage/search.png").resize((20,20)))
search_button = ttk.Button(root,image=img_search, command=search_button_clicked)
search_button.grid(row=4, column=2, pady=(10,0))


root.mainloop()