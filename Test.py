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
Representations =["GC","HC"]
print("Loading Traning Data ...")
train = architecture.load_transform_label_train_dataset("./data/Data/",'HC') 
print("Loading Testing Data ...")   
test = architecture.load_transform_test_dataset("./testimage/",'HC')   
algo_bayes = { 'algo': 'multinomial naive bayes', 'force_alpha': True }
algo_tree = { 'algo': 'decision tree', 'max_depth': 5, 'min_samples_split': 3 } 
print('Training model ...')
print(architecture.estimate_model_score(train,algo_tree,2))
# model = architecture.learn_model_from_dataset(train,algo_tree)
# print('Getting Predictions ...')
# predections = architecture.predict_sample_label(test,model[0])
# architecture.write_predictions(".","Predections.txt",predections,algo_bayes)

