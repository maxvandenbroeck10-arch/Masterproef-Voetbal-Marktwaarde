import pandas as pd
#inladen data
map_pad = r"C:\Users\maxva\OneDrive\Documents\vub\MA\Masterproef\extra variabelen github"

# 1. Defense
defensieve_stat = pd.read_csv(map_pad + r"\big5_player_defense (1)_clean.csv")
# 2. GCA
gca_acties = pd.read_csv(map_pad + r"\big5_player_gca_clean.csv")

# 3. Misc
player_mix = pd.read_csv(map_pad + r"\big5_player_misc (1)_clean.csv")

# 4. Passing
player_passen = pd.read_csv(map_pad + r"\big5_player_passing_clean.csv")

# 5. Passing Types
passen_typen_stat = pd.read_csv(map_pad + r"\big5_player_passing_types_clean.csv")

# 6. Playing Time
playing_time = pd.read_csv(map_pad + r"\big5_player_playing_time_clean.csv")

# 7. Possession
balbezit_stat = pd.read_csv(map_pad + r"\big5_player_possession_clean.csv")

# 8. Shooting
schoten_stat = pd.read_csv(map_pad + r"\big5_player_shooting_clean.csv")

# 9 Marktwaarde
value = pd.read_csv(map_pad + r"\big5_player_vals (1)_clean.csv")

#variabelen filteren op nuttioge kolommen
defensieve_stat_gefiltered = defensieve_stat[['Season_End_Year', 'Squad', 'Comp', 'Player', 'Pos', 'Age', 'Tkl_Tackles', 'TklW_Tackles', 'Tkl_Vs', 'Tkl_percent_Vs', 'Past_Vs', 'Press_Pressures', 'Succ_Pressures','_percent_Pressures','Blocks_Blocks', 'Sh_Blocks', 'ShSv_Blocks','Pass_Blocks', 'Int', 'Tkl+Int', 'Clr', 'Err', 'Def 3rd_Tackles', 'Def 3rd_Pressures']].copy()

gca_acties_gefiltered = gca_acties[['Season_End_Year', 'Player', 'SCA_SCA', 'SCA90_SCA', 'PassLive_SCA', 'PassDead_SCA', 'Drib_SCA', 'Sh_SCA', 'Def_SCA', 'GCA_GCA','GCA90_GCA', 'PassLive_GCA', 'PassDead_GCA', 'Drib_GCA', 'Sh_GCA', 'Def_GCA']].copy()

player_mix_gefilterd = player_mix[['Season_End_Year', 'Player','CrdY', 'CrdR', '2CrdY', 'Fls', 'Fld', 'Off', 'Crs', 'PKwon', 'PKcon', 'OG', 'Recov', 'Won_Aerial', 'Lost_Aerial', 'Won_percent_Aerial']].copy()

player_passen_gefilterd = player_passen[['Season_End_Year', 'Player', 'Cmp_Total', 'Cmp_percent_Total', 'Cmp_percent_Short', 'Cmp_percent_Medium', 'Cmp_percent_Long', 'Att_Total', 'Att_Long', 'Ast', 'xA', 'A_minus_xA', 'KP', 'Final_Third', 'PPA', 'CrsPA', 'Prog', 'xAG', 'A_minus_xAG']].copy()

passen_typen_stat_gefiltered = passen_typen_stat[['Season_End_Year', 'Player', 'TB_Pass', 'Press_Pass', 'Sw_Pass', 'Crs_Pass', 'CK_Pass', 'Ground_Height', 'Low_Height','High_Height', 'Left_Body', 'Right_Body', 'Head_Body', 'Cmp_Outcomes', 'Off_Outcomes', 'Out_Outcomes','Int_Outcomes', 'Blocks_Outcomes']].copy()

playing_time_gefiltered = playing_time[['Season_End_Year', 'Player', 'MP_Playing.Time', 'Min_Playing.Time', 'Mn_per_MP_Playing.Time', 'Min_percent_Playing.Time', 'Mins_Per_90_Playing.Time','Starts_Starts', 'Mn_per_Start_Starts', 'Compl_Starts', 'Subs_Subs', 'Mn_per_Sub_Subs', 'unSub_Subs', 'PPM_Team.Success', 'onG_Team.Success','onGA_Team.Success', 'plus_per__minus__Team.Success','plus_per__minus_90_Team.Success', 'On_minus_Off_Team.Success', 'onxG_Team.Success..xG.', 'onxGA_Team.Success..xG','xGplus_per__minus__Team.Success..xG','xGplus_per__minus_90_Team.Success..xG','On_minus_Off_Team.Success..xG']].copy()

balbezit_stat_gefiltered = balbezit_stat[['Season_End_Year', 'Player', 'Touches_Touches', 'Succ_percent_Dribbles', '#Pl_Dribbles', 'Megs_Dribbles', 'Carries_Carries', 'Prog_Carries', 'Targ_Receiving', 'Rec_percent_Receiving', 'Prog_Receiving', 'Mis_Dribbles', 'Dis_Dribbles']].copy()

schoten_stat_gefiltered = schoten_stat[['Season_End_Year', 'Player', 'Gls_Standard', 'SoT_percent_Standard', 'Sh_per_90_Standard', 'SoT_per_90_Standard', 'G_per_SoT_Standard', 'Dist_Standard', 'PK_Standard', 'PKatt_Standard', 'FK_Standard', 'xG_Expected', 'npxG_Expected', 'npxG_per_Sh_Expected', 'G_minus_xG_Expected', 'np:G_minus_xG_Expected']].copy()

value_gefilterd = value[['player_name', 'season_start_year', 'player_position','player_height_mtrs', 'player_market_value_euro']]
# Jaartal corrigeren
value_gefilterd['Season_End_Year'] = value_gefilterd['season_start_year']
value_gefilterd = value_gefilterd.drop(columns=['season_start_year'])
value_gefilterd = value_gefilterd.rename(columns={'player_name': 'Player'})

# Filteren op de specifieke verdediger-posities
verdediger_posities = ['Centre-Back', 'Left-Back', 'Right-Back']
value_gefilterd2 = value_gefilterd[value_gefilterd['player_position'].isin(verdediger_posities)].copy()


#nu alle kleine datasetjes samenvoegen tot 1 finale dataset

# Verwijder dubbelen in alle deelsets voor een schone merge
defensieve_stat_gefiltered = defensieve_stat_gefiltered.drop_duplicates(subset=['Player', 'Season_End_Year'])
gca_acties_gefiltered = gca_acties_gefiltered.drop_duplicates(subset=['Player', 'Season_End_Year'])
player_mix_gefilterd = player_mix_gefilterd.drop_duplicates(subset=['Player', 'Season_End_Year'])
player_passen_gefilterd = player_passen_gefilterd.drop_duplicates(subset=['Player', 'Season_End_Year'])
passen_typen_stat_gefiltered = passen_typen_stat_gefiltered.drop_duplicates(subset=['Player', 'Season_End_Year'])
playing_time_gefiltered = playing_time_gefiltered.drop_duplicates(subset=['Player', 'Season_End_Year'])
balbezit_stat_gefiltered = balbezit_stat_gefiltered.drop_duplicates(subset=['Player', 'Season_End_Year'])
schoten_stat_gefiltered = schoten_stat_gefiltered.drop_duplicates(subset=['Player', 'Season_End_Year'])
value_gefilterd2 = value_gefilterd2.drop_duplicates(subset=['Player', 'Season_End_Year'], keep='first')

#eerste 2 datasets
df_verdediging_gca = pd.merge(
    defensieve_stat_gefiltered, 
    gca_acties_gefiltered, 
    on=['Player', 'Season_End_Year'], 
    how='inner'
)

df_verdediging_gca_mix = pd.merge(
    df_verdediging_gca, 
    player_mix_gefilterd, 
    on=['Player', 'Season_End_Year'], 
    how='left'
)

df_verdediging_gca_mix_passen = pd.merge(
    df_verdediging_gca_mix, 
    player_passen_gefilterd, 
    on=['Player', 'Season_End_Year'], 
    how='left'
)

df_verdediging_gca_mix_passen_typen = pd.merge(
    df_verdediging_gca_mix_passen, 
    passen_typen_stat_gefiltered, 
    on=['Player', 'Season_End_Year'], 
    how='left'
)

df_verdediging_gca_mix_passen_typen_tijd = pd.merge(
    df_verdediging_gca_mix_passen_typen, 
    playing_time_gefiltered, 
    on=['Player', 'Season_End_Year'], 
    how='left'
)

df_verdediging_gca_mix_passen_typen_tijd_balbezit = pd.merge(
    df_verdediging_gca_mix_passen_typen_tijd, 
    balbezit_stat_gefiltered, 
    on=['Player', 'Season_End_Year'], 
    how='left'
)

df_verdediging_gca_mix_passen_typen_tijd_balbezit_schoten = pd.merge(
    df_verdediging_gca_mix_passen_typen_tijd_balbezit, 
    schoten_stat_gefiltered, 
    on=['Player', 'Season_End_Year'], 
    how='left'
)

df_verdediging_gca_mix_passen_typen_tijd_balbezit_schoten_value = pd.merge(
    df_verdediging_gca_mix_passen_typen_tijd_balbezit_schoten, 
    value_gefilterd2, 
    on=['Player', 'Season_End_Year'], 
    how='inner'
)
final_dataset2 = df_verdediging_gca_mix_passen_typen_tijd_balbezit_schoten_value.fillna(0).copy()
final_dataset2 = final_dataset2[final_dataset2['player_market_value_euro'] > 0].copy()
final_dataset2['Age'] = pd.to_numeric(final_dataset2['Age'], errors='coerce')
print(final_dataset2)


#log transformatie van marktwaarde
import numpy as np
final_dataset2['log_market_value'] = np.log1p(final_dataset2['player_market_value_euro'])


