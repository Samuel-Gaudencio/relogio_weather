from tkinter import *
import os
from time import strftime
from key import key
import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {'q': '-22.97, -42.93'}

headers = {
    "X-RapidAPI-Key": key,
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
regiao = response.json()['location']['region']
cidade = response.json()['location']['name']
sigla = ''

for i in regiao:
    if i == i.upper():
        if i != ' ':
            sigla += i

temp = response.json()['current']


root = Tk()
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(bg='#1d1d1d')

light = PhotoImage(file='brightness.png')
dark = PhotoImage(file='dark.png')


def fundo():
    if root['bg'] == '#1d1d1d':
        root['bg'] = 'white'
        button.configure(image=light, bg='white')
        tela.configure(bg='white')
        saudacao.configure(bg='white')
        data.configure(bg='white')
        hora.configure(bg='white')
        temperatura.configure(bg='white')
    else:
        root.configure(bg='#1d1d1d')
        button.configure(image=dark, bg='#1d1d1d')
        tela.configure(bg='#1d1d1d')
        saudacao.configure(bg='#1d1d1d')
        data.configure(bg='#1d1d1d')
        hora.configure(bg='#1d1d1d')
        temperatura.configure(bg='#1d1d1d')


def get_saudacao():
    name = os.getlogin().title()
    saudacao.configure(text=f'Olá, {name}')


def get_data():
    date = strftime(' %a, %d %b %Y')
    data.configure(text=date)


def get_hora():
    hours = strftime('%H:%M:%S')
    hora.configure(text=hours)
    hora.after(1000, get_hora)


def get_tempe():
    temperatura.configure(text=f'{temp["temp_c"]}°C - {cidade}, {sigla}')


tela = Canvas(width=600, height=20, bg='#1d1d1d', highlightthickness=0)
tela.pack()
button = Button(root, command=fundo, relief=SOLID, bd=0, image=dark, bg='#1d1d1d')
button.pack(pady=10)
saudacao = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 16))
saudacao.pack()
temperatura = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 14))
temperatura.pack()
data = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 14))
data.pack()
hora = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 64))
hora.pack()


get_saudacao()
get_tempe()
get_data()
get_hora()
root.mainloop()
