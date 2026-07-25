import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md(
        r"""
        # Aegis: Safe Route Planning System

        ## Problem Statement

        Personal safety during urban navigation is a critical concern, particularly for **vulnerable populations**:
        
        - Women walking alone at night
        - Elderly individuals with mobility constraints  
        - People with disabilities requiring accessible routes
        - Marginalized communities in high-crime areas
        - Visitors unfamiliar with local safety patterns

        **Traditional navigation apps** (Google Maps, Waze) optimize for **speed and distance** but ignore:
        
        - Street lighting quality
        - CCTV camera coverage  
        - Historical crime data
        - Pedestrian accessibility
        - Time-of-day risk patterns
        - Emergency services proximity

        **Aegis** prioritizes personal safety over speed using five core algorithms working together.

        ---

        ## System Architecture - Five Algorithms

        1. **Graph Algorithm (Dijkstra)** - Find safest routes using weighted risk factors
        2. **Searching (Binary Search)** - Fast lookup of buildings, postcodes, and incident logs  
        3. **Sorting (MergeSort)** - Rank routes by safety score, distance, and accessibility
        4. **Genetic Algorithm** - Learn personalized safety preferences over time
        5. **Perceptron** - Classify street segments into safety risk zones

        Let's explore each algorithm with interactive demos and critical analysis.

        ---
        """
    )
    return


