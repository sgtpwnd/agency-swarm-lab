from agency_swarm.tools import BaseTool
from pydantic import Field
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure that the necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('vader_lexicon')

class NltkTextAnalysis(BaseTool):
    """
    This tool utilizes the Natural Language Toolkit (NLTK) to analyze and process text.
    It is capable of tokenization, stemming, and sentiment analysis to interpret user inputs effectively.
    """

    text: str = Field(
        ..., description="The input text to be analyzed."
    )

    def run(self):
        """
        Executes the text analysis using NLTK, performing tokenization, stemming, and sentiment analysis.
        """
        # Tokenization
        tokens = word_tokenize(self.text)

        # Stemming
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(token) for token in tokens]

        # Sentiment Analysis
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(self.text)

        # Compile results
        analysis_results = {
            'tokens': tokens,
            'stemmed_tokens': stemmed_tokens,
            'sentiment': sentiment
        }

        return analysis_results

# Example usage:
# tool = NltkTextAnalysis(text="I love natural language processing.")
# result = tool.run()
# print(result)