import matplotlib.pyplot as plt
print("Matplotlib imported successfully")
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
print("Seaborn version:", sns.__version__)
data = {
    "Car": ["Audi", "BMW", "Ferrari", "Maclaren"],
    "Year": [2012, 2022, 2019, 2017],
    "Model": [Q7, M8, 812, 712]
}
df = pd.DataFrame(data)
df
df_long = df.melt(id_vars="Car", var_name="Year", value_name="")
sns.barplot(data=df_long, x="Model", y="Year")
plt.title("Years of car released:")
plt.show()
