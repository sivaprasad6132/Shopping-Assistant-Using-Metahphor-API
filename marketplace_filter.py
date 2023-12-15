from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def user_desired_marketplaces(prompt):
    # Sample list of marketplace urls
    document_list = [
        "www.amazon.com",
        "www2.hm.com",
        "www.zara.com","us.shein.com","www.hollisterco.com","www.walmart.com","www.macys.com","www.target.com","oldnavy.gap.com"
        # Add more marketplaces as needed
    ]

    # Input string for which you want to find similar marketplaces
    input_string = prompt

    # Initialize the TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Vectorize the documents and the input string
    tfidf_matrix = tfidf_vectorizer.fit_transform(document_list + [input_string])

    # Calculate cosine similarities between the input string and documents
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    # Get the indices of the top 1 marketplace with the highest cosine similarity
    top_indices = cosine_similarities.argsort()[0][::-1][:1]

    # Initialize a new list to store the top 1 similar marketplace
    top_similar_documents = []

    # Populate the new list with the top 1 similar marketplace from the original list
    for i in top_indices:
        top_similar_documents.append(document_list[i])
    return top_similar_documents
