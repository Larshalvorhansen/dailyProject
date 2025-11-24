# Todo:
# [x] Create a program that analyzes text files to find word frequency distributions
# [x] and export results to CSV.
# [x] Include functionality to find the most common words and basic statistics.

import csv


def makeOccuranceDict(text):
    text = text.lower()
    words = text.split()
    occuranceDict = {}
    # print(words)
    for word in words:
        instance = words.count(word)
        occuranceDict[word] = instance
    return occuranceDict


def dict2csv(dict):
    with open("occs.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for x, y in dict.items():
            # print(x, y)
            writer.writerow([x, y])
    return 0


def countWords(text):
    text = text.lower()
    words = text.split()
    return len(words)


def getMostCommonWord(text):
    occDict = makeOccuranceDict(text)
    largestOcc = 0
    word = "none"
    for x, y in occDict.items():
        if y > largestOcc:
            largestOcc = y
            word = x
    return (word, largestOcc)


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur eu rutrum odio. Curabitur ut lacus urna. Nulla facilisi. Mauris bibendum non nisl pretium aliquet. Proin maximus cursus tellus varius pulvinar. Sed dolor elit, rhoncus sed aliquam eu, dictum eget ante. Aenean congue, nisi nec luctus aliquet, lacus arcu gravida est, id tempus ante quam sed metus. Duis ut arcu placerat, volutpat mauris sed, congue nibh. Praesent a magna vel nibh laoreet semper vel et tellus. Vivamus sollicitudin dui id nisl rhoncus sollicitudin. Suspendisse et condimentum ipsum, ut iaculis ipsum. Aenean at magna ex. Nunc sit amet sapien id odio aliquam finibus. Aenean in tortor nec libero mollis ultrices. Etiam luctus gravida posuere. Nunc tristique, purus sed imperdiet tincidunt, odio eros ultrices quam, in aliquet dolor nulla vitae enim. Maecenas mollis mi ac luctus gravida. Suspendisse eget velit pharetra, iaculis metus a, placerat felis. Suspendisse in ornare quam. Vestibulum ut dictum tellus. Duis ex dui, lacinia sit amet justo vitae, faucibus bibendum nunc. Quisque a elementum erat, in semper nibh. In hac habitasse platea dictumst. Donec dictum viverra orci ac posuere. In sit amet purus sit amet urna faucibus egestas sed in nulla. Nulla id lacus in diam facilisis fringilla quis in risus. Nulla facilisis elit urna, sed dictum enim rutrum at. Etiam et ornare purus. Pellentesque non neque sed ligula tincidunt accumsan. Nam vitae lectus risus. Integer nunc elit, blandit sit amet aliquam sed, rutrum id risus. Sed ut sem non velit consequat feugiat tempor ac sapien. Vivamus porta pharetra mollis. Vivamus fringilla sodales nunc. Duis in tempor purus. Aenean interdum quis lectus ut facilisis. Ut convallis ante nunc, at lacinia felis tincidunt eu. Vestibulum ac dui mauris. Sed auctor ultrices risus, at convallis tortor malesuada a. Quisque condimentum eu odio sodales congue. Nam quis fringilla lectus. Nunc eu nunc sollicitudin, consequat magna ut, tristique ligula. Morbi id bibendum sapien. Vestibulum convallis metus finibus quam congue dapibus. Vivamus dictum aliquam rutrum. Etiam dictum varius tellus vel suscipit. Donec pellentesque, lectus vel vestibulum suscipit, nisl metus suscipit nisl, quis mollis nunc purus eget dui. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Duis fermentum faucibus velit et aliquet. Aliquam egestas erat leo, a consectetur mauris facilisis mattis. Aliquam sed quam cursus, sollicitudin mauris et, ullamcorper urna. Integer venenatis sit amet nisl eget gravida. Integer tincidunt, tortor eu molestie semper, erat quam pharetra sem, in tincidunt lacus nulla nec massa. Cras tempor dolor sed velit semper, vitae malesuada velit eleifend. Aenean sagittis sodales urna sed feugiat. Vivamus interdum nisi ut dui sodales maximus. Cras sapien nisi, euismod vitae sapien ut, hendrerit posuere augue. Donec blandit ut elit at convallis. Suspendisse ornare eros et velit interdum, varius consectetur risus facilisis. Donec pretium auctor tortor ultrices suscipit. Duis facilisis massa ipsum, euismod blandit mi fermentum in. Nullam volutpat lacus a odio tempor lacinia. "

# Testing functionality
print(makeOccuranceDict(text))
dict2csv(makeOccuranceDict(text))
print(countWords(text))
print(getMostCommonWord(text))
