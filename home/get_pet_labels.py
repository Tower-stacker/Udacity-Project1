#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Gregory Cain
# DATE CREATED:       10 /9/2021                        
# REVISED DATE:       10/9/2021
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
import os

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 

def get_pet_labels(image_dir):

    filename_list = listdir("pet_images/")
    print("\nPrints 10 filenames from folder pet_images/")
    for idx in range(0, 10, 1):
        print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )

    in_files = listdir("pet_images/")  
    results_dic = dict()

    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
            pet_labels = ""
            name_l = in_files[idx].lower()
            name_s = name_l.split("_")
            pet_name=""
            for word in name_s:
                    if word.isalpha():
                        pet_name += word + " "
                        pet_labels = pet_name.strip()
                    continue
        else:                        
            continue
                    
    results_dic[in_files[idx]] = [pet_labels] 

    items_in_dic = len(results_dic)
    print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

    if in_files[idx] not in results_dic:
        print('adding {} to {}'.format([pet_labels], in_files[idx]))
    else:
        print("** Warning: Key=", in_files[idx], 
               "already exists in results_dic with value =", 
               results_dic[in_files[idx]])
    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
        print("Filename=", key, "   Pet Label=", results_dic[key][0])

    return results_dic
