from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
authenticator = IAMAuthenticator('jEo0WFw3q27FAwFV8DzkPs1TjTZWBkyaQzzwB_8MMYmQ')
language_translator = LanguageTranslatorV3(
    version='2021-12-29',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/75e7f08f-1430-4920-9de9-3f9d1ba69228')


""" translate french text to english """
def englishToFrench(englishtext):
    if englishtext is None:
        return None
    frenchtext = language_translator.translate(
        text=englishtext,
        model_id='en-fr'
        ).get_result()
    return frenchtext.get("translations")[0].get("translation")

""" translate french text to english """
def frenchToEnglish(frenchtext):
    if frenchtext is None:
        return None
    englishtext = language_translator.translate(
        text=frenchtext,
        model_id='fr-en'
        ).get_result()
    return englishtext.get("translations")[0].get("translation")
