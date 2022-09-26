import joblib
def predict(data):
	prediction_model = joblib.load('combinations.sav')
	return prediction_model.predict(data)