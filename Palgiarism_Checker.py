from difflib import SequenceMatcher

with open('C:\\Users\\User\\Desktop\\adapter.txt') as file_1,open('C:\\Users\\User\\Desktop\\add.txt') as file_2:
   file_1_data = file_1.read()
   file_2_data = file_2.read()
   similarity = SequenceMatcher(None,file_1_data,file_2_data).ratio()
   print(similarity*100)
