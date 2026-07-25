import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import marimo as mo
    import plotly.graph_objs as go
    import time
    return go, mo, np, time


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Task 1: Insertion sort
        From the discussion in class, implement insertion sort.
        """
    )
    return


@app.cell
def _():
    def insertionSort(arr):
        for i in range(1, len(arr)):
            j = i - 1
            k = arr[i]
            while(j >= 0 and arr[j]>k):
                arr[j+1]=arr[j]
                j = j - 1
            arr[j+1]=k
        return arr

    insertionSort([34,1,3,12,13,5,24524,1,2])
    return (insertionSort,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Task 2:
        Calculate the time that Insertion Sort takes to sort an array of 1000 random elements.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("Hint: Use the *time* library and *time.time()* method to get the instant time of execution").callout()
    return


@app.cell
def _(insertionSort, time):
    t1 = time.time()
    insertionSort([43,52,1,3,124,254,42])
    t2 = time.time()
    print(t2-t1)
    return t1, t2


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Task 3: Bubble sort
        Now implement Bubble Sort
        """
    )
    return


@app.cell
def _():
    def bubbleSort(arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    k = arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=k
        return arr
    
    bubbleSort([13,4,1,424,1,3,43,4,2])
    return (bubbleSort,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""-----------------------------------------------------------""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Final Task - Interactive Sorting Visualizer
        
        **Features:**
        - Choose between Bubble Sort, Insertion Sort, and Selection Sort
        - Step through the algorithm one iteration at a time
        - Color-coded visualization showing sorted/unsorted portions
        - Performance monitoring
        - Custom array options
        """
    )
    return


@app.cell
def _(mo):
    dropdown = mo.ui.dropdown(
        options=["bubble", "insertion", "selection"], 
        value="bubble", 
        label="Choose Sorting Algorithm:"
    )
    dropdown
    return (dropdown,)


@app.cell
def _(dropdown, mo):
    explanations = {
        "bubble": "**Bubble Sort**: Compares adjacent elements and swaps them if wrong order. Largest elements 'bubble' to the end. O(n²)",
        "insertion": "**Insertion Sort**: Builds sorted array one item at a time by inserting each element into correct position. O(n²)",
        "selection": "**Selection Sort**: Finds minimum element from unsorted portion and places it at beginning. O(n²)"
    }
    mo.md(explanations[dropdown.value]).callout(kind="info")
    return (explanations,)


@app.cell
def _(mo):
    array_size = mo.ui.slider(start=10, stop=150, value=50, label="Array Size:", show_value=True)
    array_type = mo.ui.dropdown(
        options=["random", "reversed", "nearly_sorted", "few_unique"], 
        value="random", 
        label="Array Type:"
    )
    mo.hstack([array_size, array_type], justify="start")
    return array_size, array_type


@app.cell
def _(mo):
    reset_button = mo.ui.button(label="Reset Array")
    reset_button
    return (reset_button,)


@app.cell
def _(array_size, array_type, np, reset_button):
    def generate_array(size, arr_type):
        if arr_type == "random":
            return np.random.randint(0, 100, size)
        elif arr_type == "reversed":
            return np.arange(size, 0, -1)
        elif arr_type == "nearly_sorted":
            arr = np.arange(1, size + 1)
            for _ in range(size // 10):
                i, j = np.random.randint(0, size, 2)
                arr[i], arr[j] = arr[j], arr[i]
            return arr
        else:  # few_unique
            return np.random.randint(0, 10, size)
    
    n = array_size.value
    reset_button  # dependency
    
    initial_arr = generate_array(n, array_type.value)
    
    state = {
        "arr": initial_arr.copy(),
        "i": 0,
        "j": 0,
        "sorted_until": 0,
        "min_idx": 0,
        "step_times": [],
        "last_swapped": [],
        "done": False
    }
    return generate_array, initial_arr, n, state


@app.cell
def _(mo):
    next_button = mo.ui.button(value=0, on_click=lambda value: value + 1, label="Next Step →")
    next_button
    return (next_button,)


@app.cell
def _(dropdown, go, mo, n, next_button, np, state, time):
    arr = state["arr"].copy()
    i = state["i"]
    j = state["j"]
    colors = ["skyblue"] * n
    state["last_swapped"] = []
    
    start_time = time.time()
    
    if next_button.value > 0 and not state.get("done", False):
        if dropdown.value == "bubble":
            if i < n - 1:
                if j < n - i - 1:
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        state["last_swapped"] = [j, j + 1]
                    state["j"] += 1
                else:
                    state["i"] += 1
                    state["j"] = 0
                
                for k in range(n - i, n):
                    colors[k] = "lightgreen"
                if j < n - i - 1:
                    colors[j] = "salmon"
                    colors[j + 1] = "salmon"
                if state["last_swapped"]:
                    for idx in state["last_swapped"]:
                        if idx < n:
                            colors[idx] = "red"
                
                state["arr"] = arr.copy()
            else:
                state["done"] = True
                colors = ["lightgreen"] * n
        
        elif dropdown.value == "insertion":
            if i < n:
                if state["sorted_until"] <= i:
                    state["sorted_until"] = i + 1
                    state["j"] = i
                
                if j > 0 and arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
                    state["last_swapped"] = [j - 1, j]
                    state["j"] -= 1
                else:
                    state["i"] += 1
                    state["j"] = state["i"]
                
                for k in range(min(state["sorted_until"], n)):
                    colors[k] = "lightgreen"
                if j > 0 and j < n:
                    colors[j - 1] = "salmon"
                    colors[j] = "salmon"
                if state["last_swapped"]:
                    for idx in state["last_swapped"]:
                        if idx < n:
                            colors[idx] = "red"
                
                state["arr"] = arr.copy()
            else:
                state["done"] = True
                colors = ["lightgreen"] * n
        
        elif dropdown.value == "selection":
            if i < n - 1:
                if state["j"] == 0 or state["j"] <= i:
                    state["min_idx"] = i
                    state["j"] = i
                
                if state["j"] < n:
                    if arr[state["j"]] < arr[state["min_idx"]]:
                        state["min_idx"] = state["j"]
                    state["j"] += 1
                else:
                    if state["min_idx"] != i:
                        arr[i], arr[state["min_idx"]] = arr[state["min_idx"]], arr[i]
                        state["last_swapped"] = [i, state["min_idx"]]
                    state["i"] += 1
                    state["j"] = 0
                
                for k in range(i):
                    colors[k] = "lightgreen"
                if state["j"] < n and state["j"] > 0:
                    colors[state["j"]] = "salmon"
                if state["min_idx"] < n and state["min_idx"] >= i:
                    colors[state["min_idx"]] = "orange"
                if state["last_swapped"]:
                    for idx in state["last_swapped"]:
                        if idx < n:
                            colors[idx] = "red"
                
                state["arr"] = arr.copy()
            else:
                state["done"] = True
                colors = ["lightgreen"] * n
    
    step_time = (time.time() - start_time) * 1000
    if step_time > 0 and next_button.value > 0:
        state["step_times"].append(step_time)
        if len(state["step_times"]) > 10:
            state["step_times"].pop(0)
    
    avg_time = np.mean(state["step_times"]) if state["step_times"] else 0
    
    fig = go.Figure(
        data=[go.Bar(x=np.arange(n), y=arr, marker_color=colors)]
    )
    
    status = " - COMPLETE!" if state.get("done", False) else ""
    
    fig.update_layout(
        title=f"{dropdown.value.capitalize()} Sort - Step {next_button.value}{status}<br><sub>Avg. Time: {avg_time:.4f}ms</sub>",
        xaxis_title="Index",
        yaxis_title="Value",
        template="plotly_white",
        width=700,
        height=400,
        showlegend=False
    )
    
    mo.ui.plotly(fig)
    return arr, avg_time, colors, fig, i, j, start_time, status, step_time


@app.cell
def _(mo):
    mo.md("""
    **Color Legend:**  
    🔵 Blue = Unsorted | 🟢 Green = Sorted | 🔴 Red = Just Swapped | 🟠 Orange = Current Min | 🟥 Salmon = Comparing
    """).callout(kind="neutral")
    return


if __name__ == "__main__":
    app.run()