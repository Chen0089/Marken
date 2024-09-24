import lightly
from lightly.api import Client
from lightly.dataset import Dataset

client = Client(api_key='your_api_key')

dataset = Dataset.from_folder('models')
client.upload_dataset(dataset)

# (Assuming you have a chat model architecture defined)
def train_model(data):
    # Your training code here
    pass

# Load your data and train
data = client.get_dataset('dataset_id')
train_model(data)

# Save your trained model for inference
