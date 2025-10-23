# Movie-Spoiler
Spoiler Detection in Movie Reviews using DL:  An Chrome extension to classify movie reviews as spoilers or non-spoilers.
This project aims to detect whether a given movie or book review contains spoilers using Natural Language Processing (NLP) and Deep Learning. The model uses a Bidirectional LSTM (BiLSTM) network to capture contextual meaning from text and classify reviews as spoiler or non-spoiler.
**Features**
  - Text preprocessing and tokenization using Keras Tokenizer
  - Word embedding with Embedding Layer
  - Bidirectional LSTM model for sequence understanding
  - Trains, validates, and evaluates the model on labeled review data
  - Supports saving model checkpoints and evaluating performance
    
**Model Architecture**
  Embedding → BiLSTM → Dropout → Dense(ReLU) → Dropout → Dense(Sigmoid)
  - Embedding Layer: Converts words into dense vector representations
  - BiLSTM Layer: Learns contextual dependencies from both directions
  - Dropout Layers: Reduce overfitting
  - Dense Layers: Perform final classification

**Dataset**
  - The dataset contains reviews labeled as spoiler (1) or non-spoiler (0).
  - Each review is preprocessed (tokenized, padded, and truncated) to a fixed length of 512 tokens.

**Training Details**
  - Tokenizer: 30,000 vocabulary size
  - Max Sequence Length: 512
  - Embedding Dimension: 100
  - Loss Function: Binary Crossentropy
  - Optimizer: Adam
  - Evaluation Metric: Accuracy

**Results**
  - Achieved strong accuracy in classifying spoiler vs non-spoiler reviews
  - Model successfully captures contextual meaning using BiLSTM architecture

**Technologies Used**
  - Python
  - TensorFlow / Keras
  - NumPy, Pandas
  - Scikit-learn
  - NLP preprocessing
