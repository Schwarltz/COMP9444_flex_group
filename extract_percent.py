import re

def extractPercent(s):
  lst = s.split('\n')
  epochs = []
  trains = []
  tests = []
  print("Epoch Train Test")
  for line in lst:
    pattern = r"For epoch (\d+) the train accuracy is (\d+) % the test accuracy over the whole test set is (\d+) %"
    result = re.match(pattern, line)
    if result is not None:
      (epoch, train_acc, test_acc) = result.groups()
      print(epoch.ljust(6) + train_acc.ljust(6) + test_acc.ljust(4) )
      epochs.append(epoch)
      trains.append(train_acc)
      tests.append(test_acc)
  
  print("Transposed")
  print("Epochs:")
  print(epochs)
  print("Trains:")
  print(trains)
  print("Tests:")
  print(tests)






str_input = """
The model will be running on cuda:0 device
For epoch 1 the train accuracy is 30 % the test accuracy over the whole test set is 30 %
For epoch 2 the train accuracy is 45 % the test accuracy over the whole test set is 46 %
For epoch 3 the train accuracy is 47 % the test accuracy over the whole test set is 48 %
For epoch 4 the train accuracy is 53 % the test accuracy over the whole test set is 52 %
For epoch 5 the train accuracy is 58 % the test accuracy over the whole test set is 58 %
For epoch 6 the train accuracy is 56 % the test accuracy over the whole test set is 54 %
For epoch 7 the train accuracy is 63 % the test accuracy over the whole test set is 63 %
For epoch 8 the train accuracy is 68 % the test accuracy over the whole test set is 67 %
For epoch 9 the train accuracy is 66 % the test accuracy over the whole test set is 64 %
For epoch 10 the train accuracy is 63 % the test accuracy over the whole test set is 62 %
For epoch 11 the train accuracy is 70 % the test accuracy over the whole test set is 69 %
For epoch 12 the train accuracy is 70 % the test accuracy over the whole test set is 68 %
For epoch 13 the train accuracy is 74 % the test accuracy over the whole test set is 72 %
For epoch 14 the train accuracy is 75 % the test accuracy over the whole test set is 73 %
For epoch 15 the train accuracy is 73 % the test accuracy over the whole test set is 71 %
For epoch 16 the train accuracy is 74 % the test accuracy over the whole test set is 72 %
For epoch 17 the train accuracy is 78 % the test accuracy over the whole test set is 75 %
For epoch 18 the train accuracy is 78 % the test accuracy over the whole test set is 76 %
For epoch 19 the train accuracy is 80 % the test accuracy over the whole test set is 76 %
For epoch 20 the train accuracy is 80 % the test accuracy over the whole test set is 76 %
For epoch 21 the train accuracy is 81 % the test accuracy over the whole test set is 77 %
For epoch 22 the train accuracy is 81 % the test accuracy over the whole test set is 78 %
For epoch 23 the train accuracy is 83 % the test accuracy over the whole test set is 78 %
For epoch 24 the train accuracy is 84 % the test accuracy over the whole test set is 81 %
For epoch 25 the train accuracy is 83 % the test accuracy over the whole test set is 79 %
For epoch 26 the train accuracy is 85 % the test accuracy over the whole test set is 79 %
For epoch 27 the train accuracy is 84 % the test accuracy over the whole test set is 79 %
For epoch 28 the train accuracy is 85 % the test accuracy over the whole test set is 81 %
For epoch 29 the train accuracy is 86 % the test accuracy over the whole test set is 81 %
For epoch 30 the train accuracy is 86 % the test accuracy over the whole test set is 80 %
For epoch 31 the train accuracy is 85 % the test accuracy over the whole test set is 79 %
For epoch 32 the train accuracy is 88 % the test accuracy over the whole test set is 82 %
For epoch 33 the train accuracy is 87 % the test accuracy over the whole test set is 81 %
For epoch 34 the train accuracy is 88 % the test accuracy over the whole test set is 81 %
For epoch 35 the train accuracy is 88 % the test accuracy over the whole test set is 81 %
For epoch 36 the train accuracy is 88 % the test accuracy over the whole test set is 82 %
For epoch 37 the train accuracy is 90 % the test accuracy over the whole test set is 82 %
For epoch 38 the train accuracy is 88 % the test accuracy over the whole test set is 81 %
For epoch 39 the train accuracy is 90 % the test accuracy over the whole test set is 82 %
For epoch 40 the train accuracy is 89 % the test accuracy over the whole test set is 81 %
For epoch 41 the train accuracy is 90 % the test accuracy over the whole test set is 82 %
For epoch 42 the train accuracy is 90 % the test accuracy over the whole test set is 82 %
For epoch 43 the train accuracy is 91 % the test accuracy over the whole test set is 83 %
For epoch 44 the train accuracy is 92 % the test accuracy over the whole test set is 82 %
For epoch 45 the train accuracy is 89 % the test accuracy over the whole test set is 80 %
For epoch 46 the train accuracy is 92 % the test accuracy over the whole test set is 84 %
For epoch 47 the train accuracy is 92 % the test accuracy over the whole test set is 83 %
For epoch 48 the train accuracy is 92 % the test accuracy over the whole test set is 82 %
"""

if __name__ == '__main__':
  extractPercent(str_input)