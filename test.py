from NLP import NLP
nlp = NLP(
    "./models/tf_bert/model_weights_9.h5",
    "./models/spacy_ner_cpu/model-best"
)

test = [
    "OMG, such a violent expxlosion here in Santa Monica. I there are so many people injured.",
    "OMG, such a violent expxlosion here in Santa Monica. I there are so many people injured.",
    ]

bert_preds = nlp.process_bert([test])
spacy_preds = nlp.process_spacy([test])

print(f"BERT: {bert_preds}")

# print doc labels and doc ents in spacy
for i, doc in enumerate(spacy_preds):
    print(f"Doc {i}")
    print(f"{doc.text}")
    print(f"{doc.label_}")