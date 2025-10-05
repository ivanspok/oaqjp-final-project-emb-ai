from emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotions(self):
        statements = [
        'I am glad this happend',
        'I am really mad about this',
        'I feel disgusted just hearing about this',
        'I am so sad about this',
        'I am really afraid that this will happen'
        ]
        expected_results = [
        'joy',
        'anger',
        'disgust',
        'sadness',
        'fear']
        for statement, expected_result in zip(statements, expected_results):
            result = emotion_detector(statement)['dominant_emotion']
            self.assertEqual(result, expected_result)
if __name__ == "__main__":
    unittest.main()