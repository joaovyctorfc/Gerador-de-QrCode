# -*- coding: utf-8 -*-
"""QrCode Generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CrThjwyHvISGzvuVFGmwyZpXsDUcIaXq
"""

!pip install pyqrcode

import pyqrcode as pyqr
import png

url = str(input('Digite a URL: '))
tamanho = str(input ('Digite o tamanho da Imagem: '))
gerador = pyqr.create(url)

gerador.png('QrCode.png', scale = tamanho)

if gerador != 0:
  print("QrCode Gerada com Sucesso")

else: 
  print("Erro! Não foi possivel gerar o QrCode")