import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Chargement des données
df = pd.read_csv("C:xxx/raceranger_final_parsed - raceranger_final_parsed.csv")

# Fonction pour convertir un temps mm:ss en secondes
def time_to_seconds(t):
    if pd.isna(t) or t == '':
        return 0
    try:
        mins, secs = str(t).split(':')
        return int(mins) * 60 + int(secs)
    except:
        return 0

# Nettoyage des noms de colonnes
df.columns = [col.strip().replace('\n', ' ').replace('\r', '').replace('  ', ' ') for col in df.columns]

# Nettoyage du champ Finish Position pour être sûr que c’est un nombre
df['Finish Position'] = pd.to_numeric(df['Finish Position'], errors='coerce')

# Conversion des temps en secondes
df['Total Illegal Time (s)'] = df['Total Illegal Time'].apply(time_to_seconds)
df['Favourite Wheel Illegal Time (s)'] = df['Favourite Wheel Illegal Time'].apply(time_to_seconds)

# Filtrer le top 10 du classement final
df_top10 = df.sort_values(by='Finish Position').dropna(subset=['Finish Position']).head(10)

# ==============================
# 1. Scatter Plot (Top 10 classements)
# ==============================

df_filtered = df_top10[['Athlete Name', 'Total Illegal Time (s)', 'Overtakes', 'Sexe']].dropna()

sexes = df_filtered['Sexe'].unique()
for sexe in sexes:
    subset = df_filtered[df_filtered['Sexe'] == sexe]
    if subset.empty:
        continue
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=subset, x='Overtakes', y='Total Illegal Time (s)', hue='Athlete Name', palette='tab10', legend=False)
    plt.title(f'Top 10 finishers - Total Illegal Time vs Overtakes - Sexe: {sexe}')
    plt.xlabel('Overtakes')
    plt.ylabel('Total Illegal Time (s)')
    for _, row in subset.iterrows():
        plt.annotate(row['Athlete Name'], (row['Overtakes'], row['Total Illegal Time (s)']), fontsize=8, alpha=0.6)
    plt.tight_layout()
    plt.show()

# ==================================
# 2. Bar chart des duos (Top 10 finishers)
# ==================================

# On garde uniquement les duos où l’athlète suiveur est dans le top 10 du classement
duos = df_top10[['Athlete Name', 'Favourite Wheel Athlete', 'Favourite Wheel Illegal Time (s)', 'YOYOs']].dropna()
duos = duos[duos['Favourite Wheel Illegal Time (s)'] > 0]

# Agrégation au cas où un athlète a plusieurs cibles
duos_grouped = duos.groupby(['Athlete Name', 'Favourite Wheel Athlete']).agg({
    'Favourite Wheel Illegal Time (s)': 'sum',
    'YOYOs': 'sum'
}).reset_index()

# Tri du top 10 des duos les plus "draftants"
duos_top = duos_grouped.sort_values(by='Favourite Wheel Illegal Time (s)', ascending=False).head(10)

# Création des labels
labels = duos_top.apply(
    lambda row: f"{row['Athlete Name']} -> {row['Favourite Wheel Athlete']}", axis=1
)

# Bar chart
plt.figure(figsize=(10, 6))
barplot = sns.barplot(
    x='Favourite Wheel Illegal Time (s)',
    y=labels,
    data=duos_top,
    palette='viridis'
)

# Annotations YOYOs
for i, (value, yoyo) in enumerate(zip(duos_top['Favourite Wheel Illegal Time (s)'], duos_top['YOYOs'])):
    barplot.text(value + 1, i, f"YOYOs: {yoyo}", va='center')

plt.xlabel('Favourite Wheel Illegal Time (s)')
plt.ylabel('Duo (Suiveur -> Cible)')
plt.title('Top 10 finishers - Duos avec temps illégal + YOYOs')
plt.tight_layout()
plt.show()



# ==================================
# 3. Bar chart des données sur la puissance
# ==================================
positions = [
    "Solo (0 m)",
    "12 m (règlementaire)",
    "Yo-yo (8–10 m)",
    "Queue peloton (1–3 m)"
]
puissance = [330, 297, 280, 210]

# Création du graphique
plt.figure(figsize=(10, 6))
bars = plt.bar(positions, puissance)

# Étiquettes
plt.title("Puissance requise pour maintenir 54 km/h selon la position", fontsize=14)
plt.ylabel("Puissance (W)", fontsize=12)
plt.ylim(0, 350)

# Valeurs sur les barres
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, yval + 5, f'{int(yval)} W', ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

