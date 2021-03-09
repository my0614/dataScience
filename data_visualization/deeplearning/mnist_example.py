import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense

(x_train, y_train), (x_test,y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test/255.0

ds = tf.data.Dataset.from_tensor_slices((x_train,y_train)).shuffle(10000)
train_size = int(len(x_train)*0.7) #학습셋:검증셋 비율
train_ds =ds.take(train_size).batch(20) #batch -> 학습시 샘플 수
val_ds = ds.skip(train_size).batch(20)

model = Sequential()
model.add(Flatten(input_shape=(28,28))) # 입력층 (2차원을 평면화)
model.add(Dense(20, activation = 'relu')) #은닉층
model.add(Dense(20, activation = 'relu')) #은닉층
model.add(Dense(10, activation = 'softmax')) #출력층 (숫자 0~9)

model.compile(loss='sparse_categorical_crossentropy', optimizer= 'sgd', metrics = ['accuracy'])

#모델학습
hist = model.fit(train_ds, validation_data= val_ds, epochs= 10)  #fit ->학습 ,epochs ->학습횟수
print('모델 평가')
model.evaluate(x_test, y_test) #evaluate -> 성능평가평가
model.summary()
model.save('mnist_model.h5')

fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'],'y',label='train loss')
loss_ax.plot(hist.history['val_loss'],'r',label='val loss')

acc_ax.plot(hist.history['accuracy'],'b',label = 'train acc')
acc_ax.plot(hist.history['val_accuracy'],'g',label = 'val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')

acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')
plt.show()
