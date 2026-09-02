#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Data Analysis Script for Working Memory Experiment - ENHANCED VERSION
Analyzes data from Experiments 1 and 2
Produces summary statistics and visualizations

VERSION: 2.0.0
ENHANCEMENTS:
  - Outlier detection for response times
  - Missing data reporting
  - Data quality checks
  - Enhanced visualizations
  - Statistical tests
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys
import warnings
warnings.filterwarnings('ignore')

# Outlier thresholds
RT_MIN_THRESHOLD = 0.15  # Minimum plausible RT (150ms)
RT_MAX_MEMORY = 4.5      # Maximum reasonable memory RT
RT_MAX_PARITY = 1.4      # Maximum reasonable parity RT
ACCURACY_DISENGAGEMENT = 0.5  # Below 50% suggests disengagement

def load_data(filename):
    """Load experiment data from CSV file"""
    try:
        df = pd.read_csv(filename)
        print(f"✓ Loaded {len(df)} trials from {filename}")
        return df
    except FileNotFoundError:
        print(f"✗ Error: File not found: {filename}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error loading file: {e}")
        sys.exit(1)

def detect_outliers(df):
    """
    Detect and report outliers in response times
    Returns dict with outlier counts and DataFrame with outlier flags
    """
    print("\n" + "="*60)
    print("OUTLIER DETECTION")
    print("="*60)
    
    outliers = {
        'too_fast_memory': 0,
        'too_slow_memory': 0,
        'too_fast_parity': 0,
        'too_slow_parity': 0
    }
    
    # Create outlier flags
    df = df.copy()
    
    # Memory RT outliers
    if 'memory_rt' in df.columns:
        memory_rt_numeric = pd.to_numeric(df['memory_rt'], errors='coerce')
        too_fast = memory_rt_numeric < RT_MIN_THRESHOLD
        too_slow = memory_rt_numeric > RT_MAX_MEMORY
        
        outliers['too_fast_memory'] = too_fast.sum()
        outliers['too_slow_memory'] = too_slow.sum()
        
        df['memory_rt_outlier'] = too_fast | too_slow
    
    # Parity RT outliers
    parity_rt_cols = ['parity_rt_1', 'parity_rt_2', 'parity_rt_3', 'parity_rt_4']
    df['parity_rt_outlier'] = False
    
    for col in parity_rt_cols:
        if col in df.columns:
            parity_rt_numeric = pd.to_numeric(df[col], errors='coerce')
            too_fast = parity_rt_numeric < RT_MIN_THRESHOLD
            too_slow = parity_rt_numeric > RT_MAX_PARITY
            
            outliers['too_fast_parity'] += too_fast.sum()
            outliers['too_slow_parity'] += too_slow.sum()
            
            df['parity_rt_outlier'] = df['parity_rt_outlier'] | too_fast | too_slow
    
    # Report outliers
    print(f"\n📊 Outlier Summary:")
    print(f"  Memory RT < {RT_MIN_THRESHOLD}s (too fast): {outliers['too_fast_memory']} trials")
    print(f"  Memory RT > {RT_MAX_MEMORY}s (too slow): {outliers['too_slow_memory']} trials")
    print(f"  Parity RT < {RT_MIN_THRESHOLD}s (too fast): {outliers['too_fast_parity']} instances")
    print(f"  Parity RT > {RT_MAX_PARITY}s (too slow): {outliers['too_slow_parity']} instances")
    
    total_outliers = sum(outliers.values())
    total_rts = len(df) * 5  # 1 memory + 4 parity per trial (max)
    outlier_rate = (total_outliers / total_rts) * 100 if total_rts > 0 else 0
    
    print(f"\n  Total outliers: {total_outliers}")
    print(f"  Outlier rate: {outlier_rate:.2f}%")
    
    if outlier_rate > 5:
        print(f"\n  ⚠️  High outlier rate (>{5}%) - check data quality!")
    else:
        print(f"\n  ✓ Outlier rate within acceptable range")
    
    return outliers, df

