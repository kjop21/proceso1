# Librerias
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as ventana
import csv
#create file and file rader
base_de_datos =open("Process.csv")
f_reader= csv.reader(base_de_datos)
#string list
palabras= []
#fill list
for a,b,c,d,e in f_reader:
    for contador in range(int(c)):
                 palabras.append(b)

# Cambiar lista a string
cadenaDeTexto=' '.join(palabras)
print(cadenaDeTexto)
# Generate wordcloud
wordcloud1 = WordCloud(width=1500, height=1000,
                      background_color='white',
                      collocations=False,
                      include_numbers=True,
                      min_font_size=8).generate(cadenaDeTexto)
#Creamos el archivo de imagen
wordcloud1.to_file("WordCloud.png")
#Con diccionarios en vez de texto
Dictionary={}
base_de_datos.seek(0)
for a,b,c,d,e in f_reader:
    Dictionary[b]=int(c)
wordcloud2 = WordCloud(width=1500, height=1000,
                      background_color='white',
                      collocations=False,
                      include_numbers=True,
                      min_font_size=8).generate_from_frequencies(Dictionary)
# Mostrar por pantalla
ventana.figure(figsize=(8, 10), facecolor=None)
ventana.imshow(wordcloud2)
ventana.axis("off")
ventana.tight_layout(pad=0)
ventana.show()