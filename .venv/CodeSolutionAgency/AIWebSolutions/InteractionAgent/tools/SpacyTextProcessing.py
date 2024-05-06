from agency_swarm.tools import BaseTool
from pydantic import Field
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

class SpacyTextProcessing(BaseTool):
    """
    This tool harnesses the capabilities of spaCy for advanced text processing including part-of-speech tagging,
    named entity recognition, and dependency parsing. It aids in understanding complex user sentences and feedback.
    """

    text: str = Field(
        ..., description="The input text to be processed."
    )

    def run(self):
        """
        Executes the text processing using spaCy, performing part-of-speech tagging, named entity recognition,
        and dependency parsing.
        """
        # Process the text with spaCy
        doc = nlp(self.text)

        # Part-of-Speech Tagging
        pos_tags = [(token.text, token.pos_) for token in doc]

        # Named Entity Recognition
        entities = [(entity.text, entity.label_) for entity in doc.ents]

        # Dependency Parsing
        dependencies = [(token.text, token.dep_, token.head.text) for token in doc]

        # Compile results
        processing_results = {
            'pos_tags': pos_tags,
            'entities': entities,
            'dependencies': dependencies
        }

        return processing_results

# Example usage:
# tool = SpacyTextProcessing(text="Apple is looking at buying U.K. startup for $1 billion.")
# result = tool.run()
# print(result)