import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import time
    import matplotlib.pyplot as plt
    return mo, np, time, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
# Search Algorithms Assignment
This notebook implements and analyzes Linear Search and Binary Search algorithms.
"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
## Task 1: Linear Search Implementation
Implement the Linear Search Algorithm for an arbitrary input array.

**Algorithm:** Sequentially check each element until the target value is found or the end is reached.
"""
    )
    return


@app.cell
def _():
    def linSearch(arr, val):
        """
        Linear search algorithm.
        Returns the index of val in arr, or -1 if not found.
        """
        for i in range(len(arr)):
            if val == arr[i]:
                return i
        return -1
    return linSearch,


@app.cell
def _(mo, linSearch):
    # Test the linear search implementation
    test_arr = [5, 2, 8, 1, 9, 3]
    test_val = 8
    test_result = linSearch(test_arr, test_val)
    
    mo.md(
        f"""
### Task 1 Verification

**Test array:** `{test_arr}`  
**Searching for:** `{test_val}`  
**Found at index:** `{test_result}`  
**Verification:** {'✓ Correct!' if test_arr[test_result] == test_val else '✗ Error'}
"""
    )
    return test_arr, test_val, test_result


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
## Task 2: Linear Search Performance
Create an array of 500 elements (0-499), shuffle it, find number 10, and measure the time.
"""
    )
    return


