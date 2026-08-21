import tensorflow as tf
from tensorflow.keras import layers, models


# ============================================================
# 1. CARREGAMENTO DO DATASET MNIST
# ============================================================

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


# ============================================================
# 2. PRÉ-PROCESSAMENTO
# ============================================================

# Adiciona o canal da imagem:
# (28, 28) -> (28, 28, 1)

x_train = x_train[..., None]
x_test = x_test[..., None]

# Normaliza os pixels:
# 0   -> 0.0
# 255 -> 1.0

x_train = x_train / 255.0
x_test = x_test / 255.0


# ============================================================
# 3. CONSTRUÇÃO DA CNN
# ============================================================

model = models.Sequential([

    # Entrada
    layers.Input(shape=(28, 28, 1)),

    # CONVOLUÇÃO 1
    layers.Conv2D(
        filters=32,
        kernel_size=3,
        activation='relu'
    ),

    # MAX POOLING 1
    layers.MaxPooling2D(pool_size=2),

    # CONVOLUÇÃO 2
    layers.Conv2D(
        filters=64,
        kernel_size=3,
        activation='relu'
    ),

    # MAX POOLING 2
    layers.MaxPooling2D(pool_size=2),

    # TRANSFORMA MATRIZ EM VETOR
    layers.Flatten(),

    # CAMADA DENSAMENTE CONECTADA
    layers.Dense(
        64,
        activation='relu'
    ),

    # SAÍDA: 10 CLASSES
    layers.Dense(
        10,
        activation='softmax'
    )
])


# ============================================================
# 4. COMPILAÇÃO
# ============================================================

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)


# ============================================================
# 5. RESUMO DA REDE
# ============================================================

model.summary()


# ============================================================
# 6. TREINAMENTO
# ============================================================

model.fit(
    x_train,
    y_train,
    epochs=2,
    batch_size=128,
    validation_split=0.1
)


# ============================================================
# 7. AVALIAÇÃO
# ============================================================

resultado = model.evaluate(
    x_test,
    y_test,
    verbose=0
)

print("Resultado:", resultado)


# ============================================================
# 8. SALVAMENTO
# ============================================================

model.save("modelo_mnist.keras")