from transformers import pipeline


class Insights:
    def __init__(self):
        """
        Initializes the summarization pipeline for generating insights.
        """
        self.pipe = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")

    @staticmethod
    def chunks(text: str, chunk_size: int = 400) -> list[str]:
        """
        Splits the text into chunks of approximately chunk_size words.
        """
        words = text.split()
        return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    def points(self, text: str) -> list[str]:
        """
        Generates a list of insight points by summarizing each chunk.
        """
        chunks = self.chunks(text, 400)
        insights = []
        for chunk in chunks:
            result = self.pipe(chunk)
            insights.append(result[0]["summary_text"])
        return insights
