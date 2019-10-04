import numpy as np

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
        vector = np.zeros(len(self.vocab))
        for word in words:
            for i, _word in enumerate(self.vocab):
                if _word == word:
                    vector[i] += 1
        return vector
inputs = ['i like it i hola hate it that was hola good that was bad hola']

bow = BagOfWords()
bow.build_vocab(inputs)

for sentence in inputs:
    vector = bow.toarray(sentence)
    #print(sentence ,vector)
    print(vector)
