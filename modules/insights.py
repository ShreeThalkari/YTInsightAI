from transformers import pipeline

class Insights:
    def __init__(self):
        self.pipe = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")

    def chunks(self, text, chunk_size):
        words = text.split()
        return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    def points(self, text):
        chunks = self.chunks(text, 400)
        final_result = []
        for chunk in chunks:
            result = self.pipe(chunk)
            final_result.append(result[0]["summary_text"]) 
        return final_result