#Correlaties tussen de features om diegene >0.8 te verwijderen
# Voorbereiding: Definieer je features (X) en je target (y)
# We gebruiken de numerieke kolommen uit je dataset
X_selection = final_dataset2.select_dtypes(include=[np.number]).drop(columns=['log_market_value', 'player_market_value_euro'], errors='ignore')
y_selection = final_dataset2['log_market_value']

# Bereken de correlatie van ELKE variabele met de TARGET (log_market_value)
target_corr = X_selection.corrwith(y_selection).abs()

# Bereken de onderlinge correlatiematrix tussen de features
corr_matrix = X_selection.corr().abs()
print(corr_matrix)

# Filterproces: Identificeer paren met r > 0.80 en kies de beste
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

to_drop = set()
for column in upper.columns:
    # Zoek variabelen die een correlatie > 0.80 hebben met de huidige kolom
    high_corr_pairs = upper.index[upper[column] > 0.80].tolist()
    
    for pair_var in high_corr_pairs:
        # Vergelijk de correlatie van beide variabelen met de target
        corr_val_1 = target_corr[column]
        corr_val_2 = target_corr[pair_var]
        
        if corr_val_1 >= corr_val_2:
            # De huidige kolom is beter of gelijk, drop de andere
            to_drop.add(pair_var)
            print(f"Paring gevonden: '{column}' (r_y={corr_val_1:.3f}) vs '{pair_var}' (r_y={corr_val_2:.3f}). Drop: '{pair_var}'")
        else:
            # De andere variabele is beter, drop de huidige kolom
            to_drop.add(column)
            print(f"Paring gevonden: '{column}' (r_y={corr_val_1:.3f}) vs '{pair_var}' (r_y={corr_val_2:.3f}). Drop: '{column}'")

#  Maak de definitieve lijst van overgebleven variabelen
overgebleven_features = [v for v in X_selection.columns if v not in to_drop]

print("-" * 30)
print(f"Totaal aantal variabelen verwijderd: {len(to_drop)}")
print(f"Aantal variabelen overgebleven: {len(overgebleven_features)}")


# Maak nu de echte DATAFRAME aan met overgebleven kolommen + je target en ID's
# We voegen 'Player', 'Season_End_Year' en de target weer toe aan de data
id_kolommen = ['Player', 'Squad', 'Comp', 'player_position', 'log_market_value', 'player_market_value_euro']
finale_kolommen = [col for col in id_kolommen + overgebleven_features if col in final_dataset2.columns]

# Dit is nu een echte TABEL (DataFrame) in plaats van een lijst
df_final_clean = final_dataset2[finale_kolommen].copy()
print(df_final_clean.head(0))


#Assumpties Controleren
import statsmodels.api as sm
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

onderzoeks_variabelen = ['Tkl_percent_Vs', 'Int_Outcomes', 'ShSv_Blocks', 'Age']
df_final_clean['Age_Squared'] = df_final_clean['Age'] ** 2
final_dataset_assumpties= df_final_clean.dropna(subset=onderzoeks_variabelen + ['log_market_value'])

# 1 Assumptie Lineariteit
for kolom in onderzoeks_variabelen:
    plt.figure(figsize=(8, 5))
    sns.regplot(x=kolom, y='log_market_value', data=final_dataset_assumpties, 
                scatter_kws={'alpha':0.3}, line_kws={'color':'teal'})
    plt.title("Lineariteit check FBref: " + kolom)
    plt.ylabel("Log-Marktwaarde")
    plt.show()

#2 Normaliteit van de residuen
# We moeten wel de niet-numerieke kolommen en de target (log_market_value) even uitsluiten voor de X
X_full = df_final_clean.select_dtypes(include=[np.number]).drop(columns=['log_market_value'], errors='ignore')
y_full = df_final_clean['log_market_value']

# Verwijder rijen met NaN zodat het model kan draaien
mask = ~X_full.isna().any(axis=1) & ~y_full.isna()
X_clean = X_full[mask]
y_clean = y_full[mask]

# Fit een tijdelijk model met AL deze variabelen
X_clean = sm.add_constant(X_clean)
full_check_model = sm.OLS(y_clean, X_clean).fit()

# Visualisatie van de normaliteit (Histogram + Q-Q Plot)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Histogram
sns.histplot(full_check_model.resid, kde=True, color="blue", ax=ax1)
ax1.set_title("Normaliteit van Residuen")
ax1.set_xlabel("Foutmarge")

# Q-Q Plot
stats.probplot(full_check_model.resid, dist="norm", plot=ax2)
ax2.set_title("Q-Q Plot")

plt.tight_layout()
plt.show()

#3 Assumptie Homoscedasticiteit
plt.figure(figsize=(8, 5))
plt.scatter(full_check_model.fittedvalues, full_check_model.resid, alpha=0.3, color='orange')
plt.axhline(y=0, color='red', linestyle='--')
plt.title("Homoscedasticiteit: Volledige Dataset")
plt.xlabel("Voorspelde waarden")
plt.ylabel("Residuen")
plt.show()

#4 Assumptie Multicollineariteit
from statsmodels.stats.outliers_influence import variance_inflation_factor

