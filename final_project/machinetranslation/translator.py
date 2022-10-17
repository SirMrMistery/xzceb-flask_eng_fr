#import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-08-05',
    authenticator=authenticator)

language_translator.set_service_url(url)

def englishtofrench(englishtext):
    frenchtext = language_translator.translate(
        text=englishtext,
        model_id="en-fr"
    ).get_result()
    return frenchtext


def frenchtoenglish(frenchtext):
    englishtext = language_translator.translate(
        text=frenchtext,
        model_id="fr-en"
    ).get_result()
    return englishtext