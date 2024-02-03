import architecture
from PIL import Image

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
        


#######TestGlobal#######
choice = int(input('Type de representation: \n 0 pour GC et 1 pour HC '))
choice = int(input('Type de representation: \n 0 pour GC et 1 pour HC'))
Representations =["GC","HC"]
print("Loading Traning Data ...")

data = architecture.load_transform_label_train_dataset("./data/Data/",Representations[choice]) 


train = architecture.load_transform_label_train_dataset("./data/Data/",Representations[choice]) 

print("Loading Testing Data ...") 

test = architecture.load_transform_test_dataset("./testimage/",Representations[choice]) 

algo_bayes = { 'algo': 'multinomial naive bayes', 'force_alpha': True }
algo_tree = { 'algo': 'decision tree', 'max_depth': 5, 'min_samples_split': 3 } 
choice_algo = int(input("Type d'algo : \n 0 pour multinomial naive bayes et 1 pour decision tree "))
algo_list = [algo_bayes,algo_tree]
k = int(input('Number of splits : \n '))
choice_algo = int(input("Type d'algo : \n 0 pour multinomial naive bayes et 1 pour decision tree"))
algo_list = [algo_bayes,algo_tree]
print('Training model ...')
model = architecture.learn_model_from_dataset(train,algo_list[choice_algo])
print('Getting Predictions ...')
print('Score :')
print(architecture.estimate_model_score(data,algo_list[choice_algo],k))