X_all = df_final_clean.select_dtypes(include=[np.number]).drop(columns=['player_market_value_euro', 'log_market_value'], errors='ignore')
X_all = X_all.dropna() # Verwijder rijen met missende waarden voor de berekening

# Voeg constante toe
X_all_const = sm.add_constant(X_all)

# bereken VIF
vif_total = pd.DataFrame()
vif_total["Variabele"] = X_all_const.columns
vif_total["VIF"] = [variance_inflation_factor(X_all_const.values, i) for i in range(len(X_all_const.columns))]

# Filter op VIF > 5 (exclusief de constante)
vif_high = vif_total[(vif_total["VIF"] > 5) & (vif_total["Variabele"] != 'const')]

print(f"Totaal aantal variabelen aan de start: {len(X_all.columns)}")
print(f"Aantal variabelen met VIF > 5: {len(vif_high)}")
print("-" * 30)
print("Variabelen die verwijderd zouden worden (VIF > 5):")
print(vif_high.sort_values(by="VIF", ascending=False))

# Automatisch verwijderen
variabelen_te_verwijderen = vif_high["Variabele"].tolist()
X_filtered = X_all.drop(columns=variabelen_te_verwijderen)
print(X_filtered.head(0))

# Controle van de overgebleven set
print("-" * 30)
print(f"Aantal variabelen overgebleven: {len(X_filtered.columns)}")
print("Lijst van overgebleven variabelen:")
print(X_filtered.columns.tolist())

# Extra: Bereken VIF opnieuw voor de overgebleven set om te zien of alles nu < 5 is
X_filtered_const = sm.add_constant(X_filtered)
vif_after = pd.DataFrame()
vif_after["Variabele"] = X_filtered_const.columns
vif_after["VIF"] = [variance_inflation_factor(X_filtered_const.values, i) for i in range(len(X_filtered_const.columns))]

# Sorteer op VIF (hoog naar laag) en toon de top 5
top_5_vif = vif_after.sort_values(by="VIF", ascending=False).head(11)
print("-" * 30)
print("Top 5 Hoogste VIF-scores (inclusief constante):")
print(top_5_vif)

# 5. Assumptie Uitschieters (Cook's Distance)
influence = full_check_model.get_influence()
c, p = influence.cooks_distance

# Maak een DataFrame om de namen aan de afwijkingen te koppelen
cooks_df = pd.DataFrame({
    'Player': y_clean.index, 
    'Cooks_Distance': c
})

# Grafiek tekenen
plt.figure(figsize=(12, 6))
plt.stem(np.arange(len(c)), c, markerfmt=",")

# Grenswaarde bepalen (4/n)
threshold = 4 / len(y_clean)
plt.axhline(y=threshold, color='red', linestyle='--', label=f'Grens ({threshold:.4f})')

plt.title("Cook's Distance: Welke spelers hebben de grootste invloed op het model?")
plt.xlabel("Index van de speler")
plt.ylabel("Cook's Distance")
plt.legend()
plt.show()

# Toon de top 10 uitschieters (spelers boven de grens)
uitschieters = cooks_df[cooks_df['Cooks_Distance'] > threshold].sort_values(by='Cooks_Distance', ascending=False)

if len(uitschieters) > 0:
    print(f"Er zijn {len(uitschieters)} observaties boven de grens van {threshold:.4f}:")
    # We tonen de eerste 10 om het overzichtelijk te houden
    print(uitschieters.head(10))
else:
    print("Er zijn geen significante uitschieters gevonden.")



#Nu 1 dataset met alleen var met vif < 5 en met corr < 0.8
# 1. Pak de lijst met namen die de VIF hebben overleefd
features_na_vif = X_filtered.columns.tolist()

# Maak de kolom handmatig aan in de bron-dataframe als hij ontbreekt
if 'Age_Squared' not in df_final_clean.columns:
    df_final_clean['Age_Squared'] = df_final_clean['Age'] ** 2

# Update je finale_kolommen lijst
# We dwingen de ID-kolommen en Leeftijd erin, en vullen aan met de VIF-overlevers
id_en_basis = ['Player', 'Squad', 'Comp', 'player_position', 'log_market_value', 'player_market_value_euro', 'Age', 'Age_Squared']

# Zorg dat we geen dubbele kolommen krijgen
finale_kolommen = id_en_basis + [col for col in features_na_vif if col not in id_en_basis]

# 3. Maak de dataset en gebruik df_final_clean als bron
# We checken alleen of ze in df_final_clean zitten
finale_dataset3 = df_final_clean[[col for col in finale_kolommen if col in df_final_clean.columns]].copy()
print(finale_dataset3.columns.tolist())




# Toevoegen marktwaaarde voorgaand seizoen
finale_dataset3 = finale_dataset3.sort_values(by=['Player', 'Season_End_Year'])

#Maak de 'lagged' variabelen aan
# We pakken de marktwaarde EN het jaartal van de vorige observatie
finale_dataset3['prev_market_value_log'] = finale_dataset3.groupby('Player')['log_market_value'].shift(1)
finale_dataset3['prev_Season_End_Year'] = finale_dataset3.groupby('Player')['Season_End_Year'].shift(1)