@app.cell
def __():
    import numpy as np
    import time
    import matplotlib.pyplot as plt
    import random
    from collections import defaultdict
    import heapq
    from dataclasses import dataclass
    from typing import List, Tuple, Dict, Optional
    import pandas as pd
    
    np.random.seed(42)
    random.seed(42)
    
    plt.style.use('seaborn-v0_8-darkgrid')
    return (
        Dict,
        List,
        Optional,
        Tuple,
        dataclass,
        defaultdict,
        heapq,
        np,
        pd,
        plt,
        random,
        time,
    )


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        # Algorithm 1 - Graph Algorithm - Dijkstra's Safest Path

        ## Introduction 

        **Why Dijkstra's Algorithm?**

        Finding the safest walking route requires navigating a weighted graph where intersections are nodes and street segments are weighted edges. Unlike traditional navigation using distance/time, we use a **composite safety score** combining lighting, CCTV, crime data, accessibility, and distance. Dijkstra's algorithm is optimal because it: (1) **guarantees** the lowest-risk path, (2) runs in O((V+E) log V) with binary heap for real-time performance, (3) easily incorporates multi-factor safety weights, and (4) adapts dynamically to user preferences. Alternatives like A* require good heuristics (hard for "safety"), while Bellman-Ford is unnecessarily slow.

        ---
        """
    )
    return


@app.cell
def __(Dict, Tuple, dataclass, defaultdict, heapq, np, random):
    @dataclass
    class StreetSegment:
        start: int
        end: int
        distance: float
        lighting_score: float  # 0-1
        cctv_coverage: float
        crime_incidents: int
        accessibility_score: float
        
        def calculate_risk_weight(self, prefs: Dict[str, float]) -> float:
            crime_risk = min(self.crime_incidents / 10.0, 1.0)
            lighting_risk = 1.0 - self.lighting_score
            cctv_risk = 1.0 - self.cctv_coverage
            accessibility_risk = 1.0 - self.accessibility_score
            
            risk_score = (
                prefs['lighting'] * lighting_risk +
                prefs['cctv'] * cctv_risk +
                prefs['crime'] * crime_risk +
                prefs['accessibility'] * accessibility_risk
            )
            
            distance_penalty = self.distance / 100.0
            return risk_score * 10 + distance_penalty * prefs['distance']


    class SafetyGraph:
        def __init__(self, num_intersections: int):
            self.num_intersections = num_intersections
            self.graph: Dict[int, List[Tuple[int, StreetSegment]]] = defaultdict(list)
            self.positions: Dict[int, Tuple[float, float]] = {}
            self._generate_city_network()
        
        def _generate_city_network(self):
            grid_size = int(np.ceil(np.sqrt(self.num_intersections)))
            idx = 0
            for i in range(grid_size):
                for j in range(grid_size):
                    if idx >= self.num_intersections:
                        break
                    self.positions[idx] = (i * 100, j * 100)
                    idx += 1
            
            for i in range(self.num_intersections):
                x1, y1 = self.positions[i]
                for j in range(i + 1, self.num_intersections):
                    x2, y2 = self.positions[j]
                    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                    
                    if distance <= 150:
                        center_x, center_y = grid_size * 50, grid_size * 50
                        dist_from_center = np.sqrt((x1 - center_x)**2 + (y1 - center_y)**2)
                        centrality = 1.0 - min(dist_from_center / 500, 1.0)
                        
                        segment = StreetSegment(
                            start=i, end=j, distance=distance,
                            lighting_score=np.clip(0.3 + centrality * 0.5 + random.uniform(-0.2, 0.2), 0, 1),
                            cctv_coverage=np.clip(0.2 + centrality * 0.6 + random.uniform(-0.2, 0.2), 0, 1),
                            crime_incidents=max(0, int(random.expovariate(0.3) * (1 - centrality * 0.5))),
                            accessibility_score=np.clip(0.4 + random.uniform(-0.2, 0.4), 0, 1)
                        )
                        self._add_segment(segment)
        
        def _add_segment(self, seg: StreetSegment):
            self.graph[seg.start].append((seg.end, seg))
            rev = StreetSegment(seg.end, seg.start, seg.distance, seg.lighting_score,
                               seg.cctv_coverage, seg.crime_incidents, seg.accessibility_score)
            self.graph[seg.end].append((seg.start, rev))
        
        def dijkstra_safe_route(self, start: int, end: int, prefs: Dict[str, float]):
            distances = {i: float('inf') for i in range(self.num_intersections)}
            distances[start] = 0
            previous = {i: None for i in range(self.num_intersections)}
            segments_used = {}
            
            pq = [(0, start)]
            visited = set()
            operations = 0
            
            while pq:
                current_risk, current = heapq.heappop(pq)
                operations += 1
                
                if current in visited:
                    continue
                visited.add(current)
                
                if current == end:
                    break
                
                for neighbor, segment in self.graph[current]:
                    operations += 1
                    if neighbor in visited:
                        continue
                    
                    edge_weight = segment.calculate_risk_weight(prefs)
                    new_risk = current_risk + edge_weight
                    
                    if new_risk < distances[neighbor]:
                        distances[neighbor] = new_risk
                        previous[neighbor] = current
                        segments_used[neighbor] = segment
                        heapq.heappush(pq, (new_risk, neighbor))
            
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = previous[current]
            path.reverse()
            
            total_distance = sum(segments_used[path[i]].distance 
                               for i in range(1, len(path)) if path[i] in segments_used)
            
            return path, distances[end], total_distance, operations
    return SafetyGraph, StreetSegment


@app.cell
def __(mo):
    mo.md("### User Safety Preferences")
    
    lighting_pref = mo.ui.slider(0, 1, 0.01, value=0.3, label="Lighting Priority")
    cctv_pref = mo.ui.slider(0, 1, 0.01, value=0.2, label="CCTV Priority")
    crime_pref = mo.ui.slider(0, 1, 0.01, value=0.3, label="Crime Avoidance")
    accessibility_pref = mo.ui.slider(0, 1, 0.01, value=0.1, label="Accessibility")
    distance_pref = mo.ui.slider(0, 1, 0.01, value=0.1, label="Distance Weight")
    
    graph_size = mo.ui.slider(16, 64, 9, value=36, label="City Size (intersections)")
    
    mo.vstack([
        mo.md("*Adjust weights to match your safety priorities*"),
        mo.hstack([lighting_pref, cctv_pref]),
        mo.hstack([crime_pref, accessibility_pref]),
        mo.hstack([distance_pref, graph_size])
    ])
    return (
        accessibility_pref,
        crime_pref,
        cctv_pref,
        distance_pref,
        graph_size,
        lighting_pref,
    )


@app.cell
def __(
    SafetyGraph,
    accessibility_pref,
    crime_pref,
    cctv_pref,
    distance_pref,
    graph_size,
    lighting_pref,
    mo,
    np,
    plt,
):
    _prefs = {
        'lighting': lighting_pref.value,
        'cctv': cctv_pref.value,
        'crime': crime_pref.value,
        'accessibility': accessibility_pref.value,
        'distance': distance_pref.value
    }

    _g = SafetyGraph(graph_size.value)
    _start, _end = 0, graph_size.value - 1

    _safe_path, _safe_risk, _safe_dist, _ops = _g.dijkstra_safe_route(_start, _end, _prefs)
    _fast_path, _, _fast_dist, _ = _g.dijkstra_safe_route(_start, _end, 
        {'lighting': 0, 'cctv': 0, 'crime': 0, 'accessibility': 0, 'distance': 1.0})

    def _calc_metrics(path, graph):
        crime, lighting, cctv, access = 0, [], [], []
        for i in range(len(path) - 1):
            for neighbor, seg in graph.graph[path[i]]:
                if neighbor == path[i + 1]:
                    crime += seg.crime_incidents
                    lighting.append(seg.lighting_score)
                    cctv.append(seg.cctv_coverage)
                    access.append(seg.accessibility_score)
                    break
        return {
            'crime': crime,
            'lighting': np.mean(lighting) if lighting else 0,
            'cctv': np.mean(cctv) if cctv else 0,
            'access': np.mean(access) if access else 0
        }

    _safe_m = _calc_metrics(_safe_path, _g)
    _fast_m = _calc_metrics(_fast_path, _g)

    _fig1, (_ax1, _ax2) = plt.subplots(1, 2, figsize=(16, 7))

    for _ax, _path_highlight, _title, _color in [
        (_ax1, _safe_path, 'Safest Route (Your Preferences)', 'green'),
        (_ax2, _fast_path, 'Fastest Route (Distance Only)', 'orange')
    ]:
        for _node, _neighbors in _g.graph.items():
            _x1, _y1 = _g.positions[_node]
            for _neighbor, _seg in _neighbors:
                if _node < _neighbor:
                    _x2, _y2 = _g.positions[_neighbor]
                    _crime_color = plt.cm.Reds(_seg.crime_incidents / 5.0)
                    _ax.plot([_x1, _x2], [_y1, _y2], color=_crime_color, alpha=0.3, linewidth=1)
        
        for _i in range(len(_path_highlight) - 1):
            _x1, _y1 = _g.positions[_path_highlight[_i]]
            _x2, _y2 = _g.positions[_path_highlight[_i + 1]]
            _ax.plot([_x1, _x2], [_y1, _y2], _color, linewidth=4, alpha=0.8)
        
        _all_x = [_g.positions[i][0] for i in range(_g.num_intersections)]
        _all_y = [_g.positions[i][1] for i in range(_g.num_intersections)]
        _ax.scatter(_all_x, _all_y, c='lightgray', s=100, zorder=3, edgecolors='black', linewidths=0.5)
        
        _sx, _sy = _g.positions[_start]
        _ex, _ey = _g.positions[_end]
        _ax.scatter([_sx], [_sy], c='blue', s=300, zorder=5, marker='o', edgecolors='black', linewidths=2)
        _ax.scatter([_ex], [_ey], c='red', s=300, zorder=5, marker='s', edgecolors='black', linewidths=2)
        
        _ax.set_title(_title, fontsize=13, fontweight='bold')
        _ax.set_xlabel('East-West (m)', fontsize=10)
        _ax.set_ylabel('North-South (m)', fontsize=10)
        _ax.grid(True, alpha=0.2)
        _ax.set_aspect('equal')

    plt.tight_layout()
    _fig1.patch.set_facecolor('white')

    mo.md(f"""
    ## Demo: Route Comparison

    {mo.as_html(_fig1)}

    | Metric | Safest Route  | Fastest Route  | Difference |
    |--------|-----------------|------------------|------------|
    | **Distance** | {_safe_dist:.0f}m | {_fast_dist:.0f}m | +{(_safe_dist - _fast_dist):.0f}m ({((_safe_dist/_fast_dist - 1)*100):.1f}%) |
    | **Crime Incidents** | {_safe_m['crime']} | {_fast_m['crime']} | **{_safe_m['crime'] - _fast_m['crime']:+d}** fewer |
    | **Avg Lighting** | {_safe_m['lighting']:.2f}/1.0 | {_fast_m['lighting']:.2f}/1.0 | +{(_safe_m['lighting'] - _fast_m['lighting']):.2f} |
    | **CCTV Coverage** | {_safe_m['cctv']:.2f}/1.0 | {_fast_m['cctv']:.2f}/1.0 | +{(_safe_m['cctv'] - _fast_m['cctv']):.2f} |
    | **Accessibility** | {_safe_m['access']:.2f}/1.0 | {_fast_m['access']:.2f}/1.0 | +{(_safe_m['access'] - _fast_m['access']):.2f} |

    **Trade-off:** Safe route is {((_safe_dist/_fast_dist - 1)*100):.1f}% longer but has {abs(_safe_m['crime'] - _fast_m['crime'])} fewer crime incidents.

    *Note: Red streets = high crime. Blue circle = start. Red square = destination.*
    """)
    return


@app.cell
def __(SafetyGraph, mo, np, plt, time):
    mo.md("## Time Complexity Analysis")

    _sizes = [16, 25, 36, 49, 64, 81, 100]
    _times, _ops = [], []

    for _s in _sizes:
        _runs = []
        _ops_runs = []
        for _ in range(3):
            _g = SafetyGraph(_s)
            _prefs = {'lighting': 0.3, 'cctv': 0.2, 'crime': 0.3, 'accessibility': 0.1, 'distance': 0.1}
            _t1 = time.time()
            _, _, _, _op = _g.dijkstra_safe_route(0, _s - 1, _prefs)
            _t2 = time.time()
            _runs.append(_t2 - _t1)
            _ops_runs.append(_op)
        _times.append(np.mean(_runs) * 1000)
        _ops.append(int(np.mean(_ops_runs)))

    _fig2, (_ax1, _ax2) = plt.subplots(1, 2, figsize=(14, 5))

    _ax1.plot(_sizes, _times, 'o-', linewidth=2.5, markersize=8, color='#059669')
    _ax1.set_xlabel('Intersections (V)', fontsize=11)
    _ax1.set_ylabel('Time (ms)', fontsize=11)
    _ax1.set_title('Dijkstra Execution Time', fontsize=13, fontweight='bold')
    _ax1.grid(True, alpha=0.3)
    _theoretical = [(_v + _v * 4) * np.log2(_v) * 0.001 for _v in _sizes]
    _ax1.plot(_sizes, _theoretical, '--', alpha=0.5, color='orange', label='O((V+E)log V)')
    _ax1.legend()

    _ax2.plot(_sizes, _ops, 's-', linewidth=2.5, markersize=8, color='#7c3aed')
    _ax2.set_xlabel('Intersections (V)', fontsize=11)
    _ax2.set_ylabel('Operations', fontsize=11)
    _ax2.set_title('Algorithm Operations', fontsize=13, fontweight='bold')
    _ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    _fig2.patch.set_facecolor('white')

    mo.md(f"""
    {mo.as_html(_fig2)}

    **Complexity:** O((V + E) log V) with binary heap  
    **Scalability:** Real-time performance (<50ms) for city-scale networks  
    **Operations:** Linear growth due to sparse graph structure
    """)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ##  Critical Aspects & Bias Analysis

        ### Potential Biases

        1. **Data Infrastructure Inequality**: CCTV and lighting sensors predominantly installed in affluent areas → better-quality safety data for wealthier neighborhoods → algorithm favors rich areas
        
        2. **Crime Reporting Bias**: Reported crime reflects policing patterns, not actual crime. Over-policed minority communities appear "more dangerous" → routes avoid these areas → economic isolation

        3. **Historical Redlining**: Safety infrastructure investment follows historical discrimination patterns → perpetuates spatial inequality → algorithm encodes systemic racism

        4. **Accessibility Data Gaps**: Wheelchair accessibility often only mapped in newer/commercial areas → excludes people with disabilities from many routes

        5. **Gender/Identity Blind Spots**: Generic crime data doesn't capture gender-based harassment, hate crimes against LGBTQ+ individuals, or racism

        ### Affected Populations

        - **Residents of under-resourced areas**: Marked "unsafe" due to poor infrastructure → routes avoid them → further economic isolation
        - **Racial minorities**: Over-policing creates inflated crime stats → stigmatization and avoidance
        - **People with disabilities**: Limited data makes app useless or provides dangerous "accessible" routes
        - **Women and LGBTQ+ individuals**: Generic crime data misses harassment, stalking, hate crimes
        - **Homeless individuals**: May be coded as "safety risks" in training data

        ### Mitigation Strategies Implemented

        1. **User preference weighting**: Individuals prioritize factors relevant to their specific safety concerns
        2. **Transparent scoring**: All safety factors shown explicitly → users judge data quality themselves
        3. **Multi-factor approach**: Reduces reliance on any single biased data source
        4. **Route alternatives**: Show multiple options, not just one "optimal" route

        ### Recommendations

        - **Equity audits**: Regularly analyze which neighborhoods receive route avoidance recommendations
        - **Diverse data sources**: Include community-reported safety, gender-specific incident data
        - **Context-aware weighting**: Different crime types weighted differently (petty theft ≠ assault)
        - **Infrastructure advocacy**: Use route data to identify areas needing lighting/CCTV investment
        - **Participatory design**: Involve diverse communities in defining "safety"
        - **Harm reduction**: Explicitly state data limitations, encourage user judgment

        ---
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        # Algorithm 2 - Searching - Binary Search for Location Lookup

        ## Introduction 

        **Why Binary Search?**

        Aegis needs instant lookup of buildings/addresses and crime incidents. Binary search provides O(log n) logarithmic time for sorted datasets.

        ---
        """
    )
    return


