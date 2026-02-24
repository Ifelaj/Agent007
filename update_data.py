from utils.fetch_news import get_mobile_news
from utils.summarizer import summarize_text
import json

news_ng = get_mobile_news("ng")

combined = " ".join([a['title'] for a in news_ng[:5]])
summary = summarize_text(combined)

data = {
    "summary_ng": summary
}

with open("weekly_summary.json", "w") as f:
    json.dump(data, f)

print("Weekly update complete.")
