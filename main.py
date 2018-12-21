from lstm import main_LSTM
from cnn import main_CNN
from fast_text import main_fast_text
from nn_classifier import main_nn

#main_LSTM()
#main_CNN()
#main_fast_text()
main_nn("svm_rbf")
# "gradient_boosting" "random_forest" "svm_rbf" "svm_linear"