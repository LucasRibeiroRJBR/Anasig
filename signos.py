from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle


def calcular():
    y = cb_your.get()
    o = cb_other.get()

    if y == 'Áries':
        your_signo.configure(image=img_aries)
    if y == 'Touro':
        your_signo.configure(image=img_touro)
    if y == 'Gêmeos':
        your_signo.configure(image=img_gemeos)
    if y == 'Câncer':
        your_signo.configure(image=img_cancer)
    if y == 'Leão':
        your_signo.configure(image=img_leao)
    if y == 'Virgem':
        your_signo.configure(image=img_virgem)
    if y == 'Libra':
        your_signo.configure(image=img_libra)
    if y == 'Escorpião':
        your_signo.configure(image=img_escorpiao)
    if y == 'Sagitário':
        your_signo.configure(image=img_sagitario)
    if y == 'Capricórnio':
        your_signo.configure(image=img_capricornio)
    if y == 'Aquário':
        your_signo.configure(image=img_aquario)
    if y == 'Peixes':
        your_signo.configure(image=img_peixes)

    if o == 'Áries':
        other_signo.configure(image=img_aries)
    if o == 'Touro':
        other_signo.configure(image=img_touro)
    if o == 'Gêmeos':
        other_signo.configure(image=img_gemeos)
    if o == 'Câncer':
        other_signo.configure(image=img_cancer)
    if o == 'Leão':
        other_signo.configure(image=img_leao)
    if o == 'Virgem':
        other_signo.configure(image=img_virgem)
    if o == 'Libra':
        other_signo.configure(image=img_libra)
    if o == 'Escorpião':
        other_signo.configure(image=img_escorpiao)
    if o == 'Sagitário':
        other_signo.configure(image=img_sagitario)
    if o == 'Capricórnio':
        other_signo.configure(image=img_capricornio)
    if o == 'Aquário':
        other_signo.configure(image=img_aquario)
    if o == 'Peixes':
        other_signo.configure(image=img_peixes)

    # COMBINAÇÕES
    if y == 'Áries' and o == 'Áries':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Áries' and o == 'Touro':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Áries' and o == 'Gêmeos':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_10)

    if y == 'Áries' and o == 'Câncer':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Áries' and o == 'Leão':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Áries' and o == 'Virgem':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_7)

    if y == 'Áries' and o == 'Libra':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_7)

    if y == 'Áries' and o == 'Escorpião':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Áries' and o == 'Sagitário':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_9)

    if y == 'Áries' and o == 'Capricórnio':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_6)

    if y == 'Áries' and o == 'Aquário':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_10)

    if y == 'Áries' and o == 'Peixes':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Touro' and o == 'Áries':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_5)
        resul_amiz.configure(image=img_5)

    if y == 'Touro' and o == 'Touro':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_8)

    if y == 'Touro' and o == 'Gêmeos':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_10)

    if y == 'Touro' and o == 'Câncer':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_10)

    if y == 'Touro' and o == 'Leão':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Touro' and o == 'Virgem':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_7)

    if y == 'Touro' and o == 'Libra':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Touro' and o == 'Escorpião':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_7)

    if y == 'Touro' and o == 'Sagitário':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_5)
        resul_amiz.configure(image=img_6)

    if y == 'Touro' and o == 'Capricórnio':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_9)

    if y == 'Touro' and o == 'Aquário':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_6)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Touro' and o == 'Peixes':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_10)

    if y == 'Gêmeos' and o == 'Áries':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_10)

    if y == 'Gêmeos' and o == 'Touro':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Gêmeos' and o == 'Gêmeos':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_8)

    if y == 'Gêmeos' and o == 'Câncer':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Gêmeos' and o == 'Leão':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_10)

    if y == 'Gêmeos' and o == 'Virgem':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_7)

    if y == 'Gêmeos' and o == 'Libra':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Gêmeos' and o == 'Escorpião':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Gêmeos' and o == 'Sagitário':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_7)

    if y == 'Gêmeos' and o == 'Capricórnio':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Gêmeos' and o == 'Aquário':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_9)

    if y == 'Gêmeos' and o == 'Peixes':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_6)

    if y == 'Câncer' and o == 'Áries':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Câncer' and o == 'Touro':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_10)

    if y == 'Câncer' and o == 'Gêmeos':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Câncer' and o == 'Câncer':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_8)

    if y == 'Câncer' and o == 'Leão':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Câncer' and o == 'Virgem':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_10)

    if y == 'Câncer' and o == 'Libra':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Câncer' and o == 'Escorpião':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Câncer' and o == 'Sagitário':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Câncer' and o == 'Capricórnio':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_7)

    if y == 'Câncer' and o == 'Aquário':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_6)

    if y == 'Câncer' and o == 'Peixes':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_10)

    if y == 'Leão' and o == 'Áries':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Leão' and o == 'Touro':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Leão' and o == 'Gêmeos':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_10)

    if y == 'Leão' and o == 'Câncer':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Leão' and o == 'Leão':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_8)

    if y == 'Leão' and o == 'Virgem':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Leão' and o == 'Libra':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_10)

    if y == 'Leão' and o == 'Escorpião':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_7)

    if y == 'Leão' and o == 'Sagitário':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Leão' and o == 'Capricórnio':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Leão' and o == 'Aquário':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_8)

    if y == 'Leão' and o == 'Peixes':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_5)
        resul_amiz.configure(image=img_6)

    if y == 'Virgem' and o == 'Áries':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_7)

    if y == 'Virgem' and o == 'Touro':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_7)

    if y == 'Virgem' and o == 'Gêmeos':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_7)

    if y == 'Virgem' and o == 'Câncer':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_10)

    if y == 'Virgem' and o == 'Leão':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_6)

    if y == 'Virgem' and o == 'Virgem':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_8)

    if y == 'Virgem' and o == 'Libra':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Virgem' and o == 'Escorpião':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_10)

    if y == 'Virgem' and o == 'Sagitário':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_7)

    if y == 'Virgem' and o == 'Capricórnio':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Virgem' and o == 'Aquário':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Virgem' and o == 'Peixes':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_7)

    if y == 'Libra' and o == 'Áries':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_7)

    if y == 'Libra' and o == 'Touro':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Libra' and o == 'Gêmeos':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Libra' and o == 'Câncer':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Libra' and o == 'Leão':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_10)

    if y == 'Libra' and o == 'Virgem':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Libra' and o == 'Libra':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Libra' and o == 'Escorpião':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Libra' and o == 'Sagitário':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_10)

    if y == 'Libra' and o == 'Capricórnio':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_7)

    if y == 'Libra' and o == 'Aquário':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Libra' and o == 'Peixes':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Escorpião' and o == 'Áries':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Escorpião' and o == 'Touro':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_7)

    if y == 'Escorpião' and o == 'Gêmeos':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_7)

    if y == 'Escorpião' and o == 'Câncer':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Escorpião' and o == 'Leão':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_7)

    if y == 'Escorpião' and o == 'Virgem':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_10)

    if y == 'Escorpião' and o == 'Libra':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Escorpião' and o == 'Escorpião':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_10)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Escorpião' and o == 'Sagitário':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Escorpião' and o == 'Capricórnio':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Escorpião' and o == 'Aquário':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_6)

    if y == 'Escorpião' and o == 'Peixes':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Sagitário' and o == 'Áries':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_9)

    if y == 'Sagitário' and o == 'Touro':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_5)
        resul_amiz.configure(image=img_6)

    if y == 'Sagitário' and o == 'Gêmeos':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_8)

    if y == 'Sagitário' and o == 'Câncer':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Sagitário' and o == 'Leão':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Sagitário' and o == 'Virgem':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_7)

    if y == 'Sagitário' and o == 'Libra':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_10)

    if y == 'Sagitário' and o == 'Escorpião':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Sagitário' and o == 'Sagitário':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Sagitário' and o == 'Capricórnio':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Sagitário' and o == 'Aquário':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_10)

    if y == 'Sagitário' and o == 'Peixes':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Capricórnio' and o == 'Áries':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_6)

    if y == 'Capricórnio' and o == 'Touro':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_9)

    if y == 'Capricórnio' and o == 'Gêmeos':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Capricórnio' and o == 'Câncer':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_8)

    if y == 'Capricórnio' and o == 'Leão':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Capricórnio' and o == 'Virgem':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Capricórnio' and o == 'Libra':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_7)

    if y == 'Capricórnio' and o == 'Escorpião':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_10)

    if y == 'Capricórnio' and o == 'Sagitário':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Capricórnio' and o == 'Capricórnio':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_10)
        resul_amiz.configure(image=img_8)

    if y == 'Capricórnio' and o == 'Aquário':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Capricórnio' and o == 'Peixes':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Aquário' and o == 'Áries':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_10)

    if y == 'Aquário' and o == 'Touro':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_6)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Aquário' and o == 'Gêmeos':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_10)

    if y == 'Aquário' and o == 'Câncer':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_6)

    if y == 'Aquário' and o == 'Leão':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_8)

    if y == 'Aquário' and o == 'Virgem':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Aquário' and o == 'Libra':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Aquário' and o == 'Escorpião':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_6)

    if y == 'Aquário' and o == 'Sagitário':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_10)

    if y == 'Aquário' and o == 'Capricórnio':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Aquário' and o == 'Aquário':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_10)

    if y == 'Aquário' and o == 'Peixes':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_6)

    if y == 'Peixes' and o == 'Áries':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_5)

    if y == 'Peixes' and o == 'Touro':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_9)

    if y == 'Peixes' and o == 'Gêmeos':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_7)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_6)

    if y == 'Peixes' and o == 'Câncer':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_9)
        resul_amiz.configure(image=img_10)

    if y == 'Peixes' and o == 'Leão':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_5)
        resul_amiz.configure(image=img_6)

    if y == 'Peixes' and o == 'Virgem':
        resul_amor.configure(image=img_7)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_7)

    if y == 'Peixes' and o == 'Libra':
        resul_amor.configure(image=img_5)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Peixes' and o == 'Escorpião':
        resul_amor.configure(image=img_9)
        resul_sexo.configure(image=img_10)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_9)

    if y == 'Peixes' and o == 'Sagitário':
        resul_amor.configure(image=img_6)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_6)

    if y == 'Peixes' and o == 'Capricórnio':
        resul_amor.configure(image=img_8)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_8)
        resul_amiz.configure(image=img_10)

    if y == 'Peixes' and o == 'Aquário':
        resul_amor.configure(image=img_4)
        resul_sexo.configure(image=img_8)
        resul_trab.configure(image=img_6)
        resul_amiz.configure(image=img_6)

    if y == 'Peixes' and o == 'Peixes':
        resul_amor.configure(image=img_10)
        resul_sexo.configure(image=img_9)
        resul_trab.configure(image=img_7)
        resul_amiz.configure(image=img_9)


