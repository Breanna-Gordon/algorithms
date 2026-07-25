import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 1:
    Implement the Binary Search Algorithm for a sorted input array.
    """
    )
    return


@app.cell
def _():
    a = [0,2,3]
    return


# TASK 1: Implementing the iterative Binary Search
@app.function
def binSearch(arr, target):
    """
    Iterative binary search algorithm for sorted arrays.
    Returns the index of target if found, -1 otherwise.
    """
    # Initialize left and right pointers to cover the entire array
    left = 0
    right = len(arr) - 1
    
    # Continue searching while the search space is valid
    while left <= right:
        # Calculate middle index to divide search space in half
        # Using // for integer division to avoid floating point
        mid = (left + right) // 2
        
        # Check if we found the target at the middle position
        if arr[mid] == target:
            return mid  # Return the index where target was found
        
        # If target is smaller than middle element, search left half
        elif target < arr[mid]:
            right = mid - 1  # Narrow search space to left of mid
        
        # If target is larger than middle element, search right half
        else:
            left = mid + 1  # Narrow search space to right of mid
    
    # Target not found in array, return -1 to indicate failure
    return -1


@app.cell
def _(binSearch):
    binSearch([1,3,44,535,2552,14123,452525,2412414,141414144],44)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 2:
    Implement the Recursive Binary Search Algorithm for a sorted input array.
    """
    )
    return


@app.function
def binSearchRec(arr,target,left,right):
    """
    Recursive binary search implementation.
    Parameters: arr (sorted array), target (value to find), left/right (search boundaries)
    """
    # Base case: check if search space is still valid
    if (left <= right):
        # Calculate middle index of current search space
        mid = (left + right) // 2
        
        # Base case: target found at middle position
        if (target == arr[mid]):
            return mid  # Success! Return the index

        # Recursive case: target is in left half
        elif (target < arr[mid]):
            right = mid - 1  # Update right boundary to exclude mid and right half
            # Recursively search the left half
            return binSearchRec(arr,target,left,right)
        
        # Recursive case: target is in right half
        else:
            left = mid + 1  # Update left boundary to exclude mid and left half
            # Recursively search the right half
            return binSearchRec(arr,target,left,right)

    # Base case: search space exhausted, target not found
    return -1


@app.cell
def _():
    binSearchRec([1,3,44,535,2552,14123,452525,2412414,141414144],46,0,8)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 3:
    Implement Merge Sort algorithm
    """
    )
    return


@app.function
def mergeSort(A):
    """
    Recursive merge sort algorithm - divides array and merges sorted halves.
    Time complexity: O(n log n)
    """
    # Base case: array with 1 or 0 elements is already sorted
    if(len(A)>1):
        # Find the middle point to divide array into two halves
        mid = (len(A) // 2)
        
        # Divide: split array into left half (B) and right half (C)
        B = A[:mid]      # Left half from start to mid (exclusive)
        C = A[mid:]      # Right half from mid to end
        
        # Conquer: recursively sort both halves
        B = mergeSort(B)  # Sort left half
        C = mergeSort(C)  # Sort right half
        
        # Combine: merge the two sorted halves back together
        A = mergeArrays(B,C)
    
    # Return the sorted array
    return A


@app.cell
def _():
    mergeSort([31,4245,2,32,32,424,2,312,42,42,2,24,56,7])
    return


@app.function
def mergeArrays(A,B):
    """
    Merges two sorted arrays into one sorted array.
    This is the 'combine' step of merge sort.
    """
    S = []  # Result array to store merged elements
    
    # Compare elements from both arrays and add smaller one to result
    while(len(A)>0 and len(B)>0):
        if A[0] < B[0]:
            S.append(A[0])  # A's first element is smaller, add it
            A = A[1:]       # Remove first element from A (shift left)
        else:
            S.append(B[0])  # B's first element is smaller or equal, add it
            B = B[1:]       # Remove first element from B (shift left)

    # After one array is exhausted, append remaining elements from A
    while(len(A)>0):
        S.append(A[0])
        A = A[1:]

    # Append any remaining elements from B
    while(len(B)>0):
        S.append(B[0])
        B = B[1:]
    
    # Return the merged sorted array
    return S


@app.cell
def _():
    mergeArrays([1,4,6,7,8,9,10],[2,5,67,88])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 4:
    Implement Quicksort (last element as a pivot)
    """
    )
    return


@app.function
def quicksort(arr):
    """
    Quicksort algorithm using last element as pivot.
    Divides array into elements less than and greater than pivot.
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr)<=1:
        return arr
    
    # Initialize partitions for elements smaller and larger than pivot
    left=[]   # Will hold elements <= pivot
    right=[]  # Will hold elements > pivot
    
    # Choose last element as pivot (partition point)
    pivot = arr[len(arr)-1]
    
    # Partition: compare each element (except pivot) with pivot
    for i in range(len(arr)-1):
        if (arr[i]<=pivot):
            left.append(arr[i])   # Element is smaller/equal, goes to left
        else:
            right.append(arr[i])  # Element is larger, goes to right

    # Recursively sort left partition, concatenate with pivot, then right partition
    # This works because pivot is now in its final sorted position
    return quicksort(left) + [pivot] + quicksort(right)


@app.cell
def _():
    quicksort([314,31,4,636,74,6,25])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Final Task
    Below you will find a series of cells that help you to plot a tree structure. A tree structure here is something like the following:
    """
    )
    return


@app.cell
def _():
    exampleTree = [(0, None, [8, 3, 5, 4, 7, 6, 1, 2]), (1, 0, [8, 3, 5, 4]),(2,0,[7,6,1,2]) ,(3,1,[8,3]),(4,1,[5,4]),(5, 2, [7,6])]
    return (exampleTree,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Now we can use the helper functions to plot this tree structure for different iterations""")
    return


@app.cell
def _(build_graph, draw_tree, exampleTree):
    F = build_graph(exampleTree,3)
    draw_tree(F)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
            r"""
        ---------------------
        The following code was generated initially with GPT-5 plus iterations. The code generated all the helper functions defined in the first cell. The author modified it to be displayed and plotted as a tree structure using networkx library.  

        ----------
        """
        ).callout()
    return


@app.cell(hide_code=True)
def _(mo):
    import networkx as nx
    import matplotlib.pyplot as plt


    def build_graph(tree, step):
        """
        Converts tree structure into NetworkX directed graph for visualization.
        Only includes nodes up to the specified step (for progressive reveal).
        """
        G = nx.DiGraph()  # Create directed graph (parent -> child relationships)
        
        # Process each node up to current step
        for node, parent, arr in tree[:step]:
            # Add node with its array as a label (for display)
            G.add_node(node, label=str(list(arr)))
            
            # Add edge from parent to this node (if not root)
            # Root node has parent=None, so skip adding edge
            if parent is not None:
                G.add_edge(parent, node)
        
        return G



    def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
        """
        Calculate node positions for hierarchical tree layout.
        This creates the top-down tree structure you see in the visualization.
        
        Parameters:
        - G: NetworkX graph
        - width: horizontal space allocated for tree
        - vert_gap: vertical spacing between levels
        - vert_loc: starting vertical position
        """
        # Verify graph is actually a tree (no cycles)
        if not nx.is_tree(G):
            raise TypeError("hierarchy_pos only works for trees.")

        # Find root node (node with no incoming edges)
        if root is None:
            root = next(n for n,d in G.in_degree() if d==0)

        def _hierarchy_pos(G, node, left, right, vert_loc, pos):
            """
            Recursive helper to position nodes.
            Children are evenly distributed in the horizontal space between left and right.
            """
            children = list(G.successors(node))  # Get all child nodes
            
            # Position current node in center of its allocated space
            pos[node] = ((left + right) / 2, vert_loc)
            
            # If node has children, recursively position them
            if len(children) != 0:
                dx = (right - left) / len(children)  # Width allocated per child
                nextx = left  # Starting position for first child
                
                # Position each child in its allocated horizontal space
                for child in children:
                    # Move down one level (vert_loc - vert_gap)
                    _hierarchy_pos(G, child, nextx, nextx + dx, vert_loc - vert_gap, pos)
                    nextx += dx  # Move to next child's space
            
            return pos

        # Start recursive positioning from root
        return _hierarchy_pos(G, root, 0, width, vert_loc, {})


    def draw_tree(G):
        """
        Renders the tree visualization using matplotlib and NetworkX.
        Creates a visual diagram showing the algorithm's execution steps.
        """
        # Calculate hierarchical positions for all nodes
        pos = hierarchy_pos(G) 
        
        # Extract labels (array values) for each node
        labels = nx.get_node_attributes(G, "label")
        
        # Create matplotlib figure with specified size
        plt.figure(figsize=(5, 3))
        
        # Draw the graph with specified styling:
        # - with_labels=True: show node numbers
        # - labels: show array contents
        # - font_size: make text readable but not too large
        # - node_size: size of node circles
        # - node_color: aesthetic choice (light blue)
        nx.draw(
            G,
            pos,
            with_labels=True,
            labels=labels,
            font_size=5,
            node_size=500,
            node_color="lightblue",
        )
        
        plt.axis("off")  # Hide axis for cleaner appearance
        
        # Convert to marimo interactive plot
        drawM = mo.mpl.interactive(plt.gcf())
        return drawM
    return build_graph, draw_tree


@app.cell(hide_code=True)
def _(mo):
    arr_input = mo.ui.text(label="Enter array (comma-separated)", value="8,3,5,4,7,6,1,2")
    return (arr_input,)


# MAIN TASK: Add input for search value
@app.cell(hide_code=True)
def _(mo):
    val_input = mo.ui.text(label="Enter value to search", value="5")
    return (val_input,)


@app.cell(hide_code=True)
def _(mo):
    next_btn = mo.ui.button(label="Next")
    return (next_btn,)


@app.cell(hide_code=True)
def _(mo):
    reset_btn = mo.ui.button(label=" Reset")
    return (reset_btn,)


@app.cell(hide_code=True)
def _(mo):
    # Create state management for binary search step counter
    # get_count() retrieves current step number
    # set_count() updates the step number
    # Initialized to 1 (showing first step of tree)
    get_count, set_count = mo.state(1)
    return get_count, set_count


@app.cell(hide_code=True)
def _(get_count, next_btn, set_count):
    # When "Next Step" button is clicked:
    next_btn
    # Increment the step counter by 1
    # This reveals the next node in the tree visualization
    set_count(get_count()+1)
    print(get_count())  # Debug: print current step to console
    return


@app.cell(hide_code=True)
def _(reset_btn, set_count):
    # When "Reset" button is clicked:
    reset_btn
    # Set step counter back to 0
    # This hides the tree and allows user to restart visualization
    set_count(0)
    return


@app.cell(hide_code=True)
def _(arr_input):
    # Parse the comma-separated array input from the user
    arr_text = arr_input.value
    
    # Convert string to list of integers:
    # 1. Split by comma: "8,3,5,4" -> ["8","3","5","4"]
    # 2. Strip whitespace from each element
    # 3. Check if it's a valid digit with isdigit()
    # 4. Convert to integer with int()
    # This filtering prevents errors from invalid input like letters or empty strings
    arr = [int(x.strip()) for x in arr_text.split(",") if x.strip().isdigit()]
    return (arr,)


@app.function
def tree_bin_search(arr, val, tree = [],id=0,parent=None):
    """
    Creates a tree structure to visualize binary search process.
    Each node in the tree represents a search step with the current subarray.
    """
    # Add current node to tree: (node_id, parent_id, current_array)
    # This records the state at this step of the search
    tree.append((id,parent,arr))
    
    # Continue only if array has more than 1 element
    if (len(arr)>1):
        # Calculate middle index to compare with target value
        mid = len(arr) // 2

        # Case 1: target is smaller than middle element
        # Search continues in LEFT half of array
        if (val < arr[mid]):
            subarr = arr[:mid]  # Create left subarray (before mid)
            # Recursive call: new node (id+1) with current node as parent
            return tree_bin_search(subarr,val, tree,id + 1,id)
        
        # Case 2: target is larger than middle element
        # Search continues in RIGHT half of array
        elif (val > arr[mid]):
            subarr = arr[mid:]  # Create right subarray (from mid onward)
            # Recursive call: explore right branch
            return tree_bin_search(subarr,val, tree,id + 1,id)
        
        # Case 3: target equals middle element - FOUND!
        else:
            subarr = [arr[mid]]  # Create final node with just the found element
            # One more recursive call to add the final node to tree
            return tree_bin_search(subarr,val, tree,id + 1,id)

    # Base case: array has 1 element, search is complete
    # Return the complete tree structure
    return tree


# MAIN TASK: Implement tree_merge_sort function
@app.function
def tree_merge_sort(arr, tree=[], id=0, parent=None):
    """
    Creates a tree structure for Merge Sort algorithm visualization.
    Unlike binary search (which only opens ONE branch), merge sort opens TWO branches.
    This represents the divide-and-conquer approach: split array in half repeatedly.
    """
    # Add current node to tree with its array state
    tree.append((id, parent, arr))
    
    # Only split if array has more than 1 element
    if len(arr) > 1:
        # Calculate middle point to divide array
        mid = len(arr) // 2
        left_arr = arr[:mid]    # Left half
        right_arr = arr[mid:]   # Right half
        
        # IMPORTANT: We need to calculate correct IDs for right subtree
        # The right subtree's ID must come AFTER all nodes in left subtree
        # Otherwise node IDs would overlap and cause visualization errors
        left_tree_size = count_merge_nodes(left_arr)
        
        # Recursively create LEFT subtree
        # Left child gets next ID (id + 1), and current node as parent
        tree_merge_sort(left_arr, tree, id + 1, id)
        
        # Recursively create RIGHT subtree
        # Right child ID must skip all left subtree nodes
        # Formula: id + 1 (for this level) + left_tree_size (all left descendants)
        tree_merge_sort(right_arr, tree, id + 1 + left_tree_size, id)
    
    # Return complete tree showing all divide steps
    return tree


@app.function
def count_merge_nodes(arr):
    """
    Helper function to count how many nodes will be in a merge sort subtree.
    This is crucial for assigning correct IDs in the tree structure.
    
    Why we need this: In merge sort, both left AND right subtrees are created.
    If we don't calculate the size of the left subtree first, the right subtree
    will have overlapping node IDs with the left subtree.
    
    Example: If left subtree has 3 nodes (IDs 1,2,3), right subtree must start at ID 4.
    """
    # Base case: single element = 1 node
    if len(arr) <= 1:
        return 1
    
    # Recursive case: 
    # Total nodes = 1 (current node) + nodes in left subtree + nodes in right subtree
    mid = len(arr) // 2
    return 1 + count_merge_nodes(arr[:mid]) + count_merge_nodes(arr[mid:])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Binary Search Visualization""")
    return


@app.cell
def _(
    arr,
    arr_input,
    build_graph,
    draw_tree,
    get_count,
    mo,
    next_btn,
    reset_btn,
    val_input,
):
    # MAIN TASK: Modified to use val_input instead of fixed value 5
    
    # Parse the search value from user input, default to 5 if invalid
    search_val = int(val_input.value) if val_input.value.strip().isdigit() else 5
    
    # Generate the complete binary search tree for visualization
    # tree=[] creates a fresh tree for each execution
    tree = tree_bin_search(arr, search_val, tree=[])
    
    # Determine which step to display (limited by total tree length)
    # get_count() tracks how many times "Next" button was clicked
    step = min(get_count(), len(tree))
    
    # Build the graph structure for the current step
    # This only includes nodes up to the current step
    G = build_graph(tree, step)

    # Create the user interface with vertical stack layout
    mo.vstack([
        # Top row: all input controls in horizontal layout
        mo.hstack([arr_input, val_input, next_btn, reset_btn]),
        # Display current step information
        mo.md(f"### Binary Search - Step {step}/{len(tree)} (Searching for {search_val})"),
        # Render the tree visualization
        draw_tree(G),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Merge Sort Visualization""")
    return


@app.cell(hide_code=True)
def _(mo):
    merge_arr_input = mo.ui.text(label="Enter array for Merge Sort (comma-separated)", value="8,3,5,4,7,6,1,2")
    return (merge_arr_input,)


@app.cell(hide_code=True)
def _(mo):
    merge_next_btn = mo.ui.button(label="Next Step ")
    return (merge_next_btn,)


@app.cell(hide_code=True)
def _(mo):
    merge_reset_btn = mo.ui.button(label=" Reset")
    return (merge_reset_btn,)


@app.cell(hide_code=True)
def _(mo):
    # Separate state management for merge sort visualization
    # Independent from binary search so both can be used simultaneously
    # get_merge_count() retrieves current step
    # set_merge_count() updates current step
    get_merge_count, set_merge_count = mo.state(1)
    return get_merge_count, set_merge_count


@app.cell(hide_code=True)
def _(get_merge_count, merge_next_btn, set_merge_count):
    # Handle "Next Step" button for merge sort visualization
    merge_next_btn
    # Increment merge sort step counter
    # Shows next division in the merge sort tree
    set_merge_count(get_merge_count()+1)
    return


@app.cell(hide_code=True)
def _(merge_reset_btn, set_merge_count):
    # Handle "Reset" button for merge sort visualization
    merge_reset_btn
    # Reset merge sort step counter to 0
    # Clears the visualization so user can start over
    set_merge_count(0)
    return


@app.cell(hide_code=True)
def _(merge_arr_input):
    # Parse user input for merge sort array (same process as binary search)
    merge_arr_text = merge_arr_input.value
    
    # Convert comma-separated string to integer array
    # Only includes valid integer values, ignores invalid input
    merge_arr = [int(x.strip()) for x in merge_arr_text.split(",") if x.strip().isdigit()]
    return (merge_arr,)


@app.cell
def _(
    build_graph,
    draw_tree,
    get_merge_count,
    merge_arr,
    merge_arr_input,
    merge_next_btn,
    merge_reset_btn,
    mo,
    tree_merge_sort,
):
    # MAIN TASK: Merge Sort visualization using tree_merge_sort function
    
    # Generate the complete merge sort tree structure
    # This shows ALL the divisions that will happen during merge sort
    # tree=[] ensures we start fresh each time
    merge_tree = tree_merge_sort(merge_arr, tree=[])
    
    # Control which step of the algorithm to display
    # get_merge_count() increases each time "Next Step" is clicked
    merge_step = min(get_merge_count(), len(merge_tree))
    
    # Build graph showing only nodes up to current step
    # This creates the progressive reveal effect as user clicks "Next"
    merge_G = build_graph(merge_tree, merge_step)

    # Render the user interface
    mo.vstack([
        # Control panel with input field and buttons
        mo.hstack([merge_arr_input, merge_next_btn, merge_reset_btn]),
        # Status display showing progress through algorithm
        mo.md(f"### Merge Sort - Step {merge_step}/{len(merge_tree)}"),
        # Tree visualization showing divide phase of merge sort
        draw_tree(merge_G),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Tasks:
    -  Modify the previous cell so it allows the user to input the value to search for (now it is fixed to 5)
    -  Create a new function ```tree_merge_sort()```. This function is similar to ```tree_bin_search()``` but it created the tree for a Merge Sort algorithm (i.e. instead of only opening one branch like binary search, now it always open two branches). Use the same helper functions to plot the merge sort tree for each iteration.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #### Extra Tasks (not compulsory, just if you want to learn more):
    - Add a dropdown menu that allows you to choose between Binary Search and Mergesort and then it shows the corresponding tree.
    - Add as a third option the Quicksort algorithm with its corresponding tree
    - Modify the helper functions so for the Binary search algorithm it displays the whole tree (not only the chosen left or right child node), and it also show the chosen path (i.e. chosen nodes) with a different colour. You might have to add an extra attribute to the nodes of the tree that accounts whether they belong to the path or not. Then, in the ```draw_tree()``` helper function (particularly, in the ```nx.draw()``` part) you can give a ```color``` option to nodes.
    """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()