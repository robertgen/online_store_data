import pandas as pd
import numpy as np
df = pd.read_csv('online_store_data.csv')
rows, columns = df.shape
# 1. ↓
df['quantity_sold'] = df['quantity_sold'].astype('Int32')
df['num_of_ratings'] = df['num_of_ratings'].astype('Int32')
print(df.dtypes)
# 2. ↓
df['quantity_in_stock'] = pd.to_numeric(df['quantity_in_stock'], errors='coerce') # - Am folosit to_numeric deoarece unele valori aveau scris 'out_of_stock' in loc de 0
df['quantity_in_stock'] = df['quantity_in_stock'].astype('Int32')
print(df.dtypes)
# 3. ↓
df['date_added'] = pd.to_datetime(df['date_added'], format='%d_%b_%y', errors='coerce')
print(df.dtypes)
# 4. ↓
def parse_rating(text):
    if pd.isna(text) or str(text).strip().lower() == "no reviews":
        return np.nan
    parts = str(text).replace(',', '').split()
    try:
        return float(parts[0])
    except (ValueError, IndexError):
      return np.nan
df['rating'] = df['rating'].apply(parse_rating)
print(df.filter(items=['product_name', 'rating']).head(30))
# 5. ↓
missing_rows = df[df[['product_name']].isna().all(axis=1)]
df.dropna(subset=['product_name'], how='all', inplace=True)
print(missing_rows) # - Arata randurile care au fost sters, cele cu 'NaN' la product_name
# 6. ↓
df.dropna(thresh=6, inplace=True)
print(df.isnull().sum()) # - Am pastrat randurile cu cel putin 6 valori nenule
# 7. ↓
df.drop_duplicates(keep='first', inplace=True, ignore_index=False)
print(df[df.duplicated(keep=False)])
# 2.1 ↓
df['revenue'] = df['price']*df['quantity_sold']
print(df[['product_name', 'revenue']].head(10)) # - Am creat coloana revenue si am afisat primele 10 produse
# 3.1 ↓
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
print("Tastaturile cu cel mai mare venit: ↓")
mask1 = (df['category'] == 'Keyboards')
cele_mai_bune_tastaturi = df[mask1].sort_values(by='revenue', ascending=False)
print(cele_mai_bune_tastaturi.filter(items=['product_name', 'revenue']).head(10))
# 3.2 ↓
print("Televizoarele cu cel mai mic venit: ↓")
mask2 = (df['category'] == 'TVs')
cele_mai_proaste_televizoare = df[mask2].sort_values(by='revenue')
print(cele_mai_proaste_televizoare.filter(items=['product_name', 'revenue']).head(10))
