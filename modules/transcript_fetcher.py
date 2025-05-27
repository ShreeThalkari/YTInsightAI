from youtube_transcript_api import (
    YouTubeTranscriptApi,
    VideoUnavailable,
    TranscriptsDisabled,
    NoTranscriptFound,
    CouldNotRetrieveTranscript,
    YouTubeTranscriptApiException,
)
import langcodes
#import textwrap


class Fetcher:
    def yt_transcript(self, video_id: str, lang: str) -> str:
        """
        Fetches transcript text from YouTube video by video_id and language.
        Returns transcript text or error message.
        """
        try:
            text_list = []
            langcode = langcodes.find(lang).language
            ytt_api = YouTubeTranscriptApi()
            transcript_list = ytt_api.list_transcripts(video_id)

            transcript = transcript_list.find_transcript(['en', langcode])

            for snippet in transcript.fetch():
                text_list.append(snippet.text)
            text = " ".join(text_list).replace("\n", " ").strip()

            return text

        except (
            VideoUnavailable,
            TranscriptsDisabled,
            NoTranscriptFound,
            CouldNotRetrieveTranscript,
            YouTubeTranscriptApiException,
            Exception,
        ) as e:
            return f"❌ Failed to get transcript: {e}"

# Code for future use to translate any language to English; currently disabled due to API limits and costs.
            # if transcript.language_code != "en":
            #     # Split text into 4000-character chunks (safe buffer under 5000 limit)
            #     chunks = textwrap.wrap(text, width=4000)
            #     translated_chunks = [
            #         GoogleTranslator(source="auto", target="en").translate(chunk)
            #         for chunk in chunks
            #     ]
            #     english_ver = " ".join(translated_chunks)
            #     return english_ver
            # else: