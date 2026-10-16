import unittest
from unittest.mock import patch, Mock

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test the emotion detector for all five emotions."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_anger(self, mock_post):
        self.check_emotion(mock_post, "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_disgust(self, mock_post):
        self.check_emotion(mock_post, "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_fear(self, mock_post):
        self.check_emotion(mock_post, "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_joy(self, mock_post):
        self.check_emotion(mock_post, "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_sadness(self, mock_post):
        self.check_emotion(mock_post, "sadness")

    def check_emotion(self, mock_post, dominant):
        """Mock the API response and verify the dominant emotion."""
        scores = {
            "anger": 0.1,
            "disgust": 0.1,
            "fear": 0.1,
            "joy": 0.1,
            "sadness": 0.1,
        }
        scores[dominant] = 0.9

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {"emotion": scores}
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("This is a test sentence.")

        self.assertEqual(result["dominant_emotion"], dominant)
        for emotion in scores:
            self.assertEqual(result[emotion], scores[emotion])


if __name__ == "__main__":
    unittest.main()
