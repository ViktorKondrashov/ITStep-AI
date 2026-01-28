import onnxruntime as ort
from torchvision import transforms
from PIL import Image
import numpy as np


# назви класів(порід собак)
class_names = [
    'beagle',
    'bulldog',
    'dalmatian',
    'german-shepherd',
    'husky',
    'labrador-retriever',
    'poodle',
    'rottweiler'
]

# відкриваємо модель
session = ort.InferenceSession(
    "model.onnx"
)

# трансформер
test_transformer = transforms.Compose([
       transforms.Resize([224, 224]),
       transforms.ToTensor()
])

# отримати зображення
img = Image.open("data/lesson many/husky10.jpg")

# застовусавти трансформер
input_tensor = test_transformer(img)

# змінюємо shape(добавити 1)
input_tensor = input_tensor.unsqueeze(0)

# перевести в numpy
input_tensor = input_tensor.numpy()

# використання моделі
results = session.run(
    None,  # отримати всі результати
    input_feed={
        "image": input_tensor
    }
)

result = results[0][0]
print(result)

# отримати індекс де найбільша ймовірність
ind = result.argmax()

# тримати назву класу
label = class_names[ind]

# отримати ймовірність
# softmax
max_num = result.max()
result -= max_num
exp_result = np.exp(result)
probs = exp_result / exp_result.sum()

prob = probs[ind]

print(f"Індекс найбільшої ймовірності: {ind}")
print(f"Порода собаки: {label}")
print(f"Ймовірність: {prob}")

img.show(f"{label} {prob:.2f}%")