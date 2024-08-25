import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.util import ngrams
from collections import Counter
import math
import csv
import re  # Added for readability analysis
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

def extract_keywords(text, ngram_range=(1, 2)):
    """Extracts keywords and n-grams from text using NLTK, focusing on meaningful words."""
    stop_words = set(stopwords.words('english'))

    # Extend the stopwords list with additional common words that are not useful in a resume context
    additional_stopwords = {'may', 'might', 'also', 'many', 'can', 'will', 'us', 'one', 'new', 'like', 'related', 'works'}
    stop_words.update(additional_stopwords)

    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    
    # POS tagging to focus on nouns, adjectives, and verbs
    pos_tags = pos_tag(words)
    filtered_words = [word for word, tag in pos_tags if word not in stop_words and len(word) > 2 and (tag.startswith('NN') or tag.startswith('VB') or tag.startswith('JJ'))]

    ngram_keywords = []
    for n in range(ngram_range[0], ngram_range[1] + 1):
        ngram_keywords.extend([' '.join(grams) for grams in ngrams(filtered_words, n)])
    
    return ngram_keywords

def compute_tf(keywords):
    """Computes term frequency for each keyword."""
    tf = Counter(keywords)
    total_keywords = len(keywords)
    tf = {word: count / total_keywords for word, count in tf.items()}
    return tf

def compute_idf(job_description_keywords, resume_keywords):
    """Computes inverse document frequency for each keyword."""
    all_keywords = set(job_description_keywords + resume_keywords)
    num_docs = 2  # We have two 'documents': job description and resume
    
    idf = {}
    for keyword in all_keywords:
        count = sum(1 for doc in [job_description_keywords, resume_keywords] if keyword in doc)
        idf[keyword] = math.log((num_docs + 1) / (1 + count)) + 1  # Smoothing to prevent division by zero
    return idf

def compute_tfidf(tf, idf):
    """Computes TF-IDF score for each keyword."""
    tfidf = {word: tf[word] * idf[word] for word in tf}
    return tfidf

def calculate_similarity(job_description_keywords, resume_keywords):
    """Calculates the similarity percentage and the number of common words."""
    common_keywords = set(job_description_keywords).intersection(set(resume_keywords))
    similarity_percentage = (len(common_keywords) / len(set(job_description_keywords))) * 100 if job_description_keywords else 0
    return similarity_percentage, len(common_keywords)

def merge_similar_keywords(recommended_keywords):
    """Merge similar keywords by prioritizing longer n-grams and removing overlaps."""
    merged_keywords = {}
    for keyword, score in sorted(recommended_keywords.items(), key=lambda item: (-len(item[0].split()), item[1]), reverse=True):
        # Add keyword only if it's not a substring of a longer n-gram already in the list
        if not any(keyword in k.split() or k in keyword for k in merged_keywords):
            merged_keywords[keyword] = score
    return merged_keywords

