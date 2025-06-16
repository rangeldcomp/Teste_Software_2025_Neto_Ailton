import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Baixar se necessário 
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')

# Mapear treebank_tag para formato do WordNet
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
    
def lemmatize_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)

    lemmatized_words = []
    for word, tag in pos_tags:
        wordnet_pos = get_wordnet_pos(tag)
        lemma = lemmatizer.lemmatize(word, pos=wordnet_pos)
        lemmatized_words.append(lemma)
    
    return ' '.join(lemmatized_words)

def lemmatize_sentence_without_pos_tag(sentence):
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)

    lemmatized_words = []
    for word, _ in pos_tags:
        lemma = lemmatizer.lemmatize(word)
        lemmatized_words.append(lemma)
    
    return ' '.join(lemmatized_words)

def lemmatize_sentence_no_conversion_tag(sentence):
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)

    lemmatized_words = []
    for word, tag in pos_tags:
        lemma = lemmatizer.lemmatize(word, pos=tag)
        lemmatized_words.append(lemma)
    
    return ' '.join(lemmatized_words)


# Exemplo
text = "The children were better at running than the adults."

# TEXTO ORIGINAL
print("Original:", text)
print('\n')

# LEMATIZAÇÃO E CONVERSÃO SUGERIDA NA RESPOSTA
print("Lemmatized with map:", lemmatize_sentence(text))

print('\n')
# LEMATIZAÇÃO SEM USO DE POS_TAG
print("Lemmatized without pos_tag:", lemmatize_sentence_without_pos_tag(text))

# TESTE DE USO ERRADO ( DESCOMENTE CASO QUEIRA VER O ERRO)
print('\n')
# print("Lemmatized without pos_tag:", lemmatize_sentence_no_conversion_tag(text))