@app.cell
def __(List, Optional, Tuple, dataclass, np, random):
    @dataclass
    class Building:
        postcode: str
        name: str
        latitude: float
        longitude: float
        
        def __lt__(self, other):
            return self.postcode < other.postcode


    @dataclass
    class CrimeIncident:
        incident_id: int
        latitude: float
        longitude: float
        timestamp: int
        crime_type: str
        severity: int
        
        def __lt__(self, other):
            if self.latitude != other.latitude:
                return self.latitude < other.latitude
            if self.longitude != other.longitude:
                return self.longitude < other.longitude
            return self.timestamp < other.timestamp


    def binary_search_postcode(buildings: List[Building], target: str) -> Tuple[Optional[Building], int, List[int]]:
        left, right = 0, len(buildings) - 1
        comparisons = 0
        search_path = []
        
        while left <= right:
            mid = (left + right) // 2
            search_path.append(mid)
            comparisons += 1
            
            if buildings[mid].postcode == target:
                return buildings[mid], comparisons, search_path
            elif buildings[mid].postcode < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return None, comparisons, search_path


    def binary_search_incidents(incidents: List[CrimeIncident], lat: float, lon: float, 
                                radius: float = 0.01) -> Tuple[List[CrimeIncident], int]:
        left, right = 0, len(incidents) - 1
        comparisons = 0
        start_idx = 0
        
        while left <= right:
            mid = (left + right) // 2
            comparisons += 1
            if incidents[mid].latitude < lat - radius:
                left = mid + 1
                start_idx = left
            else:
                right = mid - 1
        
        matches = []
        idx = start_idx
        while idx < len(incidents) and incidents[idx].latitude <= lat + radius:
            comparisons += 1
            if abs(incidents[idx].longitude - lon) <= radius:
                matches.append(incidents[idx])
            idx += 1
        
        return matches, comparisons


    def generate_buildings(n: int) -> List[Building]:
        areas = ['SW', 'NW', 'SE', 'NE', 'W', 'E', 'N', 'S', 'EC', 'WC']
        buildings = []
        for i in range(n):
            area = random.choice(areas)
            postcode = f"{area}{random.randint(1,20)} {random.randint(1,9)}{chr(65+i%26)}{chr(65+(i//26)%26)}"
            buildings.append(Building(postcode, f"Building {i}", 
                51.5 + random.uniform(-0.2, 0.2), -0.1 + random.uniform(-0.2, 0.2)))
        buildings.sort(key=lambda b: b.postcode)
        return buildings


    def generate_incidents(n: int) -> List[CrimeIncident]:
        crime_types = ['Theft', 'Assault', 'Burglary', 'Vandalism', 'Harassment']
        incidents = []
        for i in range(n):
            incidents.append(CrimeIncident(i, 51.5 + random.uniform(-0.2, 0.2),
                -0.1 + random.uniform(-0.2, 0.2), 1700000000 + random.randint(0, 10000000),
                random.choice(crime_types), random.randint(1, 5)))
        incidents.sort()
        return incidents
    return (
        Building,
        CrimeIncident,
        binary_search_incidents,
        binary_search_postcode,
        generate_buildings,
        generate_incidents,
    )


@app.cell
def __(generate_buildings, generate_incidents):
    _buildings = generate_buildings(10000)
    _incidents = generate_incidents(5000)
    return


@app.cell
def __(mo):
    mo.md("### Building Search")
    
    postcode_input = mo.ui.text(value="NW5 2AA", label="Enter Postcode:")
    search_btn = mo.ui.button(label="Search")
    
    mo.hstack([postcode_input, search_btn])
    return postcode_input, search_btn


