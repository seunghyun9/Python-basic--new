from keras.datasets import mnist
import tensorflow as tf
from matplotlib import pyplot as plt

_, (x_test, y_test) = mnist.load_data()
x_test = x_test / 255.0 # 데이터 정규화

# 모델 불러오기
model = tf.keras.models.load_model('./save/mnist_model.h5')
model.summary()
plt.imshow(x_test[20],cmap="gray")
plt.show()

picks = [20]
y_prod = model.predict(x_test[picks], verbose=0)
predicted = y_prod.argmax(axis=1)
print("손글씨 예측값:",predicted)

