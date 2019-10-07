import numpy as np
import matplotlib.pyplot as plt

class BagOfWords:
    def __init__(self):
        self.vocab = [] #lista de palabras

    def build_vocab(self , sentences):
        for sentence in sentences:
            for word in sentence.split(' '):
                if word not in self.vocab:
                    self.vocab.append(word)
        self.vocab.sort() #ordenado alfabeticamente
        print(self.vocab) #imprimimos el vocabulario
        #print(len(self.vocab), ' palabras') #Cuantas palabras tenemos
          
    def toarray(self , sentence): # 'i like it'
        words = sentence.split(' ')
        plt.hist(words, bins=60, alpha=1, edgecolor = 'black',  linewidth=1)
        vector = np.zeros(len(self.vocab))
        for word in words:
            for i, _word in enumerate(self.vocab):
                if _word == word:
                    vector[i] += 1
        return vector

f = open ('texto2.txt')
inputs = f.read().split(',')
f.close()


bow = BagOfWords()
bow.build_vocab(inputs)

for sentence in inputs:
    vector = bow.toarray(sentence)
    #print(sentence ,vector)
    print(vector)
