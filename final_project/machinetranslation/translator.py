import os
import json
import ast
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    if english_text is None:
        return None

    french = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_info = json.dumps(french, ensure_ascii=False)
    french_text = ast.literal_eval(french_info)['translations'][0]
    french_text = french_text['translation']

    return french_text

def french_to_english(french_text):
    if french_text is None:
        return None

    english = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    english_info = json.dumps(english, ensure_ascii=False)
    english_text = ast.literal_eval(english_info)['translations'][0]
    english_text = english_text['translation']

    return english_text
