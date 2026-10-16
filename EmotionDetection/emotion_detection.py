
import requests


def emotion_detector(text_to_analyze):
    """Detect emotions and return formatted scores."""
    if not text_to_analyze or not text_to_analyze.strip():
        return None

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json={"raw_document": {"text": text_to_analyze}},
            timeout=15
        )

        if response.status_code == 400:
            return None

        response.raise_for_status()
        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]

        result = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
        }

        result["dominant_emotion"] = max(
            emotions, key=emotions.get
        )
        return result

    except (requests.RequestException, ValueError, KeyError, IndexError):
        return None
