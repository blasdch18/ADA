import numpy as np

class BagOfWords:
	def __init__(self):
			self.vocab = [] #lista de palabras

	def build_vocab(self , sentences):
			for sentence in sentences:
					for word in sentence.split(' '):
							if word not in self.vocab:
									self.vocab.append(word)
			self.vocab.sort()			
			print(len(self.vocab),'words')

	def toarray(self , sentence): # 'i like it'
		words =sentence.split('  ')
		#print(words)
		vector =np.zeros(len(self.vocab))

		for word in words:
				for i, _word in enumerate(self.vocab):
					#print(i, word)
						if _word == word:
								vector[i] = 1.0
		return vector

inputs = ['i like it', 'i hate it', 'that was good', 'that was bad']

bow = BagOfWords()
bow.build_vocab(inputs)

for sentence in inputs:
	vector = bow.toarray(sentence)

	print(sentence ,vector)