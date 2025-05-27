from transformers import pipeline

class QnA:
    def __init__(self):
        self.pipe = pipeline("question-answering", model="deepset/roberta-base-squad2")

    def chunks(self, summary, chunk_size):
        words = summary.split()
        return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    def questions(self, question, summary):
        chunks = self.chunks(summary, 350)
        result = []
        for chunk in chunks:
            answer = self.pipe(question = question, context = chunk)
            result.append((answer['score'], answer['answer']))
        final_result = max(result, key = lambda x: x[0])[1]
        return final_result