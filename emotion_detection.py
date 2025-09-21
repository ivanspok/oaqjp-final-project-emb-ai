import requests

def emotion_detector(text_to_analyze):
    emotions = {}
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=header, json=payload)
    
    if response.status_code == 200:
        res = response.json()
        anger_score = res['emotionPredictions'][0]['emotion']['anger']
        disgust_score = res['emotionPredictions'][0]['emotion']['disgust']
        fear_score = res['emotionPredictions'][0]['emotion']['fear']
        joy_score = res['emotionPredictions'][0]['emotion']['joy']
        sadness_score = res['emotionPredictions'][0]['emotion']['sadness']
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        max_value = -9999
        for key, value in emotions.items():
            if value > max_value:
                max_value = value
                dominant_emotion = key
        emotions['dominant_emotion'] = dominant_emotion        
    return emotions




