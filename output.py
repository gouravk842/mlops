model.add(Dense(units=1, activation='sigmoid'))
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
from keras_preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory(
        "dog&cat/training_set",
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
test_set = test_datagen.flow_from_directory(
        "dog&cat/test_set",
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
a=model.fit(
        training_set,
        steps_per_epoch=800,
        epochs=2,
        validation_data=test_set,
        validation_steps=100)
b=a.history['accuracy'][0]*100
if b >=80:
        model.save('trained.h5')
        exit 1
else:
        exit 0