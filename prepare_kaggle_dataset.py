#!/usr/bin/env python
# coding: utf-8

"""
Dataset Preparation Script for News Category Classification Project
Author: Muhammet Ali Yoldar (200444035)
Turkish Aeronautical Association University

This script prepares the Kaggle News Category Dataset
for use with the BBC News Classification notebook.
"""

import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create directories if they don't exist
os.makedirs('inputs', exist_ok=True)
os.makedirs('models', exist_ok=True)
os.makedirs('outputs', exist_ok=True)

print("Processing Kaggle News Category Dataset...")

# Use the manually downloaded dataset file
news_file = "News_Category_Dataset_v3.json"
print(f"Loading dataset from: {news_file}")

# Read the JSON file line by line
data = []
with open(news_file, 'r', encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line))
        
# Convert to DataFrame
df_news = pd.DataFrame(data)

print(f"Original dataset shape: {df_news.shape}")
print(f"Number of unique categories: {df_news['category'].nunique()}")

# Analyze category distribution
category_counts = df_news['category'].value_counts()
print("\nAll categories in the dataset:")
print(category_counts)

# Create a combined text field for all articles
df_news['text'] = df_news['headline'] + ' ' + df_news['short_description']

# Create a mapping for BBC categories to similar Kaggle categories
bbc_category_mapping = {
    'business': ['BUSINESS', 'MONEY', 'FINANCE', 'ECONOMIC'],
    'entertainment': ['ENTERTAINMENT', 'ARTS', 'CULTURE', 'COMEDY', 'ARTS & CULTURE', 'MEDIA'],
    'politics': ['POLITICS', 'WORLDPOST', 'WORLD NEWS', 'WORLD'],
    'sport': ['SPORTS', 'SPORT'],
    'tech': ['TECH', 'SCIENCE & TECH', 'TECHNOLOGY', 'SCIENCE']
}

# Select articles from categories similar to BBC categories
selected_articles = pd.DataFrame()
for bbc_category, kaggle_categories in bbc_category_mapping.items():
    category_articles = df_news[df_news['category'].isin(kaggle_categories)].copy()
    if len(category_articles) > 0:
        # Label with BBC category name
        category_articles['labels'] = bbc_category
        selected_articles = pd.concat([selected_articles, category_articles])

# Reset index after concatenation
selected_articles = selected_articles.reset_index(drop=True)

print(f"\nSelected articles from categories similar to BBC categories:")
for category in sorted(selected_articles['labels'].unique()):
    count = len(selected_articles[selected_articles['labels'] == category])
    print(f"{category}: {count} articles")

# Create a simple dataset with just labels and text (matching BBC format)
bbc_format_data = pd.DataFrame({
    'labels': selected_articles['labels'],
    'text': selected_articles['text']
})

print(f"\nFinal dataset shape: {bbc_format_data.shape}")

# Save the prepared dataset to CSV
output_path = 'inputs/news_category_dataset.csv'
bbc_format_data.to_csv(output_path, index=False)
print(f"Dataset saved to {output_path}")

# Visualize the distribution of BBC-like categories
plt.figure(figsize=(10, 6))
sns.countplot(y=bbc_format_data['labels'], order=bbc_format_data['labels'].value_counts().index)
plt.title('Distribution of BBC-like Categories in Kaggle Dataset')
plt.tight_layout()
plt.savefig('outputs/bbc_categories_distribution.png')
plt.close()

# Save category mapping for reference
with open('inputs/category_mapping.json', 'w') as f:
    json.dump({
        "bbc_categories": sorted(bbc_format_data['labels'].unique().tolist()),
        "mapping_used": bbc_category_mapping,
        "category_counts": {category: len(bbc_format_data[bbc_format_data['labels'] == category]) 
                            for category in sorted(bbc_format_data['labels'].unique())}
    }, f, indent=2)

print("\nDataset preparation complete! You can now use this dataset in your notebook.")
print("To use this dataset, replace the original dataset loading line with:")
print("original_data = pd.read_csv('inputs/news_category_dataset.csv')") 