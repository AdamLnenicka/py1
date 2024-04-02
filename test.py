from EmotionDetection import emotion_detector

# Test with non-blank entry
result1 = emotion_detector("I am happy")
print(result1)  # Expected: Emotions detected

# Test with blank entry
result2 = emotion_detector("")
print(result2)  # Expected: Emotions set to None
