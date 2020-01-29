from string import punctuation
import itertools
import math
import sys

class SimilarityScorer:
    """ Class for comparing and scoring 2 different texts
        
        Public Methods:
                create_count_dict -> Creates dictionary for each input text where key is word and value is list of positions it appears in
                compare_texts -> Scores similiarity between 2 texts 
                ** Must run create_count_dict first to score text ** """

    def __init__(self, input_text_1, input_text_2):
        self.length_1 = None
        self.text_1 = input_text_1
        self.word_dict_1 = {}

        self.length_2 = None
        self.text_2 = input_text_2
        self.word_dict_2 = {}


    def create_count_dict(self):
        """Takes each text and creates a dictionary with key as the word and value as a list of positions where the word occurs in the text"""

        # Creates word dictionary for input 1
        text_1_list = self.text_1.strip().split()
        self.length_1 = len(text_1_list)
        for index, word in enumerate(text_1_list):
            clean_word = self.strip_punc(word)
            if clean_word in self.word_dict_1.keys():
                current_index = self.word_dict_1[clean_word]
                current_index.append(index)
                self.word_dict_1[clean_word] = current_index
            else:
                self.word_dict_1[clean_word] = [index]
        
        # Creates word dictionary for input 2
        text_2_list = self.text_2.strip().split()
        self.length_2 = len(text_2_list)
        for index, word in enumerate(text_2_list):
            clean_word = self.strip_punc(word)
            if clean_word in self.word_dict_2.keys():
                current_index = self.word_dict_2[clean_word]
                current_index.append(index)
                self.word_dict_2[clean_word] = current_index
            else:
                self.word_dict_2[clean_word] = [index]


    def strip_punc(self, input_word):
        """ Utility function to strip punctation and convert words to lower case
            Input: word from text
            Return: lowercase and stripped punctiation word """

        punc_table = str.maketrans('','', punctuation)
        return input_word.lower().translate(punc_table)


    def compare_texts(self):
        """ Iterates through both text dictionaries and calls score_text to score each key in dictionary
            Return: Overall Similarity score -> 1 means exact, 0 means nothing in common """

        current_score = 0

        if self.length_1 >= self.length_2:
            longer_text = self.word_dict_1
            longer_length = self.length_1
            shorter_text = self.word_dict_2
        else:
            longer_text = self.word_dict_2
            longer_length = self.length_2
            shorter_text = self.word_dict_1

        # Scores each set of common words between 2 texts
        for key, item in longer_text.items():
            if key in shorter_text.keys():
                current_score += self.__score_text(item, shorter_text[key], longer_length)

        return current_score / longer_length
        

    def __score_text(self, values1, values2, longer_length):
        """ Scores each common word appearing in each text, calls score_words to create similiarity index for same words in different positions
            Inputs: values1 and values2 -> List of positions where commond word appears in each text
                    longer_length -> Overall word count of longer text
            Return: score -> Similarity Score for given common word in texts """

        score = 0

        length1 = len(values1)
        length2 = len(values2)
        
        set1 = set(values1)
        set2 = set(values2)

        # Common words between texts in exact same spot, given score of 1
        common = set1.intersection(set2)
        for value in list(common):
            score += 1
            set1.remove(value)
            set2.remove(value)
        
        diff_list1 = list(set1)
        diff_list2 = list(set2)

        # Common words not in same spot within text, will be assgined similarity index between 0 to 1 (exclusive)
        if length1 >= length2:
            score += self.__score_words(diff_list2, diff_list1, longer_length)
        else:
            score += self.__score_words(diff_list1, diff_list2, longer_length)

        return score


    def __score_words(self, short_list, long_list, overall_length):
        """ Assigns a similiarity index to words that appear in both texts, but not in exact same spot
            Input: short_list -> list of given word positions in text with less occurances of given word
                   long_list -> list of given word positions in text with more occcurances of given word
            Return: score -> Similairity score for common words in different positions between 2 texts """

        score = 0

        # Iterates through list of text postions till empty
        while len(short_list) != 0:
            for item in short_list:
                temp = math.inf
                short_value = None
                long_value = None

                for compare_item in long_list:
                    # Takes similairity between closest together words relative to their position in the text
                    diff = abs(item - compare_item)
                    if diff < temp:
                        temp = diff
                        short_value = item
                        long_value = compare_item

                score += (1 - (diff / overall_length))
                # Removes both indices/positions of text in order to prevent duplication in iteration
                short_list.remove(item)
                long_list.remove(compare_item)

        return score
                
        