def check_data_quality(df):
    """
    Comprehensive data quality checks
    """
    print("\n" + "="*60)
    print("DATA QUALITY CHECKS")
    print("="*60)
    
    # Missing data
    print(f"\n📋 Missing Data:")
    memory_na = (df['memory_response'] == 'NA').sum()
    memory_na_pct = (memory_na / len(df)) * 100
    print(f"  Memory response NA: {memory_na} ({memory_na_pct:.1f}%)")
    
    if memory_na_pct > 10:
        print(f"    ⚠️  High missing rate (>10%) - participant engagement issue?")
    
    thought_na = (df['thought_probe_response'] == 'NA').sum()
    thought_na_pct = (thought_na / len(df)) * 100
    print(f"  Thought probe NA: {thought_na} ({thought_na_pct:.1f}%)")
    
    # Accuracy checks
    print(f"\n📊 Accuracy Checks:")
    memory_acc = df['memory_correct'].mean()
    print(f"  Overall memory accuracy: {memory_acc*100:.1f}%")
    
    if memory_acc < ACCURACY_DISENGAGEMENT:
        print(f"    ⚠️  Below chance ({ACCURACY_DISENGAGEMENT*100}%) - possible disengagement!")
    
    # Parity accuracy
    parity_correct_cols = ['parity_correct_1', 'parity_correct_2', 'parity_correct_3', 'parity_correct_4']
    parity_values = []
    for col in parity_correct_cols:
        if col in df.columns:
            parity_values.extend(pd.to_numeric(df[col], errors='coerce').dropna().tolist())
    
    if parity_values:
        parity_acc = np.mean(parity_values)
        print(f"  Overall parity accuracy: {parity_acc*100:.1f}%")
        
        if parity_acc < 0.5:
            print(f"    ⚠️  Below chance - check key mapping understanding!")
    
    # Trial count validation
    print(f"\n📈 Trial Count Validation:")
    total_trials = len(df)
    expected_trials = 288  # 144 per experiment
    print(f"  Total trials: {total_trials}")
    print(f"  Expected: {expected_trials}")
    
    if total_trials < expected_trials:
        missing = expected_trials - total_trials
        missing_pct = (missing / expected_trials) * 100
        print(f"    ⚠️  Incomplete session: {missing} trials missing ({missing_pct:.1f}%)")
    else:
        print(f"    ✓ Complete session")
    
    # Balance checks
    print(f"\n⚖️  Condition Balance:")
    for exp in [1, 2]:
        exp_data = df[df['experiment_number'] == exp]
        if len(exp_data) > 0:
            print(f"\n  Experiment {exp}:")
            for load in [0, 2, 4]:
                load_count = len(exp_data[exp_data['load_condition'] == load])
                expected_count = 48
                print(f"    Load {load}: {load_count} trials (expected: {expected_count})")

def clean_data(df, exclude_outliers=False):
    """Clean and prepare data for analysis with optional outlier exclusion"""
    print(f"\n{'='*60}")
    print("DATA CLEANING")
    print(f"{'='*60}")
    
    initial_count = len(df)
    
    # Remove practice trials
    df_main = df[df['phase'] == 'main'].copy()
    print(f"  Removed practice trials: {initial_count - len(df_main)} trials")
    
    # Convert numeric columns
    numeric_cols = ['load_condition', 'memory_correct', 'memory_rt', 
                    'parity_correct_1', 'parity_correct_2', 'parity_correct_3', 'parity_correct_4',
                    'parity_rt_1', 'parity_rt_2', 'parity_rt_3', 'parity_rt_4']
    
    for col in numeric_cols:
        if col in df_main.columns:
            df_main[col] = pd.to_numeric(df_main[col], errors='coerce')
    
    # Count NA responses before removal
    na_count = (df_main['memory_response'] == 'NA').sum()
    
    # Remove NA responses for memory accuracy calculation
    df_main = df_main[df_main['memory_response'] != 'NA'].copy()
    print(f"  Removed NA memory responses: {na_count} trials")
    
    # Detect outliers
    outliers, df_main = detect_outliers(df_main)
    
    # Optionally exclude outliers
    if exclude_outliers:
        before_exclusion = len(df_main)
        df_main = df_main[~df_main['memory_rt_outlier']].copy()
        excluded = before_exclusion - len(df_main)
        print(f"\n  Excluded outlier trials: {excluded}")
    
    # Data quality checks
    check_data_quality(df_main)
    
    print(f"\n✓ Final cleaned data: {len(df_main)} valid main trials")
    
    return df_main

