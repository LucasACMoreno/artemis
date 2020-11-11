#exemplo de BOW - Bag od Words - Classificar músicas dos beatles e rolling stones

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split as tts
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv('dataset.csv')

# limpeza do dataFrame (df)
df.describe() # carrega o df
df.head(5) # para saber doq se trata o dataset
df.isnull().sum() # conta a qunatidade de registros nulos
df[df.classificacao.isnull()] # mostra onde está o registro nulo


#faz a limpeza do arquivo tirando o registro, o axis é para limpar somente o registro e não a coluna toda
df = df.dropna(axis=0)

# PROCESSAMENTO - BAG OF WORDS
lyrics = df['texto']
words = lyrics.str.lower().str.split() #lista de palavras

set_words  = set() #conjunto de palavras únicas (já retira as palavras iguais e coloca na ordem) - faz a intersecção dos conjuntos
#criando o conjunto de palavras (adicionando a palavras no conjunto set_words)
#for word in set_words:
	#set_words.update(word)
	
[set_words.update(word) for word in words] #for em uma única linha - programação funcional

#zip - zipar 2 informações
vocabulary = dict(zip(set_words, range(len(set_words)))) #estrutura de dicionário de palavras únicas | palavra e indice

# Criar uma Funcao que:
# A. conta a presenca de cada palavra única
# B. Cria uma matriz de posições relativa às posições do vocabulario, e
#    computa a frequencia, de um texto passado.
#
# Ex: ola mundo, mundo azul -> a frequência de  mundo é 2.
# been - 69: aparece 15 vezes
def count_words(text, vocabulary):
	frequency = [0] * len(vocabulary)
	
	for word in text:
		if word in vocabulary:
			position = vocabulary[word]
			frequency[position] += 1
	return frequency
	
#contar a frequencia de cada palavra da nossa bag
all_words_freq = [count_words(word, vocabulary) for word in words]

# treinar modelos
# separar previsores (dados de entrada - X) e classe (y)
x = np.array(all_words_freq)
y = np.array(df['classificacao'])

# dados de treinamento e de teste
x_train, x_test, y_train, y_test = tts(x, y, test_size=0.3, random_state=0)

#treinar o modelo GaussianNB
classifier = GaussianNB()
classifier.fit(x_train, y_train)

# previsão 
result = classifier.predict(x_test)
print(result)
score = accuracy_score(result, y_test)








