#!/usr/bin/env python3
"""
Main entry point for the AV Technology Patent Mining project.
This script demonstrates the usage of the core pipeline modules.
"""

import sys
from src.pipeline import load_patent_dataframe, build_text_corpus, normalize_publication_dates

def main():
    print("Initializing AV Technology Patent Mining Pipeline...")
    
    try:
        # Load the dataset
        print("Loading patent dataset...")
        df = load_patent_dataframe()
        
        if df.empty:
            print("Warning: Dataset is empty.")
            return

        # Preprocess dates
        print("Normalizing publication dates...")
        df = normalize_publication_dates(df)
        
        # Build text corpus for analysis
        print("Building text corpus...")
        corpus = build_text_corpus(df)
        
        # Display summary statistics
        print("\n" + "="*30)
        print("PROJECT SUMMARY STATISTICS")
        print("="*30)
        print(f"Total Patents Loaded: {len(df)}")
        print(f"Date Range: {df['date_published'].min().date()} to {df['date_published'].max().date()}")
        print(f"Unique Applicants: {df['applicant_name'].nunique()}")
        
        top_applicants = df['applicant_name'].value_counts().head(5)
        print("\nTop 5 Applicants:")
        for name, count in top_applicants.items():
            print(f"- {name}: {count}")
        
        print("="*30)
        print("Pipeline initialized successfully.")

    except FileNotFoundError as e:
        print(f"Error: Data file not found. {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
