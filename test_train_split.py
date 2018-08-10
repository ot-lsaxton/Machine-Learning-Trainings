import pandas as pd

df = pd.read_csv('Titanic.csv')

sample_size = int(df.shape[0] / 3)

training_data = df.sample(n=sample_size*2)

testing_data = df.sample(n=sample_size)

print(training_data.shape, testing_data.shape)

training_data.to_csv('training.csv', index=False)
testing_data.to_csv('testing.csv', index=False)