# Bereken het verschil in jaren (de gap)
finale_dataset3['year_gap'] = finale_dataset3['Season_End_Year'] - finale_dataset3['prev_Season_End_Year']
# Dit verwijdert automatisch de eerste seizoenen van spelers (NaN) ÉN de gap years (2, 3, 4...)
finale_dataset4 = finale_dataset3[finale_dataset3['year_gap'] == 1].copy()

# Optioneel: Verwijder de hulpkolommen om je data schoon te houden
finale_dataset4 = finale_dataset4.drop(columns=['prev_Season_End_Year', 'year_gap']) #behoud alleen rijen waar de gap EXACT 1 jaar is)
print(finale_dataset4)


#Beschrijving dataset
print(len(finale_dataset4))
print(finale_dataset4['Player'].nunique())
print(finale_dataset4['Squad'].nunique())

#check de verdeling per competitie en dan per seizoen
comp_stats = finale_dataset4['Comp'].value_counts().reset_index()
comp_stats.columns = ['Competitie', 'Aantal Observaties']
comp_stats['Percentage'] = (comp_stats['Aantal Observaties'] / len(finale_dataset4) * 100).round(2)
print(comp_stats.to_string(index=False))

seizoen_stats = finale_dataset4['Season_End_Year'].value_counts().sort_index().reset_index()
seizoen_stats.columns = ['Seizoen', 'Aantal Observaties']
seizoen_stats['Percentage'] = (seizoen_stats['Aantal Observaties'] / len(finale_dataset4) * 100).round(2)
print(seizoen_stats.to_string(index=False))

#Verdeling per positie
counts = finale_dataset4['player_position'].value_counts()
percentages = finale_dataset4['player_position'].value_counts(normalize=True) * 100

# Zet het netjes in een tabelletje
positie_verdeling = pd.DataFrame({
    'Aantal': counts,
    'Percentage (%)': percentages
})

print(positie_verdeling.round(2))


#assumpties opnieuw controleren op finale dataset
import statsmodels.api as sm
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

onderzoeks_variabelen = ['Tkl_percent_Vs', 'Int_Outcomes', 'ShSv_Blocks', 'Age', 'Age_Squared']
finale_dataset4= finale_dataset4.dropna(subset=onderzoeks_variabelen + ['log_market_value'])

# 1 Assumptie Lineariteit
for kolom in onderzoeks_variabelen:
    plt.figure(figsize=(8, 5))
    sns.regplot(x=kolom, y='log_market_value', data=final_dataset_assumpties, 
                scatter_kws={'alpha':0.3}, line_kws={'color':'teal'})
    plt.title("Lineariteit check FBref: " + kolom)
    plt.ylabel("Log-Marktwaarde")
    plt.show()

#2 Normaliteit van de residuen
# We moeten wel de niet-numerieke kolommen en de target (log_market_value) even uitsluiten voor de X
X_full = finale_dataset4.select_dtypes(include=[np.number]).drop(columns=['log_market_value'], errors='ignore')
y_full = finale_dataset4['log_market_value']

# Verwijder rijen met NaN zodat het model kan draaien
mask = ~X_full.isna().any(axis=1) & ~y_full.isna()
X_clean = X_full[mask]
y_clean = y_full[mask]

# Fit een tijdelijk model met AL deze variabelen
X_clean = sm.add_constant(X_clean)
full_check_model = sm.OLS(y_clean, X_clean).fit()

# Visualisatie van de normaliteit (Histogram + Q-Q Plot)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Histogram
sns.histplot(full_check_model.resid, kde=True, color="blue", ax=ax1)
ax1.set_title("Normaliteit van Residuen")
ax1.set_xlabel("Foutmarge")

# Q-Q Plot
stats.probplot(full_check_model.resid, dist="norm", plot=ax2)
ax2.set_title("Q-Q Plot")

plt.tight_layout()
plt.show()

#3 Assumptie Homoscedasticiteit
plt.figure(figsize=(8, 5))
plt.scatter(full_check_model.fittedvalues, full_check_model.resid, alpha=0.3, color='orange')
plt.axhline(y=0, color='red', linestyle='--')
plt.title("Homoscedasticiteit: Volledige Dataset")
plt.xlabel("Voorspelde waarden")
plt.ylabel("Residuen")
plt.show()


# 4 Assumptie Uitschieters (Cook's Distance)
influence = full_check_model.get_influence()
c, p = influence.cooks_distance

# Maak een DataFrame om de namen aan de afwijkingen te koppelen
cooks_df = pd.DataFrame({
    'Player': y_clean.index, 
    'Cooks_Distance': c
})

# Grafiek tekenen
plt.figure(figsize=(12, 6))
plt.stem(np.arange(len(c)), c, markerfmt=",")

# Grenswaarde bepalen (4/n)
threshold = 4 / len(y_clean)
plt.axhline(y=threshold, color='red', linestyle='--', label=f'Grens ({threshold:.4f})')

plt.title("Cook's Distance: Welke spelers hebben de grootste invloed op het model?")
plt.xlabel("Index van de speler")
plt.ylabel("Cook's Distance")
plt.legend()
plt.show()


