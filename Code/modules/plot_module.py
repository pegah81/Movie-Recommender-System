import matplotlib.pyplot as plt
import seaborn as sns


def featureAnalysis(feature, dataset):
    a = dataset.describe()
    b = a[feature].to_frame().T
    fig, ax = plt.subplots(2, 1, figsize=(20, 18))
    sns.histplot(x=dataset[feature], data=dataset, kde=True, element="step", ax=ax[0])
    sns.boxplot(data=dataset, x=feature, ax=ax[1])
    return (b)


def barPlot(dataset, feature, color, y, n):
    freq = {}
    total_values = len(dataset)

    for element in dataset[feature]:
        freq[element] = freq.get(element, 0) + 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    elements = [item[0] for item in sorted_freq]
    frequencies = [item[1] for item in sorted_freq]
    elements = elements[::-1]
    frequencies = frequencies[::-1]

    plt.figure(figsize=(20, y))
    plt.barh(elements, frequencies, color=color)

    # Customize the plot
    plt.xlabel('Frequency')
    plt.ylabel('Elements')
    plt.title('Bar Plot with Frequency')

    # Sort the elements based on frequency
    sorted_elements = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

    # Print the top 3 elements, frequencies, and percentages
    for i in range(min(n, len(sorted_elements))):
        element = sorted_elements[i]
        frequency = freq[element]
        percentage = frequency / total_values * 100
        print(f"{element}: Frequency = {frequency}, Percentage = {percentage:.2f}%")
    # Display the plot
    plt.show()
    return sorted_elements
