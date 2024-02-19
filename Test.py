import architecture
from PIL import Image
import matplotlib.pyplot as plt
image_path_mer = "./testimage/Mer.jpeg" 
image_path_mountain = "./testimage/Mountain.jpeg"
image_path_list = [image_path_mer,image_path_mountain]
representation_list = ['HC','GC','PX']
####TestRepresentation####
def test_representation():
    for path in image_path_list:
        print(f"Test Image : {path}")
        for rep in representation_list:
            print(f"Representation : {rep}")
            print(f"{list(architecture.raw_image_to_representation(path,rep))}\n")

        print("End Test")

# test_representation()
def test_model() : 

    algo_bayes = { 'algo': 'multinomial naive bayes', 'force_alpha': True }
    algo_tree = { 'algo': 'decision tree', 'max_depth': 5, 'min_samples_split': 3 } 
    algo_list = [algo_bayes,algo_tree]
    datatest =  architecture.load_transform_test_dataset(r"./testimage/", 'GC') 
    data = architecture.load_transform_label_train_dataset(r"./data/Data/",'GC')
    model = architecture.learn_model_from_dataset(data,algo_tree)[0]
    predictions = architecture.predict_sample_label(datatest, model)
    architecture.write_predictions(r".\data\Data", "PrÃ©diction_des_tests2.txt",predictions, algo_tree )
    print("End Test")

print(test_model())


#######TestGlobal#######
choice = int(input('Type de representation: \n saisissez 0 pour GC, 1 pour HC ou 2 pour PX \n '))
Representations =["GC","HC","PX"]
print("Loading Traning Data ...")

data = architecture.load_transform_label_train_dataset("./data/Data/",Representations[choice]) 

algo_bayes = { 'algo': 'multinomial naive bayes', 'force_alpha': True }
algo_tree = { 'algo': 'decision tree', 'max_depth': 5, 'min_samples_split': 3 } 
algo_SVM ={'algo':'SVM', 'dual':'auto','random_state':0}
algo_neighbors = {'algo':'k nearest neighbors', 'n_neighbors': 5 }
choice_algo = int(input("Type d'algo : \n 0 pour multinomial naive0 bayes et 1 pour decision tree et 2 pour SVM  et 3 pour K plus proches voisins "))
algo_list = [algo_bayes,algo_tree,algo_SVM,algo_neighbors]
k = int(input('Number of splits : \n '))
print('Training model ...')
print('Getting Predictions ...')
print('Score :')
print(architecture.estimate_model_score(data,algo_list[choice_algo],k))
