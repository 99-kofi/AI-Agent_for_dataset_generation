from crawl_serper import search_google
from summarize_content import summarize_text
from newspaper import Article
import pandas as pd
import os
import time

def handle_query(query, limit=5):
    results = search_google(query, num_results=limit)
    dataset = []

    for item in results:
        url = item["link"]
        title = item.get("title", "")
        snippet = item.get("snippet", "")

        try:
            article = Article(url)
            article.download()
            article.parse()
            full_text = article.text

            summary = summarize_text(full_text)

            dataset.append({
                "title": title,
                "url": url,
                "snippet": snippet,
                "full_text": full_text,
                "summary": summary,
                "tags": [query]
            })

            time.sleep(1)  # avoid being blocked
        except Exception as e:
            print(f"Error processing {url}: {e}")
            continue

    df = pd.DataFrame(dataset)
    if not os.path.exists("data"):
        os.makedirs("data")
    df.to_json(f"data/{query.replace(' ', '_')}.json", indent=4)
    df.to_csv(f"data/{query.replace(' ', '_')}.csv", index=False)
    return df
