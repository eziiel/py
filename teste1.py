from gensim.models import Word2Vec
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.neighbors import KNeighborsClassifier

# Exemplo de dados
data = {
    'entrada': [
        "quando cliente tem alguma dúvida ou sugestão sobre o plano, pode ser também para mudança de endereço quando já tem um plano ativo, dúvidas em geral ao serviço quando já contratado, benefícios, vantagens, quando o cliente tem alguma dúvida em geral relacionado ao provedor, etc",
        "para auxiliar o cliente com o serviço prestado (lentidão, falta de conexão, problemas com o uso do serviço, rompimento/defeito em fibra ou cabo, aparelhos, falha na entrega do serviço, seja link ou equipamentos)",
        "relacionado a dúvidas de serviços - aquisição, valor de contrato, contrato, viabilidade de instalação, taxas, contratar um serviço de novo plano, novo cliente.",
        "relacionado a valores, boletos, faturas em geral(envolvendo pagamento do serviço já adquirido), solicitação de pagamento, quando cliente informa que perdeu o boleto ou o PIX.",
        "relacionado a ordem de serviço já agendada ou programada a qual uma equipe irá ato local e validar funcionabilidade de produto (atendimento já programado ou gerado)",
        "baseada em cumprimentos (bom dia, boa tarde, boa noite)",
        "como se um novo chat tivesse sido iniciado após outro atendimento já finalizado (Obrigado, boa noite, eu que agradeço, etc.)",
        "quando não possível identificar o que foi inserido"
    ],
    'categoria': [
        "SAC",
        "SUPORTE",
        "COMERCIAL",
        "FINANCEIRO",
        "AGENDAMENTO",
        "SAUDACAO",
        "AGRADECIMENTO",
        "INDEFINIDO"
    ]
}

# Tokenizar as entradas
tokenized_sentences = [sentence.lower().split() for sentence in data['entrada']]

# print(tokenized_sentences)
# Treinar o modelo Word2Vec
model = Word2Vec(tokenized_sentences, vector_size=150, window=3, min_count=1, workers=4)
# print(model)


# Função para calcular o vetor médio
def calcular_vetor_medio(sentence, model):
    words = sentence.split()
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    if word_vectors:
        return np.mean(word_vectors, axis=0)
    else:
        return np.zeros(model.vector_size)

# Gerar vetores médios para cada entrada
X = np.array([calcular_vetor_medio(sentence.lower(), model) for sentence in data['entrada']])

from sklearn.neighbors import KNeighborsClassifier

# Mapear categorias para números
categoria_mapping = {cat: idx for idx, cat in enumerate(data['categoria'])}
y = np.array([categoria_mapping[cat] for cat in data['categoria']])

# Treinar o classificador
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X, y)

# Função para prever a categoria de uma nova entrada
def prever_categoria(nova_entrada, model, classifier):
    vetor_novo = calcular_vetor_medio(nova_entrada.lower(), model)
    return list(categoria_mapping.keys())[classifier.predict([vetor_novo])[0]]

# Treinar o vetor TF-IDF com as entradas
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_df=0.85, min_df=4)

X = vectorizer.fit_transform(data['entrada'])

# Mapear as categorias para números
y = np.array([categoria_mapping[cat] for cat in data['categoria']])

# Treinar o classificador k-NN
classifier = KNeighborsClassifier(n_neighbors= 4)

classifier.fit(X, y)

# Prever a categoria de uma nova entrada
nova_entrada = input("como posso ajudar?")
X_novo = vectorizer.transform([nova_entrada])
categoria_prevista = list(categoria_mapping.keys())[classifier.predict(X_novo)[0]]
# print(categoria_prevista)

print(f"A categoria prevista para a entrada é: {categoria_prevista}")
