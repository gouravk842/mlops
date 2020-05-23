model.add(Convolution2D(filters=32,
                        kernel_size=(3,3),
                        activation='relu',
                        input_shape=(64, 64, 3)
                        ))
model.add(MaxPooling2D(pool_size=(2,2)))