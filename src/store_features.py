import pandas as pd
import json
from src.compute_features_targets import compute_features_targets

def store_features(features, targets, filename):
    df = pd.DataFrame({
        'features': features,
        'targets': targets
    })
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    with open("data/weather_data.json") as f:
        data = json.load(f)
        
    features, targets = compute_features_targets(data)
    store_features(features, targets, "data/features_store.csv")
