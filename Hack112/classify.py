import os
from google.cloud import language_v1beta2
from google.cloud.language_v1beta2 import enums
from google.cloud.language_v1beta2 import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\Eddy Luceddy\\Desktop\\api acc\\My First Project-585014a5278c.JSON"


def classify(text):
    language_client = language_v1beta2.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT
    )
    result = language_client.classify_text(document)
    newsConfidence = None
    for category in result.categories:
        #print("Hi")
        #print(category.name)
        if "/News" in category.name:
            newsConfidence = category.confidence
            break
    return newsConfidence
        #print('category name: ', category.name)
        #print('category confidence: ', category.confidence, '\n')
