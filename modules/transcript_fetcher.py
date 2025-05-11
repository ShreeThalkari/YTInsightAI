from youtube_transcript_api import YouTubeTranscriptApi

class Fetecher:
    def yt_transcript(self, code):
        transcript = YouTubeTranscriptApi.get_transcript(code)
        text = " ".join(entry['text'].replace("\n", " ").strip() for entry in transcript)
        return text        