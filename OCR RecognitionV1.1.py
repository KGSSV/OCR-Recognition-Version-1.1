import tkinter
import requests
from tkinter import filedialog, StringVar, BOTH, END, DISABLED, NORMAL
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
    # now deletethe url_ent as the user has taken the pain to select the file meaning he is wants local file ocr method so delete contains of url_ent
    url_ent.delete(0, END)
    global filepointer
    global location
    filepathlist = []
    filename = filedialog.askopenfilename(
        initialdir="./", title="Open Image", filetypes=(("Image Files", "*.png"), ('All Files', "*.*")))
    with open(filename, 'rb') as f:
        # filename variable contains the entire path to the selected file (png file)
        path = filename
        # remove ('/)
        path = path.replace("/", " ")
        # now the file path '/' is removed now append it into filepathlist and split based on words
        filepathlist.append(path)
        filepathlist = filepathlist[0].split()
        # select the last word
        word = filepathlist[-1]
        # now config the button text to notify the user has selected the file
        open_file_button.config(text=word)
        # as the file name contains path copy it into global variable so that it could be used anywhere in the program
        location = filename
        # same with file pointer variable
        filepointer = f


def gettext():
    te.config(state=NORMAL)
    te.delete(1.0, END)
    te.config(state=DISABLED)
    # required stuff
    # ----------------------------------------
    url = 'https://api.ocr.space/parse/image'
    api_key = 'a07656b96688957'
    # ----------------------------------------

    # map the language selected by approproyare keyword
    lang_dict = {'Arabic': 'ara', 'Dutch': 'dut', 'English': 'eng',
                 'French': 'fre', 'German': 'ger', 'None': 'eng'}
    lang = lang_dict[langvar.get()]

    # if length is there means user wants to use the url method but if images is already sleected then url entry box must be cleared
    length = len(url_ent.get())

    if length > 12:
        # remove the contents if used before

        # get the link
        link = url_ent.get() + '.png'
        # payload
        payload = {'apikey': api_key, 'url': link, 'language': lang}
        # response
        response = requests.request('POST', url, data=payload)
        # the returned response is in class  = str convert to dict bu json method to be able too iterate through the response
        response = response.json()

        dat = str(response['ParsedResults'][0]['ParsedText'])
        sub = ['\r', '\n', '\r\n', '\n\r']
        for s in sub:
            dat = dat.replace(s, " ")
        te.config(state=NORMAL)
        te.insert('1.0', dat)
        te.config(state=DISABLED)
        url_ent.delete(0, END)

    else:
        # remove the contents if used before

        # access the file pointer to operate some functions in the file selected
        global filepointer
        # get the location of the file  ( can get via the filedialog method of askopenfilename return the file path)
        global location
        # using the file pointer now open it as it would have got closed automatically after the 'with open' scope got over
        # we have the location in location paramenter so use as parameters in open function
        filepointer = open(location, 'rb')
        # payload and make the request
        payload = {'apikey': api_key,
                   'language': lang}
        response = requests.request(
            'POST', url, data=payload, files={'filename': filepointer})
        # convert to json so the response can be iterable
        response = response.json()

        dat = str(response['ParsedResults'][0]['ParsedText'])
        sub = ['\r', '\n', '\r\n', '\n\r']
        for s in sub:
            dat = dat.replace(s, " ")
        te.config(state=NORMAL)
        te.insert('1.0', dat)
        te.config(state=DISABLED)
        open_file_button.config(text='Open File')


def show_guide():
    guide = tkinter.Toplevel()
    guide.iconbitmap('icon.ico')
    guide.title('Features And Updates')
    guide.geometry('470x500+' + str(root.winfo_x() + 710) +
                   "+" + str(root.winfo_y()))
    label1 = tkinter.Label(
        guide, text='-> Code Name Changed to v1.1 (29 - 11 - 2020)', font=font1)
    label2 = tkinter.Label(
        guide, text='       -> redefined UI changes', font=font1,)
    label3 = tkinter.Label(
        guide, text='-> New Features & Updates : ', font=font1,)
    label4 = tkinter.Label(
        guide, text='       -> Some Fixes To remote file Access', font=font1,)
    label5 = tkinter.Label(
        guide, text='       -> Added language support', font=font1,)
    label6 = tkinter.Label(
        guide, text='       -> Local Support File Access Added ', font=font1)
    label7 = tkinter.Label(guide, text='       -> Friendly UI', font=font1,)
    label11 = tkinter.Label(
        guide, text='-> Code Name Changed to v1.2 (1 - 12 - 2020)', font=font1,)
    label17 = tkinter.Label(guide, text='-> Fixes : ', font=font1)
    label12 = tkinter.Label(
        guide, text='       -> Major bug Fixed (URL Method misbehavior Fixed)', font=font1)
    label13 = tkinter.Label(
        guide, text='       -> UI Experenced Enhanced', font=font1)
    label14 = tkinter.Label(
        guide, text='       -> Output Console Fixed (appending issues)', font=font1)
    label15 = tkinter.Label(
        guide, text='       -> Backend Code cleaned', font=font1)
    label16 = tkinter.Label(
        guide, text='       -> Japanese lang OCR Support removed', font=font1)
    label18 = tkinter.Label(
        guide, text='\n\nRESTRICTED TO .PNG FORMAT PHOTOS', font=font2)

    label1.grid(row=0, column=0, padx=5, pady=(0, 5), sticky='w')
    label3.grid(row=1, column=0, padx=5, pady=(0, 5), sticky='w')
    label2.grid(row=2, column=0, padx=5, pady=(0, 5), sticky='w')
    label4.grid(row=3, column=0, padx=5, pady=(0, 5), sticky='w')
    label5.grid(row=4, column=0, padx=5, pady=(0, 5), sticky='w')
    label6.grid(row=5, column=0, padx=5, pady=(0, 5), sticky='w')
    label7.grid(row=6, column=0, padx=5, pady=(0, 5), sticky='w')
    label11.grid(row=8, column=0, padx=5, pady=(0, 5), sticky='w')
    label17.grid(row=9, column=0, padx=5, pady=(0, 5), sticky='w')
    label12.grid(row=10, column=0, padx=5, pady=(0, 5), sticky='w')
    label13.grid(row=11, column=0, padx=5, pady=(0, 5), sticky='w')
    label14.grid(row=12, column=0, padx=5, pady=(0, 5), sticky='w')
    label15.grid(row=13, column=0, padx=5, pady=(0, 5), sticky='w')
    label16.grid(row=14, column=0, padx=5, pady=(0, 5), sticky='w')
    label18.grid(row=15, column=0, padx=5, pady=(0, 5), sticky='w')


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
            'English', 'French', 'German']
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
te.config(state=DISABLED)

# run the windowns main loop
root.mainloop()