@app.cell
def _(mo, np, time, linSearch, plt):
    # Create and shuffle array
    t2_arr = np.arange(500)
    np.random.shuffle(t2_arr)

    # Search for 10 and measure time
    t2_start = time.perf_counter()
    t2_idx = linSearch(t2_arr, 10)
    t2_end = time.perf_counter()
    t2_elapsed = t2_end - t2_start

    # Visualize where 10 was found in the array
    t2_fig, (t2_ax1, t2_ax2) = plt.subplots(1, 2, figsize=(14, 4))
    
    # Show position in array
    t2_positions = np.arange(500)
    t2_colors = ['red' if i == t2_idx else 'lightblue' for i in t2_positions]
    t2_ax1.bar(t2_positions[::10], t2_arr[::10], color=[t2_colors[i] for i in range(0, 500, 10)])
    t2_ax1.axvline(x=t2_idx, color='red', linestyle='--', linewidth=2, label=f'Found at index {t2_idx}')
    t2_ax1.set_xlabel('Index')
    t2_ax1.set_ylabel('Value')
    t2_ax1.set_title('Array Visualization (every 10th element shown)')
    t2_ax1.legend()
    t2_ax1.grid(True, alpha=0.3)
    
    # Show search progression
    t2_search_positions = list(range(t2_idx + 1))
    t2_ax2.plot(t2_search_positions, [1]*len(t2_search_positions), 'o-', markersize=3, alpha=0.6)
    t2_ax2.scatter([t2_idx], [1], color='red', s=200, zorder=5, label='Target found')
    t2_ax2.set_xlabel('Comparison Number')
    t2_ax2.set_ylabel('')
    t2_ax2.set_title(f'Linear Search Progress: {t2_idx + 1} comparisons')
    t2_ax2.set_yticks([])
    t2_ax2.legend()
    t2_ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

    mo.md(
        f"""
### Task 2 Results

**Array size:** 500 elements  
**Value searched:** 10  
**Found at index:** `{t2_idx}`  

**Time elapsed:** `{t2_elapsed:.8f}` seconds  
**Comparisons needed:** {t2_idx + 1} out of 500 possible

The visualization shows where the value was found in the shuffled array.
"""
    )
    return t2_arr, t2_idx, t2_elapsed


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
## Task 3: Statistical Analysis of Linear Search
Run 1000 trials and analyze the time distribution.
"""
    )
    return


@app.cell
def _(mo, np, time, plt, linSearch):
    t3_N = 1000
    t3_times = np.empty(t3_N, dtype=float)
    t3_positions = np.empty(t3_N, dtype=int)

    # Run 1000 searches
    for t3_i in range(t3_N):
        t3_arr = np.arange(500)
        np.random.shuffle(t3_arr)
        
        t3_start = time.perf_counter()
        t3_pos = linSearch(t3_arr, 10)
        t3_end = time.perf_counter()
        
        t3_times[t3_i] = t3_end - t3_start
        t3_positions[t3_i] = t3_pos

    # Create comprehensive visualization
    t3_fig = plt.figure(figsize=(16, 10))
    t3_gs = t3_fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
    
    # Histogram of times
    t3_ax1 = t3_fig.add_subplot(t3_gs[0, :])
    t3_ax1.hist(t3_times * 1e6, bins=50, color='steelblue', edgecolor='black', alpha=0.7)
    t3_ax1.axvline(x=np.mean(t3_times) * 1e6, color='red', linestyle='--', 
                linewidth=2, label=f'Mean: {np.mean(t3_times)*1e6:.2f} μs')
    t3_ax1.axvline(x=np.median(t3_times) * 1e6, color='green', linestyle='--', 
                linewidth=2, label=f'Median: {np.median(t3_times)*1e6:.2f} μs')
    t3_ax1.set_xlabel('Time (microseconds)')
    t3_ax1.set_ylabel('Frequency')
    t3_ax1.set_title('Linear Search Time Distribution (1000 runs)')
    t3_ax1.legend()
    t3_ax1.grid(True, alpha=0.3)
    
    # Position distribution
    t3_ax2 = t3_fig.add_subplot(t3_gs[1, 0])
    t3_ax2.hist(t3_positions, bins=50, color='coral', edgecolor='black', alpha=0.7)
    t3_ax2.axvline(x=np.mean(t3_positions), color='red', linestyle='--', 
                linewidth=2, label=f'Mean: {np.mean(t3_positions):.1f}')
    t3_ax2.set_xlabel('Index Position')
    t3_ax2.set_ylabel('Frequency')
    t3_ax2.set_title('Distribution of Found Positions')
    t3_ax2.legend()
    t3_ax2.grid(True, alpha=0.3)
    
    
    
    
    
    # Statistics table
    t3_ax5 = t3_fig.add_subplot(t3_gs[2, 1])
    t3_ax5.axis('off')
    t3_stats_data = [
        ['Statistic', 'Value'],
        ['Number of runs', f'{t3_N}'],
        ['Mean time', f'{np.mean(t3_times)*1e6:.3f} μs'],
        ['Median time', f'{np.median(t3_times)*1e6:.3f} μs'],
        ['Std deviation', f'{np.std(t3_times)*1e6:.3f} μs'],
        ['Min time', f'{np.min(t3_times)*1e6:.3f} μs'],
        ['Max time', f'{np.max(t3_times)*1e6:.3f} μs'],
        ['Mean position', f'{np.mean(t3_positions):.1f}'],
        ['Theoretical avg', '250 (middle of array)']
    ]
    t3_table = t3_ax5.table(cellText=t3_stats_data, cellLoc='left', loc='center',
                      colWidths=[0.5, 0.5])
    t3_table.auto_set_font_size(False)
    t3_table.set_fontsize(10)
    t3_table.scale(1, 2)
    # Style header row
    for t3_j in range(2):
        t3_table[(0, t3_j)].set_facecolor('#40466e')
        t3_table[(0, t3_j)].set_text_props(weight='bold', color='white')
    
    plt.show()

    mo.md(
        f"""
### Task 3 Results

**Summary Statistics:**
- **Total runs:** {t3_N}
- **Mean time:** {np.mean(t3_times)*1e6:.3f} μs
- **Median time:** {np.median(t3_times)*1e6:.3f} μs
- **Standard deviation:** {np.std(t3_times)*1e6:.3f} μs
- **Mean position found:** {np.mean(t3_positions):.1f} (expected: ~250)

**Analysis:**
The histogram shows the distribution of search times across 1000 randomized arrays. 
Since the target value (10) can appear anywhere with equal probability, we expect 
to find it around the middle of the array on average (index ~250), which requires 
~250 comparisons. The scatter plot shows the positive correlation between position 
and time - elements found later in the array take longer to locate.
"""
    )
    return t3_N, t3_times, t3_positions


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
## Task 4: Binary Search (Iterative)
Implement the Binary Search Algorithm for a sorted input array.

**Algorithm:** Repeatedly divide the search interval in half. Compare the target 
with the middle element and eliminate half of the search space.
"""
    )
    return


@app.cell
def _():
    def binSearch(arr, val):
        """
        Binary search algorithm (iterative).
        Returns the index of val in sorted arr, or -1 if not found.
        """
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    return binSearch,


@app.cell
def _(mo, np, binSearch, plt):
    # Test binary search with visualization
    t4_arr = np.array([1, 2, 3, 4, 5, 7, 8, 10, 12, 15, 18, 20, 23, 25, 28, 30])
    t4_target = 20
    
    # Track the search process
    t4_search_steps = []
    t4_left, t4_right = 0, len(t4_arr) - 1
    
    while t4_left <= t4_right:
        t4_mid = (t4_left + t4_right) // 2
        t4_search_steps.append((t4_left, t4_mid, t4_right, t4_arr[t4_mid]))
        if t4_arr[t4_mid] == t4_target:
            break
        elif t4_arr[t4_mid] < t4_target:
            t4_left = t4_mid + 1
        else:
            t4_right = t4_mid - 1
    
    t4_idx = binSearch(t4_arr, t4_target)
    
    # Visualize the binary search process
    t4_fig, t4_axes = plt.subplots(len(t4_search_steps), 1, figsize=(14, 2*len(t4_search_steps)))
    if len(t4_search_steps) == 1:
        t4_axes = [t4_axes]
    
    for t4_step, (t4_ax) in enumerate(t4_axes):
        t4_left_val, t4_mid_val, t4_right_val, t4_mid_arr = t4_search_steps[t4_step]
        
        t4_colors = ['lightgray'] * len(t4_arr)
        for t4_i in range(t4_left_val, t4_right_val + 1):
            t4_colors[t4_i] = 'lightblue'
        t4_colors[t4_mid_val] = 'yellow'
        if t4_mid_val == t4_idx:
            t4_colors[t4_mid_val] = 'lime'
        
        t4_ax.bar(range(len(t4_arr)), t4_arr, color=t4_colors, edgecolor='black')
        t4_ax.set_xlim(-0.5, len(t4_arr) - 0.5)
        t4_ax.set_ylabel('Value')
        t4_ax.set_title(f'Step {t4_step + 1}: Check middle[{t4_mid_val}]={t4_mid_arr} | ' + 
                    (f'Found!' if t4_mid_arr == t4_target else 
                     f'Too {"small" if t4_mid_arr < t4_target else "large"}, search {"right" if t4_mid_arr < t4_target else "left"}'))
        t4_ax.grid(True, alpha=0.3, axis='y')
        
        # Add index labels
        for t4_j in range(len(t4_arr)):
            t4_ax.text(t4_j, -2, str(t4_j), ha='center', fontsize=8)
    
    plt.xlabel('Array Index')
    plt.tight_layout()
    plt.show()

    mo.md(
        f"""
### Task 4 Results

**Array:** `{t4_arr.tolist()}`  
**Searching for:** `{t4_target}`  

**Number of steps:** {len(t4_search_steps)}  
**Comparisons:** {len(t4_search_steps)} (vs {len(t4_arr)} max for linear search)

**Search Process:**
{chr(10).join([f"Step {i+1}: Checked index {s[1]} (value={s[3]})" for i, s in enumerate(t4_search_steps)])}

The visualization shows how binary search eliminates half the search space at each step.
"""
    )
    return t4_arr, t4_idx, t4_target


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
## Task 5: Binary Search (Recursive)
Implement the Recursive Binary Search Algorithm for a sorted input array.

**Algorithm:** Same as iterative binary search but implemented using recursion.
"""
    )
    return


@app.cell
def _():
    def binSearchRec(arr, left, right, val):
        """
        Binary search algorithm (recursive).
        Returns the index of val in sorted arr, or -1 if not found.
        """
        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            return binSearchRec(arr, mid + 1, right, val)
        else:
            return binSearchRec(arr, left, mid - 1, val)
    return binSearchRec,


@app.cell
def _(mo, np, binSearchRec, plt):
    # Test recursive binary search
    t5_arr = np.array([1, 2, 3, 4, 5, 7, 8, 10, 12, 15, 18, 20])
    t5_target = 7
    t5_idx = binSearchRec(t5_arr, 0, len(t5_arr) - 1, t5_target)
    
    # Visualize the array with result
    t5_fig, t5_ax = plt.subplots(figsize=(12, 4))
    t5_colors = ['lightblue' if t5_i != t5_idx else 'lime' for t5_i in range(len(t5_arr))]
    t5_bars = t5_ax.bar(range(len(t5_arr)), t5_arr, color=t5_colors, edgecolor='black', linewidth=1.5)
    
    # Highlight the found element
    if t5_idx != -1:
        t5_ax.annotate(f'Found!\nValue: {t5_arr[t5_idx]}\nIndex: {t5_idx}',
                   xy=(t5_idx, t5_arr[t5_idx]), xytext=(t5_idx, t5_arr[t5_idx] + 4),
                   ha='center', fontsize=11, fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                   arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    
    t5_ax.set_xlabel('Array Index', fontsize=12)
    t5_ax.set_ylabel('Value', fontsize=12)
    t5_ax.set_title(f'Recursive Binary Search: Finding {t5_target}', fontsize=14, fontweight='bold')
    t5_ax.grid(True, alpha=0.3, axis='y')
    
    # Add index labels
    for t5_i, t5_bar in enumerate(t5_bars):
        t5_height = t5_bar.get_height()
        t5_ax.text(t5_bar.get_x() + t5_bar.get_width()/2., -1.5, f'{t5_i}',
                ha='center', va='top', fontsize=9, color='gray')
    
    plt.tight_layout()
    plt.show()

    mo.md(
        f"""
### Task 5 Results

**Array:** `{t5_arr.tolist()}`  
**Searching for:** `{t5_target}`  
**Found at index:** `{t5_idx}`  


**Recursive vs Iterative:** Both implementations produce the same result but use different 
approaches. Recursive binary search is more elegant but uses stack space for each recursive call.
"""
    )
    return t5_arr, t5_idx, t5_target


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
## Performance Comparison: Linear vs Binary Search
Let's compare the performance of all three search methods.
"""
    )
    return


@app.cell
def _(mo, np, time, linSearch, binSearch, binSearchRec, plt):
    # Performance comparison
    perf_sizes = [100, 500, 1000, 2000, 5000, 10000]
    perf_lin_times = []
    perf_bin_times = []
    perf_binrec_times = []
    
    for perf_size in perf_sizes:
        # Average over 100 runs for each size
        perf_lin_avg = 0
        perf_bin_avg = 0
        perf_binrec_avg = 0
        
        for _ in range(100):
            perf_arr = np.arange(perf_size)
            np.random.shuffle(perf_arr)
            perf_target = np.random.randint(0, perf_size)
            
            # Linear search (unsorted)
            perf_start = time.perf_counter()
            linSearch(perf_arr, perf_target)
            perf_lin_avg += time.perf_counter() - perf_start
            
            # Binary search (sorted)
            perf_sorted_arr = np.sort(perf_arr)
            perf_start = time.perf_counter()
            binSearch(perf_sorted_arr, perf_target)
            perf_bin_avg += time.perf_counter() - perf_start
            
            # Recursive binary search (sorted)
            perf_start = time.perf_counter()
            binSearchRec(perf_sorted_arr, 0, len(perf_sorted_arr) - 1, perf_target)
            perf_binrec_avg += time.perf_counter() - perf_start
        
        perf_lin_times.append(perf_lin_avg / 100 * 1e6)  # Convert to microseconds
        perf_bin_times.append(perf_bin_avg / 100 * 1e6)
        perf_binrec_times.append(perf_binrec_avg / 100 * 1e6)
    
    # Visualization
    perf_fig, (perf_ax1, perf_ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Linear scale
    perf_ax1.plot(perf_sizes, perf_lin_times, 'o-', label='Linear Search', linewidth=2, markersize=8)
    perf_ax1.plot(perf_sizes, perf_bin_times, 's-', label='Binary Search (Iterative)', linewidth=2, markersize=8)
    perf_ax1.plot(perf_sizes, perf_binrec_times, '^-', label='Binary Search (Recursive)', linewidth=2, markersize=8)
    perf_ax1.set_xlabel('Array Size', fontsize=12)
    perf_ax1.set_ylabel('Average Time (μs)', fontsize=12)
    perf_ax1.set_title('Search Algorithm Performance Comparison', fontsize=14, fontweight='bold')
    perf_ax1.legend(fontsize=11)
    perf_ax1.grid(True, alpha=0.3)
    
    # Log scale
    perf_ax2.loglog(perf_sizes, perf_lin_times, 'o-', label='Linear Search O(n)', linewidth=2, markersize=8)
    perf_ax2.loglog(perf_sizes, perf_bin_times, 's-', label='Binary Search O(log n)', linewidth=2, markersize=8)
    perf_ax2.loglog(perf_sizes, perf_binrec_times, '^-', label='Binary Search Rec O(log n)', linewidth=2, markersize=8)
    perf_ax2.set_xlabel('Array Size (log scale)', fontsize=12)
    perf_ax2.set_ylabel('Average Time (μs, log scale)', fontsize=12)
    perf_ax2.set_title('Performance Comparison (Log-Log Scale)', fontsize=14, fontweight='bold')
    perf_ax2.legend(fontsize=11)
    perf_ax2.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    plt.show()
    
    # Create comparison table
    perf_comparison_data = []
    for perf_i, perf_size in enumerate(perf_sizes):
        perf_speedup = perf_lin_times[perf_i] / perf_bin_times[perf_i]
        perf_comparison_data.append([perf_size, f'{perf_lin_times[perf_i]:.2f}', f'{perf_bin_times[perf_i]:.2f}', 
                               f'{perf_binrec_times[perf_i]:.2f}', f'{perf_speedup:.1f}x'])
    
    mo.md(
        f"""
### Performance Comparison Results

| Array Size | Linear (μs) | Binary Iter (μs) | Binary Rec (μs) | Speedup |
|------------|-------------|------------------|-----------------|---------|
{chr(10).join([f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} |" for row in perf_comparison_data])}

**Key Observations:**
1. **Linear Search:** O(n) complexity - time grows linearly with array size
2. **Binary Search:** O(log n) complexity - much faster for large arrays
3. **Recursive vs Iterative:** Both have similar performance, recursive has slight overhead
4. **Speedup:** Binary search becomes increasingly advantageous as array size grows

**Note:** Binary search requires the array to be sorted, while linear search works on any array.
"""
    )
    return perf_sizes, perf_lin_times, perf_bin_times, perf_binrec_times


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
## Interactive Search Tool
Test the search algorithms with your own data!
"""
    )
    return


@app.cell
def _(mo):
    ui_arr_text = mo.ui.text_area(
        label="Enter array (comma/space separated)",
        value="15, 3, 8, 22, 10, 6, 1, 19, 25, 12",
    )
    ui_val = mo.ui.number(label="Value to search", value=10)
    ui_method = mo.ui.dropdown(
        label="Search method",
        options=["Linear", "Binary (iterative)", "Binary (recursive)"],
        value="Linear",
    )
    mo.vstack([ui_arr_text, ui_val, ui_method])
    return ui_arr_text, ui_method, ui_val


@app.cell
def _(mo, ui_arr_text, ui_method, ui_val, linSearch, binSearch, binSearchRec, time, plt):
    import re

    ui_arr = [int(x) for x in re.findall(r"-?\d+", ui_arr_text.value)]
    ui_target = int(ui_val.value)

    if not ui_arr:
        _result = mo.md(" Please enter a valid array.")
    else:
        # Perform search
        ui_start = time.perf_counter()
        if ui_method.value == "Linear":
            ui_idx = linSearch(ui_arr, ui_target)
            ui_used = ui_arr
            ui_sorted = False
        elif ui_method.value == "Binary (iterative)":
            ui_used = sorted(ui_arr)
            ui_idx = binSearch(ui_used, ui_target)
            ui_sorted = True
        else:
            ui_used = sorted(ui_arr)
            ui_idx = binSearchRec(ui_used, 0, len(ui_used) - 1, ui_target)
            ui_sorted = True
        ui_end = time.perf_counter()
        ui_elapsed = ui_end - ui_start

        # Visualize
        ui_fig, ui_ax = plt.subplots(figsize=(14, 5))
        
        ui_colors = []
        for ui_i in range(len(ui_used)):
            if ui_i == ui_idx:
                ui_colors.append('lime')  # Found
            elif ui_sorted:
                ui_colors.append('lightblue')  # Sorted array
            else:
                ui_colors.append('coral')  # Unsorted array
        
        ui_bars = ui_ax.bar(range(len(ui_used)), ui_used, color=ui_colors, edgecolor='black', linewidth=1.5)
        
        if ui_idx != -1:
            ui_ax.annotate(f'✓ Found at index {ui_idx}',
                       xy=(ui_idx, ui_used[ui_idx]), xytext=(ui_idx, ui_used[ui_idx] + max(ui_used)*0.1),
                       ha='center', fontsize=12, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.8),
                       arrowprops=dict(arrowstyle='->', lw=2, color='darkgreen'))
        
        ui_ax.set_xlabel('Array Index', fontsize=12)
        ui_ax.set_ylabel('Value', fontsize=12)
        ui_title = f'{ui_method.value} Search for value {ui_target}'
        if ui_sorted and ui_method.value != "Linear":
            ui_title += ' (Array Sorted)'
        ui_ax.set_title(ui_title, fontsize=14, fontweight='bold')
        ui_ax.grid(True, alpha=0.3, axis='y')
        
        # Add index labels
        for ui_j in range(len(ui_used)):
            ui_ax.text(ui_j, -max(ui_used)*0.05, str(ui_j), ha='center', fontsize=9, color='gray')
        
        plt.tight_layout()
        plt.show()
        
        ui_status = "✓ Found" if ui_idx != -1 else "✗ Not Found"
        _result = mo.md(
            f"""
### Interactive Search Result

**Method:** {ui_method.value}  
**Original array:** `{ui_arr}`  
**Array used:** `{ui_used}` {'(sorted)' if ui_sorted else '(original order)'}  
**Value searched:** `{ui_target}`  
**Result:** {ui_status}  
**Index:** `{ui_idx}`  
**Time elapsed:** `{ui_elapsed*1e6:.3f}` microseconds

{'**Verification:** Value at index = `' + str(ui_used[ui_idx]) + '` ✓' if ui_idx != -1 else '**Note:** Value not found in array'}
"""
        )
    
    _result
    return ui_arr, ui_used, ui_idx, ui_target, ui_elapsed, ui_sorted




if __name__ == "__main__":
    app.run()