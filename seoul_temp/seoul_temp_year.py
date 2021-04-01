    import csv
    import matplotlib.pyplot as plt
    import random


    f = open('./seoul.csv')
    data = csv.reader(f)
    next(data)
    result = []
    result2 = []

    for row in data:
        month = row[0].split('-')[0]
        if row[-1] != '':s
            if month == '2002':
                result.append(float(row[-1]))
            if month == '2003':
                result2.append(float(row[-1]))
            



    plt.boxplot(result,result2)
    plt.show()