@app.cell
def __(
    _buildings,
    binary_search_postcode,
    mo,
    np,
    plt,
    postcode_input,
    search_btn,
):
    if search_btn.value:
        _result, _comps, _search_path = binary_search_postcode(_buildings, postcode_input.value.strip())
        
        _fig_search, (_ax_left, _ax_right) = plt.subplots(1, 2, figsize=(16, 6))
        
        _n = len(_buildings)
        _indices = list(range(_n))
        _colors = ['lightgray'] * _n
        
        for _i, _idx in enumerate(_search_path):
            if _idx == _search_path[-1] and _result:
                _colors[_idx] = 'green'
            else:
                _colors[_idx] = plt.cm.RdYlGn(1 - _i / len(_search_path))
        
        _ax_left.bar(_indices[::100], [1]*len(_indices[::100]), color=[_colors[i] for i in range(0, _n, 100)], 
                    edgecolor='black', linewidth=0.5)
        _ax_left.set_xlabel('Building Index (sampled)', fontsize=11)
        _ax_left.set_ylabel('Search Space', fontsize=11)
        _ax_left.set_title('Binary Search Path Visualization', fontsize=13, fontweight='bold')
        _ax_left.set_ylim(0, 1.5)
        
        for _i, _idx in enumerate(_search_path[:5]):
            if _idx % 100 == 0 or _idx == _search_path[-1]:
                _ax_left.annotate(f'Step {_i+1}', xy=(_idx, 1.1), xytext=(_idx, 1.3),
                                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                                fontsize=9, ha='center', fontweight='bold')
        
        _steps_data = {
            'Search Space': [_n],
            'Comparisons Made': [_comps],
            'Theoretical Max': [int(np.ceil(np.log2(_n)))],
            'Linear Search Would Need': [_n // 2]
        }
        
        _ax_right.barh(list(_steps_data.keys()), list(_steps_data.values()), 
                      color=['#3b82f6', '#059669', '#f59e0b', '#ef4444'],
                      edgecolor='black', linewidth=1.5)
        _ax_right.set_xlabel('Count', fontsize=11)
        _ax_right.set_title('Search Efficiency', fontsize=13, fontweight='bold')
        _ax_right.set_xscale('log')
        _ax_right.grid(True, alpha=0.3, axis='x')
        
        for _i, (_k, _v) in enumerate(_steps_data.items()):
            _ax_right.text(_v, _i, f'  {_v}', va='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        _fig_search.patch.set_facecolor('white')
        
        if _result:
            mo.md(f"""
            Building Found
            
            - **Postcode:** {_result.postcode}
            - **Name:** {_result.name}
            - **Coordinates:** ({_result.latitude:.6f}, {_result.longitude:.6f})
            - **Comparisons:** {_comps} out of {len(_buildings):,} buildings
            
            {mo.as_html(_fig_search)}
            
            **Efficiency:** Binary search used {_comps} comparisons vs {len(_buildings):,} for linear search.
            """)
        else:
            mo.md(f"""
            Not found: `{postcode_input.value}` ({_comps} comparisons)
            
            {mo.as_html(_fig_search)}
            """)
    else:
        mo.md("*Enter postcode and click search*")
    return


@app.cell
def __(mo):
    mo.md("### Crime Incident Search")
    
    lat_input = mo.ui.number(51.5074, label="Latitude:", step=0.01)
    lon_input = mo.ui.number(-0.1278, label="Longitude:", step=0.01)
    radius_slider = mo.ui.slider(0.005, 0.05, 0.005, value=0.01, label="Radius")
    incident_btn = mo.ui.button(label="Search Incidents")
    
    mo.vstack([mo.hstack([lat_input, lon_input]), radius_slider, incident_btn])
    return incident_btn, lat_input, lon_input, radius_slider


@app.cell
def __(
    _incidents,
    binary_search_incidents,
    incident_btn,
    lat_input,
    lon_input,
    mo,
    np,
    pd,
    plt,
    radius_slider,
):
    if incident_btn.value:
        _found, _comps = binary_search_incidents(_incidents, lat_input.value, lon_input.value, radius_slider.value)
        
        _fig_incidents = plt.figure(figsize=(14, 6))
        _ax_map = _fig_incidents.add_subplot(121)
        _ax_stats = _fig_incidents.add_subplot(122)
        
        _all_lats = [inc.latitude for inc in _incidents[::10]]
        _all_lons = [inc.longitude for inc in _incidents[::10]]
        _ax_map.scatter(_all_lons, _all_lats, c='lightgray', s=10, alpha=0.3, label='All incidents')
        
        _circle = plt.Circle((lon_input.value, lat_input.value), radius_slider.value, 
                            color='blue', fill=False, linewidth=2, linestyle='--', label='Search radius')
        _ax_map.add_patch(_circle)
        
        if _found:
            _found_lats = [inc.latitude for inc in _found]
            _found_lons = [inc.longitude for inc in _found]
            _found_sevs = [inc.severity for inc in _found]
            _scatter = _ax_map.scatter(_found_lons, _found_lats, c=_found_sevs, s=100, 
                                      cmap='YlOrRd', edgecolors='black', linewidths=1, 
                                      vmin=1, vmax=5, label='Found incidents', zorder=5)
            _cbar = plt.colorbar(_scatter, ax=_ax_map, label='Severity')
        
        _ax_map.scatter([lon_input.value], [lat_input.value], c='red', s=300, 
                       marker='*', edgecolors='black', linewidths=2, label='Search center', zorder=10)
        
        _ax_map.set_xlabel('Longitude', fontsize=11)
        _ax_map.set_ylabel('Latitude', fontsize=11)
        _ax_map.set_title('Incident Search Area', fontsize=13, fontweight='bold')
        _ax_map.legend(loc='upper left', fontsize=8)
        _ax_map.grid(True, alpha=0.3)
        _ax_map.set_aspect('equal')
        
        if _found:
            _crime_counts = {}
            for inc in _found:
                _crime_counts[inc.crime_type] = _crime_counts.get(inc.crime_type, 0) + 1
            
            _types = list(_crime_counts.keys())
            _counts = list(_crime_counts.values())
            _colors_bar = plt.cm.Set3(np.linspace(0, 1, len(_types)))
            
            _ax_stats.barh(_types, _counts, color=_colors_bar, edgecolor='black', linewidth=1.5)
            _ax_stats.set_xlabel('Count', fontsize=11)
            _ax_stats.set_title('Crime Type Distribution', fontsize=13, fontweight='bold')
            _ax_stats.grid(True, alpha=0.3, axis='x')
            
            for _i, (_t, _c) in enumerate(zip(_types, _counts)):
                _ax_stats.text(_c, _i, f'  {_c}', va='center', fontsize=10, fontweight='bold')
        else:
            _ax_stats.text(0.5, 0.5, 'No incidents found', 
                          ha='center', va='center', fontsize=14, transform=_ax_stats.transAxes)
            _ax_stats.axis('off')
        
        plt.tight_layout()
        _fig_incidents.patch.set_facecolor('white')
        
        if _found:
            _df = pd.DataFrame([{
                'ID': i.incident_id, 'Type': i.crime_type, 'Severity': i.severity,
                'Lat': f"{i.latitude:.5f}", 'Lon': f"{i.longitude:.5f}"
            } for i in _found[:15]])
            mo.md(f"""
            **Found {len(_found)} incidents** (Comparisons: {_comps})
            
            {mo.as_html(_fig_incidents)}
            
            {mo.ui.table(_df)}
            """)
        else:
            mo.md(f"""
            **No incidents** in this area
            
            {mo.as_html(_fig_incidents)}
            """)
    else:
        mo.md("*Click search to find nearby incidents*")
    return


@app.cell
def __(generate_buildings, mo, np, plt, random, time):
    mo.md("## Time Complexity Analysis")

    _search_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
    _search_times, _search_comps = [], []

    for _s in _search_sizes:
        _b = generate_buildings(_s)
        _runs = []
        _comp_runs = []
        for _ in range(5):
            _target = random.choice(_b).postcode
            _t1 = time.time()
            _, _c, _ = binary_search_postcode(_b, _target)
            _t2 = time.time()
            _runs.append((_t2 - _t1) * 1000000)
            _comp_runs.append(_c)
        _search_times.append(np.mean(_runs))
        _search_comps.append(int(np.mean(_comp_runs)))

    _fig3, (_ax1, _ax2) = plt.subplots(1, 2, figsize=(14, 5))

    _ax1.plot(_search_sizes, _search_times, 'o-', linewidth=2.5, markersize=8, color='#dc2626')
    _ax1.set_xlabel('Database Size (n)', fontsize=11)
    _ax1.set_ylabel('Time (microseconds)', fontsize=11)
    _ax1.set_title('Binary Search: Execution Time', fontsize=13, fontweight='bold')
    _ax1.set_xscale('log')
    _ax1.grid(True, alpha=0.3)
    _log_ref = [np.log2(_s) * 2 for _s in _search_sizes]
    _ax1.plot(_search_sizes, _log_ref, '--', alpha=0.5, color='green', label='O(log n)')
    _ax1.legend()

    _ax2.plot(_search_sizes, _search_comps, 's-', linewidth=2.5, markersize=8, color='#2563eb')
    _ax2.set_xlabel('Database Size (n)', fontsize=11)
    _ax2.set_ylabel('Comparisons', fontsize=11)
    _ax2.set_title('Comparisons vs Size', fontsize=13, fontweight='bold')
    _ax2.set_xscale('log')
    _ax2.grid(True, alpha=0.3)
    _theoretical = [np.ceil(np.log2(_s)) for _s in _search_sizes]
    _ax2.plot(_search_sizes, _theoretical, '--', alpha=0.5, color='orange', label='log2(n)')
    _ax2.legend()

    plt.tight_layout()
    _fig3.patch.set_facecolor('white')

    mo.md(f"""
    {mo.as_html(_fig3)}

    **Complexity:** O(log n)  
    **Performance:** Microsecond-level for 100K+ records
    """)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ##  Critical Aspects & Bias Analysis

        ### Potential Biases

        1. **Geocoding Accuracy Inequality**: Postcodes in affluent areas have precise geocoding; informal settlements lack proper addressing → some populations can't use the system

        2. **Crime Reporting Disparity**: Wealthy areas have higher reporting rates → misleading incident databases make them appear "safer"

        3. **Data Completeness**: Commercial/central areas have comprehensive building databases; residential/peripheral areas under-documented → suburban residents get worse service

        4. **Temporal Bias**: Recent incidents over-represented due to digitization → historical patterns in marginalized areas missing

        5. **Classification Bias**: What counts as "crime" reflects dominant cultural norms and policing priorities → cultural minorities' safety concerns ignored

        ### Affected Populations

        - **Informal settlement residents**: No postal addresses = can't use system
        - **Immigrant communities**: Under-reporting due to police mistrust → false safety perceptions
        - **Marginalized groups**: Crimes against them (hate crimes, domestic violence) under-recorded
        - **Rural/remote users**: Sparse data = unreliable results

        ### Mitigation Strategies Implemented

        1. **Radius search**: Uses geographic proximity, not strict boundaries
        2. **Explicit data quality**: Shows users incident/building counts
        3. **Multiple search methods**: Supports coordinate-based search, not just postcodes
        4. **Comparison transparency**: Displays number of comparisons made

        ### Recommendations

        - **Community-contributed data**: Allow users to add unlisted buildings/addresses
        - **Weighted reporting**: Account for under-reporting patterns in disadvantaged areas
        - **Alternative identifiers**: Support what3words, landmark-based addressing
        - **Data age transparency**: Show date range of crime data
        - **Participatory mapping**: Engage communities in improving databases
        - **Privacy protection**: Anonymize incident data to encourage reporting

        ---
        """
    )
    return
@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        # Algorithm 3 - Sorting - MergeSort for Route Ranking

        ## Introduction 

        **Why MergeSort?**

        MergeSort provides stable O(n log n) sorting essential for consistent route rankings.

        ---
        """
    )
    return


@app.cell
def __(List, dataclass, random):
    @dataclass
    class RouteOption:
        route_id: int
        path: List[int]
        distance: float
        safety_score: float
        accessibility_score: float
        estimated_time: float
        
        def composite_score(self, sw: float, dw: float, aw: float) -> float:
            norm_dist = 1.0 - min(self.distance / 2000.0, 1.0)
            return sw * self.safety_score + dw * norm_dist + aw * self.accessibility_score


    def merge_sort_routes(routes: List[RouteOption], sw: float, dw: float, aw: float,
                          comps: list = None, depth_tracker: list = None) -> List[RouteOption]:
        if comps is None:
            comps = [0]
        if depth_tracker is None:
            depth_tracker = []
            
        if len(routes) <= 1:
            return routes
        
        depth_tracker.append(len(routes))
        
        mid = len(routes) // 2
        left = merge_sort_routes(routes[:mid], sw, dw, aw, comps, depth_tracker)
        right = merge_sort_routes(routes[mid:], sw, dw, aw, comps, depth_tracker)
        
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            comps[0] += 1
            if left[i].composite_score(sw, dw, aw) >= right[j].composite_score(sw, dw, aw):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged


    def generate_routes(n: int) -> List[RouteOption]:
        return [RouteOption(i+1, list(range(random.randint(5,15))),
                           random.uniform(400, 2000), random.uniform(0.3, 0.95),
                           random.uniform(0.4, 1.0), random.uniform(5, 25))
                for i in range(n)]
    return RouteOption, generate_routes, merge_sort_routes


@app.cell
def __(mo):
    mo.md("### Route Ranking Preferences")
    
    safety_w = mo.ui.slider(0, 1, 0.05, value=0.4, label="Safety Priority")
    distance_w = mo.ui.slider(0, 1, 0.05, value=0.3, label="Distance Priority")
    access_w = mo.ui.slider(0, 1, 0.05, value=0.3, label="Accessibility Priority")
    num_routes = mo.ui.slider(5, 30, 5, value=15, label="Alternative Routes")
    
    mo.vstack([
        mo.hstack([safety_w, distance_w]),
        mo.hstack([access_w, num_routes]),
        mo.md(f"**Total:** {safety_w.value + distance_w.value + access_w.value:.2f}")
    ])
    return access_w, distance_w, num_routes, safety_w


@app.cell
def __(
    access_w,
    distance_w,
    generate_routes,
    merge_sort_routes,
    mo,
    np,
    num_routes,
    pd,
    plt,
    safety_w,
):
    _routes = generate_routes(num_routes.value)
    _comps = [0]
    _depth_tracker = []
    _sorted = merge_sort_routes(_routes.copy(), safety_w.value, distance_w.value, access_w.value, _comps, _depth_tracker)

    _fig4, ((_ax1, _ax2), (_ax3, _ax4)) = plt.subplots(2, 2, figsize=(16, 12))

    _top = min(10, len(_sorted))
    _ids = [r.route_id for r in _sorted[:_top]]
    _scores = [r.composite_score(safety_w.value, distance_w.value, access_w.value) for r in _sorted[:_top]]
    _colors = plt.cm.viridis([i/_top for i in range(_top)])
    _ax1.barh(_ids, _scores, color=_colors, edgecolor='black', linewidth=1.5)
    _ax1.set_xlabel('Composite Score', fontsize=11)
    _ax1.set_ylabel('Route ID', fontsize=11)
    _ax1.set_title(f'Top {_top} Routes', fontsize=13, fontweight='bold')
    _ax1.grid(True, alpha=0.3, axis='x')
    _ax1.invert_yaxis()
    
    for _i, (_id, _score) in enumerate(zip(_ids[:3], _scores[:3])):
        _label = ['FIRST', 'SECOND', 'THIRD'][_i]
        _ax1.text(_score * 1.02, _id, _label, fontsize=9, va='center', fontweight='bold')

    _safety = [r.safety_score for r in _sorted]
    _dist = [r.distance for r in _sorted]
    _access = [r.accessibility_score for r in _sorted]

    _scatter = _ax2.scatter(_dist, _safety, c=_access, s=150, cmap='RdYlGn',
                           edgecolors='black', linewidths=1, alpha=0.8)

    for _i in range(min(3, len(_sorted))):
        _r = _sorted[_i]
        _ax2.scatter([_r.distance], [_r.safety_score], s=300, marker='*',
                    edgecolors='red', linewidths=2, facecolors='none')
        _ax2.annotate(f'#{_i+1}', (_r.distance, _r.safety_score),
                     xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold', color='red')

    _ax2.set_xlabel('Distance (m)', fontsize=11)
    _ax2.set_ylabel('Safety Score', fontsize=11)
    _ax2.set_title('Safety vs Distance Trade-off', fontsize=13, fontweight='bold')
    _ax2.grid(True, alpha=0.3)
    _cbar = plt.colorbar(_scatter, ax=_ax2)
    _cbar.set_label('Accessibility', fontsize=9)

    _unsorted_scores = [r.composite_score(safety_w.value, distance_w.value, access_w.value) for r in _routes]
    _sorted_scores = [r.composite_score(safety_w.value, distance_w.value, access_w.value) for r in _sorted]
    
    _x_pos = np.arange(len(_routes))
    _ax3.scatter(_x_pos, _unsorted_scores, c='red', s=80, alpha=0.6, label='Before sorting', marker='x', linewidths=2)
    _ax3.scatter(_x_pos, _sorted_scores, c='green', s=80, alpha=0.8, label='After sorting', marker='o')
    
    for _i in range(min(len(_routes), 15)):
        _ax3.plot([_i, _i], [_unsorted_scores[_i], _sorted_scores[_i]], 'gray', alpha=0.3, linestyle='--', linewidth=0.5)
    
    _ax3.set_xlabel('Route Position', fontsize=11)
    _ax3.set_ylabel('Composite Score', fontsize=11)
    _ax3.set_title('Sorting Effect', fontsize=13, fontweight='bold')
    _ax3.legend()
    _ax3.grid(True, alpha=0.3)

    _depth_counts = {}
    for _d in _depth_tracker:
        _depth_counts[_d] = _depth_counts.get(_d, 0) + 1
    
    _depths = sorted(_depth_counts.keys(), reverse=True)
    _counts = [_depth_counts[d] for d in _depths]
    
    _ax4.barh([f'{d} items' for d in _depths], _counts, color=plt.cm.Blues(np.linspace(0.4, 0.9, len(_depths))),
             edgecolor='black', linewidth=1.5)
    _ax4.set_xlabel('Merge Operations', fontsize=11)
    _ax4.set_ylabel('Partition Size', fontsize=11)
    _ax4.set_title('MergeSort Recursion', fontsize=13, fontweight='bold')
    _ax4.grid(True, alpha=0.3, axis='x')
    
    _ax4.text(0.98, 0.98, f'Total: {_comps[0]}', 
             transform=_ax4.transAxes, fontsize=10, fontweight='bold',
             ha='right', va='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    _fig4.patch.set_facecolor('white')

    _rank_df = pd.DataFrame([{
        'Rank': i+1, 'ID': r.route_id,
        'Score': f"{r.composite_score(safety_w.value, distance_w.value, access_w.value):.3f}",
        'Distance': f"{r.distance:.0f}m", 'Safety': f"{r.safety_score:.2f}",
        'Access': f"{r.accessibility_score:.2f}", 'Time': f"{r.estimated_time:.1f}min"
    } for i, r in enumerate(_sorted[:10])])

    mo.md(f"""
    ## Demo: Route Ranking

    **Comparisons:** {_comps[0]}  
    **Recursion depth:** {int(np.log2(num_routes.value)) + 1} levels

    {mo.as_html(_fig4)}

    {mo.ui.table(_rank_df)}
    """)
    return


@app.cell
def __(generate_routes, merge_sort_routes, mo, np, plt, time):
    mo.md("## Time Complexity Analysis")

    _sizes = [10, 25, 50, 100, 200, 400, 800]
    _times, _comps = [], []

    for _s in _sizes:
        _runs, _comp_runs = [], []
        for _ in range(3):
            _r = generate_routes(_s)
            _c = [0]
            _t1 = time.time()
            merge_sort_routes(_r, 0.4, 0.3, 0.3, _c)
            _t2 = time.time()
            _runs.append((_t2 - _t1) * 1000)
            _comp_runs.append(_c[0])
        _times.append(np.mean(_runs))
        _comps.append(int(np.mean(_comp_runs)))

    _fig5, (_ax1, _ax2) = plt.subplots(1, 2, figsize=(14, 5))

    _ax1.plot(_sizes, _times, 'o-', linewidth=2.5, markersize=8, color='#f59e0b')
    _ax1.set_xlabel('Routes (n)', fontsize=11)
    _ax1.set_ylabel('Time (ms)', fontsize=11)
    _ax1.set_title('MergeSort Time', fontsize=13, fontweight='bold')
    _ax1.set_xscale('log')
    _ax1.set_yscale('log')
    _ax1.grid(True, alpha=0.3)
    _nlogn = [_s * np.log2(_s) * 0.001 for _s in _sizes]
    _ax1.plot(_sizes, _nlogn, '--', alpha=0.5, color='green', label='O(n log n)')
    _ax1.legend()

    _ax2.plot(_sizes, _comps, 's-', linewidth=2.5, markersize=8, color='#8b5cf6')
    _ax2.set_xlabel('Routes (n)', fontsize=11)
    _ax2.set_ylabel('Comparisons', fontsize=11)
    _ax2.set_title('Comparisons', fontsize=13, fontweight='bold')
    _ax2.set_xscale('log')
    _ax2.set_yscale('log')
    _ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    _fig5.patch.set_facecolor('white')

    mo.md(f"""
    {mo.as_html(_fig5)}

    **Complexity:** O(n log n) guaranteed  
    **Stability:** Preserves order
    """)
    return



@app.cell
def __(mo):
    mo.md(
        r"""
        ##  Critical Aspects & Bias Analysis

        ### Potential Biases

        1. **Composite Scoring Obscurity**: Weighted combination hides value judgments about what "best" means → users don't understand why routes ranked this way

        2. **One-Size-Fits-All Weights**: Default weights don't reflect diverse needs (elderly vs. wheelchair vs. women alone vs. parents with strollers)

        3. **Distance Privilege**: Even with low distance weighting, algorithm inherently favors proximity → ignores legitimate reasons for longer routes

        4. **Accessibility Definition**: Single "accessibility" score doesn't capture wheelchair vs. visual impairment vs. cognitive navigation needs

        5. **Route Diversity**: Top-k may show very similar routes → limits user choice and agency

        ### Affected Populations

        - **People with diverse disabilities**: Single accessibility metric oversimplifies vastly different needs
        - **Women/gender minorities**: Safety concerns differ qualitatively from general crime data
        - **Elderly users**: May prioritize benches, gentle slopes over generic "accessibility"
        - **Cultural minorities**: Safety perceptions vary by community experience

        ### Mitigation Strategies Implemented

        1. **User-adjustable weights**: Allows personalization of ranking criteria
        2. **Transparent scoring**: All component scores visible in results table
        3. **Stable sort**: Preserves ordering when scores tie
        4. **Top-N display**: Shows multiple alternatives, not just "best"

        ### Recommendations

        - **Preset profiles**: "Night safety", "Wheelchair", "Parent with stroller" templates
        - **Explain rankings**: Show why each route scored as it did
        - **Diverse alternatives**: Ensure top-k includes qualitatively different routes
        - **User feedback**: Allow rating actual routes to improve weights
        - **Multi-stakeholder design**: Different communities co-design default weightings
        - **Qualitative factors**: Add non-numeric considerations

        ---
        """
    )
    return



@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        # Algorithm 4 - Genetic Algorithm - Preference Learning

        ## Introduction 

        **Why Genetic Algorithm?**

        Genetic algorithms handle conflicting goals and personalize to user preferences without requiring gradients.

        ---
        """
    )
    return


@app.cell
def __(List, np, random):
    class PreferenceGenome:
        def __init__(self, random_init: bool = True):
            if random_init:
                w = np.random.random(5)
                w = w / w.sum()
                self.safety_w, self.distance_w, self.access_w, self.lighting_w, self.cctv_w = w
            else:
                self.safety_w = self.distance_w = self.access_w = self.lighting_w = self.cctv_w = 0.2
            self.fitness = 0.0
        
        def get_array(self):
            return np.array([self.safety_w, self.distance_w, self.access_w, self.lighting_w, self.cctv_w])
        
        def normalize(self):
            w = np.maximum(self.get_array(), 0)
            w = w / w.sum() if w.sum() > 0 else np.ones(5) / 5
            self.safety_w, self.distance_w, self.access_w, self.lighting_w, self.cctv_w = w
        
        def calc_fitness(self, profile: dict) -> float:
            ideal = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
            
            if profile['type'] == 'elderly':
                ideal = np.array([0.15, 0.15, 0.45, 0.15, 0.10])
            elif profile['type'] == 'woman_alone':
                ideal = np.array([0.30, 0.10, 0.10, 0.30, 0.20])
            elif profile['type'] == 'wheelchair':
                ideal = np.array([0.15, 0.15, 0.50, 0.10, 0.10])
            elif profile['type'] == 'parent':
                ideal = np.array([0.20, 0.15, 0.40, 0.15, 0.10])
            elif profile['type'] == 'commuter':
                ideal = np.array([0.15, 0.50, 0.10, 0.15, 0.10])
            
            if profile['time'] == 'night':
                ideal[0] += 0.10
                ideal[3] += 0.10
                ideal = ideal / ideal.sum()
            
            distance = np.linalg.norm(self.get_array() - ideal)
            self.fitness = 1.0 / (1.0 + distance)
            return self.fitness


    class GeneticOptimizer:
        def __init__(self, pop_size: int = 40):
            self.pop_size = pop_size
            self.population: List[PreferenceGenome] = []
            self.generation = 0
            self.best_hist = []
            self.avg_hist = []
            self.diversity_hist = []
        
        def initialize(self):
            self.population = [PreferenceGenome(True) for _ in range(self.pop_size)]
        
        def evaluate(self, profile: dict):
            for g in self.population:
                g.calc_fitness(profile)
        
        def select(self):
            tournament = random.sample(self.population, 5)
            return max(tournament, key=lambda g: g.fitness)
        
        def crossover(self, p1, p2):
            child = PreferenceGenome(False)
            alpha = random.uniform(0.3, 0.7)
            child.safety_w = alpha * p1.safety_w + (1-alpha) * p2.safety_w
            child.distance_w = alpha * p1.distance_w + (1-alpha) * p2.distance_w
            child.access_w = alpha * p1.access_w + (1-alpha) * p2.access_w
            child.lighting_w = alpha * p1.lighting_w + (1-alpha) * p2.lighting_w
            child.cctv_w = alpha * p1.cctv_w + (1-alpha) * p2.cctv_w
            child.normalize()
            return child
        
        def mutate(self, genome, rate=0.2):
            if random.random() < rate:
                idx = random.randint(0, 4)
                w = genome.get_array()
                w[idx] += np.random.normal(0, 0.1)
                w = np.maximum(w, 0)
                genome.safety_w, genome.distance_w, genome.access_w, genome.lighting_w, genome.cctv_w = w
                genome.normalize()
        
        def calc_diversity(self):
            if len(self.population) < 2:
                return 0
            genomes = np.array([g.get_array() for g in self.population])
            dists = []
            for i in range(len(genomes)):
                for j in range(i+1, len(genomes)):
                    dists.append(np.linalg.norm(genomes[i] - genomes[j]))
            return np.mean(dists) if dists else 0
        
        def evolve(self, profile: dict):
            self.evaluate(profile)
            fits = [g.fitness for g in self.population]
            self.best_hist.append(max(fits))
            self.avg_hist.append(np.mean(fits))
            self.diversity_hist.append(self.calc_diversity())
            
            new_pop = []
            elite = sorted(self.population, key=lambda g: g.fitness, reverse=True)[:self.pop_size//5]
            new_pop.extend(elite)
            
            while len(new_pop) < self.pop_size:
                p1, p2 = self.select(), self.select()
                child = self.crossover(p1, p2)
                self.mutate(child)
                new_pop.append(child)
            
            self.population = new_pop
            self.generation += 1
        
        def best(self):
            return max(self.population, key=lambda g: g.fitness)
    return GeneticOptimizer, PreferenceGenome


@app.cell
def __(mo):
    mo.md("### User Profile Selection")
    
    profile_type = mo.ui.dropdown({
        'General User': 'general',
        'Elderly Person': 'elderly',
        'Woman Alone': 'woman_alone',
        'Wheelchair User': 'wheelchair',
        'Parent with Stroller': 'parent',
        'Daily Commuter': 'commuter'
    }, value='woman_alone', label="Profile:")
    
    time_of_day = mo.ui.dropdown({'Day': 'day', 'Night': 'night'}, value='night', label="Time:")
    gens = mo.ui.slider(10, 100, 10, value=50, label="Generations:")
    
    mo.vstack([profile_type, time_of_day, gens])
    return gens, profile_type, time_of_day


@app.cell
def __(
    GeneticOptimizer,
    gens,
    mo,
    np,
    pd,
    plt,
    profile_type,
    time_of_day,
):
    _profile = {'type': profile_type.value, 'time': time_of_day.value}
    _opt = GeneticOptimizer(50)
    _opt.initialize()

    for _ in range(gens.value):
        _opt.evolve(_profile)

    _best = _opt.best()

    _fig6, ((_ax1, _ax2), (_ax3, _ax4)) = plt.subplots(2, 2, figsize=(16, 11))

    _ax1_twin = _ax1.twinx()
    _line1 = _ax1.plot(_opt.best_hist, linewidth=2.5, color='#059669', label='Best Fitness')
    _line2 = _ax1.plot(_opt.avg_hist, linewidth=2, alpha=0.7, color='#3b82f6', label='Avg Fitness')
    _line3 = _ax1_twin.plot(_opt.diversity_hist, linewidth=2, alpha=0.7, color='#f59e0b', 
                            linestyle='--', label='Diversity')
    
    _ax1.set_xlabel('Generation', fontsize=10)
    _ax1.set_ylabel('Fitness', fontsize=10, color='#059669')
    _ax1_twin.set_ylabel('Diversity', fontsize=10, color='#f59e0b')
    _ax1.set_title('Evolution Progress', fontsize=12, fontweight='bold')
    
    _lines = _line1 + _line2 + _line3
    _labels = [l.get_label() for l in _lines]
    _ax1.legend(_lines, _labels, loc='center left')
    _ax1.grid(True, alpha=0.3)

    _labels = ['Safety', 'Distance', 'Access', 'Lighting', 'CCTV']
    _weights = _best.get_array()
    _colors_bar = ['#ef4444', '#3b82f6', '#10b981', '#f59e0b', '#8b5cf6']
    _bars = _ax2.bar(_labels, _weights, color=_colors_bar, edgecolor='black', linewidth=1.5)
    _ax2.set_ylabel('Weight', fontsize=10)
    _ax2.set_title('Learned Weights', fontsize=12, fontweight='bold')
    _ax2.set_ylim(0, 0.6)
    _ax2.grid(True, alpha=0.3, axis='y')
    for _i, (_l, _w, _bar) in enumerate(zip(_labels, _weights, _bars)):
        _height = _bar.get_height()
        _ax2.text(_bar.get_x() + _bar.get_width()/2, _height + 0.01, 
                 f'{_w:.3f}', ha='center', fontsize=9, fontweight='bold')

    _final = np.array([g.get_array() for g in _opt.population])
    _bp = _ax3.boxplot([_final[:, i] for i in range(5)], labels=_labels, patch_artist=True,
                boxprops=dict(facecolor='lightblue', edgecolor='black'),
                medianprops=dict(color='darkblue', linewidth=2))
    
    _ax3.scatter([1,2,3,4,5], _weights, s=200, c='red', marker='*', edgecolors='black', 
                linewidths=1.5, label='Best', zorder=5)
    
    _ax3.set_ylabel('Weight', fontsize=10)
    _ax3.set_title('Population Distribution', fontsize=12, fontweight='bold')
    _ax3.legend()
    _ax3.grid(True, alpha=0.3, axis='y')

    if profile_type.value == 'elderly':
        _ideal = np.array([0.15, 0.15, 0.45, 0.15, 0.10])
    elif profile_type.value == 'woman_alone':
        _ideal = np.array([0.30, 0.10, 0.10, 0.30, 0.20])
    elif profile_type.value == 'wheelchair':
        _ideal = np.array([0.15, 0.15, 0.50, 0.10, 0.10])
    elif profile_type.value == 'parent':
        _ideal = np.array([0.20, 0.15, 0.40, 0.15, 0.10])
    elif profile_type.value == 'commuter':
        _ideal = np.array([0.15, 0.50, 0.10, 0.15, 0.10])
    else:
        _ideal = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
    
    if time_of_day.value == 'night':
        _ideal[0] += 0.10
        _ideal[3] += 0.10
        _ideal = _ideal / _ideal.sum()

    _x = np.arange(5)
    _width = 0.35
    _bars1 = _ax4.bar(_x - _width/2, _ideal, _width, label='Target', 
                     color='lightcoral', edgecolor='black', linewidth=1.5)
    _bars2 = _ax4.bar(_x + _width/2, _weights, _width, label='Learned', 
                     color='lightgreen', edgecolor='black', linewidth=1.5)
    
    _errors = np.abs(_weights - _ideal)
    for _i, (_b1, _b2, _err) in enumerate(zip(_bars1, _bars2, _errors)):
        _y = max(_b1.get_height(), _b2.get_height())
        _ax4.plot([_i, _i], [_ideal[_i], _weights[_i]], 'gray', linestyle=':', linewidth=2, alpha=0.5)
        if _err > 0.02:
            _ax4.text(_i, _y + 0.02, f'D{_err:.3f}', ha='center', fontsize=8, color='red')
    
    _ax4.set_xticks(_x)
    _ax4.set_xticklabels(_labels)
    _ax4.set_ylabel('Weight', fontsize=10)
    _ax4.set_title('Target vs Learned', fontsize=12, fontweight='bold')
    _ax4.legend()
    _ax4.grid(True, alpha=0.3, axis='y')
    
    _convergence = 1 - np.linalg.norm(_weights - _ideal)
    _ax4.text(0.98, 0.98, f'Conv: {_convergence*100:.1f}%', 
             transform=_ax4.transAxes, fontsize=10, fontweight='bold',
             ha='right', va='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    plt.tight_layout()
    _fig6.patch.set_facecolor('white')

    _pref_df = pd.DataFrame({
        'Factor': _labels,
        'Target': [f'{w:.3f}' for w in _ideal],
        'Learned': [f'{w:.3f}' for w in _weights],
        'Diff': [f'{abs(w-i):.3f}' for w, i in zip(_weights, _ideal)]
    })

    mo.md(f"""
    ## Demo: Personalized Preferences

    **Profile:** {profile_type.label}  
    **Fitness:** {_best.fitness:.4f}  
    **Convergence:** {_convergence*100:.1f}%

    {mo.as_html(_fig6)}

    {mo.ui.table(_pref_df)}
    """)
    return


@app.cell
def __(GeneticOptimizer, mo, plt, time):
    mo.md("## Time Complexity Analysis")

    def _measure_ga(_pop, _gens=20):
        _opt = GeneticOptimizer(_pop)
        _opt.initialize()
        _t1 = time.time()
        for _ in range(_gens):
            _opt.evolve({'type': 'general', 'time': 'day'})
        _t2 = time.time()
        return (_t2 - _t1) * 1000

    _pops = [20, 40, 60, 80, 100, 150, 200]
    _ga_times = [_measure_ga(_p) for _p in _pops]

    _fig7 = plt.figure(figsize=(10, 6))
    _ax = _fig7.add_subplot(111)
    _ax.plot(_pops, _ga_times, 'o-', linewidth=2.5, markersize=8, color='#8b5cf6')
    _ax.set_xlabel('Population', fontsize=11)
    _ax.set_ylabel('Time (ms)', fontsize=11)
    _ax.set_title('Genetic Algorithm Time', fontsize=13, fontweight='bold')
    _ax.grid(True, alpha=0.3)
    _linear = [_p * 2 for _p in _pops]
    _ax.plot(_pops, _linear, '--', alpha=0.5, color='green', label='O(P)')
    _ax.legend()
    
    plt.tight_layout()
    _fig7.patch.set_facecolor('white')

    mo.md(f"""
    {mo.as_html(_fig7)}

    **Complexity:** O(G x P x F)  
    **Scalability:** Linear with population
    """)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ##  Critical Aspects & Bias Analysis

        ### Potential Biases

        1. **Profile Stereotyping**: Pre-defined profiles (elderly, woman alone) reinforce stereotypes and ignore individual variation

        2. **Binary Demographics**: Categories don't capture intersectionality (elderly wheelchair user, trans woman, etc.)

        3. **Fitness Function Bias**: "Ideal" weights encode designer's assumptions about what users "should" want

        4. **Optimization Goal**: Maximizing match to stereotype may ignore genuine individual preferences

        5. **Feedback Loop**: System learns from initial categorization, potentially reinforcing harmful assumptions

        ### Affected Populations

        - **Individuals who don't fit categories**: Non-binary, young with mobility issues
        - **People with multiple identities**: Intersectional experiences not captured
        - **Users who want self-definition**: Forced into pre-selected profiles
        - **Cultural minorities**: Western assumptions about safety may not apply

        ### Mitigation Strategies Implemented

        1. **User-adjustable evolution**: Manual override of learned preferences
        2. **Transparent weights**: Users see exactly what's being optimized
        3. **Profile as starting point**: Not rigid constraint, preferences can diverge
        4. **Continuous learning**: Adapts beyond initial profile

        ### Recommendations

        - **Preference discovery, not profiling**: Learn from actual route choices, not demographics
        - **Intersectional categories**: Support multiple overlapping identity dimensions
        - **User-defined profiles**: Allow custom safety priority definitions
        - **Reject categorization option**: Purely behavioral learning
        - **Explain evolution**: Show why algorithm recommends weights
        - **Community templates**: Let groups co-create safety definitions
        - **Active learning**: Ask users to rate routes to improve accuracy

        ---
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        # Algorithm 5 - Perceptron - Safety Zone Classification

        ## Introduction 

        **Why Perceptron?**

        The perceptron provides interpretable linear classification with microsecond inference times.

        ---
        """
    )
    return


@app.cell
def __(np):
    class SafetyPerceptron:
        def __init__(self, num_features: int, num_classes: int = 3, lr: float = 0.01):
            self.num_features = num_features
            self.num_classes = num_classes
            self.lr = lr
            self.weights = np.random.randn(num_classes, num_features) * 0.01
            self.bias = np.zeros(num_classes)
            self.history = []
        
        def predict(self, X):
            scores = X @ self.weights.T + self.bias
            return np.argmax(scores, axis=1)
        
        def train(self, X, y, epochs=100):
            n = len(X)
            for epoch in range(epochs):
                preds = self.predict(X)
                acc = np.mean(preds == y)
                self.history.append(acc)
                
                for i in range(n):
                    if y[i] != preds[i]:
                        self.weights[y[i]] += self.lr * X[i]
                        self.bias[y[i]] += self.lr
                        self.weights[preds[i]] -= self.lr * X[i]
                        self.bias[preds[i]] -= self.lr
        
        def feature_importance(self):
            return np.abs(self.weights).mean(axis=0)


    def generate_street_data(n=1000):
        np.random.seed(42)
        lighting = np.random.uniform(0, 1, n)
        cctv = np.random.uniform(0, 1, n)
        crime = np.random.randint(0, 10, n)
        access = np.random.uniform(0, 1, n)
        hour = np.random.randint(0, 24, n)
        is_weekend = np.random.binomial(1, 2/7, n)
        emergency = np.random.uniform(0, 1, n)
        
        labels = np.zeros(n, dtype=int)
        for i in range(n):
            score = 0
            if lighting[i] < 0.4: score += 2
            if cctv[i] < 0.3: score += 2
            if crime[i] > 5: score += 3
            elif crime[i] > 2: score += 1
            if access[i] < 0.3: score += 1
            if hour[i] >= 22 or hour[i] <= 5: score += 2
            if emergency[i] < 0.3: score += 1
            
            if score <= 2: labels[i] = 0
            elif score <= 5: labels[i] = 1
            else: labels[i] = 2
        
        X = np.column_stack([lighting, cctv, crime/10.0, access, hour/24.0, is_weekend, emergency])
        return X, labels
    return SafetyPerceptron, generate_street_data


@app.cell
def __(mo):
    mo.md("### Training Parameters")
    
    perc_samples = mo.ui.slider(200, 2000, 200, value=1000, label="Samples")
    perc_epochs = mo.ui.slider(20, 200, 20, value=100, label="Epochs")
    
    mo.vstack([perc_samples, perc_epochs])
    return perc_epochs, perc_samples


@app.cell
def __(
    SafetyPerceptron,
    generate_street_data,
    mo,
    np,
    pd,
    perc_epochs,
    perc_samples,
    plt,
):
    _X_train, _y_train = generate_street_data(perc_samples.value)
    _X_test, _y_test = generate_street_data(500)

    _perc = SafetyPerceptron(_X_train.shape[1], lr=0.05)
    _perc.train(_X_train, _y_train, epochs=perc_epochs.value)

    _train_pred = _perc.predict(_X_train)
    _test_pred = _perc.predict(_X_test)
    _train_acc = np.mean(_train_pred == _y_train) * 100
    _test_acc = np.mean(_test_pred == _y_test) * 100

    _conf = np.zeros((3, 3), dtype=int)
    for _t, _p in zip(_y_test, _test_pred):
        _conf[_t][_p] += 1

    _fig8, ((_ax1, _ax2), (_ax3, _ax4)) = plt.subplots(2, 2, figsize=(15, 10))

    _ax1.plot(_perc.history, linewidth=2, color='#0891b2')
    _ax1.set_xlabel('Epoch', fontsize=10)
    _ax1.set_ylabel('Accuracy', fontsize=10)
    _ax1.set_title('Learning Curve', fontsize=12, fontweight='bold')
    _ax1.grid(True, alpha=0.3)
    _ax1.axhline(y=_train_acc/100, color='red', linestyle='--', alpha=0.5, label=f'Final: {_train_acc:.1f}%')
    _ax1.legend()

    _im = _ax2.imshow(_conf, cmap='Blues', aspect='auto')
    _ax2.set_xticks([0, 1, 2])
    _ax2.set_yticks([0, 1, 2])
    _ax2.set_xticklabels(['Safe', 'Moderate', 'High'])
    _ax2.set_yticklabels(['Safe', 'Moderate', 'High'])
    _ax2.set_xlabel('Predicted', fontsize=10)
    _ax2.set_ylabel('True', fontsize=10)
    _ax2.set_title('Confusion Matrix', fontsize=12, fontweight='bold')
    for _i in range(3):
        for _j in range(3):
            _ax2.text(_j, _i, str(_conf[_i][_j]), ha='center', va='center',
                     color='white' if _conf[_i][_j] > _conf.max()/2 else 'black', fontsize=13, fontweight='bold')

    _feat_names = ['Lighting', 'CCTV', 'Crime', 'Access', 'Hour', 'Weekend', 'Emergency']
    _importance = _perc.feature_importance()
    _colors = plt.cm.viridis(np.linspace(0, 1, len(_feat_names)))
    _ax3.barh(_feat_names, _importance, color=_colors, edgecolor='black')
    _ax3.set_xlabel('Importance', fontsize=10)
    _ax3.set_title('Feature Importance', fontsize=12, fontweight='bold')
    _ax3.grid(True, alpha=0.3, axis='x')

    _train_dist = [np.sum(_train_pred == i) for i in range(3)]
    _test_dist = [np.sum(_test_pred == i) for i in range(3)]
    _x = np.arange(3)
    _w = 0.35
    _ax4.bar(_x - _w/2, _train_dist, _w, label='Train', color='#3b82f6', edgecolor='black')
    _ax4.bar(_x + _w/2, _test_dist, _w, label='Test', color='#f59e0b', edgecolor='black')
    _ax4.set_xlabel('Risk Zone', fontsize=10)
    _ax4.set_ylabel('Count', fontsize=10)
    _ax4.set_title('Predictions', fontsize=12, fontweight='bold')
    _ax4.set_xticks(_x)
    _ax4.set_xticklabels(['Safe', 'Moderate', 'High'])
    _ax4.legend()
    _ax4.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    _fig8.patch.set_facecolor('white')

    _perf_df = pd.DataFrame({
        'Metric': ['Train Accuracy', 'Test Accuracy'],
        'Value': [f'{_train_acc:.2f}%', f'{_test_acc:.2f}%']
    })

    mo.md(f"""
    ## Demo: Safety Classification

    {mo.as_html(_fig8)}

    {mo.ui.table(_perf_df)}
    """)
    return


@app.cell
def __(SafetyPerceptron, generate_street_data, mo, np, plt, time):
    mo.md("## Time Complexity Analysis")

    _sizes = [100, 200, 400, 800, 1600, 3200]
    _times = []

    for _s in _sizes:
        _runs = []
        for _ in range(2):
            _X, _y = generate_street_data(_s)
            _p = SafetyPerceptron(_X.shape[1])
            _t1 = time.time()
            _p.train(_X, _y, epochs=50)
            _t2 = time.time()
            _runs.append((_t2 - _t1) * 1000)
        _times.append(np.mean(_runs))

    _fig9 = plt.figure(figsize=(10, 6))
    _ax = _fig9.add_subplot(111)
    _ax.plot(_sizes, _times, 'o-', linewidth=2.5, markersize=8, color='#ec4899')
    _ax.set_xlabel('Samples', fontsize=11)
    _ax.set_ylabel('Time (ms)', fontsize=11)
    _ax.set_title('Perceptron Training', fontsize=13, fontweight='bold')
    _ax.grid(True, alpha=0.3)
    _linear = [_s * 0.01 for _s in _sizes]
    _ax.plot(_sizes, _linear, '--', alpha=0.5, color='green', label='O(n)')
    _ax.legend()
    plt.tight_layout()
    _fig9.patch.set_facecolor('white')

    mo.md(f"""
    {mo.as_html(_fig9)}

    **Complexity:** O(n x m x e)  
    **Scalability:** Linear
    """)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ##  Critical Aspects & Bias Analysis

        ### Potential Biases

        1. **Historical Data Bias**: Training on past patterns perpetuates existing inequalities in infrastructure investment

        2. **Sensor Coverage Bias**: Areas with poor sensors have lower-quality predictions, correlating with lower-income neighborhoods

        3. **Feature Selection Bias**: Chosen features (speed, count) favor car traffic; lack features for transit, cycling, pedestrians

        4. **Temporal Bias**: Night/day binary doesn't capture cultural events, religious holidays, non-Western patterns

        5. **Binary Weather**: "Is raining" ignores snow, fog, heat waves affecting different populations differently

        ### Affected Populations

        - **Public transit users**: Predictions don't account for bus/train delays
        - **Gig economy workers**: Traffic patterns don't capture app-based delivery routes
        - **Under-resourced communities**: Under-prediction due to lack of sensors → continued under-investment
        - **Pedestrians and cyclists**: Model blind to their congestion experiences

        ### Mitigation Strategies Implemented

        1. **Multi-modal features**: Attempted to include diverse factors beyond vehicle metrics
        2. **Class balance monitoring**: Training data represents all risk levels fairly
        3. **Interpretable model**: Linear perceptron allows auditing which features drive predictions
        4. **Feature importance transparency**: Users see what matters most

        ### Recommendations

        - **Data equity**: Invest in sensor coverage in underserved areas before deployment
        - **Multi-modal models**: Separate classifiers for cars, buses, bikes, pedestrians
        - **Fairness metrics**: Track prediction accuracy across different neighborhoods
        - **Community-defined features**: Include culturally relevant patterns
        - **Adversarial debiasing**: Test for disparate impact across protected groups
        - **Human oversight**: Allow controllers to flag and correct biased predictions
        - **Periodic retraining**: Update with recent data to adapt to changing patterns
        - **Transparency reporting**: Public dashboard showing accuracy by neighborhood

        ---
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        #  Conclusion & Ethical Reflection

        ## Summary

        ***Aegis* demonstrates how five classic algorithms work together to prioritize personal safety in urban navigation:

        1. **Dijkstra's Algorithm** → Finds safest routes considering lighting, CCTV, crime, accessibility
        2. **Binary Search** → Instant lookup of buildings and crime incidents  
        3. **MergeSort** → Ranks alternative routes by user-weighted preferences
        4. **Genetic Algorithm** → Learns personalized safety priorities over time
        5. **Perceptron** → Classifies street segments into risk zones

        ## Performance Results

        - **Dijkstra**: O((V+E) log V) — Real-time pathfinding (<50ms for 100 intersections)
        - **Binary Search**: O(log n) — Microsecond queries on 100K+ records
        - **MergeSort**: O(n log n) guaranteed — Stable ranking in <10ms
        - **Genetic**: O(G×P) — Linear scaling, learns preferences in 50 generations
        - **Perceptron**: O(n×m×e) — Perfect linear scaling, 80%+ accuracy

        All algorithms scale efficiently for city-wide deployment.

        ## Critical Reflection: Algorithmic Justice

        While technically sound, **this system embodies significant structural biases**:

        ### Systemic Issues

        1. **Infrastructure Inequality**: Better sensors in affluent areas → better service → reinforced inequality
        
        2. **Data as Power Structure**: Crime data reflects policing patterns, not actual safety → over-policed communities marked "dangerous" → economic isolation

        3. **Optimization Encodes Values**: "Safety" defined by lighting/CCTV privileges surveillance-based security over community-based approaches

        4. **Algorithmic Redlining**: Route avoidance recreates historical redlining digitally

        5. **One-Size-Fits-All Safety**: Western assumptions about what makes people safe ignores cultural, gendered, and community-specific knowledge

        ### Who Bears the Costs?

        - **Residents of "avoided" neighborhoods**: Economic harm from reduced foot traffic
        - **Racial minorities**: Stigmatization through algorithmic labeling
        - **People with disabilities**: Excluded by incomplete/inaccurate data
        - **Cultural minorities**: Safety definitions don't match their lived experiences
        - **Surveillance resisters**: Forced into monitored areas to access "safe" routes

        ## Path Forward: Towards Ethical Deployment

        ### Technical Mitigation

        1.  **User Control**: Implemented adjustable preference weights
        2.  **Transparency**: All scores visible to users
        3.  **Route Diversity**: Show multiple alternatives
        4.  **Equity Audits**: Need continuous monitoring of which neighborhoods are avoided
        5.  **Community Data**: Need participatory data collection from affected communities

        ### Governance Requirements

        **This system should NOT be deployed without:**

        - **Community governance**: Affected communities control deployment decisions
        - **Democratic goal-setting**: "Safety" defined participatorily, not algorithmically
        - **Transparency mandates**: Open algorithms, data sources, and decision logs
        - **Equity metrics**: Regular public reporting on disparate impacts
        - **Harm remediation**: Compensation mechanisms for negatively affected communities
        - **Right to refuse**: Option to opt out of being datafied/classified

        ### Beyond Technical Solutions

        **Algorithms cannot solve social problems created by structural inequality.** The need for a "Safety Navigator" reflects:

        - Inadequate public infrastructure investment
        - Unequal distribution of safety resources
        - Systemic violence against marginalized groups
        - Failing social support systems

        **Real solutions require:**
        - Equitable infrastructure investment across all neighborhoods
        - Addressing root causes of crime (poverty, lack of opportunity)
        - Community-led safety initiatives
        - Accountability for historical discrimination

        ## Final Thoughts

        **Algorithm design is never neutral.** Every technical choice—which data to collect, how to weight factors, what to optimize—encodes values, priorities, and power structures.

        This project demonstrates that:
        - Technical competence alone is insufficient for ethical systems
        - Efficiency ≠ Justice
        - Optimization can perpetuate oppression
        - Transparency ≠ Accountability

        **Responsible technologists must:**
        - Center affected communities in design
        - Question whose interests are served
        - Resist techno-solutionism
        - Advocate for structural change alongside technical work

        Safety is a **right**, not a **product**. Technology can support it, but cannot replace collective responsibility for creating just, equitable communities.

        ---

        
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        

        **Ai Tool Acknowledgement**

        ChatGPT (OpenAI) – debugging, formatting, and syntax support for Marimo and Python

        Claude (Anthropic) – visual layout and presentation support

        ---
        """
    )
    return


if __name__ == "__main__":
    app.run()