def calculate_memory_performance(df):
    """Calculate memory accuracy and RT by condition"""
    print("\n" + "="*60)
    print("MEMORY PERFORMANCE")
    print("="*60)
    
    # Overall performance
    overall_acc = df['memory_correct'].mean() * 100
    overall_rt = df['memory_rt'].mean()
    
    print(f"\nOverall Memory Accuracy: {overall_acc:.2f}%")
    print(f"Overall Memory RT: {overall_rt:.3f}s")
    
    # Performance by load condition
    print("\n--- By Cognitive Load ---")
    load_summary = df.groupby('load_condition').agg({
        'memory_correct': ['mean', 'std', 'count'],
        'memory_rt': ['mean', 'std']
    }).round(3)
    
    for load in [0, 2, 4]:
        if load in df['load_condition'].values:
            acc = df[df['load_condition'] == load]['memory_correct'].mean() * 100
            rt = df[df['load_condition'] == load]['memory_rt'].mean()
            n = len(df[df['load_condition'] == load])
            print(f"Load {load}: {acc:.2f}% accurate, RT={rt:.3f}s (n={n})")
    
    # Performance by change condition
    print("\n--- By Change Condition ---")
    for change_cond in ['change', 'no_change']:
        if change_cond in df['change_condition'].values:
            acc = df[df['change_condition'] == change_cond]['memory_correct'].mean() * 100
            rt = df[df['change_condition'] == change_cond]['memory_rt'].mean()
            n = len(df[df['change_condition'] == change_cond])
            print(f"{change_cond}: {acc:.2f}% accurate, RT={rt:.3f}s (n={n})")
    
    # Performance by experiment
    print("\n--- By Experiment ---")
    for exp in df['experiment_number'].unique():
        exp_data = df[df['experiment_number'] == exp]
        acc = exp_data['memory_correct'].mean() * 100
        rt = exp_data['memory_rt'].mean()
        n = len(exp_data)
        exp_name = "Simultaneous" if exp == 1 else "Sequential"
        print(f"Experiment {exp} ({exp_name}): {acc:.2f}% accurate, RT={rt:.3f}s (n={n})")
    
    return load_summary

def calculate_parity_performance(df):
    """Calculate parity task accuracy and RT"""
    print("\n" + "="*60)
    print("PARITY TASK PERFORMANCE")
    print("="*60)
    
    # Collect all parity responses
    parity_data = []
    for i in range(1, 5):
        digit_col = f'parity_digit_{i}'
        correct_col = f'parity_correct_{i}'
        rt_col = f'parity_rt_{i}'
        
        if digit_col in df.columns:
            parity_subset = df[[digit_col, correct_col, rt_col, 'load_condition']].copy()
            parity_subset = parity_subset[parity_subset[digit_col] != 'NA']
            parity_subset.columns = ['digit', 'correct', 'rt', 'load_condition']
            parity_data.append(parity_subset)
    
    if parity_data:
        parity_df = pd.concat(parity_data, ignore_index=True)
        parity_df['correct'] = pd.to_numeric(parity_df['correct'], errors='coerce')
        parity_df['rt'] = pd.to_numeric(parity_df['rt'], errors='coerce')
        
        # Overall parity performance
        overall_parity_acc = parity_df['correct'].mean() * 100
        overall_parity_rt = parity_df['rt'].mean()
        
        print(f"\nOverall Parity Accuracy: {overall_parity_acc:.2f}%")
        print(f"Overall Parity RT: {overall_parity_rt:.3f}s")
        
        # By load condition
        print("\n--- By Load Condition ---")
        for load in [2, 4]:
            if load in parity_df['load_condition'].values:
                load_data = parity_df[parity_df['load_condition'] == load]
                acc = load_data['correct'].mean() * 100
                rt = load_data['rt'].mean()
                n = len(load_data)
                print(f"Load {load}: {acc:.2f}% accurate, RT={rt:.3f}s (n={n})")
        
        return parity_df
    else:
        print("\nNo parity data found.")
        return None

