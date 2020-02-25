import pandas as pd
import numpy as np

data = pd.read_excel('cleaned1.xlsx')

fileNum = 20
inEachFile = 200

randIdx = np.random.choice(
    range(len(data)), size=fileNum*inEachFile, replace=False)

while fileNum > 0:
    out = pd.DataFrame(columns=['comment', 'sentiment', 'aspect'])
    for i in randIdx[:inEachFile]:
        out = out.append(
            {'comment': data['comment'][i], 'sentiment': 0, 'aspect': ''}, ignore_index=True)
    out.to_excel('lable-file-%d.xlsx' % (int(fileNum)))
    randIdx=randIdx[inEachFile:]
    fileNum-=1
