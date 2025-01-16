import re

# Read the original file content
with open('The Origin - Chunks.md', 'r') as file:
    content = file.read()

# Define a function to process clusters
def process_clusters(content):
    # First regex: Bold all Cluster x: occurrences correctly
    content = re.sub(r'(Cluster \d+:)', r'**\1**', content)

    # Second regex: Transform all Description: to \n**Description:**
    content = re.sub(r'\nDescription:', r'  \n**Description:**', content)

    # Third regex: Transform all Keywords: to \n**Keywords:**
    content = re.sub(r'\nKeywords:', r'  \n**Keywords:**', content)

    return content

# Process the content
formatted_content = process_clusters(content)

# Save the transformed content to a new file
with open('The Origin - Transformed_Chunks.md', 'w') as file:
    file.write(formatted_content)

print("The clusters have been successfully reformatted and saved to 'The Origin - Transformed_Chunks.md'.")
