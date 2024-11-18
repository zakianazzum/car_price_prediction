import pickle

with open("preprocessor.pkl", "rb") as file:
    preprocessor = pickle.load(file)

with open("lm.pkl", "rb") as file:
    loaded_lm = pickle.load(file)


new_data = {
    "Brand": ["Toyota"],
    "Year": [2020],
    "Engine Size": [1.8],
    "Fuel Type": ["Petrol"],
    "Transmission": ["Automatic"],
    "Mileage": [25000],
    "Condition": ["Like New"],
    "Model": ["Corolla"],
}

import pandas as pd

new_data_df = pd.DataFrame(new_data)

new_data_encoded = preprocessor.transform(new_data_df)

predictions = loaded_lm.predict(new_data_df)

print("predicted car price:", predictions[0])
