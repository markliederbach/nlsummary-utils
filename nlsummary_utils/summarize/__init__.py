import re
import nltk
import heapq

class Summary:

    def __init__(self, text, language=None, max_sentence_length=30):
        self.text = text
        self.language = language or "english"
        self.max_sentence_length = max_sentence_length

    def get_summary(self, top_sentences=2):
        """
        Provide a transformed list of string representing the top n sentences from the text blob.
        Args:
            top_sentences (int): Number of sentences to return

        Returns:
            list(str): List of the top n sentences.
        """
        sentence_frequencies = self.get_weighted_sentence_frequencies()
        return heapq.nlargest(
            top_sentences,
            sentence_frequencies,
            key=sentence_frequencies.get
        )

    def _tokenize_text(self, text):
        return nltk.sent_tokenize(self._tokenizable_text(text))

    def _get_stopwords(self, language):
        return nltk.corpus.stopwords.words(language)

    def _tokenizable_text(self, text):
        return re.sub(r"\s+", " ", text)

    def _clean_special_characters(self, text):
        formatted_text = re.sub(r"[^a-zA-Z]", " ", text)
        return self._tokenizable_text(formatted_text)

    def get_word_frequencies(self, text, language):
        word_frequencies = {}
        for word in nltk.word_tokenize(self._clean_special_characters(text)):
            if word not in self._get_stopwords(language):
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
        return word_frequencies

    def get_weighted_word_frequencies(self, text, language):
        word_frequencies = self.get_word_frequencies(text, language)
        maximum_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word] / maximum_frequency)
        return word_frequencies

    def get_weighted_sentence_frequencies(self):
        sentence_scores = {}
        word_frequencies = self.get_weighted_word_frequencies(self.text, self.language)
        sentence_list = self._tokenize_text(self.text)
        for sentence in sentence_list:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in word_frequencies.keys():
                    if len(sentence.split(" ")) <= self.max_sentence_length:
                        if sentence not in sentence_scores.keys():
                            sentence_scores[sentence] = word_frequencies[word]
                        else:
                            sentence_scores[sentence] += word_frequencies[word]
        return sentence_scores