root = Tk()
root.title('Anasig')

# ESTILO
style = ThemedStyle(root)
style.set_theme('arc')

# TÍTULO
img_titulo = ImageTk.PhotoImage(Image.open('img/titulo.png'))
titulo = Label(root, image=img_titulo)
titulo.grid(row=0, columnspan=2)

# FRAMES
frm_your = ttk.LabelFrame(root, text='Seu Signo', width=120, height=80)
frm_your.grid(row=1, column=0, padx=2)
frm_your.grid_propagate(False)
frm_other = ttk.LabelFrame(root, text='Signo Dele(a)', width=120, height=80)
frm_other.grid(row=1, column=1, padx=2)
frm_other.grid_propagate(False)

# IMAGENS
img_aries = ImageTk.PhotoImage(Image.open('img/aries.png'))
img_touro = ImageTk.PhotoImage(Image.open('img/touro.png'))
img_gemeos = ImageTk.PhotoImage(Image.open('img/gemeos.png'))
img_cancer = ImageTk.PhotoImage(Image.open('img/cancer.png'))
img_leao = ImageTk.PhotoImage(Image.open('img/leao.png'))
img_virgem = ImageTk.PhotoImage(Image.open('img/virgem.png'))
img_libra = ImageTk.PhotoImage(Image.open('img/libra.png'))
img_escorpiao = ImageTk.PhotoImage(Image.open('img/escorpiao.png'))
img_sagitario = ImageTk.PhotoImage(Image.open('img/sagitario.png'))
img_capricornio = ImageTk.PhotoImage(Image.open('img/capricornio.png'))
img_aquario = ImageTk.PhotoImage(Image.open('img/aquario.png'))
img_peixes = ImageTk.PhotoImage(Image.open('img/peixes.png'))
img_0 = ImageTk.PhotoImage(Image.open('img/nivel/0.png'))
img_1 = ImageTk.PhotoImage(Image.open('img/nivel/1.png'))
img_2 = ImageTk.PhotoImage(Image.open('img/nivel/2.png'))
img_3 = ImageTk.PhotoImage(Image.open('img/nivel/3.png'))
img_4 = ImageTk.PhotoImage(Image.open('img/nivel/4.png'))
img_5 = ImageTk.PhotoImage(Image.open('img/nivel/5.png'))
img_6 = ImageTk.PhotoImage(Image.open('img/nivel/6.png'))
img_7 = ImageTk.PhotoImage(Image.open('img/nivel/7.png'))
img_8 = ImageTk.PhotoImage(Image.open('img/nivel/8.png'))
img_9 = ImageTk.PhotoImage(Image.open('img/nivel/9.png'))
img_10 = ImageTk.PhotoImage(Image.open('img/nivel/10.png'))
img_vazio = ImageTk.PhotoImage(Image.open('img/nivel/vazio.png'))
img_seta = ImageTk.PhotoImage(Image.open('img/seta.png'))

