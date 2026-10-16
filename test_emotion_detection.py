
import unittest
from unittest.mock import patch

from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_joy(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.02,
                    "disgust": 0.01,
                    "fear": 0.03,
                    "joy": 0.90,
                    "sadness": 0.04
                }
            }]
        }

        result = emotion_detector("I am happy")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.90)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_anger(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.80,
                    "disgust": 0.02,
                    "fear": 0.05,
                    "joy": 0.03,
                    "sadness": 0.10
                }
            }]
        }

        result = emotion_detector("I am angry")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_sadness(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.05,
                    "disgust": 0.05,
                    "fear": 0.10,
                    "joy": 0.10,
                    "sadness": 0.70
                }
            }]
        }

        result = emotion_detector("I am sad")
        self.assertEqual(result["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()
