
#Загрузка и отображение данных
f = open('belye_nochi.txt', "r")
text = f.read()


#Предварительная обработка текста
text = text.lower()
import string
spec_chars = string.punctuation + '\n\xa0«»\t—…' 

def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])

text = remove_chars_from_text(text, spec_chars)
text = remove_chars_from_text(text, string.digits)

#Токенизация текста
from nltk import word_tokenize
text_tokens = word_tokenize(text)

#print(type(text_tokens), len(text_tokens))
#print(text_tokens[:10])

import nltk
text = nltk.Text(text_tokens)
#print(type(text))

#Расчёт частоты встречаемости слов
from nltk.probability import FreqDist
fdist = FreqDist(text)
#print(fdist.most_common(5))
#fdist.plot(30,cumulative=False)

#Удаление стоп-слов
from nltk.corpus import stopwords
russian_stopwords = stopwords.words("russian")
russian_stopwords.extend(['это', 'нею', 'б'])
#print(len(russian_stopwords))

text_tokens = [token.strip() for token in text_tokens if token not in russian_stopwords]
text = nltk.Text(text_tokens)
fdist_sw = FreqDist(text)
#print(fdist_sw.most_common(10))

#Построение облака слов
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text_raw = " ".join(text)
wordcloud = WordCloud().generate(text_raw)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
