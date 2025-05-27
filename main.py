from modules import transcript_fetcher
from modules import link_code
from modules import summarizer
from modules import qa_engine
from modules import insights
import spacy

yt_link = input("Youtube Link: ")
lang = input("Language used in Youtube Video: ")

#Class Callers
yt_code = link_code.Code.retriever(yt_link)
fetch = transcript_fetcher.Fetecher()

#Final Text For Videos having subtitles. 
text = fetch.yt_transcript(yt_code, lang)
print(text)

summary = summarizer.Summerization()
result = summary.summarizer(text)
print(result)


insight = insights.Insights()
nlp = spacy.load("en_core_web_sm")
points = insight.points(text)

print("Key Insights:\n")
for point in points:
    doc = nlp(point)
    for sent in doc.sents:
        print(f"👉 {sent.text}")

yn = input("Do you have any questions?(Y/N): ")
while(yn.lower() == "y"):
    question = input("Questions: ")
    qna = qa_engine.QnA()
    answer = qna.questions(question, text)
    print(answer)
    yn = input("Do you have any more questions?(Y/N): ")
