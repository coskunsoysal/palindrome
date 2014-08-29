__author__ = 'coskun.soysal'

import sys
from collections import defaultdict

class Palindrome(object):

    """
    Check all palindrome words in a file
    """

    def __init__(self):
        """
        Initilaze method
        :return:
        """
        self._DEFAULT_FILE = "wordsEn.txt"
        self.result = ""

    def main(self):
        """
         Main method of palindrome class
        :return:
        """
        file = raw_input("Enter file name: ") or self._DEFAULT_FILE
        self.file = file
        list_of_words = self.file2words(self.file)

        count = 0
        for word in list_of_words:
            if self.is_palindrome_of(word):
                self.result += "".join([str(count), "   ", word, "   ", word[::-1], "\n"])
                print "".join([str(count), "   ", word, "   ", word[::-1], "\n"])
                count += 1

        del list_of_words

        self.write_to_file("result.txt",self.result)

    def file2words(self, file='wordEn.txt'):
        """
        Convert txt file to list of words
        :param file: Input file for given word list
        :return: list of given words
        """
        try:
            with open(file, 'r') as f:
                ret = []
                for line in f:
                    ret += line.split()
                return ret
        except IOError:
            print "%s is not a valid file." % file
            sys.exit()

    def is_palindrome_of(self, word):
        """
        Compare two words for palindrome test
        :param word1:
        :param word2:
        :return: True or False if they are palindrome
        """
        return word == word[::-1]

    def write_to_file(self, filename, palindromes):
        """
        Write palindrome words to file
        :param filename: Output file
        :param palindromes: Palindrome string
        :return:
        """
        f = open(filename, "w")
        f.write(palindromes)
        f.close()

Palindrome().main()