try:
    import time
    import tkinter
    import os
    # from PIL import Image
    import pyautogui
    import customtkinter
except:
    os.system('pip install -r requirements.txt')
    print("package has been installed")


def on_closing():
    # Set a flag to indicate that the app is closing
    global app_closing
    app_closing = True
    print("Closing app, Please wait")
    app.quit()


def on_cancel(self):
    # Set a flag when click cancel button
    global app_closing
    app_closing = True
    self.statusLabel.configure(text="Task has been canceled!!", text_color="cyan")
    self.statusLabel.update()
    print("task has cancel")


class MainWindow(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        # row 0
        self.timesTitle = customtkinter.CTkLabel(self, text="Time", font=("Roboto", 16))

        # row 1
        self.messageTitle = customtkinter.CTkLabel(self, text="Message", font=("Roboto", 16))
        self.delayTitle = customtkinter.CTkLabel(self, text="Delay (Milliseconds)", font=("Roboto", 16))

        # row 2
        self.message = customtkinter.CTkEntry(self, placeholder_text="Enter message", width=300, height=30)
        self.times = customtkinter.CTkEntry(self, placeholder_text="How many time..?", width=300, height=30)
        self.delay = customtkinter.CTkEntry(self, placeholder_text="Enter delay", width=300, height=30)

        # row 3
        self.statusLabel = customtkinter.CTkLabel(self, text="Press to start!!", text_color="green",
                                                  font=("Roboto", 16))

        # row 4
        self.processBar = customtkinter.CTkProgressBar(self, width=250, height=10, progress_color="green")
        self.processBar.set(0)
        self.processLabel = customtkinter.CTkLabel(self, text="", font=("Roboto", 16))

        self.cancelBtn = customtkinter.CTkButton(self, text="Cancel", command=lambda: on_cancel(self))

        # Update self.processBar and self.processLabel
        def update_processBar(value, max_value):
            percent = value / max_value
            self.processBar.set(percent)
            self.processLabel.configure(text=str(value) + "/" + str(max_value) + " times")
            self.processLabel.update()
            print(str(percent) + "-" + str(max_value))

        # Easter egg
        def easter_egg(msg):
            if msg == "gay":
                global app_closing
                app_closing = True
                self.messageTitle.configure(text="You are gay!", text_color="red")
                self.timesTitle.configure(text="You are gay!", text_color="red")
                self.delayTitle.configure(text="You are gay!", text_color="red")
                self.statusLabel.configure(text="You are gay!", text_color="red")
                self.easter_msg = customtkinter.CTkLabel(self, text="You Are Gay: ERROR404, Closing app.",
                                                         text_color="red", font=("Roboto", 30))
                self.easter_msg.grid(row=5, column=1, padx=20)
                self.update()
                time.sleep(5)
                self.quit()

        # spam function
        def spam():
            global app_closing
            app_closing = False
            status = self.statusLabel
            message = str(self.message.get())

            # Easter egg
            easter_egg(message)
            # Convert and Value check
            try:
                times = int(self.times.get())
            except ValueError:
                status.configure(text="Time isn't integer, Please try again.", text_color="red")
                self.times.delete(0, tkinter.END)
                self.times.insert(0, 1)
                return
            try:
                delay = float(self.delay.get())
            except ValueError:
                status.configure(text="Delay isn't integer or decimal.  Please try again.", text_color="red")
                self.delay.delete(0, tkinter.END)
                self.delay.insert(0, 0)
                return

            # pre-start
            count = 5
            for i in range(0, count):
                status.configure(text="Start in " + str(count) + " !!", text_color="gold")
                status.update()
                count -= 1
                time.sleep(1)
            status.configure(text_color="green", text="Start!!")
            now = 1

            # add process bar
            self.processBar.grid(row=4, column=1, padx=20, pady=20)

            # Spam start
            for i in range(0, times):
                update_processBar(now, times)
                now = now + 1
                pyautogui.typewrite(message + "\n")
                time.sleep(delay)

                # If Close or Cancel
                if app_closing:
                    return

        # open setting window function
        # self.setting_window = None
        #
        # def open_setting(self):
        #     if self.setting_window is None or not self.setting_window.winfo_exists():
        #         self.setting_window = ToplevelWindow(self)  # create window if its None or destroyed
        #     else:
        #         self.setting_window.focus()  # if window exists focus it

        self.startBtn = customtkinter.CTkButton(self, text="Start", command=spam)
        self.messageTitle.grid(row=1, column=0, pady=7)
        self.timesTitle.grid(row=1, column=1, pady=7)
        self.delayTitle.grid(row=1, column=2, pady=7)

        self.message.grid(row=2, column=0, padx=20, pady=7, sticky="ew")
        self.times.grid(row=2, column=1, padx=20, pady=7, sticky="ew")
        self.delay.grid(row=2, column=2, padx=20, pady=7, sticky="ew")
        self.delay.insert(0, 0)

        self.startBtn.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        self.cancelBtn.grid(row=3, column=1, padx=20, pady=20, sticky="nsew")
        self.statusLabel.grid(row=3, column=2, pady=7)

        self.processLabel.grid(row=5, column=1, padx=20)

        # Setting button
        # settings_image = customtkinter.CTkImage(dark_image=Image.open("setting-lines.png"), size=(20, 20))
        # self.settings = customtkinter.CTkButton(self, image=settings_image, text="", fg_color="#f4f4f4", width=40,
        #                                         command=lambda: open_setting(self))
        # self.settings.grid(row=5, column=2)

        self.alwaysOnTopVar = tkinter.BooleanVar(value=False)

        def always_on_top_toggle():
            if self.alwaysOnTopVar.get():
                self.master.wm_attributes("-topmost", 1)
            else:
                self.master.wm_attributes("-topmost", 0)

        self.switch = customtkinter.CTkSwitch(self,
                                              text="Always on Top",
                                              variable=self.alwaysOnTopVar,
                                              onvalue=True, offvalue=False,
                                              command=always_on_top_toggle,
                                              font=("Roboto", 18))
        self.switch.grid(row=5, column=2, pady=50)


# Settings Window

# class ToplevelWindow(customtkinter.CTkToplevel):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.title("Settings")
#         self.geometry("400x300")
#         self.alwaysOnTopVar = tkinter.BooleanVar(value=False)
#
#         self.switch = customtkinter.CTkSwitch(self,
#                                               text="Always on Top",
#                                               variable=self.alwaysOnTopVar,
#                                               onvalue=True, offvalue=False,
#                                               command=self.on_always_on_top_switch,
#                                               font=("Roboto", 20))
#         self.switch.pack(pady=50)
#     Bug
#     def on_always_on_top_switch(self):
#         """Toggle the always on
#         top attribute of the Tk root window."""
#         if self.alwaysOnTopVar.get():
#             self.wm_attributes("-topmost", True)
#         else:
#             self.wm_attributes("-topmost", False)


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("TantaiHaha Spammer")
        self.geometry("1060x300")

        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure((0, 1), weight=1)

        self.my_frame = MainWindow(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # open Setting function

    #     self.toplevel_window = None
    #
    # def open_toplevel(self):
    #     if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
    #         self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
    #     else:
    #         self.toplevel_window.focus()  # if window exists focus it


if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
