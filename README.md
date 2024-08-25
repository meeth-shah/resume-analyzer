# Resume Optimizer: ATS Compatibility, Skill Gap Analysis, and Readability Improvement

## Overview

**Resume Optimizer** is a Python script designed to help you enhance your resume by optimizing it for Applicant Tracking Systems (ATS), performing a skill gap analysis, and improving readability. This tool extracts relevant keywords and skills from multiple job descriptions, compares them against your resume, and provides actionable recommendations to increase your chances of getting noticed by recruiters and hiring managers.

## Features

- **ATS Compatibility Check**: Identifies potential issues in your resume that may affect its compatibility with Applicant Tracking Systems (ATS).
- **Skill Gap Analysis**: Compares the skills listed in job descriptions with those in your resume and identifies any missing skills that could be critical for your desired job.
- **Keyword Recommendation**: Suggests keywords and phrases to add to your resume based on job description analysis, enhancing your resume's relevance.
- **Readability Analysis**: Evaluates the readability of your resume using metrics like Flesch Reading Ease and Flesch-Kincaid Grade Level to ensure clarity and conciseness.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/resume-optimizer.git
   cd resume-optimizer

2. **Install the Required Python Packages**

   Make sure you have Python installed (version 3.6 or later). Install the required libraries using pip:

   ```bash
   pip install PyPDF2 nltk
   Download NLTK Data
   ```

3. **Run the following Python commands to download the necessary NLTK data**:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('averaged_perceptron_tagger')
   ```

## Usage
1. **Prepare Your Resume and Job Descriptions**

- Save your resume as a PDF file (e.g., Resume.pdf).
- Collect job descriptions relevant to your target position and save them in a CSV file (e.g., job_data_dump.csv). Ensure the job descriptions are in a column named Job Description.
Run the Script

2. **Modify the paths in the script to point to your resume PDF and job descriptions CSV file. Then run the script:**
   ```bash
   python resume_optimizer.py
   ```

## Interpret the Results

- ATS Compatibility Check: Review any potential compatibility issues.
- Skill Gap Analysis: Identify any missing skills and consider adding them to your resume.
- Keyword Recommendation: Add suggested keywords to enhance your resume's relevance to the job descriptions.
- Readability Analysis: Use the readability metrics to ensure your resume is clear and concise.


## Example Output

   After running the script, you might see output like the following:

   ```vbnet
   === Similarity Analysis ===
   Similarity between resume and job description: 4.75%
   Number of common keywords: 114
   
   Analysis Report:
    - Total Keywords in Job Description: 5247
    - Total Keywords in Resume: 567
    - Unique Keywords in Job Description: 2402
    - Unique Combined Keywords: 2771
    - Missing Keywords in Resume: 2288
    - Recommended Keywords Based on TF-IDF (after merging similar keywords): 626
   
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
    - proficiency: 0.0035
    - supports: 0.0035
   
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
   
   Keyword: proficiency
    - Use this keyword naturally in sentences that reflect your skills and experience.
   
   Keyword: supports
    - Use this keyword in a context where you provided technical, managerial, or operational support.
   
   
   === Readability Analysis ===
   Total Words: 388
   Total Sentences: 8
   Average Sentence Length: 48.50 words
   Flesch Reading Ease: -25.11
   Flesch-Kincaid Grade Level: 28.81
   
   === Skill Gap Analysis ===
   Skills missing in your resume that are mentioned in job descriptions: data visualization, customer service, time management, communication, risk management, presentation
   ```

## License
   This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
   For any questions or suggestions, please open an issue on this GitHub repository or contact me at meeth.shah@outlook.com
