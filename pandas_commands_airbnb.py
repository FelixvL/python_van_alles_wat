# vind geheel file op: https://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2024-09-05/data/listings.csv.gz
# https://insideairbnb.com/get-the-data/
import pandas

df = pandas.read_csv("listings.csv")

print(df.columns)

def printAlles(kolom):
    for i, bdr in df.iterrows():
        print(kolom, ": ", bdr[kolom])

def hoogsteEnLaagstePrijs():
    df['price'] = df['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
    print("Laagste prijs:", df['price'].min())
    print("Hoogste prijs:", df['price'].max())
    print("Gemiddelde prijs:", df['price'].mean())
    print("Gemiddelde aantalnachten:", df['minimum_nights'].mean())

def buurtMetMeesteLocaties():
    most_listings_neighbourhood = df['neighbourhood_cleansed'].value_counts().idxmax()
    most_listings_count = df['neighbourhood_cleansed'].value_counts().max()
    print(f"De buurt met de meeste Airbnb-locaties is: {most_listings_neighbourhood}, met {most_listings_count} locaties.")

def prijsPerBuurt():
    df['price'] = df['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
    average_price_per_neighbourhood = df.groupby('neighbourhood_cleansed')['price'].mean()
    print(average_price_per_neighbourhood.head())

def zomaarTwee():
    # 1. Gemiddelde prijs per buurt, gesorteerd van hoog naar laag
    avg_price_sorted = df.groupby('neighbourhood_cleansed')['price'].mean().sort_values(ascending=False)
    print(avg_price_sorted)

    # 2. Selecteer 'name', 'price', en 'room_type' waar de prijs > 300
    high_price_listings = df[df['price'] > 300][['name', 'price', 'room_type']].head(10)
    print(high_price_listings)

def hostsMetMeerDanEenListing():
    hosts_with_multiple_listings = df.groupby('host_id')['id'].count()
    hosts_with_more_than_one_listing = hosts_with_multiple_listings[hosts_with_multiple_listings > 1].count()
    print(f"Aantal verhuurders met meer dan één listing: {hosts_with_more_than_one_listing}")

def prijsIcmKamerAantal():
    price_per_bedrooms = df.groupby('bedrooms')['price'].mean()
    print(price_per_bedrooms)

def corrReviewEnPrijs():
    df_filtered = df[['review_scores_rating', 'price']].dropna()
    correlation = df_filtered['review_scores_rating'].corr(df_filtered['price'])
    print(f"Correlatie tussen beoordelingen en prijs: {correlation}")

buurtMetMeesteLocaties()
# hoogsteEnLaagstePrijs()
# printAlles("price")
printAlles("neighbourhood_cleansed")
prijsPerBuurt()
zomaarTwee()
hostsMetMeerDanEenListing()
prijsIcmKamerAantal()
corrReviewEnPrijs()