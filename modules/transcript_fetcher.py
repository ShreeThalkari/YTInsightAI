from youtube_transcript_api import (YouTubeTranscriptApi, YouTubeTranscriptApiException, VideoUnavailable, TranscriptsDisabled, NoTranscriptFound, CouldNotRetrieveTranscript)

class Fetecher:
    def yt_transcript(self, code):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(code)
            text = " ".join(entry['text'].replace("\n", " ").strip() for entry in transcript)
            return text        
        
        except (VideoUnavailable, TranscriptsDisabled, NoTranscriptFound, CouldNotRetrieveTranscript, YouTubeTranscriptApiException, Exception) as e:
            return f"❌ Failed to get transcript: {e}"