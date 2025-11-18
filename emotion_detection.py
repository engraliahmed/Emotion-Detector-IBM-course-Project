import requests
import json


def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion_predictions = formatted_response["emotionPredictions"][0]["emotion"]
        anger = emotion_predictions["anger"]
        disgust = emotion_predictions["disgust"]
        fear = emotion_predictions["fear"]
        joy = emotion_predictions["joy"]
        sadness = emotion_predictions["sadness"]

        emotion_scores = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant_emotion,
        }

    elif response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }