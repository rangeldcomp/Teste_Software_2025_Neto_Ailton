import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

words = ['running', 'better', 'feet', 'cars']

# Lematização sem passar POS (default = noun)
lemmas_default = [lemmatizer.lemmatize(word) for word in words]

# Lematização passando POS (exemplo: 'running' como verbo)
lemmas_with_pos = [
    lemmatizer.lemmatize('running', pos='v'),  # verbo
    lemmatizer.lemmatize('better', pos='a'),   # adjetivo
    lemmatizer.lemmatize('feet', pos='n'),     # substantivo
    lemmatizer.lemmatize('cars', pos='n')      # substantivo
]

print("Sem POS:", lemmas_default)
print("Com POS:", lemmas_with_pos)

# Saída esperada
#
# Sem POS: ['running', 'better', 'foot', 'car']
# Com POS: ['run', 'good', 'foot', 'car']