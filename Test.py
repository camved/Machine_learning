import architecture
from PIL import Image
import matplotlib.pyplot as plt
from alive_progress import alive_bar
from datetime import datetime

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
    architecture.write_predictions(r"./Test", "Prediction_des_tests2.txt",predictions, algo_tree )
    print("End Test")

# print(test_model())


#######TestGlobal#######
# choice = int(input('Type de representation: \n saisissez 0 pour GC, 1 pour HC ou 2 pour PX \n '))
# Representations =["GC","HC","PX"]
# print("Loading Traning Data ...")

# data = architecture.load_transform_label_train_dataset("./data/Data/",Representations[choice]) 

# algo_bayes = { 'algo': 'multinomial naive bayes', 'force_alpha': True }
# algo_tree = { 'algo': 'decision tree', 'max_depth': 5, 'min_samples_split': 3 } 
# algo_SVM ={'algo':'SVM', 'dual':'auto','random_state':0}
# algo_neighbors = {'algo':'k nearest neighbors', 'n_neighbors': 5 }
# choice_algo = int(input("Type d'algo : \n 0 pour multinomial naive bayes,  1 pour decision tree,  2 pour SVM  ou 3 pour K plus proches voisins \n "))
# algo_list = [algo_bayes,algo_tree,algo_SVM,algo_neighbors]
# k = int(input('Number of splits : \n '))
# print('Training model ...')
# print('Getting Predictions ...')
# print('Score :')
# print(architecture.estimate_model_score(data,algo_list[choice_algo],k))


def automated_tester():
    algo_bayes = { 'algo': 'multinomial naive bayes', 'force_alpha': True }
    algo_tree = { 'algo': 'decision tree', 'max_depth': 5, 'min_samples_split': 3 } 
    algo_SVM ={'algo':'SVM', 'dual':'auto','random_state':0}
    algo_neighbors = {'algo':'k nearest neighbors', 'n_neighbors': 5 }
    algo_list = [algo_bayes,algo_tree,algo_SVM,algo_neighbors]
    Representations =["GC","HC","PX"]
    list_of_splits = [4,3,7,9,10]
    output =""
    for rep in Representations:
        
        data = architecture.load_transform_label_train_dataset("./data/Data/",rep) 
        output += f"##Representation {rep} :\n"
    
        for algo in algo_list:
            output+= "#"+str(algo)+"  \n"
            with alive_bar() as bar:
                for k in list_of_splits:
                    output += f"Number of splits {k} :\n"+ str(architecture.estimate_model_score(data,algo,k))+"\n"
                    bar()
    return output

def wrtite_log_file(log):
    file = open(r"./Test/"+str(datetime.now().strftime("%H_%M_%S"))+".md",'w') 
    file.write(log)  
    file.close()
wrtite_log_file(automated_tester())


############Test#############
#print(architecture.transform_horizontally(r"./testimage/PlageAgadirmaroc.jpg",2,1))
#print(architecture.couper_image(r'./Test/image_etiree.jpg'))