# We maken een tijdelijke DataFrame met de namen en de afstand
cooks_df = pd.DataFrame({
    'Player_Name': finale_dataset4.loc[y_clean.index, 'Player'],
    'Cooks_Distance': c # Vervang 'cooks_d' door de variabele waar je waarden in staan
})

outliers = cooks_df[cooks_df['Cooks_Distance'] > threshold]

# Sorteer ze van hoog naar laag zodat de grootste boosdoeners bovenaan staan
outliers_sorted = outliers.sort_values(by='Cooks_Distance', ascending=False)

# Toon de top 20 (of de hele lijst)
print(f"Er zijn {len(outliers_sorted)} observaties boven de grens.")
print("-" * 30)
print(outliers_sorted.head(20))


#Correlatie matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Bereken de correlaties 
numeric_df = finale_dataset4.select_dtypes(include=[np.number])
correlations = numeric_df.corr()['log_market_value'].drop('log_market_value').sort_values(ascending=False) 
# Top 20 hoogste correlaties weergeven
top_corr = correlations.head(20)
# De bar chart
plt.figure(figsize=(10, 8))
sns.barplot(x=top_corr.values, y=top_corr.index, palette='viridis')

# Styling 
plt.title('Correlatie tussen features en Log-Marktwaarde', fontsize=15)
plt.xlabel('Pearson Correlatie Coëfficiënt', fontsize=12)
plt.ylabel('Features', fontsize=12)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1) # De nul-lijn
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


#Corrlatiematrix tussen de feutures (alleen deze 12 anders is veel te lang)
vars_voor_matrix = [
    'log_market_value', 'player_market_value_euro', 'Age', 'player_height_mtrs',
    'Tkl_percent_Vs', 'Int_Outcomes', 'Won_percent_Aerial', 'Won_Aerial', 
    'Fls', 'Rec_percent_Receiving', 'xGplus_per__minus__Team.Success..xG', 'SoT_per_90_Standard'
]
# Bereken de correlatiematrix
corr_df = finale_dataset4[vars_voor_matrix].corr()

# Maak de matrix "triangular" 
mask = np.triu(np.ones_like(corr_df, dtype=bool))
tri_df = corr_df.mask(mask)

# Voeg de nummering toe aan de labels 
new_labels = [f"({i+1}) {col}" for i, col in enumerate(vars_voor_matrix)]
header_numbers = [f"({i+1})" for i in range(len(vars_voor_matrix))]

tri_df.index = new_labels
tri_df.columns = header_numbers
final_table = tri_df.round(2).replace(np.nan, '')

# Toon de tabel
print("Table B.1")
print("Correlation Matrix")
print("-" * 100)
display(final_table)


#Discriptieve statistieken
finale_dataset4['player_height_mtrs'] = finale_dataset4['player_height_mtrs'].replace(0, np.nan)

# Maak een kopie om je originele data niet te overschrijven
df_tabel = finale_dataset4.copy()

# Voeg de kolom toe vanuit de andere dataset
df_tabel['Marktwaarde (Mln €)'] = finale_dataset4['player_market_value_euro'] / 1_000_000

selectie = [
    'Marktwaarde (Mln €)', 'Age', 'player_height_mtrs', 'Mn_per_MP_Playing.Time', 'npxG_per_Sh_Expected', 
    'Cmp_percent_Long', 'SCA90_SCA', 'Succ_percent_Dribbles', 'Won_percent_Aerial', 'Tkl_percent_Vs', 
   'ShSv_Blocks', 'Int_Outcomes', 'Err', 'Fls', 'CrdY', 'CrdR', 'OG'
]

descriptieve_tabel = df_tabel[selectie].describe().transpose()

# Kies kolimmen die ik wil, dus verwijder 25% en 75%
kolommen_die_ik_wil = ['count', 'mean', 'std', 'min', '50%', 'max']
descriptieve_tabel = descriptieve_tabel[kolommen_die_ik_wil]

# Hernoem de kolomnamen naar Nederlands
descriptieve_tabel.columns = ['Aantal', 'Gemiddelde', 'Standaard Deviatie.', 'Min', 'Mediaan', 'Max']
descriptieve_tabel = descriptieve_tabel.round(2)
print(descriptieve_tabel)




#start verklarend model
# Omdat de eerste seizoenen van een speler nu geen 'vorige waarde' hebben (NaN), moeten we die rijen even negeren voor deze specifieke regressie.
baseline_data = finale_dataset4.dropna(subset=['prev_market_value_log', 'log_market_value'])

# 1 Baseline model
# Definieer X en y
y = baseline_data['log_market_value']
X = baseline_data['prev_market_value_log']
X = sm.add_constant(X) # Voeg de intercept toe

# Fit het model
baseline_model = sm.OLS(y, X).fit()

# Bekijk de resultaten
print(baseline_model.summary())

# 2 Toevoegen van leeftijd, grootte en gespeelde minuten
# Selecteer je kolommen
X2_columns = ['prev_market_value_log', 'Age', 'Age_Squared', 'player_height_mtrs']
X2 = baseline_data[X2_columns].copy()

