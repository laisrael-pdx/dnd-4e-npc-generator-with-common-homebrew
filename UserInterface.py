import wx
from Character import create_character

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent = None, title = "Hey look, it works! :)")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        ask_techniques = self.ask(message = "Would you like to use techniques? (enter \"y\" or \"n\")")
        ask_techniques = ask_techniques.upper()
        if (ask_techniques == "Y"):
            use_techniques = True
        else:
            use_techniques = False
        ask_backgrounds = self.ask(message = "Would you like to use backgrounds? (enter \"y\" or \"n\")")
        ask_backgrounds = ask_backgrounds.upper()
        if (ask_backgrounds == "Y"):
            use_backgrounds = True
        else:
            use_backgrounds = False
        new_character = create_character(use_techniques, use_backgrounds)
        print("Your character is: ")
        print(new_character)
        test_text2 = wx.StaticText(panel, label = new_character.__str__())
        wx.StaticText.Wrap(test_text2, 380)
        panel.SetSizer(my_sizer)
        self.Show()

    def ask(self, parent=None, message=""):
        dialogue = wx.TextEntryDialog(parent, message)
        dialogue.ShowModal()
        result = dialogue.GetValue()
        dialogue.Destroy()
        return result

def run_gui():
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
    
'''

References:

Basic UI tutorial (wxPython): https://realpython.com/python-gui-with-wxpython/#getting-started-with-wxpython
Get user input in wxpython: https://stackoverflow.com/questions/18532827/using-wxpython-to-get-input-from-user
Multithreaded GUI walkthrough: https://wiki.wxpython.org/MainLoopAsThread
Displaying text in wxpython: https://www.geeksforgeeks.org/wxpython-add-text-in-window/

'''