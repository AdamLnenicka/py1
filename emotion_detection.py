# emotion_detection.py

import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()['text']
    else:
        return "Error: Failed to analyze emotion."