# Standaardiseer de variabelen (Z-score)
X2_scaled = (X2 - X2.mean()) / X2.std()

# Voeg nu de constante toe aan de GESTANDAARDISEERDE data
X2_scaled = sm.add_constant(X2_scaled)

# Fit Model 
model2_scaled = sm.OLS(y, X2_scaled).fit()
print(model2_scaled.summary())

# 3 Toevoegen defensieve variabelen
# Update de lijst (zonder de 'onderdelen')
defensieve_vars_clean = ['Tkl_percent_Vs','_percent_Pressures', 'ShSv_Blocks', 'Int_Outcomes', 'Err', 'Won_Aerial', 'Won_percent_Aerial', 'Off_Outcomes']
model3_vars = X2_columns + defensieve_vars_clean


# Selecteer de data
X3 = baseline_data[model3_vars].copy()

# STANDAARDISEREN (Z-score) - Dit lost het Condition Number op!
X3_scaled = (X3 - X3.mean()) / X3.std()

# Voeg de constante toe
X3_scaled = sm.add_constant(X3_scaled)
y = baseline_data['log_market_value']

# Fit Model 3
model3_final = sm.OLS(y, X3_scaled).fit()
print(model3_final.summary())

# 4 Finale model
#Start met alle numerieke variabelen
alle_numerieke_vars = baseline_data.select_dtypes(include=[np.number]).columns.tolist()
# 2. Maak een lijst van variabelen die je NIET wilt (Target, ID's én de dubbelingen)
exclude_vars = [
    'log_market_value', 'player_market_value_euro', 'Player', 'Season_End_Year', 
    'Squad', 'Comp', 'player_position',
    ]
# Maak de definitieve lijst voor Model 4
# We nemen alle numerieke variabelen MIN de uitsluitingen
model4_vars = [v for v in alle_numerieke_vars if v not in exclude_vars]
X4 = baseline_data[model4_vars].copy()

# VERWIJDER KOLOMMEN MET 0 VARIATIE (Voorkomt delen door nul)
# Als een kolom overal dezelfde waarde heeft, kan hij niet gestandaardiseerd worden.
X4 = X4.loc[:, X4.std() > 0]

# VERWIJDERE RIJEN MET MISSENDE WAARDEN (NaN)
# OLS kan niet omgaan met lege cellen. We filteren y mee zodat ze even lang blijven.
mask = X4.notna().all(axis=1)
X4_clean = X4[mask]
y_clean = baseline_data.loc[mask, 'log_market_value']

# STANDAARDISEREN
# Nu we zeker weten dat std > 0 en er geen NaNs zijn, kunnen we veilig schalen
X4_scaled = (X4_clean - X4_clean.mean()) / X4_clean.std()

# VOEG CONSTANTE TOE EN FIT MODEL
X4_scaled = sm.add_constant(X4_scaled)
model4_final = sm.OLS(y_clean, X4_scaled).fit()

# Bekijk de resultaten
print(model4_final.summary())



#Alle modellen naast elkaar
from stargazer.stargazer import Stargazer
from IPython.display import display, HTML

# 1. Maak het stargazer object
stargazer = Stargazer([baseline_model, model2_scaled, model3_final, model4_final])

stargazer.covariate_order([
    'const', 'prev_market_value_log', 'Age', 'Age_Squared', 'player_height_mtrs', 
    'Tkl_percent_Vs', '_percent_Pressures', 'ShSv_Blocks', 'Int_Outcomes', 'Err', 
    'Won_Aerial', 'Won_percent_Aerial', 'Off_Outcomes',
    'Fls', 'Fld', 'Off', 'PKwon', 'PKcon', 'OG', 'CrdY', 'CrdR', '2CrdY',
    'Cmp_percent_Long', 'Cmp_percent_Medium', 'Cmp_percent_Short', 
    'TB_Pass', 'CK_Pass', 'Left_Body', 'Rec_percent_Receiving',
    'SCA90_SCA', 'Def_SCA', 'Drib_SCA', 'Sh_SCA', 'GCA90_GCA', 'Def_GCA', 
    'PassDead_GCA', 'Drib_GCA', 'Sh_GCA', 'A_minus_xA',
    'Succ_percent_Dribbles', '#Pl_Dribbles', 'Megs_Dribbles',
    'SoT_percent_Standard', 'Sh_per_90_Standard', 'SoT_per_90_Standard', 
    'G_per_SoT_Standard', 'Dist_Standard', 'FK_Standard', 'npxG_per_Sh_Expected',
    'Mn_per_MP_Playing.Time', 'Mn_per_Start_Starts', 'Subs_Subs', 'Mn_per_Sub_Subs', 'unSub_Subs', 
    'PPM_Team.Success', 'xGplus_per__minus__Team.Success..xG'
])

