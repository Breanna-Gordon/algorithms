import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Example 1: Maxone""")
    return


@app.cell
def _():
    import random, numpy as np, matplotlib.pyplot as plt
    import marimo as mo
    return mo, np, plt, random


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 1: Initialisation
    Implement the ```createInital(nInd,nBits)``` function that creates ```nInd``` arrays of ```nBits``` bits each one, where each bit is 1 or 0 with 50% chance.
    """
    )
    return


@app.cell
def _(random):
    def createInitial(nInd, nBits):
        return [[1 if random.random() < 0.5 else 0 for _ in range(nBits)] for _ in range(nInd)]
    return (createInitial,)


# Visible output for Task 1
@app.cell
def _(createInitial):
    createInitial(5, 5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 2: Evaluation
    Implement the ```fitness(individual)``` function that receives an array ```individual``` and it returns ```nOnes```, the number of ones that the array contains (you can assume the array only contains zeros or ones).
    """
    )
    return


@app.cell
def _():
    def fitness(individual):
        return int(sum(individual))
    return (fitness,)


# Visible output for Task 2
@app.cell
def _(fitness):
    print(fitness([1, 0, 1, 0, 1]))
    print(fitness([1, 1, 1, 1, 1]))
    print(fitness([0, 0, 0, 0, 0]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Task 3: Selection""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Implement the ```selectThreeWinners(population)``` function, that takes as an input the whole population. This function should do the following:
    1. Select randomly two individuals from ```population```, then compare their fitness and select the one with highest fitness. This individual is called ```firstWinner```
    2. Repeat the above step twice, in order to obtain ```secondWinner``` and ```thirdWinner```
    3. Return ```firstWinner```,```secondWinner```, and ```thirdWinner```

    You can use the ```random.sample(population,k)``` for randomly extract ```k``` elements from ```population```
    """
    )
    return


@app.cell
def _(fitness, random):
    def selectThreeWinners(population):
        def tournament2(pop):
            a, b = random.sample(pop, 2)
            return a if fitness(a) >= fitness(b) else b

        firstWinner = tournament2(population)
        secondWinner = tournament2(population)
        thirdWinner = tournament2(population)
        return firstWinner, secondWinner, thirdWinner
    return (selectThreeWinners,)


# Visible output for Task 3
@app.cell
def _(createInitial, fitness, selectThreeWinners):
    pop_demo = createInitial(10, 8)
    w1, w2, w3 = selectThreeWinners(pop_demo)

    print("Population (first 3 individuals):")
    print(pop_demo[0], "fitness =", fitness(pop_demo[0]))
    print(pop_demo[1], "fitness =", fitness(pop_demo[1]))
    print(pop_demo[2], "fitness =", fitness(pop_demo[2]))

    print("\nWinners:")
    print("W1:", w1, "fitness =", fitness(w1))
    print("W2:", w2, "fitness =", fitness(w2))
    print("W3:", w3, "fitness =", fitness(w3))
    return pop_demo, w1, w2, w3


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 4: Crossover
    Implement the ```crossover(parent1,parent2)``` function, that takes as an input two individuals ```parent1``` and ```parent2``` and returns ```firstChild``` and ```secondChild``` which are obtained with the following procedure:
    1. Create a random crossover point x, with ```x=[1,len(parent1)-1]```
    2. Create ```firstChild```, an array containing the same elements from ```parent1``` from index 0 to x-1, and containing the same elements from ```parent2``` from index x to len(parent)-1.
    3. Create ```secondChild``` as the inverse combination from ```firstChild```
    """
    )
    return


@app.cell
def _(random):
    def crossover(parent1, parent2):
        n = len(parent1)
        x = random.randint(1, n - 1)
        firstChild = parent1[:x] + parent2[x:]
        secondChild = parent2[:x] + parent1[x:]
        return firstChild, secondChild
    return (crossover,)


# Visible output for Task 4
@app.cell
def _(crossover, fitness):
    p1 = [1, 0, 1, 1, 0, 1, 0, 1]
    p2 = [0, 1, 0, 0, 1, 0, 1, 0]
    c1, c2 = crossover(p1, p2)

    print("Parent 1:", p1, "fitness =", fitness(p1))
    print("Parent 2:", p2, "fitness =", fitness(p2))
    print("Child 1 :", c1, "fitness =", fitness(c1))
    print("Child 2 :", c2, "fitness =", fitness(c2))
    return c1, c2, p1, p2


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 5: Mutation
    Implement the ```mutation(individual,pMut)``` function, that takes as an input an array ```individual``` and ```pMut```, the probability of mutation, and for each element of ```individual``` it changes its value (from 0 to 1 or from 1 to 0) with probability ```pMut```
    """
    )
    return


@app.cell
def _(random):
    def mutation(individual, pMutation):
        out = individual[:]
        for i in range(len(out)):
            if random.random() < pMutation:
                out[i] = 1 - out[i]
        return out
    return (mutation,)


