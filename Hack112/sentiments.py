import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\Eddy Luceddy\\Desktop\\api acc\\My First Project-585014a5278c.JSON"

def sentiment_text(text):
    """Detects sentiment in the text."""
    client = language.LanguageServiceClient()
    """
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    """
    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects sentiment in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    sentiment = client.analyze_sentiment(document).document_sentiment
    #print('Score: {}'.format(sentiment.score))
    #print(sentiment.score)
    return sentiment.score
    #print('Magnitude: {}'.format(sentiment.magnitude))

