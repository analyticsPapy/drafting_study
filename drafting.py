import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Chargement des données
df = pd.read_csv("C:\Users\combe\Documents\workplace\drafting_study\raceranger_final_parsed - raceranger_final_parsed.csv")

# Configuration générale
sns.set(style="whitegrid")
plt.rcParams["axes.titlesize"] = 13

# Création d'une figure pour chaque graphique
figures = []

# 1. Classement vs Temps total d’infraction
fig1 = plt.figure(figsize=(12, 6))
order = df_viz[df_viz["Finish Position"].apply(lambda x: str(x).isdigit())]
order = order.sort_values(by="Finish Position")
sns.barplot(data=order, x="Finish Position", y="Total Illegal Time (s)", hue="Sexe")
plt.title("Temps total d'infraction en fonction du classement")
plt.ylabel("Temps total d'infraction (s)")
fig1.savefig("/mnt/data/plot_position_vs_illegal_time.png")
plt.close(fig1)

# 2. Part du temps illégal liée aux YOYOs
fig2 = plt.figure(figsize=(10, 6))
df_viz["YOYO Contribution (%)"] = df_viz["Favourite Wheel Illegal Time (s)"] / df_viz["Total Illegal Time (s)"].replace(0, 1) * 100
sns.histplot(data=df_viz, x="YOYO Contribution (%)", hue="Sexe", bins=20, kde=True, multiple="stack")
plt.title("Part du temps illégal attribuée aux YOYOs")
fig2.savefig("/mnt/data/plot_yoyo_share.png")
plt.close(fig2)

# 3. Corrélation entre YOYOs et position finale
fig3 = plt.figure(figsize=(8, 6))
df_numeric = df_viz[df_viz["Finish Position"].apply(lambda x: str(x).isdigit())]
sns.scatterplot(data=df_numeric, x="YOYOs", y=df_numeric["Finish Position"].astype(int), hue="Sexe")
plt.title("Nombre de YOYOs vs Position finale")
plt.ylabel("Position (plus bas = meilleur classement)")
fig3.savefig("/mnt/data/plot_yoyos_vs_position.png")
plt.close(fig3)

# 4. Top 10 des plus grands suiveurs
fig4 = plt.figure(figsize=(10, 6))
top_followers = df_viz.sort_values("Favourite Wheel Illegal Time (s)", ascending=False).head(10)
sns.barplot(data=top_followers, y="Athlete Name", x="Favourite Wheel Illegal Time (s)", hue="Sexe")
plt.title("Top 10 des plus grands suiveurs (drafting derrière un même athlète)")
plt.xlabel("Temps de suivi illégal (s)")
plt.ylabel("Athlète")
fig4.savefig("/mnt/data/plot_top_followers.png")
plt.close(fig4)

# 5. Athlètes avec la plus longue infraction unique
fig5 = plt.figure(figsize=(10, 6))
longest_follow = df_viz.sort_values("Single Longest Illegal Follow Time (s)", ascending=False).head(10)
sns.barplot(data=longest_follow, y="Athlete Name", x="Single Longest Illegal Follow Time (s)", hue="Sexe")
plt.title("Plus longues infractions uniques")
plt.xlabel("Temps (s)")
plt.ylabel("Athlète")
fig5.savefig("/mnt/data/plot_longest_single_draft.png")
plt.close(fig5)

# 6. Comparaison sexe vs stratégie (Boxplots)
fig6 = plt.figure(figsize=(12, 6))
melted = df_viz.melt(id_vars=["Sexe"], value_vars=[
    "Total Illegal Time (s)", "YOYOs", "Overtakes"
], var_name="Comportement", value_name="Valeur")
sns.boxplot(data=melted, x="Comportement", y="Valeur", hue="Sexe")
plt.title("Comportements selon le sexe")
fig6.savefig("/mnt/data/plot_sex_comparison.png")
plt.close(fig6)

# Liens vers les graphes générés
[
    "sandbox:/mnt/data/plot_position_vs_illegal_time.png",
    "sandbox:/mnt/data/plot_yoyo_share.png",
    "sandbox:/mnt/data/plot_yoyos_vs_position.png",
    "sandbox:/mnt/data/plot_top_followers.png",
    "sandbox:/mnt/data/plot_longest_single_draft.png",
    "sandbox:/mnt/data/plot_sex_comparison.png"
]
