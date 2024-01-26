import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    # Fungsi untuk membersihkan dan memproses teks
    cleaned_text = ''.join(e.lower() for e in text if e.isalnum() or e.isspace())
    return cleaned_text

def search_hadith(query):
    # List untuk menyimpan hasil pencarian
    search_results = []

    # Nama file basis data hadis yang baru
    base_path = "db/"
    hadith_databases = [f"{base_path}{database}" for database in ["abu-daud.json", "ahmad.json", "bukhari.json", "darimi.json", "ibnu-majah.json", "malik.json", "muslim.json", "nasai.json", "tirmidzi.json"]]

    # Ekstrak kata kunci dari query
    query_keywords = preprocess_text(query)

    # Membangun corpus dari teks hadis
    corpus = []
    hadith_data_list = []

    for database in hadith_databases:
        with open(database, 'r', encoding='utf-8') as file:
            hadith_data = json.load(file)
            hadith_data_list.append(hadith_data)
            for hadith in hadith_data:
                corpus.append(preprocess_text(hadith["id"]))

    if not corpus:
        print("No hadith data found.")
        return

    # Menambahkan query ke dalam corpus
    corpus.append(query_keywords)

    # Menggunakan TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Menghitung cosine similarity antara query dan teks hadis
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    # Menyimpan hasil dengan similarity score di atas batas tertentu (misalnya 0.2)
    for query_idx, score in enumerate(similarity_scores[0]):
        for hadith_idx, _ in enumerate(hadith_data_list):
            if score > 0.5 and query_idx < len(hadith_data_list[hadith_idx]):
                search_results.append({
                    "file": hadith_databases[hadith_idx],
                    "hadith": hadith_data_list[hadith_idx][query_idx],
                    "similarity_score": score
                })

    # Menampilkan hasil pencarian
    # for result in search_results:
    #     print(f"File: {result['file'].split('/')[-1].split('.')[0]}")
    #     print(json.dumps(result['hadith'], ensure_ascii=False, indent=2))
    #     print(f"Similarity Score: {result['similarity_score']}")
    #     print("\n" + "-"*50 + "\n")

    return search_results

# Contoh penggunaan
search_hadith("telah menceritakan kepada [Abdul Aziz yakni bin Muhammad]")
