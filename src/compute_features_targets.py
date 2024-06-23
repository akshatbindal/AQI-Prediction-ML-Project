import json
import os

def compute_features_targets(data):
    features = []
    targets = []
    
    forecast = data['forecast']['pm25']
    for i in range(len(forecast) - 1):
        features.append(forecast[i])
        targets.append(forecast[i + 1])
    
    return features, targets

if __name__ == "__main__":
    file_path = os.path.join("data", "weather_data.json")
    with open(file_path) as f:
        data = json.load(f)
        
    features, targets = compute_features_targets(data)
    print("Features:", features)
    print("Targets:", targets)
