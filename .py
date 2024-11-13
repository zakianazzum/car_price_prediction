import pickle

with open("preprocessor.pkl", "rb") as file:
    preprocessor = pickle.load(file)

with open("car_price_model.pkl", "rb") as file:
    loaded_lm = pickle.load(file)


new_data = {
    "Brand": ["BMW"],
    "Year": [2018],
    "Engine Size": [4.4],
    "Fuel Type": ["Electric"],
    "Transmission": ["Manual"],
    "Mileage": [143190],
    "Condition": ["Used"],
    "Model": ["5 Series"],
}

import pandas as pd

new_data_df = pd.DataFrame(new_data)

new_data_encoded = preprocessor.transform(new_data_df)

predictions = loaded_lm.predict(new_data_df)

print("predicted car price:", predictions[0])
