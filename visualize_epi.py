import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("epi_raw.csv")
df['ts'] = pd.to_datetime(df['ts'])

# ---- 1. Epidemic curve (cases per day)
daily = df.groupby(df['ts'].dt.date).size()

plt.figure()
plt.plot(daily.index, daily.values)
plt.title("Epidemic Curve (Cases per Day)")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.xticks(rotation=45)
plt.show()


# ---- 2. Cases by location
loc = df['location'].value_counts()

plt.figure()
plt.bar(loc.index, loc.values)
plt.title("Cases by Location")
plt.xlabel("City")
plt.ylabel("Cases")
plt.show()


# ---- 3. Vaccinated vs Unvaccinated
vax = df['vaccinated'].value_counts()

plt.figure()
plt.bar(["Vaccinated", "Unvaccinated"], vax.values)
plt.title("Vaccination Status Distribution")
plt.ylabel("Cases")
plt.show()


# ---- 4. Age distribution
plt.figure()
plt.hist(df['age'], bins=10)
plt.title("Age Distribution of Cases")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
