from modules import transcript_fetcher
from modules import link_code
from modules import summarizer
from modules import qa_engine
from modules import insights
import spacy


def main():
    yt_link = input("YouTube Link: ").strip()
    lang = input("Language used in YouTube Video (e.g. en, hi): ").strip()

    # Extract YouTube video ID
    yt_code = link_code.Code.retrieve(yt_link)
    if not yt_code:
        print("❌ Could not extract video ID from the link.")
        return

    fetch = transcript_fetcher.Fetcher()

    # Fetch transcript text
    text = fetch.yt_transcript(yt_code, lang)
    if text.startswith("❌"):
        print(text)
        return

    print("\n=== Transcript Extracted ===\n")
    print(text[:1000] + "...")  # Print only first 1000 chars for readability

    summary = summarizer.Summarization()
    result = summary.summarize(text)
    print("\n=== Summary ===\n")
    print(result)

    insight = insights.Insights()
    nlp = spacy.load("en_core_web_sm")
    points = insight.points(text)

    print("\n=== Key Insights ===\n")
    for point in points:
        doc = nlp(point)
        for sent in doc.sents:
            print(f"👉 {sent.text}")

    # Initialize QnA once (reuse pipeline)
    qna = qa_engine.QnA()

    yn = input("\nDo you have any questions? (Y/N): ").strip()
    while yn.lower() == "y":
        question = input("Question: ").strip()
        answer = qna.questions(question, text)
        print(f"Answer: {answer}")
        yn = input("Do you have any more questions? (Y/N): ").strip()


if __name__ == "__main__":
    main()
