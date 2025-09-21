import requests

def emotion_detector(text_to_analyze):
    emotions = {}
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=header, json=payload)

    return response.text



















        # if response.status_code == '200':
    #     res = response.json

    #     emotions = {
    #         'anger': anger_score,
    #         'disgust': disgust_score,
    #         'fear': fear_score,
    #         'joy': joy_score,
    #         'sadness': sadness_score,
    #         'dominant_emotion': '<name of the dominant emotion>'
    #     }