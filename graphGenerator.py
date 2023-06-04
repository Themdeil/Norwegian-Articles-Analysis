import os
import csv
import matplotlib.pyplot as plt
import numpy as np
# Define the TSV file path
tsv_file_da = 'da-2005.tsv' # Rouge GAUCHE
tsv_file_ap = 'ap-2005.tsv' # Bleu DROITE

# Define the output folder path
output_folder = 'graphs'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Read the TSV data
data_da = []
with open(tsv_file_da, 'r') as tsvfile_da:
    reader = csv.reader(tsvfile_da, delimiter='\t')
    for row in reader:
        data_da.append(row)

# Get the headers and remove the 'Index' column
headers_da = data_da[0][1:]

# Get the index values to plot
indices = [row[0][:4] for row in data_da]
indices_sorted = sorted(set(indices))  # Sort and remove duplicates
index_interval = max(len(indices_sorted) // 10, 1)
indices_to_plot_da = indices_sorted[::index_interval]

# Remove the headers and 'Index' column from the data
data_da = data_da[1:]
data_da = [[int(value) for value in row[1:]] for row in data_da]



data_ap = []
with open(tsv_file_ap, 'r') as tsvfile_ap:
    reader = csv.reader(tsvfile_ap, delimiter='\t')
    for row in reader:
        data_ap.append(row)

# Get the headers and remove the 'Index' column
headers_ap = data_ap[0][1:]

# Get the index values to plot
indices = [row[0][:4] for row in data_ap]
indices_sorted = sorted(set(indices))  # Sort and remove duplicates
index_interval = max(len(indices_sorted) // 10, 1)
indices_to_plot_ap = indices_sorted[::index_interval]

# Remove the headers and 'Index' column from the data
data_ap = data_ap[1:]
data_ap = [[int(value) for value in row[1:]] for row in data_ap]

header = ["likestilling","voldta"]
# Iterate over each word and generate a line graph
for i, word in enumerate(header):
    # Get the counts for the current word
    if word == "voldta":
        a = 4
        b = 5
    if word == "likestilling":
        a = 0
        b = 2
    counts_da = [row[a] for row in data_da]

    counts_ap = [row[b] for row in data_ap]
    
    fig, ax1 = plt.subplots()  # Subplot for Plot 1
    new_da = np.linspace(0, len(counts_da), num=len(counts_ap))
    new_counts = np.interp(new_da, range(len(counts_da)), counts_da)
    # Create a line graph
    ax1.plot(range(len(new_counts)), new_counts, color='r', label='Dagsavisen')
    ax1.plot(range(len(counts_ap)), counts_ap, color='b', label='Aftenposten')
    plt.xlabel("Nbr d'articles")
    plt.ylabel("Nbr d'apparution")
    plt.title(f'Occurrences du mot "{word}" dans Dagsavisen et Aftenposten en 2005')
    plt.legend()
    # Set the x-tick locations and labels
    xticks_da = [indices.index(index) for index in indices_to_plot_da]
    #plt.xticks(xticks_da, indices_to_plot_da, rotation=90)

    # Save the graph as a PNG file
    output_file = os.path.join(output_folder, f'{word}_{tsv_file_da}_line.png')
    plt.savefig(output_file)
    plt.close()

print(f"Line graphs saved in {output_folder}")