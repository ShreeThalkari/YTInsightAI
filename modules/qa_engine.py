from transformers import pipeline


class QnA:
    def __init__(self):
        """
        Initializes the question answering pipeline once for reuse.
        """
        self.pipe = pipeline("question-answering", model="deepset/roberta-base-squad2")

    @staticmethod
    def chunks(text: str, chunk_size: int = 350) -> list[str]:
        """
        Splits the text into chunks of approximately chunk_size words.
        """
        words = text.split()
        return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    def questions(self, question: str, context: str) -> str:
        """
        Answers the question based on the provided context.
        Uses chunking to handle long context inputs.
        Returns the answer with highest confidence.
        """
        chunks = self.chunks(context, 350)
        results = []
        for chunk in chunks:
            answer = self.pipe(question=question, context=chunk)
            results.append((answer['score'], answer['answer']))
        # Return answer with highest confidence score
        final_answer = max(results, key=lambda x: x[0])[1]
        return final_answer