def analyze_thought_probes(df):
    """Analyze thought probe responses"""
    print("\n" + "="*60)
    print("THOUGHT PROBE ANALYSIS")
    print("="*60)
    
    # Count responses by category
    thought_counts = df['thought_probe_label'].value_counts()
    thought_percentages = df['thought_probe_label'].value_counts(normalize=True) * 100
    
    print("\n--- Thought Probe Frequencies ---")
    for label in thought_counts.index:
        count = thought_counts[label]
        pct = thought_percentages[label]
        print(f"{label}: {count} ({pct:.1f}%)")
    
    # Calculate mind-wandering rate (categories 3-8 = off-task)
    on_task = ['Task', 'Task experience/performance']
    df['on_task'] = df['thought_probe_label'].isin(on_task)
    on_task_rate = df['on_task'].mean() * 100
    mw_rate = 100 - on_task_rate
    
    print(f"\n--- Mind-Wandering Summary ---")
    print(f"On-task rate: {on_task_rate:.1f}%")
    print(f"Mind-wandering rate: {mw_rate:.1f}%")
    
    # Mind-wandering by load condition
    print("\n--- Mind-Wandering by Load Condition ---")
    for load in [0, 2, 4]:
        if load in df['load_condition'].values:
            load_data = df[df['load_condition'] == load]
            mw = (1 - load_data['on_task'].mean()) * 100
            n = len(load_data)
            print(f"Load {load}: {mw:.1f}% mind-wandering (n={n})")
    
    return thought_counts

