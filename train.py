from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import math
from itertools import cycle
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, learning_curve, KFold
k_fold= 5
kf = KFold(n_splits = k_fold, random_state=35, shuffle=True) 
total_accuracy = 0
total_mse = 0
total_rmse = 0
num_classes = 4
total_recall=0
total_precision=0
total_f1=0


for train_index, test_index in kf.split(x_all):
  
    X_train, X_test = x_all.iloc[train_index, :],x_all.iloc[test_index, :]
    y_train, y_test = y_all[train_index], y_all[test_index] 
    model = build_model(X_train,y_train)

    pred_values = np.round(model.run(np.array(X_test)))
    y_test=np.array(y_test)
    y_test=y_test.astype(np.int)

    y_true = np.zeros((len(y_test), num_classes))
    for i in range(len(y_test)):
        y_true[i, y_test[i]-1] = 1


    acc = accuracy_score(y_true,pred_values.T)
    print ("-----------------------------------")
    print("Accuracy: {0}".format(acc))
    print(sklearn.metrics.classification_report(y_true,pred_values.T))

    total_accuracy+=acc
    
    MSE = mean_squared_error(y_true,pred_values.T)
    print("\n")
    print("Mean Square Error:")
    print(MSE)    
    total_mse+=MSE
    RMSE = math.sqrt(MSE)
    print("\n")
    print("Root Mean Square Error:")
    print(RMSE)
    total_rmse+=RMSE
    
    recall=recall_score(y_true,pred_values.T, average='weighted')
    total_recall+=recall

    precision=precision_score(y_true,pred_values.T, average='weighted')
    total_precision+=precision

    f1=f1_score(y_true,pred_values.T, average='weighted')
    total_f1+=f1

    # Compute ROC curve and ROC area for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    i=1
    for i in range(num_classes):
        fpr[i], tpr[i], _ = roc_curve(y_true[:, i], pred_values.T[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    plt.figure()
    colors = cycle(['red','green', 'darkorange', 'cornflowerblue'])
    lw = 2
    i=1
    for i, color in zip(range(num_classes), colors):
      
        plt.plot(fpr[i], tpr[i], color=color, lw=lw, label=' {0}st class ROC curve (AUC = {1:0.2f})'''.format(i, roc_auc[i]))

    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc="lower right")
    plt.show()


print("Average accuracy :", (float) (total_accuracy/k_fold))
print("Average MSE :", (float) (total_mse/k_fold))
print("Average RMSE :", (float) (total_rmse/k_fold))
print("Average precision :", (float) (total_precision/k_fold))
print("Average recall :", (float) (total_recall/k_fold))
print("Average f1 :", (float) (total_f1/k_fold))
