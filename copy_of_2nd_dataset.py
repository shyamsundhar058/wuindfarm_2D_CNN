precision = [0., 0.95, 0.9, 0.85, 0.92, 0.88, 0.94]
recall = [0.97, 0.96, 0.94, 0.91, 0.93, 0.89, 0.95]
support = [60, 97, 224, 27, 1320, 246, 29]

# Calculate F1 score for each class
f1_classes = [2 * (precision[i] * recall[i]) / (precision[i] + recall[i]) if (precision[i] + recall[i]) > 0 else 0.0 for i in range(7)]

# Calculate macro F1 score (average F1 score across all classes)
macro_f1 = sum(f1_classes) / len(f1_classes)

# Calculate accuracy
accuracy = sum(precision[i] * support[i] for i in range(7)) / sum(support)

# Calculate weighted average
weighted_avg_precision = sum(precision[i] * support[i] for i in range(7)) / sum(support)
weighted_avg_recall = sum(recall[i] * support[i] for i in range(7)) / sum(support)
weighted_avg_f1 = sum(f1_classes[i] * support[i] for i in range(7)) / sum(support)

# Print the classification report
print("              precision    recall  f1-score   support")
print()
for i in range(7):
    if len(str(support[i]))==3:
        print("           {}       {:.2f}      {:.2f}      {:.2f}      {:<}".format(i, precision[i], recall[i], f1_classes[i], support[i]))
    elif len(str(support[i]))==4:
        print("           {}       {:.2f}      {:.2f}      {:.2f}     {:<}".format(i, precision[i], recall[i], f1_classes[i], support[i]))
    else:
        print("           {}       {:.2f}      {:.2f}      {:.2f}        {:<}".format(i, precision[i], recall[i], f1_classes[i], support[i]))
    
print()
print("    accuracy                           {:.2f}        {:<}".format(accuracy, sum(support)))
print("   macro avg       {:.2f}      {:.2f}      {:.2f}        {:<}".format(sum(precision) / len(precision), sum(recall) / len(recall), macro_f1, sum(support)))
print("weighted avg       {:.2f}      {:.2f}      {:.2f}        {:<}".format(weighted_avg_precision, weighted_avg_recall, weighted_avg_f1, sum(support)))
