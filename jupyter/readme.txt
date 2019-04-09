XGBoost_SHAP --- Training of ML model and usage of SHAP (if all modules are installed, the code can be run step by step)
ExperimentEvaluation --- Evaluation of experiment data, with statistics, plots and significance tests (if all modules are installed, the code can be run step by step)

the .p (pickle) files and the data folder contain data that the jupyter notebooks access





### How to load final data from pickle files into jupyter notebook ###

# Load the model from a pickle in a file
model_0815 = pickle.load( open( "final_model.p", "rb" ) )

# Load the explainer from a pickle in a file 
explainer_0815 = pickle.load( open( "final_explainer.p", "rb" ) )

# Load the shap values from a pickle in a file
shap_values_0815 = pickle.load( open( "final_shapValues.p", "rb" ) )

# Load the set from a pickle in a file
set_0815_shap = pickle.load( open( "final_set.p", "rb" ) )

# Load the test data from a pickle in a file
test_0815 = pickle.load( open( "final_testData.p", "rb" ) )

# Load the train data from a pickle in a file 
train_0815 = pickle.load( open( "final_trainData.p", "rb" ) )

# Load the entire data from a pickle in a file 
pre_train_0815 = pickle.load( open( "final_beforeSplitData.p", "rb" ) )

# Load the test labels from a pickle in a file
y_test_0815 = pickle.load( open( "final_testLabels.p", "rb" ) )

# Load the train labels from a pickle in a file
y_train_0815 = pickle.load( open( "final_trainLabels.p", "rb" ) )

# Load the test data reduced values from a pickle in a file
test_df_reduced = pickle.load( open( "final_testDataReduced.p", "rb" ) )

# Load the predict from a pickle in a file
predict = pickle.load( open( "final_prediction.p", "rb" ) )

# Load the predict train from a pickle in a file
predict_train = pickle.load( open( "predict_train.p", "rb" ) )

# Load the df reduced from a pickle in a file
df_reduced = pickle.load( open( "df_reduced.p", "rb" ) )