from transformers import pipeline


class Summarization:
    def __init__(self):
        """
        Initializes the summarization pipeline using facebook/bart-large-cnn.
        """
        self.pipe = pipeline("summarization", model="facebook/bart-large-cnn")
        self.max_input_words = 400

    @staticmethod
    def chunk_text(text: str, chunk_size: int = 400) -> list[str]:
        """
        Splits text into chunks of approx chunk_size words.
        """
        words = text.split()
        return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    def summarize(self, text: str) -> str:
        """
        Summarizes the text by chunking and aggregating results.
        """
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
