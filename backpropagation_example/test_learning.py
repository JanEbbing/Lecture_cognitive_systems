from perceptron import Classifier_Perceptron
my_perc = Classifier_Perceptron(activation_function=lambda x:x)
mydata = [ ((-0.4,0.8),1),((-0.8,-0.2),1),((0.3,1.6),-1),((-0.4,1.5),-1) ]
print(my_perc.train_classification(mydata))
print("Weights: %s" % my_perc.weight_list)
print("Offset: %s" % my_perc.offset)