def recommend_keywords_with_weighting(job_description, resume_text):
    """Recommends keywords to add to the resume based on weighted importance."""
    # Adjust ngram_range as needed (e.g., (1, 2) for unigrams and bigrams)
    job_keywords = extract_keywords(job_description, ngram_range=(1, 2))
    resume_keywords = extract_keywords(resume_text, ngram_range=(1, 2))

    print(f"\nAnalysis Report:")
    print(f" - Total Keywords in Job Description: {len(job_keywords)}")
    print(f" - Total Keywords in Resume: {len(resume_keywords)}")
    
    # Compute TF for job description
    tf_job = compute_tf(job_keywords)
    print(f" - Unique Keywords in Job Description: {len(tf_job)}")

    # Compute IDF using both job description and resume
    idf = compute_idf(job_keywords, resume_keywords)
    print(f" - Unique Combined Keywords: {len(idf)}")
    
    # Compute TF-IDF for job description
    tfidf_job = compute_tfidf(tf_job, idf)

    # Recommend missing keywords with high TF-IDF
    missing_keywords = set(job_keywords) - set(resume_keywords)
    print(f" - Missing Keywords in Resume: {len(missing_keywords)}")

    recommended_keywords = {word: tfidf_job[word] for word in missing_keywords if tfidf_job[word] > 0}

    # Merge similar keywords to avoid duplicates
    merged_keywords = merge_similar_keywords(recommended_keywords)
    print(f" - Recommended Keywords Based on TF-IDF (after merging similar keywords): {len(merged_keywords)}")
    
    # Sort by TF-IDF score in descending order
    sorted_recommended_keywords = sorted(merged_keywords.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_recommended_keywords

def provide_contextual_advice(keywords):
    """Provides advice on how to incorporate keywords in context."""
    print("\n=== Keyword Implementation Advice ===")
    for keyword, score in keywords:
        print(f"Keyword: {keyword}")
        if "risk" in keyword or "management" in keyword:
            print(" - Consider mentioning this keyword in the context of project management, risk assessment, or financial analysis.")
        elif "support" in keyword:
            print(" - Use this keyword in a context where you provided technical, managerial, or operational support.")
        elif "development" in keyword or "programs" in keyword:
            print(" - Discuss training programs or career development initiatives you were involved in.")
        else:
            print(" - Use this keyword naturally in sentences that reflect your skills and experience.")
        print()

def readability_analysis(text):
    """Analyzes the resume text for readability using Flesch-Kincaid formulas."""
    sentences = re.split(r'[.!?]', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    words = word_tokenize(text)
    words = [word for word in words if word.isalpha()]

    total_words = len(words)
    total_sentences = len(sentences)
    avg_sentence_length = total_words / total_sentences if total_sentences > 0 else 0

    syllable_count = sum([count_syllables(word) for word in words])

    flesch_reading_ease = 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (syllable_count / total_words)
    flesch_kincaid_grade = 0.39 * (total_words / total_sentences) + 11.8 * (syllable_count / total_words) - 15.59

    print("\n=== Readability Analysis ===")
    print(f"Total Words: {total_words}")
    print(f"Total Sentences: {total_sentences}")
    print(f"Average Sentence Length: {avg_sentence_length:.2f} words")
    print(f"Flesch Reading Ease: {flesch_reading_ease:.2f}")
    print(f"Flesch-Kincaid Grade Level: {flesch_kincaid_grade:.2f}")

def count_syllables(word):
    """A basic syllable counter function."""
    word = word.lower()
    syllables = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        syllables += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syllables += 1
    if word.endswith("e"):
        syllables -= 1
    if syllables == 0:
        syllables += 1
    return syllables

def skill_gap_analysis(job_description, resume_text):
    """Identifies skills missing from the resume that are frequently required in job descriptions."""
    common_skills = {"communication", "teamwork", "problem-solving", "adaptability", "critical thinking", "leadership", "time management", "project management", "data analysis", "risk management", "customer service", "presentation", "data visualization"}
    job_skills = extract_keywords(job_description, ngram_range=(1, 2))
    resume_skills = extract_keywords(resume_text, ngram_range=(1, 2))

    missing_skills = common_skills - set(resume_skills)
    matched_skills = common_skills & set(job_skills)

    print("\n=== Skill Gap Analysis ===")
    print("Skills missing in your resume that are mentioned in job descriptions: " + ", ".join(missing_skills.intersection(matched_skills)))

def main():
    # Hide Tkinter root window
    Tk().withdraw()

    # Open file dialog to select CSV file
    print("Select the CSV file containing job descriptions:")
    csv_file_path = askopenfilename(filetypes=[("CSV files", "*.csv")])

    # Open file dialog to select PDF resume file
    print("Select your resume PDF file:")
    resume_pdf_path = askopenfilename(filetypes=[("PDF files", "*.pdf")])

    combined_job_description_csv = ""

    # Read job descriptions from CSV file
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Use DictReader to read CSV rows as dictionaries
        for row in reader:
            # Access the 'Job Description' column for each row and concatenate the descriptions
            combined_job_description_csv += " " + row['Job Description']  # Adjust this to match the exact column name in your CSV file
    
    # Use the combined job description from the CSV for analysis
    combined_job_description = combined_job_description_csv

    # Extract text from your resume
    resume_text = extract_text_from_pdf(resume_pdf_path)

    # Extract keywords from combined job descriptions and resume text
    job_keywords = extract_keywords(combined_job_description, ngram_range=(1, 2))
    resume_keywords = extract_keywords(resume_text, ngram_range=(1, 2))
    
    # Calculate similarity between resume and job descriptions
    similarity_percentage, common_word_count = calculate_similarity(job_keywords, resume_keywords)
    
    print("\n=== Similarity Analysis ===")
    print(f"Similarity between resume and job description: {similarity_percentage:.2f}%")
    print(f"Number of common keywords: {common_word_count}")
    
    # Recommend keywords to add to the resume with weighting
    recommended_keywords = recommend_keywords_with_weighting(combined_job_description, resume_text)
    
    print("\n=== Recommended Keywords to Add ===")
    if recommended_keywords:
        print("Top keywords to consider adding to your resume:")
        for keyword, score in recommended_keywords[:10]:  # Limit to top 10 keywords for clarity
            print(f" - {keyword}: {score:.4f}")
        # Provide advice on how to implement keywords
        provide_contextual_advice(recommended_keywords[:10])
    else:
        print("No additional keywords to recommend.")
    
    # Readability Analysis
    readability_analysis(resume_text)

    # Skill Gap Analysis
    skill_gap_analysis(combined_job_description, resume_text)

if __name__ == "__main__":
    main()