# Visible output for Task 5
@app.cell
def _(fitness, mutation):
    ind = [1, 0, 0, 1, 1, 0, 1, 0]
    print("Before:", ind, "fitness =", fitness(ind))
    print("After (pMut=0.2):", mutation(ind, 0.2), "fitness =", fitness(mutation(ind, 0.2)))
    return (ind,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""------""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Putting all together
    Now we implement our ```runGA()``` function, that will call every other function we created.
    """
    )
    return


@app.cell
def _(createInitial, crossover, fitness, mutation, selectThreeWinners):
    def runGA(totalIndividuals, numberBits, numberIterations, pMutation):
        fitnesses = []
        population = createInitial(totalIndividuals, numberBits)

        for k in range(0, numberIterations):
            winners = selectThreeWinners(population)

            next_gen = []
            for i in [0, 1]:
                for j in range(i + 1, 3):
                    c1, c2 = crossover(winners[i], winners[j])
                    next_gen.append(c1)
                    next_gen.append(c2)

            combined = population + next_gen
            for i in range(len(combined)):
                combined[i] = mutation(combined[i], pMutation)

            combined.sort(key=fitness)
            population = combined[-totalIndividuals:]

            fitnesses.append(max([fitness(ind) for ind in population]))

        return fitnesses
    return (runGA,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""And we call the function with specific values for the parameters""")
    return


@app.cell
def _(plt, runGA):
    _fit = runGA(100, 50, 10, 0.01)
    plt.plot(range(len(_fit)), _fit)
    plt.xlabel("Generation")
    plt.ylabel("Best fitness")
    plt.title("MaxOne GA progress")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""------""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 6:
    Explore modifying the selection and crossover processes to achieve a better fitness. You can also modify how the ```next_gen``` is being defined in ```runGA()```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---------""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Example 2: Maximising a real-valued function""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    We want to find the values $x^{*}$ and $y^{*}$ such that $f(x,y)=-(x+y)^2$ has a maximum.

    We can start with random arrays of two elements $[x_0,y_0]$ where $x_0,y_0\in[-1,1]$ and use genetic algorithm to see if we find the optimal solution.

    Let's visualise $f(x,y)$:
    """
    )
    return


@app.cell(hide_code=True)
def _(np, plt):
    plt.rcParams['figure.dpi'] = 300

    from matplotlib import cm
    from matplotlib.ticker import LinearLocator
    _fig, _ax = plt.subplots(subplot_kw={'projection': '3d'})
    _X = np.arange(-5, 5, 0.25)
    _Y = np.arange(-5, 5, 0.25)
    _X, _Y = np.meshgrid(_X, _Y)
    _Z = -(_X ** 2 + _Y ** 2)
    _surf = _ax.plot_surface(_X, _Y, _Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    _ax.set(xlabel='X', ylabel='Y', zlabel='Z')
    plt.show()
    return LinearLocator, cm


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ------------
    Now let's create some initial points and plot them together
    """
    )
    return


