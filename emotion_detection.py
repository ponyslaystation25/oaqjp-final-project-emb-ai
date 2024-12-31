import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)

    if "emotionPredictions" in formatted_response and len(formatted_response["emotionPredictions"]) > 0:
        emotion_data = formatted_response["emotionPredictions"][0].get("emotion", {})
    else:
        raise ValueError("Invalid response structure: 'emotionPredictions' is missing or empty")

    emotions = {
        "anger": emotion_data.get("anger",0),
        "disgust": emotion_data.get("disgust",0),
        "fear": emotion_data.get("fear",0),
        "joy": emotion_data.get("joy",0),
        "sadness": emotion_data.get("sadness",0),

    }

    dominant_emotion = max(emotions, key = emotions.get)

    result = {
        'anger': emotions["anger"],
        'disgust': emotions["disgust"],
        'fear': emotions["fear"],
        'joy': emotions["joy"],
        'sadness': emotions["sadness"],
        'dominant emotion': dominant_emotion,

    }

    return result