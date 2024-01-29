#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cecile capponi, AMU
L3 Informatique, 2023/24
"""

"""
Computes a representation of an image from the (gif, png, jpg...) file 
-> representation can be (to extend) 
'HC': color histogram
'PX': tensor of pixels
'GC': matrix of gray pixels 
other to be defined
--
input = an image (jpg, png, gif)
output = a new representation of the image
"""    
def raw_image_to_representation(image, representation):

    return None

"""
Returns a relevant structure embedding train images described according to the 
specified representation and associate each image (name or/and location) to its label.
-> Representation can be (to extend) 
'HC': color histogram
'PX': tensor of pixels 
'GC': matrix of gray pixels
other to be defined
--
input = where are the examples, which representation of the data must be produced ? 
output = a relevant structure (to be discussed, see below) where all the images of the
directory have been transformed, named and labelled according to the directory they are
stored in (the structure lists all the images, each image is made up of 3 informations,
namely its name, its representation and its label)
This structure will later be used to learn a model (function learn_model_from_dataset)
-- uses function raw_image_to_representation
"""
def load_transform_label_train_dataset(directory, representation):
    return None
    
    
"""
Returns a relevant structure embedding test images described according to the 
specified representation.
-> Representation can be (to extend) 
'HC': color histogram
'PX': tensor of pixels 
'GC': matrix of gray pixels 
other to be defined
--
input = where are the data, which represenation of the data must be produced ? 
output = a relevant structure, preferably the same chosen for function load_transform_label_train_data
-- uses function raw_image_to_representation
-- must be consistant with function load_transform_label_train_dataset
-- while be used later in the project
"""
def load_transform_test_dataset(directory, representation):
    return None

"""
Learn a model (function) from a pre-computed representation of the dataset, using the algorithm 
and its hyper-parameters described in algo_dico
For example, algo_dico could be { algo: 'decision tree', max_depth: 5, min_samples_split: 3 } 
or { algo: 'multinomial naive bayes', force_alpha: True }
--
input = transformed labelled dataset, the used learning algo and its hyper-parameters (better a dico)
output =  a model fit with data
"""
def learn_model_from_dataset(train_dataset, algo_dico):
    model = None
    return model

"""
Given one example (previously loaded with its name and representation),
computes its class according to a previously learned model.
--
input = representation of one data, the learned model
output = the label of that one data (+1 or -1)
-- uses the model learned by function learn_model_from_dataset
"""
def predict_example_label(example, model):
    label = 1  # could be -1
    return label


"""
Computes a structure that computes and stores the label of each example of the dataset, 
using a previously learned model. 
--
input = a structure embedding all transformed data to a representation, and a model
output =  a structure that associates a label to each identified data (image) of the input dataset
"""
def predict_sample_label(dataset, model):
    predictions = None
    return predictions

"""
Save the predictions on dataset to a text file with syntax:
image_name <space> label (either -1 or 1)  
NO ACCENT  
In order to be perfect, the first lines of this file should indicate the details
of the learning methods used, with its hyper-parameters (in order to do so, the signature of
the function must be changed, as well as the signatures of some previous functions in order for 
these details to be transmitted along the pipeline. 
--
input = where to save the predictions, structure embedding the dataset
output =  OK if the file has been saved, not OK if not
"""
def write_predictions(directory, filename, predictions):
    return None

"""
Estimates the accuracy of a previously learned model using train data, 
either through CV or mean hold-out, with k folds.
input = the train labelled data as previously structured, the type of model to be learned
(as in function learn_model_from_data), and the number of split to be used either 
in a hold-out or by cross-validation 
output =  The score of success (betwwen 0 and 1, the higher the better, scores under 0.5
are worst than random guess)
"""
def estimate_model_score(train_dataset, algo_dico, k):
    return None

    