@app.cell(hide_code=True)
def _(mo, np, random):
    import plotly.graph_objects as go

    population = []
    for i in range(100):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        population.append([x, y])

    x_vals = [p[0] for p in population]
    y_vals = [p[1] for p in population]
    z_vals = [-x**2 - y**2 for x, y in population]

    scatter = go.Scatter3d(
        x=x_vals,
        y=y_vals,
        z=z_vals,
        mode='markers',
        marker=dict(size=5, color=z_vals, colorscale='Viridis', opacity=0.8),
        name='Points'
    )

    X = np.linspace(-1, 1, 50)
    Y = np.linspace(-1, 1, 50)
    X, Y = np.meshgrid(X, Y)
    Z = -X**2 - Y**2

    surface = go.Surface(
        x=X, y=Y, z=Z,
        colorscale='Viridis', opacity=0.5, showscale=False
    )

    fig = go.Figure(data=[surface, scatter])
    fig.update_layout(
        title="Interactive 3D Plot of f(x,y) = -x² - y²",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z = -x² - y²",
        ),
        width=700,
        height=600,
    )

    mo.ui.plotly(fig)
    return X, Y, Z, fig, go, population, scatter, surface, x_vals, y_vals, z_vals


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Final Task:
    Implement the following functions to run a genetic algorithm for the probklem stated above. 
    your algorithm should do the following:
    - Create an initial population of 100 points scattered randomnly in the range $x=[-1,1]$ and $y=[-1,1]$
    - Calculate the fitness of each point is given by evaluating the point in the function $f(x,y)$.
    - Selection process is similar as Example 1 (i.e. selecting three winners)
    - You can implement whatever crossover you consider adequate.
    - For each step, each individual suffers a mutation on each of its coordinates $x$ and $y$ which are modified by a random noise $\delta$, where $\delta=[-0.05,0.05]$ (uniformly distributed).
    - Implement the ```runGA_1()``` function so it runs 100 iterations of the algorithm. Check if the points converge to a solution.

    ## Extra task (not compulsory):
    - Plot the points for each iteration of the algorithm together with the surface. Visualise how the points move through the surface
    - Visualise how the points move through the surface by plotting the path or trail that they leave when they move from one iteration to the next one.
    """
    )
    return


@app.cell
def _(random):
    def createInitial_1():
        population = []
        for _ in range(100):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            population.append([x, y])
        return population
    return (createInitial_1,)


@app.cell
def _():
    def fitness_1(individual):
        x, y = individual
        return -((x + y) ** 2)
    return (fitness_1,)


@app.cell
def _(fitness_1, random):
    def selectThreeWinners_1(population):
        def tournament2(pop):
            a, b = random.sample(pop, 2)
            return a if fitness_1(a) >= fitness_1(b) else b

        firstWinner = tournament2(population)
        secondWinner = tournament2(population)
        thirdWinner = tournament2(population)
        return (firstWinner, secondWinner, thirdWinner)
    return (selectThreeWinners_1,)


@app.cell
def _(random):
    def crossover_1(parent1, parent2):
        alpha = random.random()
        x1, y1 = parent1
        x2, y2 = parent2
        firstChild = [alpha * x1 + (1 - alpha) * x2, alpha * y1 + (1 - alpha) * y2]
        secondChild = [(1 - alpha) * x1 + alpha * x2, (1 - alpha) * y1 + alpha * y2]
        return (firstChild, secondChild)
    return (crossover_1,)


@app.cell
def _(random):
    def mutation_1(individual, pMutation=1.0):
        x, y = individual

        if random.random() < pMutation:
            x += random.uniform(-0.05, 0.05)
        if random.random() < pMutation:
            y += random.uniform(-0.05, 0.05)

        x = max(-1, min(1, x))
        y = max(-1, min(1, y))
        return [x, y]
    return (mutation_1,)


@app.cell
def _(createInitial_1, crossover_1, fitness_1, mutation_1, selectThreeWinners_1):
    def runGA_1():
        population = createInitial_1()
        best_fitnesses = []
        history = [[p[:] for p in population]]

        elite_size = 10

        for _ in range(100):
            population.sort(key=fitness_1)
            elites = [p[:] for p in population[-elite_size:]]

            winners = selectThreeWinners_1(population)

            children = []
            for i in [0, 1]:
                for j in range(i + 1, 3):
                    c1, c2 = crossover_1(winners[i], winners[j])
                    children.append(c1)
                    children.append(c2)

            next_gen = elites + [mutation_1(ch, 1.0) for ch in children]

            while len(next_gen) < 100:
                c1, c2 = crossover_1(winners[0], winners[1])
                next_gen.append(mutation_1(c1, 1.0))
                if len(next_gen) < 100:
                    next_gen.append(mutation_1(c2, 1.0))

            next_gen.sort(key=fitness_1)
            population = next_gen[-100:]

            best_fitnesses.append(max(fitness_1(p) for p in population))
            history.append([p[:] for p in population])

        return history, best_fitnesses
    return (runGA_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Running the Genetic Algorithm""")
    return


@app.cell
def _(runGA_1):
    history, best_fitnesses = runGA_1()
    return best_fitnesses, history


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Use the slider to explore different iterations:**""")
    return


@app.cell
def _(history, mo):
    slider = mo.ui.slider(0, len(history) - 1, value=len(history) - 1, label="Iteration")
    slider
    return (slider,)


@app.cell
def _(fitness_1, go, history, mo, np, slider):
    t = int(slider.value)
    pop_t = history[t]
    x_vals_ga = [p[0] for p in pop_t]
    y_vals_ga = [p[1] for p in pop_t]
    z_vals_ga = [fitness_1(p) for p in pop_t]

    X_ga = np.linspace(-1, 1, 80)
    Y_ga = np.linspace(-1, 1, 80)
    X_ga, Y_ga = np.meshgrid(X_ga, Y_ga)
    Z_ga = -((X_ga + Y_ga) ** 2)

    surface_ga = go.Surface(x=X_ga, y=Y_ga, z=Z_ga, colorscale="Viridis", opacity=0.45, showscale=False)
    scatter_ga = go.Scatter3d(
        x=x_vals_ga, y=y_vals_ga, z=z_vals_ga,
        mode="markers",
        marker=dict(size=4, color=z_vals_ga, colorscale="Viridis", opacity=0.9),
        name=f"Population @ iter {t}",
    )

    fig_ga = go.Figure(data=[surface_ga, scatter_ga])
    fig_ga.update_layout(
        title=f"Population on f(x,y)=-(x+y)² (iteration {t})",
        scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
        width=760,
        height=620,
    )

    mo.ui.plotly(fig_ga)
    return (
        X_ga,
        Y_ga,
        Z_ga,
        fig_ga,
        pop_t,
        scatter_ga,
        surface_ga,
        t,
        x_vals_ga,
        y_vals_ga,
        z_vals_ga,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Best Fitness Over Generations""")
    return


@app.cell
def _(best_fitnesses, plt):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(best_fitnesses)), best_fitnesses)
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.title("Best Fitness Over Generations (f(x,y) = -(x+y)²)")
    plt.grid(True)
    plt.show()
    return


if __name__ == "__main__":
    app.run()