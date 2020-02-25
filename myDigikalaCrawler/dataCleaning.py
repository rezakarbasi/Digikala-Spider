import pandas as pd
import hazm
import numpy as np
from unidecode import unidecode

maxLenSent = 20


def CleanPersianText(text):
    _normalizer = hazm.Normalizer()
    text = _normalizer.normalize(text)
    return text


data = pd.read_csv('crawled2.csv').astype(str)
# data.loc[0][2].replace(',','')
# float(unidecode(data.loc[0][2]))

out = pd.DataFrame(columns=['comment', 'prod id', 'price',
                            'like', 'dislike', 'date', 'person', 'buyer'])

nameDF = pd.DataFrame(columns=['name', 'id'])
names = [data.values[1, 1]]
price = float(unidecode(data.values[1, 2].replace(',', '')))
nameDF = nameDF.append(
    {'name': names[-1], 'price': price, 'id': 1}, ignore_index=True)

for i in data.values[:]:
    name = i[1]
    price = i[2]
    comment = i[3]
    data_person = i[4]
    likes = i[5]
    disLike = i[6]

    price = float(unidecode(price.replace(',', '')))

    if name != names[-1]:
        names.append(name)
        nameDF = nameDF.append(
            {'name': names[-1], 'price': price, 'id': len(names)}, ignore_index=True)
    name = len(names)

    data_person = data_person.split('\n')
    person = data_person[0]
    buyer = False
    if len(data_person) == 2:
        date = data_person[1]
    elif len(data_person) == 3:
        date = data_person[2]
        buyer = True
    elif len(data_person) == 1:
        date = ''
    else:
        print('-----------new data person----------------')
        print(data_person)

    likes = int(unidecode(likes.replace(',', '')))

    disLike = int(unidecode(disLike.replace(',', '')))

    temp = {'comment': comment, 'prod id': name, 'price': price, 'like': likes,
            'dislike': disLike, 'date': date, 'person': person, 'buyer': buyer}

    for sent in hazm.sent_tokenize(CleanPersianText(comment)):
        comment = hazm.word_tokenize(sent)

        while len(comment) >= maxLenSent:
            temp['comment'] = ' '.join(comment[:maxLenSent])
            comment = comment[(maxLenSent-2):]

            out = out.append(temp, ignore_index=True)
        if len(comment) > 3:
            temp['comment'] = ' '.join(comment)
            out = out.append(temp, ignore_index=True)

out.to_excel('cleaned1.xlsx')
nameDF.to_excel('Prod_spec1.xlsx')
