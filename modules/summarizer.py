from transformers import pipeline

class Summerization:
    def __init__(self):
        self.pipe = pipeline("summarization", model="facebook/bart-large-cnn")
        self.max_input_words = 400 

    def chunk_text(self, text, chunk_size=400):
        words = text.split()
        return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    def summarizer(self, text):
        chunks = self.chunk_text(text, chunk_size=self.max_input_words)
        summaries = []

        for chunk in chunks:
            input_len = len(chunk.split())

            max_len = min(512, max(30, int(input_len * 0.6))) 
            min_len = max(10, int(max_len * 0.3))

            summary = self.pipe(chunk, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']
            summaries.append(summary)

        final_summary = "\n\n".join(summaries)
        return final_summary