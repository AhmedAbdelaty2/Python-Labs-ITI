from typing import Counter

file_name = input('please enter the file name: ')

f = open(file_name, 'r')
counting = Counter(f.read().lower().split())

f2 = open('popular_words.txt', 'w')
f2.write(str(counting.most_common(20)))