# 3. Hernoem ze voor een NL-talige thesis (gebaseerd op je screenshot)
stargazer.rename_covariates({
    # Basis & Fysiek
    'const': 'Constante',
    'prev_market_value_log': 'Marktwaarde (t-1) [log]',
    'Age': 'Leeftijd',
    'Age_Squared': 'Leeftijd kwadraat',
    'player_height_mtrs': 'Lengte',
    
    # Verdedigend
    'Tkl_percent_Vs': 'Tackle succes (%)',
    '_percent_Pressures': 'Drukzet succes (%)',
    'ShSv_Blocks': 'Geblokte schoten',
    'Int_Outcomes': 'Onderscheppingen',
    'Err': 'Cruciale fouten',
    'Won_Aerial': 'Luchtduels gewonnen',
    'Won_percent_Aerial': 'Luchtduel succes (%)',
    'Off_Outcomes': 'Buitenspel uitgelokt',
    
    # Discipline & Fouten
    'Fls': 'Overtredingen begaan',
    'Fld': 'Overtredingen uitgelokt',
    'Off': 'Buitenspel',
    'PKwon': "Penalty's versierd",
    'PKcon': "Penalty's weggegeven",
    'OG': 'Eigen doelpunten',
    'CrdY': 'Gele kaarten',
    'CrdR': 'Rode kaarten',
    '2CrdY': 'Tweede gele kaarten',
    
    # Passing
    'Cmp_percent_Long': 'Passzuiverheid lang (%)',
    'Cmp_percent_Medium': 'Passzuiverheid medium (%)',
    'Cmp_percent_Short': 'Passzuiverheid kort (%)',
    'TB_Pass': 'Steekpasses',
    'CK_Pass': 'Corners genomen',
    'Left_Body': 'Passes linkervoet',
    'Rec_percent_Receiving': 'Aannamepercentage (%)',
    
    # Aanvallend & Creativiteit
    'SCA90_SCA': 'Shot-Creating Actions',
    'Def_SCA': 'SCA (def.)',
    'Drib_SCA': 'SCA (drib.)',
    'Sh_SCA': 'SCA (schot)',
    'GCA90_GCA': 'Goal-Creating Actions',
    'Def_GCA': 'GCA (def.)',
    'PassDead_GCA': 'GCA (spelh.)',
    'Drib_GCA': 'GCA (drib.)',
    'Sh_GCA': 'GCA (schot)',
    'A_minus_xA': 'Assists minus xA',
    'Succ_percent_Dribbles': 'Dribbel succes (%)',
    '#Pl_Dribbles': 'Tegenstanders gepasseerd',
    'Megs_Dribbles': "Panna's",
    
    # Schieten
    'SoT_percent_Standard': 'Schotnauwkeurigheid (%)',
    'Sh_per_90_Standard': 'Schoten',
    'SoT_per_90_Standard': 'Schoten op doel',
    'G_per_SoT_Standard': 'Doelpunten per schot op doel',
    'Dist_Standard': 'Schotafstand',
    'FK_Standard': 'Vrije trappen',
    'npxG_per_Sh_Expected': 'xG per schot (np)',
    
    # Speeltijd & Team Performance
    'Mn_per_MP_Playing.Time': 'Minuten per wedstrijd',
    'Mn_per_Start_Starts': 'Minuten per basisplaats',
    'Subs_Subs': 'Invalbeurten',
    'Mn_per_Sub_Subs': 'Minuten per invalbeurt',
    'unSub_Subs': 'Ongebruikte reserve (bank)',
    'PPM_Team.Success': 'Punten per wedstrijd (PPM)',
    'xGplus_per__minus__Team.Success..xG': 'Team Net xG Rating'
})

# 1. Schakel de automatische statistieken uit die ONDER de lijn staan
stargazer.show_r2 = False
stargazer.show_adj_r2 = False
stargazer.show_n = False
stargazer.show_f_statistic = False
stargazer.show_residual_std_err = False

# 2. Voeg nu ALLES handmatig toe in de volgorde die jij wilt. 
# Alles wat je hier toevoegt komt in één blok.
models = [baseline_model, model2_scaled, model3_final, model4_final]

stargazer.add_line('Observations', [str(int(m.nobs)) for m in models])
stargazer.add_line('R²', [f"{m.rsquared:.3f}" for m in models])
stargazer.add_line('Adj. R²', [f"{m.rsquared_adj:.3f}" for m in models])
stargazer.add_line('F Statistic', [f"{m.fvalue:.2f}" for m in models])
stargazer.add_line('Prob (F-statistic)', [f"{m.f_pvalue:.3f}" for m in models])
stargazer.add_line('Log-Likelihood', [f"{m.llf:.1f}" for m in models])
stargazer.add_line('AIC', [f"{m.aic:.1f}" for m in models])
stargazer.add_line('BIC', [f"{m.bic:.1f}" for m in models])

# 5. Styling
stargazer.custom_columns(['Model 1', 'Model 2', 'Model 3', 'Model 4'])
stargazer.show_model_numbers(False)
# 2. De juiste functie voor decimalen (probeer deze naam)
try:
    stargazer.significant_digits(3)
except AttributeError:
    # Als die ook niet werkt, probeer deze (sommige versies gebruiken dit)
    stargazer.show_precision = 3 

display(HTML(stargazer.render_html()))
