import architecture


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

#test_representation()
        


#######TestGlobal#######
train = architecture.load_transform_label_train_dataset("./data/Data/",'PX')    
test = architecture.load_transform_test_dataset("./testimage/",'HC')   
algo_dico = { 'algo': 'multinomial naive bayes', 'force_alpha': True }
model = architecture.learn_model_from_dataset(train,algo_dico)
predections = architecture.predict_sample_label(test,model[0])
architecture.write_predictions("./","first",predections,algo_dico)

