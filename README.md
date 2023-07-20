# word-generator
Simple Python word generator script made for my brother

## Description  
**🌐 word_generator.py**  
The script takes characters provided by the user and generates all possible permutations and combinations of those characters. It creates word combinations considering from a single character up to the entirety of the input. The results are saved into two text files: one contains the words with each character enclosed in brackets "【】", while the other has just the plain words.

**🌐 word_generator2.py**  
This script prompts the user for the number of word groups and the words in each group. Then, it picks one word from each group to generate all possible combinations and permutations of those words. The generated words range in length from 2 to 6 characters. The constructed words are saved into a text file. The program iterates through the combinations up to three times to avoid infinite looping.

**🌐 word_generator3.py**  
This script prompts the user for the number of word groups and the words in each group. Each group should consist of 8 words, where the first 4 words and the next 4 words are paired to form 4 new groups.

Subsequently, the word combinations and permutations are formed from these word groups. The script picks one word from each group to generate all possible combinations and permutations of those words. The generated words range in length from 2 to the number of groups the user has inputted.

Since it's picking from 4 different groups, the iteration happens a maximum of 2 times, meaning you can choose one word out of the two available in each group.

Finally, the constructed words are saved into a text file and the program prompts the user to exit

## 설명  
**🌐 word_generator.py**  
사용자로부터 입력받은 문자들을 기반으로, 그 문자들의 모든 순열과 조합을 생성합니다. 1개의 문자부터 입력받은 문자 전체까지의 조합을 고려하여 가능한 모든 단어 조합을 생성하며, 이 결과를 두 개의 텍스트 파일에 저장합니다. 하나의 파일에는 각 문자를 괄호 "【】"로 감싼 결과가 저장되며, 다른 파일에는 괄호 없이 문자열만 저장됩니다.

**🌐 word_generator2.py**  
이 스크립트는 사용자로부터 단어 그룹의 수와 각 그룹의 단어들을 입력받습니다. 그런 다음, 각 그룹으로부터 하나씩 단어를 선택하여 그 단어들의 모든 가능한 조합과 순열을 생성합니다. 이렇게 생성된 단어들은 2개에서 6개까지의 길이를 가집니다. 그렇게 생성된 단어들은 텍스트 파일에 저장됩니다. 이 프로그램은 무한 루프를 피하기 위해 3번 동안 조합을 반복하고 종료됩니다.

**🌐 word_generator3.py**  
이 스크립트는 사용자로부터 단어 그룹의 수와 각 그룹의 단어들을 입력받습니다. 각 그룹에는 8개의 단어가 있어야 합니다. 첫 4개의 단어와 다음 4개의 단어가 쌍을 이루어 4개의 새로운 그룹에 추가됩니다.

이후에는 단어 그룹에서 단어의 조합과 순열을 생성합니다. 이 스크립트는 각 그룹으로부터 단어를 선택하고, 그 단어들의 모든 가능한 조합과 순열을 생성합니다. 이렇게 생성된 단어들의 길이는 2개에서 사용자가 입력한 그룹의 수까지의 길이를 가집니다.

조합을 생성할 때 4개의 서로 다른 그룹으로부터 선택하므로, 최대 2번의 반복이 가능합니다. 즉, 각 그룹에서 두 단어 중 하나를 선택할 수 있습니다.

마지막으로 생성된 단어들을 텍스트 파일에 저장하고 프로그램을 종료합니다.

.
