import pandas as pd
import matplotlib.pyplot as plt

#a = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
#print(a)
"""линейная диограмма"""
plt.title('Кривая')

week = pd.Series({"12.09": 90, "13.09": 56,
                   "14.09": 23, "14.09": 78, "15.09": 60, "16.09": 70, "17.09": 90})
plt.plot(week)
plt.show()

"""круговая диограмма"""
name = pd.Series({
    "igor": 50,
    "egor": 100,
    "vasa": 150
})

plt.pie(name, labels=name.index)
plt.show()

"""столбчатая диограмма"""
marks = pd.Series({
    "5": 6,
    "4": 17,
    "3": 14,
    "2": 4,
    "1": 1,
})

plt.bar(marks.index, height=marks)
plt.show()




