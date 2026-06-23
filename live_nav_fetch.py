import requests
import pandas as pd

# ---- PART 1: Fetch HDFC Top 100 Direct ----
print("Downloading HDFC Top 100...")
response = requests.get("https://api.mfapi.in/mf/125497")
data = response.json()
df = pd.DataFrame(data['data'])
df.to_csv('data/raw/hdfc_top100_nav.csv', index=False)
print(f"Done! {len(df)} records saved")

# ---- PART 2: Fetch 5 Bluechip Funds ----
funds = {
    'SBI_Bluechip': 119551,
    'ICICI_Bluechip': 120503,
    'Nippon_LargeCap': 118632,
    'Axis_Bluechip': 119092,
    'Kotak_Bluechip': 120841
}

for fund_name, code in funds.items():
    print(f"Downloading {fund_name}...")
    response = requests.get(f"https://api.mfapi.in/mf/{code}")
    data = response.json()
    df = pd.DataFrame(data['data'])
    df.to_csv(f'data/raw/{fund_name}_nav.csv', index=False)
    print(f"Done! {len(df)} records saved!")

print("\nAll funds downloaded successfully!")