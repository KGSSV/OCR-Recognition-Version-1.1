import tkinter
import requests
from tkinter import filedialog, StringVar, BOTH
from io import BytesIO

root = tkinter.Tk()

font1 = ('SimSum', 12)
font2 = ('SimSum', 17)

# frames
input_frame = tkinter.Frame(root, bg='#A0A6DE')
input_frame1 = tkinter.Frame(
    input_frame, bg='#A0A6DE',)    # frame inside frames
input_frame2 = tkinter.Frame(
    input_frame, bg='#A0A6DE')    # frame inside frames

output_frame = tkinter.Frame(root, bg='#A0A6DE')

input_frame.pack(fill=BOTH, expand=True)
output_frame.pack(fill=BOTH, expand=True)

input_frame1.grid(row=0, column=0)
input_frame2.grid(row=0, column=1)


root.title('OCR Extractor V1.1')
root.geometry('695x500')
root.resizable(0, 0)
root.iconbitmap('icon.ico')


def openimage():
    global info
    global loc
    filename = filedialog.askopenfilename(
        initialdir="./", title="Open Image", filetypes=(("Image Files", "*.png"), ('All Files', "*.*")))
    with open(filename, 'rb') as f:

        name = filename
        name = name.replace("/", " ")
        print(name)
        l1 = []
        l1.append(name)
        l1 = l1[0].split()
        word = l1[-1]
        open_file_button.config(text=word)
        loc = filename
        info = f


def gettext():
    global info
    global loc
    info = open(loc, 'rb')
    print(info)

    # required stuff
    # ----------------------------------------
    url = 'https://api.ocr.space/parse/image'
    api_key = 'a07656b96688957'
    # ----------------------------------------

    lang_dict = {'Arabic': 'ara', 'Dutch': 'dut', 'English': 'eng',
                 'French': 'fre', 'German': 'ger', 'Japanese': 'jap', 'None': 'eng'}
    lang = lang_dict[langvar.get()]
    print(lang)
    length = len(url_ent.get())

    if length > 10:

        link = url_ent.get() + '.png'
        payload = {'apikey': api_key, 'url': link, 'language': lang}
        response = requests.request('POST', url, data=payload)
        print(response)
        response = response.json()
        print(response)
        dat = str(response['ParsedResults'][0]['ParsedText'])
        sub = ['\r', '\n', '\r\n', '\n\r']
        for s in sub:
            dat = dat.replace(s, " ")
        te.insert('1.0', dat)

    else:
        payload = {'apikey': api_key,
                   'language': lang}
        response = requests.request(
            'POST', url, data=payload, files={'filename': info})
        print(response)
        response = response.json()
        print(response)
        dat = str(response['ParsedResults'][0]['ParsedText'])
        sub = ['\r', '\n', '\r\n', '\n\r']
        for s in sub:
            dat = dat.replace(s, " ")
        te.insert('1.0', dat)
        open_file_button.config(text='Open File')


def show_guide():
    guide = tkinter.Toplevel()
    guide.iconbitmap('icon.ico')
    guide.title('Features And Updates')
    guide.geometry('350x500+' + str(root.winfo_x() + 710) +
                   "+" + str(root.winfo_y()))
    label1 = tkinter.Label(
        guide, text='-> Code Name Changed to v1.1', font=font1,)
    label2 = tkinter.Label(guide, text='-> redefined UI changes', font=font1,)
    label3 = tkinter.Label(guide, text='-> New Features : ', font=font1,)
    label4 = tkinter.Label(
        guide, text='       -> Some Fixes To remote file Access', font=font1,)
    label5 = tkinter.Label(
        guide, text='       -> Added language support', font=font1,)
    label6 = tkinter.Label(
        guide, text='       -> Local Support File Access Added', font=font1,)
    label7 = tkinter.Label(guide, text='       -> Friendly UI', font=font1,)
    label8 = tkinter.Label(
        guide, text='-> Special Thanks to ocr.space to provide API support', font=font1,)
    label9 = tkinter.Label(guide, text='VERSION V1.1', font=font1,)

    label10 = tkinter.Label(guide, text='Notes :', font=font1)
    label11 = tkinter.Label(
        guide, text='If you have a file selected and url entered \n priority is given to url method', font=font1)

    label1.grid(row=0, column=0, padx=5, pady=(0, 5), sticky='w')
    label2.grid(row=1, column=0, padx=5, pady=(0, 5), sticky='w')
    label3.grid(row=2, column=0, padx=5, pady=(0, 5), sticky='w')
    label4.grid(row=3, column=0, padx=5, pady=(0, 5), sticky='w')
    label5.grid(row=4, column=0, padx=5, pady=(0, 5), sticky='w')
    label6.grid(row=5, column=0, padx=5, pady=(0, 5), sticky='w')
    label7.grid(row=6, column=0, padx=5, pady=(0, 5), sticky='w')
    label9.grid(row=7, column=0, padx=5, pady=(0, 5), sticky='w')
    label9.grid(row=8, column=0, padx=5, pady=(0, 5), sticky='w')
    label10.grid(row=9, column=0, padx=5, pady=(0, 5), sticky='w')
    label11.grid(row=10, column=0, pady=(0, 5), sticky='w')


local_label = tkinter.Label(
    input_frame1, text='Select File : ', bg='#A0A6DE', font=font1)
open_file_button = tkinter.Button(
    input_frame1, text='Open File', width=36, font=font1, command=openimage)


local_label.grid(row=0, column=0, padx=20, pady=(5, 10))
open_file_button.grid(row=0, column=1, columnspan=2,
                      padx=20, pady=(5, 10), sticky='w')


or_label = tkinter.Label(input_frame1, text='OR', font=font2, bg='#A0A6DE')
or_label.grid(row=1, column=1, padx=20, pady=(5, 0))

remote_label = tkinter.Label(
    input_frame1, text='Enter URL : ', bg='#A0A6DE', font=font1)
url_ent = tkinter.Entry(input_frame1, width=30, font=(10))

remote_label.grid(row=2, column=0, padx=20, pady=(5, 10))
url_ent.grid(row=2, column=1, padx=20, pady=(5, 10),)


language = ['None', 'Arabic', 'Dutch',
            'English', 'French', 'German', 'Japanese']
langvar = StringVar()   # variable which tracks which of the following  is selected
langvar.set('None')
dropbox = tkinter.OptionMenu(input_frame2, langvar, *language)
get_text = tkinter.Button(input_frame2, text='Get Text',
                          bg='#A0A6DE', font=(10), activebackground='#A0A6DE', command=gettext, width=15, borderwidth=0)
dropbox.config(height=1, width=8, borderwidth=1)

refresh = tkinter.Button(input_frame2, text='Features',
                         width=9, command=show_guide)

dropbox.grid(row=0, column=0, sticky='w', pady=(0, 10), padx=(0, 5))
refresh.grid(row=0, column=0, sticky='e', pady=(0, 10))
get_text.grid(row=1, column=0, pady=(28, 10))


te = tkinter.Text(output_frame, height=22, width=85)
te.grid(row=0, column=0, padx=5, sticky='N')

# run the windowns main loop
root.mainloop()
