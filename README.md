# Resume Optimizer: ATS Compatibility, Skill Gap Analysis, and Readability Improvement

## Overview

**Resume Optimizer** is a Python script designed to help you enhance your resume by optimizing it for Applicant Tracking Systems (ATS), performing a skill gap analysis, and improving readability. This tool extracts relevant keywords and skills from multiple job descriptions, compares them against your resume, and provides actionable recommendations to increase your chances of getting noticed by recruiters and hiring managers.

## Features

- **ATS Compatibility Check**: Scans your resume for potential issues that might prevent Applicant Tracking Systems (ATS) from correctly reading and interpreting your information. This feature helps ensure your resume will be seen by recruiters and not filtered out by software.

- **Skill Gap Analysis**: Compares the skills listed in your resume with those frequently required in the job descriptions. It identifies any missing skills that could be crucial for your desired job, enabling you to address these gaps with additional training or by highlighting related experiences.

- **Keyword Recommendation**: Suggests relevant keywords and phrases to add to your resume based on job description analysis. Including these keywords can enhance your resume's relevance and improve its chances of matching the search queries used by recruiters.

- **Readability Analysis**: Evaluates your resume's readability using metrics like Flesch Reading Ease and Flesch-Kincaid Grade Level. This analysis helps ensure that your resume is easy to understand, which can increase the likelihood of it being read fully by recruiters.

### Key Metrics Explained

The tool provides several types of analysis results, some of which are detailed below:

#### Analysis Report

- **Unique Combined Keywords**: This metric represents the total number of distinct keywords found when combining both the job descriptions and your resume. It helps to understand the overlap and variety of keywords between the documents. A higher number indicates a broad range of keywords, while a lower number might suggest a narrow focus.

- **Missing Keywords in Resume**: This number shows how many keywords from the job descriptions are not found in your resume. These missing keywords could represent skills, experiences, or qualifications that you haven’t highlighted but are valuable for the job. Adding these keywords can help align your resume more closely with the job requirements.

- **Recommended Keywords Based on TF-IDF**: TF-IDF (Term Frequency-Inverse Document Frequency) is a statistical measure used to evaluate the importance of a word in a document relative to a set of documents. Here, it identifies which keywords are important across multiple job descriptions and are missing from your resume. This helps prioritize the most critical keywords to include in your resume for better alignment with job postings.

#### Readability Analysis

- **Flesch Reading Ease**: This score measures how easy your resume is to read. A higher score (60-70) indicates that your resume is easier to read, while a lower score suggests more complex text. A negative score, as seen in the example output, indicates very difficult readability, often due to long, complex sentences. You should aim for a score that makes your resume accessible and easy to digest.

- **Flesch-Kincaid Grade Level**: This indicates the education level required to understand your resume. A higher grade level suggests your resume might be too complex, potentially deterring some readers. Ideally, you want a grade level around 8-12, making your resume accessible to a broad audience, including recruiters and hiring managers.

These metrics help ensure that your resume is tailored to meet the specific requirements and preferences of potential employers, increasing your chances of being selected by both ATS systems and human recruiters.

## Installation

Follow these steps to install and run the Resume Optimizer program on your local machine:

### Step-by-Step Installation Guide

1. **Clone the Repository**

   Start by cloning the repository from GitHub to your local machine. Open a terminal or command prompt and run the following commands:

   ```bash
   git clone https://github.com/meeth-shah/resume-analyzer.git
   cd resume-analyzer
   ```
This will download the project files and navigate into the project directory.

2. **Set Up Your Python Environment**

Ensure you have Python 3.6 or later installed on your system. You can download Python from the official Python website.

It's recommended to use a virtual environment to manage your Python dependencies. To create a virtual environment, run:

   ```bash
   python -m venv env
   ```

Activate the virtual environment:
**Windows:**

   ```bash
   .\env\Scripts\activate
   ```

**macOS/Linux:**

   ```bash
   source env/bin/activate
   ```

This step ensures that all Python packages installed will be isolated to this project, avoiding conflicts with other projects on your machine.