# FRAME frm_your
cb_your = ttk.Combobox(frm_your, width=15)
cb_your['values'] = ('Áries', 'Touro', 'Gêmeos', 'Câncer', 'Leão', 'Virgem',
                     'Libra', 'Escorpião', 'Sagitário', 'Capricórnio', 'Aquário', 'Peixes')
cb_your.grid(row=0, column=0)

your_signo = ttk.Label(frm_your)
your_signo.grid(row=1, columnspan=2)

# FRAME frm_other -------------------
cb_other = ttk.Combobox(frm_other, width=15)
cb_other['values'] = ('Áries', 'Touro', 'Gêmeos', 'Câncer', 'Leão', 'Virgem',
                      'Libra', 'Escorpião', 'Sagitário', 'Capricórnio', 'Aquário', 'Peixes')
cb_other.grid(row=0, column=0)

other_signo = ttk.Label(frm_other)
other_signo.grid(row=1, columnspan=2)

seta = ttk.Label(root, image=img_seta)
seta.grid(row=2, columnspan=2)

botao = ttk.Button(root, text='Calcular', command=calcular, width=30)
botao.grid(row=3, columnspan=2, pady=5)


# Placares

amor = ttk.Label(root, text='Amor')
amor.grid(row=4, columnspan=2)
resul_amor = ttk.Label(root, text='', image=img_vazio)
resul_amor.grid(row=5, columnspan=2)

sexo = ttk.Label(root, text='Sexo')
sexo.grid(row=6, columnspan=2)
resul_sexo = ttk.Label(root, text='', image=img_vazio)
resul_sexo.grid(row=7, columnspan=2)

trabalho = ttk.Label(root, text='Trabalho')
trabalho.grid(row=8, columnspan=2)
resul_trab = ttk.Label(root, text='', image=img_vazio)
resul_trab.grid(row=9, columnspan=2)

amizade = ttk.Label(root, text='Amizade')
amizade.grid(row=10, columnspan=2)
resul_amiz = ttk.Label(root, text='', image=img_vazio)
resul_amiz.grid(row=11, columnspan=2)


root.mainloop()
