#!/bin/bash

# Get user input for folder name
read -p "Enter the folder name: " folder_name

# Create a new folder
mkdir "$folder_name"

# Change into the new folder
cd "$folder_name"

# Get user input for the number of files
read -p "Enter the number of files to create: " num_files

# Create multiple files
for ((i=1; i<=$num_files; i++))
do
  touch "file$i.txt"
done

# Display a message
echo "New folder '$folder_name' and $num_files files created successfully!"
