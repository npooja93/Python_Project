load_final_window = Image.open("image1.JPEG")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    load_final_window = load_final_window.resize((screen_width, screen_height))
    render = ImageTk.PhotoImage(load_final_window)
    img = Label(window, image=render)
    img.image = render
    img.place(x=0, y=0)