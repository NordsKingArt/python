import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.style.use("fivethirtyeight")


df = pd.read_csv("data.csv")
all_languages = dict()

# Obtaining languages with their popularity
for x in df["LanguagesWorkedWith"]:
    languages = x.split(";")
    for language in languages:
        if language in all_languages:
            all_languages[language]+=1
        else:
            all_languages[language]=0


plt.barh(list(all_languages.keys()), list(all_languages.values()))


plt.xlabel("# of programmers")
plt.tight_layout()
plt.show()