**Install Required Python Packages**

Install the necessary Python libraries using pip. This program depends on several packages for its functionality:

   ```bash
   pip install PyPDF2 nltk
   ```

`PyPDF2`: A library used for reading text from PDF files, which is essential for extracting the content of your resume.

`nltk`: The Natural Language Toolkit, used for text processing tasks like tokenization, stopword removal, and part-of-speech tagging.
Download NLTK Data

The program uses NLTK for various natural language processing tasks. You need to download some specific datasets that NLTK uses for processing text. Run the following commands in a Python shell or script:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('averaged_perceptron_tagger')
   ```
`punkt`: A tokenizer that divides text into sentences and words.

`stopwords`: A list of common words (like "the", "is", etc.) that are often removed during text processing.

`averaged_perceptron_tagger`: A part-of-speech tagger, used to assign parts of speech to words in a text, which helps in identifying keywords.
Run the Program

Execute the script to start optimizing your resume. The program will prompt you to select your resume PDF and a CSV file containing job descriptions.

   ```bash
   python resume_analyzer_csv_final.py
   ```

A file dialog will appear allowing you to select the required files:

**Resume PDF**: Select the PDF file of your resume.

**CSV File**: Select the CSV file containing job descriptions (make sure the job descriptions are in a column named "Job Description").

## How to Prepare Your Files for Optimal Results

To get the most out of the Resume Optimizer, there are a few manual steps you'll need to take. This preparation will ensure that the program can analyze your resume effectively and provide meaningful insights.

### 1. Collecting Job Descriptions

For the Resume Optimizer to perform a **Skill Gap Analysis** and recommend relevant keywords, you need to provide a CSV file containing job descriptions of the positions you are targeting. This allows the program to understand what employers are looking for and compare that with the content of your resume.

**Steps to Collect Job Descriptions:**

- **Identify Relevant Job Listings**: Search for job listings that match your desired position or career path. Websites like LinkedIn, Indeed, Glassdoor, and company career pages are good places to start.
- **Copy Job Descriptions**: Manually copy the job descriptions of at least 5-10 job listings. The more job descriptions you include, the better the program can identify common skills and keywords required.
- **Paste into a CSV File**: Open a spreadsheet program like Microsoft Excel or Google Sheets and paste each job description into a new row in a column labeled `Job Description`.

### 2. Preparing the CSV File

Your CSV file should be structured in a way that the program can easily read and process it. Here’s how you should format your CSV file:

**CSV File Format:**

| Job Title           | Company Name     | Job Description                                                              |
|---------------------|------------------|------------------------------------------------------------------------------|
| Data Analyst        | ABC Corp         | Responsible for data analysis, reporting, and visualization using SQL and Python. |
| Business Analyst    | XYZ Inc.         | Analyze business processes and develop strategies for optimization.              |
| Marketing Specialist| Marketing Solutions | Conduct market research and analysis to support marketing strategies.         |

- **Column Names**: Ensure that your CSV file has a column named `Job Description`. This is crucial because the program looks specifically for this column name to extract job descriptions.
- **Data Entry**: Only the text in the `Job Description` column is analyzed. You can add other columns (like `Job Title` and `Company Name`) for your reference, but they are not required for the program to function.
- **Save as CSV**: Once you have pasted all the job descriptions, save the file in CSV format (e.g., `job_data_dump.csv`). 

### 3. Preparing Your Resume

The program requires a PDF version of your resume to analyze it effectively. Follow these guidelines to ensure your resume is ready for analysis:

**Resume Preparation Tips:**

- **Save as PDF**: Make sure your resume is saved as a PDF file. The program cannot read Word documents or other formats.
- **Clear and Simple Formatting**: Use a simple layout with clear section headers (like "Work Experience," "Education," and "Skills"). Avoid using complex formatting like tables or images that might confuse the program.
- **Highlight Key Skills**: Ensure that your resume includes all relevant skills, experiences, and keywords related to the jobs you are applying for. This increases the chance of matching the keywords found in the job descriptions.

### 4. Running the Program

After preparing your CSV file and resume PDF, run the Resume Optimizer program as described in the **Installation** section. The program will prompt you to select the files, analyze them, and provide insights based on the data.

By following these steps and preparing your files carefully, you can maximize the effectiveness of the Resume Optimizer and make your resume stand out to recruiters and hiring managers.

### How to Interpret the Output

1. **Similarity Analysis**: This section shows how well your resume matches the keywords found in job descriptions. A higher similarity percentage means your resume aligns more closely with what employers are looking for. If the similarity percentage is low, consider revising your resume to include more relevant keywords.

   - **Analysis Report**: Provides detailed statistics on keywords from job descriptions compared to those in your resume, including missing keywords. Use this data to identify and add important keywords that could improve your resume’s relevance.

3. **Recommended Keywords to Add**: This section suggests specific keywords to include in your resume to improve its relevance to job descriptions. Incorporate these keywords naturally in your resume where they align with your experience and skills.

4. **Keyword Implementation Advice**: Detailed suggestions on how to integrate recommended keywords effectively into your resume. Use these tips to ensure the keywords enhance your resume without appearing forced or out of context.

5. **Readability Analysis**: This analysis provides metrics on how easy your resume is to read. If your Flesch Reading Ease score is low or the Flesch-Kincaid Grade Level is high, simplify your language and shorten sentences to make your resume more accessible.

6. **Skill Gap Analysis**: Identifies critical skills from job descriptions that are missing from your resume. Address these gaps by highlighting relevant experiences or acquiring new skills to strengthen your resume.

By understanding and applying these insights, you can optimize your resume to be more effective in your job search, improving both ATS compatibility and appeal to recruiters.

## Example Output

   ```yaml
   === Similarity Analysis ===
   Similarity between resume and job description: 4.75%
   Number of common keywords: 114
   
   Analysis Report:
    - Total Keywords in Job Description: 5247
    - Total Keywords in Resume: 567
    - Unique Keywords in Job Description: 2402
    - Unique Combined Keywords: 2771
    - Missing Keywords in Resume: 2288
    - Recommended Keywords Based on TF-IDF (after merging similar keywords): 625
   
   === Recommended Keywords to Add ===
   Top keywords to consider adding to your resume:
    - risk: 0.0086
    - visualization: 0.0067
    - insights: 0.0064
    - external: 0.0048
    - development: 0.0040
    - decision: 0.0038
    - internal: 0.0035
    - technical: 0.0035
    - supports: 0.0035
    - proficiency: 0.0035
   
   === Keyword Implementation Advice ===
   Keyword: risk
    - Consider mentioning this keyword in the context of project management, risk assessment, or financial analysis.
   
   Keyword: visualization
    - Use this keyword naturally in sentences that reflect your skills and experience.
   
   Keyword: insights
    - Use this keyword naturally in sentences that reflect your skills and experience.
   
   Keyword: external
    - Use this keyword naturally in sentences that reflect your skills and experience.
   
   Keyword: development
    - Discuss training programs or career development initiatives you were involved in.
   
   Keyword: decision
    - Use this keyword naturally in sentences that reflect your skills and experience.
   
   Keyword: internal
    - Use this keyword naturally in sentences that reflect your skills and experience.
   
   Keyword: technical
    - Use this keyword naturally in sentences that reflect your skills and experience.
   
   Keyword: supports
    - Use this keyword in a context where you provided technical, managerial, or operational support.
   
   Keyword: proficiency
    - Use this keyword naturally in sentences that reflect your skills and experience.
   
   
   === Readability Analysis ===
   Total Words: 388
   Total Sentences: 8
   Average Sentence Length: 48.50 words
   Flesch Reading Ease: -25.11
   Flesch-Kincaid Grade Level: 28.81
   
   === Skill Gap Analysis ===
   Skills missing in your resume that are mentioned in job descriptions: time management, presentation, customer service, communication, risk management, data visualization
   ```

## License
   This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
   For any questions or suggestions, please open an issue on this GitHub repository or contact me at meeth.shah@outlook.com
