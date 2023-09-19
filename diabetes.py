import numpy as np
import pickle



loaded_model = pickle.load(open('trained_model.sav','rb'))
input_data = ()
input_data = np.asarray(input_data).reshape(1,-1)

prediction = loaded_model.predict(input_data)
print(prediction)

if (prediction == 0):
    print('The person is not Diabetic')

else:
    print('The person is Diabetic')