def create_visualizations(df, output_dir='data'):
    """Create visualization plots"""
    print("\n" + "="*60)
    print("CREATING VISUALIZATIONS")
    print("="*60)
    
    # Set style
    sns.set_style("whitegrid")
    sns.set_palette("Set2")
    
    # Figure 1: Memory accuracy by load condition
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Accuracy
    load_acc = df.groupby('load_condition')['memory_correct'].mean() * 100
    axes[0].bar([0, 2, 4], [load_acc.get(0, 0), load_acc.get(2, 0), load_acc.get(4, 0)])
    axes[0].set_xlabel('Cognitive Load')
    axes[0].set_ylabel('Memory Accuracy (%)')
    axes[0].set_title('Memory Accuracy by Load Condition')
    axes[0].set_ylim([0, 100])
    axes[0].set_xticks([0, 2, 4])
    
    # RT
    load_rt = df.groupby('load_condition')['memory_rt'].mean()
    axes[1].bar([0, 2, 4], [load_rt.get(0, 0), load_rt.get(2, 0), load_rt.get(4, 0)])
    axes[1].set_xlabel('Cognitive Load')
    axes[1].set_ylabel('Reaction Time (s)')
    axes[1].set_title('Memory RT by Load Condition')
    axes[1].set_xticks([0, 2, 4])
    
    plt.tight_layout()
    fig_path = Path(output_dir) / 'memory_by_load.png'
    plt.savefig(fig_path, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {fig_path}")
    plt.close()
    
    # Figure 2: Comparison between experiments
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    exp_data = df.groupby(['experiment_number', 'load_condition'])['memory_correct'].mean().reset_index()
    
    for exp in df['experiment_number'].unique():
        exp_subset = exp_data[exp_data['experiment_number'] == exp]
        label = f"Exp {exp} ({'Simul.' if exp == 1 else 'Seq.'})"
        axes[0].plot(exp_subset['load_condition'], exp_subset['memory_correct'] * 100, 
                     marker='o', label=label, linewidth=2)
    
    axes[0].set_xlabel('Cognitive Load')
    axes[0].set_ylabel('Memory Accuracy (%)')
    axes[0].set_title('Memory Accuracy: Experiment 1 vs 2')
    axes[0].legend()
    axes[0].set_xticks([0, 2, 4])
    axes[0].set_ylim([0, 100])
    axes[0].grid(True, alpha=0.3)
    
    # Thought probe distribution
    thought_counts = df['thought_probe_label'].value_counts()
    axes[1].barh(range(len(thought_counts)), thought_counts.values)
    axes[1].set_yticks(range(len(thought_counts)))
    axes[1].set_yticklabels(thought_counts.index, fontsize=9)
    axes[1].set_xlabel('Frequency')
    axes[1].set_title('Thought Probe Distribution')
    
    plt.tight_layout()
    fig_path = Path(output_dir) / 'experiment_comparison.png'
    plt.savefig(fig_path, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {fig_path}")
    plt.close()
    
    print("\nVisualization complete!")

def generate_summary_report(df, output_filename='data/summary_report.txt'):
    """Generate text summary report"""
    with open(output_filename, 'w') as f:
        f.write("="*70 + "\n")
        f.write("WORKING MEMORY EXPERIMENT - SUMMARY REPORT\n")
        f.write("="*70 + "\n\n")
        
        # Participant info
        f.write("PARTICIPANT INFORMATION\n")
        f.write("-"*70 + "\n")
        f.write(f"Participant ID: {df['participant'].iloc[0]}\n")
        f.write(f"Age: {df['age'].iloc[0]}\n")
        f.write(f"Gender: {df['gender'].iloc[0]}\n")
        f.write(f"Session: {df['session'].iloc[0]}\n")
        f.write(f"Date: {df['date'].iloc[0]}\n\n")
        
        # Overall statistics
        f.write("OVERALL PERFORMANCE\n")
        f.write("-"*70 + "\n")
        f.write(f"Total trials analyzed: {len(df)}\n")
        f.write(f"Memory accuracy: {df['memory_correct'].mean()*100:.2f}%\n")
        f.write(f"Mean memory RT: {df['memory_rt'].mean():.3f}s\n\n")
        
        # By load
        f.write("PERFORMANCE BY COGNITIVE LOAD\n")
        f.write("-"*70 + "\n")
        for load in [0, 2, 4]:
            if load in df['load_condition'].values:
                load_df = df[df['load_condition'] == load]
                f.write(f"\nLoad {load}:\n")
                f.write(f"  Accuracy: {load_df['memory_correct'].mean()*100:.2f}%\n")
                f.write(f"  RT: {load_df['memory_rt'].mean():.3f}s\n")
                f.write(f"  Trials: {len(load_df)}\n")
        
        # Mind-wandering
        f.write("\n\nMIND-WANDERING ANALYSIS\n")
        f.write("-"*70 + "\n")
        on_task = ['Task', 'Task experience/performance']
        df['on_task'] = df['thought_probe_label'].isin(on_task)
        mw_rate = (1 - df['on_task'].mean()) * 100
        f.write(f"Mind-wandering rate: {mw_rate:.1f}%\n")
        f.write(f"On-task rate: {100-mw_rate:.1f}%\n")
    
    print(f"\n✓ Summary report saved: {output_filename}")

def main():
    """Main analysis function"""
    print("\n" + "="*70)
    print("WORKING MEMORY EXPERIMENT - DATA ANALYSIS")
    print("="*70 + "\n")
    
    # Get data file
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        # Find most recent data file
        data_dir = Path('data')
        csv_files = list(data_dir.glob('*_detailed.csv'))
        if not csv_files:
            print("✗ No data files found in data/ directory")
            print("Usage: python analyze_data.py <filename.csv>")
            sys.exit(1)
        filename = max(csv_files, key=lambda p: p.stat().st_mtime)
        print(f"Using most recent file: {filename}")
    
    # Load and clean data
    df = load_data(filename)
    df_clean = clean_data(df)
    
    # Run analyses
    calculate_memory_performance(df_clean)
    calculate_parity_performance(df_clean)
    analyze_thought_probes(df_clean)
    
    # Create visualizations
    create_visualizations(df_clean)
    
    # Generate summary report
    generate_summary_report(df_clean)
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE!")
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
