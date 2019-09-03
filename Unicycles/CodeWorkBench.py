# using VDC for coding, then copying into Colab

# Directory with our training bicycle pictures
train_bicycle_dir = os.path.join('//tmp/Training_Unicycle_Bicycle/Bicycle')

# Directory with our training unicycle pictures
train_unicycle_dir = os.path.join('/tmp/Training_Unicycle_Bicycle/Unicycle')

# Directory with our validation bicycle pictures
validation_bicycle_dir = os.path.join('/tmp/Validation_Unicycle_Bicycle/Bicycle')

# Directory with our validation unicycle pictures
validation_unicycle_dir = os.path.join('/tmp/Validation_Unicycle_Bicycle/Unicycle')

train_bicycle_names = os.listdir(train_bicycle_dir)
print(train_bicycle_names[:10])

train_unicycle_names = os.listdir(train_unicycle_dir)
print(train_unicycle_names[:10])

validation_bicycle_names = os.listdir(validation_bicycle_dir)
print(train_bicycle_names[:10])

validation_unicycle_names = os.listdir(validation_unicycle_dir)
print(train_unicycle_names[:10])

##

print('total training bicycle images:', len(os.listdir(train_bicycle_dir)))
print('total training unicycle images:', len(os.listdir(train_unicycle_dir)))
print('total validation bicycle images:', len(os.listdir(validation_bicycle_dir)))
print('total validation unicycle images:', len(os.listdir(validation_unicycle_dir)))


##

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# All images will be rescaled by 1./255
train_datagen = ImageDataGenerator(rescale=1/255)
validation_datagen = ImageDataGenerator(rescale=1/255)

# Flow training images in batches of 20 using train_datagen generator
train_generator = train_datagen.flow_from_directory(
        '/tmp/Training_Unicycle_Bicycle',  # This is the source directory for training images
        target_size=(300, 300),  # All images will be resized to 300x300
        batch_size=80,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')

# Flow training images in batches of 128 using train_datagen generator
validation_generator = validation_datagen.flow_from_directory(
        '/tmp/Validation_Unicycle_Bicycle',  # This is the source directory for training images
        target_size=(300, 300),  # All images will be resized to 150x150
        batch_size=20,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')

##



history = model.fit_generator(
      train_generator,
      steps_per_epoch=11,  
      epochs=15,
      verbose=1,
      validation_data = validation_generator,
      validation_steps=11)

##

import numpy as np
import random
from tensorflow.keras.preprocessing.image import img_to_array, load_img

# Let's define a new Model that will take an image as input, and will output
# intermediate representations for all layers in the previous model after
# the first.
successive_outputs = [layer.output for layer in model.layers[1:]]
#visualization_model = Model(img_input, successive_outputs)
visualization_model = tf.keras.models.Model(inputs = model.input, outputs = successive_outputs)
# Let's prepare a random input image from the training set.
bicycle_img_files = [os.path.join(train_bicycle_dir, f) for f in train_bicycle_names]
unicylce_img_files = [os.path.join(train_unicycle_dir, f) for f in train_unicycle_names]
img_path = random.choice(bicycle_img_files + unicylce_img_files)

img = load_img(img_path, target_size=(300, 300))  # this is a PIL image
x = img_to_array(img)  # Numpy array with shape (150, 150, 3)
x = x.reshape((1,) + x.shape)  # Numpy array with shape (1, 150, 150, 3)

# Rescale by 1/255
x /= 255

# Let's run our image through our network, thus obtaining all
# intermediate representations for this image.
successive_feature_maps = visualization_model.predict(x)

# These are the names of the layers, so can have them as part of our plot
layer_names = [layer.name for layer in model.layers]

# Now let's display our representations
for layer_name, feature_map in zip(layer_names, successive_feature_maps):
  if len(feature_map.shape) == 4:
    # Just do this for the conv / maxpool layers, not the fully-connected layers
    n_features = feature_map.shape[-1]  # number of features in feature map
    # The feature map has shape (1, size, size, n_features)
    size = feature_map.shape[1]
    # We will tile our images in this matrix
    display_grid = np.zeros((size, size * n_features))
    for i in range(n_features):
      # Postprocess the feature to make it visually palatable
      x = feature_map[0, :, :, i]
      x -= x.mean()
      x /= x.std()
      x *= 64
      x += 128
      x = np.clip(x, 0, 255).astype('uint8')
      # We'll tile each filter into this big horizontal grid
      display_grid[:, i * size : (i + 1) * size] = x
    # Display the grid
    scale = 20. / n_features
    plt.figure(figsize=(scale * n_features, scale))
    plt.title(layer_name)
    plt.grid(False)
    plt.imshow(display_grid, aspect='auto', cmap='viridis')