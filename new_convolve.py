model.add(Convolution2D(filters=32,
                        kernel_size=(3,3),
                        activation='relu'
                        ))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Convolution2D(filters=32,
                        kernel_size=(3,3),
                        activation='relu'
                        ))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Convolution2D(filters=32,
                        kernel_size=(3,3),
                        activation='relu'
                        ))
model.add(MaxPooling2D(pool_size=(2,2)))

