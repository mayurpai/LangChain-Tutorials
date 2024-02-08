from langchain.document_loaders import UnstructuredURLLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders.csv_loader import CSVLoader

text_loader = TextLoader("./nvda_news_1.txt")
text_data = text_loader.load()
print(text_data)
print(text_data[0].page_content)
print(text_data[0].metadata["source"])  # ./nvda_news_1.txt
print(text_loader.file_path)  # ./nvda_news_1.txt


csv_loader = CSVLoader("./movies.csv", source_column="title")
csv_data = csv_loader.load()
print(csv_data)
print(csv_data[0].page_content)
print(csv_data[0].metadata)

uu_loader = UnstructuredURLLoader(
    urls=[
        "https://www.moneycontrol.com/news/business/banks/hdfc-bank-re-appoints-sanmoy-chakrabarti-as-chief-risk-officer-11259771.html",
        "https://www.moneycontrol.com/news/business/markets/market-corrects-post-rbi-ups-inflation-forecast-icrr-bet-on-these-top-10-rate-sensitive-stocks-ideas-11142611.html"
    ]
)

uu_data = uu_loader.load()
print(uu_data)
