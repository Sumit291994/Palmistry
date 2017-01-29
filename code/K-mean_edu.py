import sys
import math
import random
import subprocess

def main():
    print "Applying K-Mean Algorithm on Education, k = 3 "
    f = open("databases/index.txt","r")
    n = int(f.read())
    f.close()
    # How many points are in our dataset?
    num_points = n-1
    
    # For each of those points how many dimensions do they have?
    dimensions = 3
    
    # Bounds for the values of those points in each dimension
    lower = 0
    upper = 100
    
    # The K in k-means. How many clusters do we assume exist?
    num_clusters = 3
    
    # When do we say the optimization has 'converged' and stop updating clusters
    opt_cutoff = 0.5
    
    # Generate some points
    points = [makeRandomPoint(dimensions, i) for i in xrange(num_points)]
    print points 
    # Cluster those data!
    clusters = kmeans(points, num_clusters, opt_cutoff)

    maxx = []
    for j in range(num_clusters):
        maxx.append(0)

    f = open("databases/index.txt","r")
    n = int(f.read())
    f.close()

    x = []
    y = []
    z = []
    ratios = []

    for i in range (n-1):
        s = "databases/Education/"+str(i+1)+".txt"
        f = open(s,"r")
        x.append(int(f.readline()))
        y.append(int(f.readline()))
        z.append(int(f.readline()))
        #print x[i],y[i],z[i]
        f.close()
        
        s = "databases/Ratios/"+str(i+1)+".txt"
        f = open(s,"r")
        ratios.append(float(f.readline()))
        f.close()
        
    # Print our clusters
    for i,c in enumerate(clusters):
        for p in c.points:
            print " Cluster: ", i, "\t Point :", p
            for j in range(n-1):
                if p.coords[0]==x[j] and p.coords[1]==y[j] and p.coords[2]==z[j]:
                    if maxx[i] < ratios[j]:
                        maxx[i]=ratios[j]
            
           # print p.coords[0]
    print maxx
    maxx.sort()
    print maxx
    f = open("datarule/Education.txt","w")
    for j in range(num_clusters):
         f.write(str(maxx[j])+'\n')
   
    f.close()
    

class Point:
    '''
    An point in n dimensional space
    '''
    def __init__(self, coords):
        '''
        coords - A list of values, one per dimension
        '''
        
        self.coords = coords
        self.n = len(coords)
        
    def __repr__(self):
        return str(self.coords)

class Cluster:
    '''
    A set of points and their centroid
    '''
    
    def __init__(self, points):
        '''
        points - A list of point objects
        '''
        
        if len(points) == 0: raise Exception("ILLEGAL: empty cluster")
        # The points that belong to this cluster
        self.points = points
        
        # The dimensionality of the points in this cluster
        self.n = points[0].n
        
        # Assert that all points are of the same dimensionality
        for p in points:
            if p.n != self.n: raise Exception("ILLEGAL: wrong dimensions")
            
        # Set up the initial centroid (this is usually based off one point)
        self.centroid = self.calculateCentroid()
        
    def __repr__(self):
        '''
        String representation of this object
        '''
        return str(self.points)
    
    def update(self, points):
        '''
        Returns the distance between the previous centroid and the new after
        recalculating and storing the new centroid.
        '''
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculateCentroid()
        shift = getDistance(old_centroid, self.centroid) 
        return shift
    
    def calculateCentroid(self):
        '''
        Finds a virtual center point for a group of n-dimensional points
        '''
        numPoints = len(self.points)
        # Get a list of all coordinates in this cluster
        coords = [p.coords for p in self.points]
        # Reformat that so all x's are together, all y'z etc.
        unzipped = zip(*coords)
        # Calculate the mean for each dimension
        centroid_coords = [math.fsum(dList)/numPoints for dList in unzipped]
        
        return Point(centroid_coords)

def kmeans(points, k, cutoff):
    
    # Pick out k random points to use as our initial centroids
    initial = random.sample(points, k)
    
    # Create k clusters using those centroids
    clusters = [Cluster([p]) for p in initial]
    
    # Loop through the dataset until the clusters stabilize
    loopCounter = 0
    while True:
        # Create a list of lists to hold the points in each cluster
        lists = [ [] for c in clusters]
        clusterCount = len(clusters)
        
        # Start counting loops
        loopCounter += 1
        # For every point in the dataset ...
        for p in points:
            # Get the distance between that point and the centroid of the first
            # cluster.
            smallest_distance = getDistance(p, clusters[0].centroid)
        
            # Set the cluster this point belongs to
            clusterIndex = 0
        
            # For the remainder of the clusters ...
            for i in range(clusterCount - 1):
                # calculate the distance of that point to each other cluster's
                # centroid.
                distance = getDistance(p, clusters[i+1].centroid)
                # If it's closer to that cluster's centroid update what we
                # think the smallest distance is, and set the point to belong
                # to that cluster
                if distance < smallest_distance:
                    smallest_distance = distance
                    clusterIndex = i+1
            lists[clusterIndex].append(p)
        
        # Set our biggest_shift to zero for this iteration
        biggest_shift = 0.0
        
        # As many times as there are clusters ...
        for i in range(clusterCount):
            # Calculate how far the centroid moved in this iteration
            shift = clusters[i].update(lists[i])
            # Keep track of the largest move from all cluster centroid updates
            biggest_shift = max(biggest_shift, shift)
        
        # If the centroids have stopped moving much, say we're done!
        if biggest_shift < cutoff:
            print "Converged after %s iterations" % loopCounter
            break
    return clusters

def getDistance(a, b):
    '''
    Euclidean distance between two n-dimensional points.
    Note: This can be very slow and does not scale well
    '''
    if a.n != b.n:
        raise Exception("ILLEGAL: non comparable points")
    
    ret = reduce(lambda x,y: x + pow((a.coords[y]-b.coords[y]), 2),range(a.n),0.0)
    return math.sqrt(ret)

def makeRandomPoint(n, i):
    '''
    Returns a Point object with n dimensions and values between lower and
    upper in each of those dimensions
    '''
   # p = Point([random.uniform(lower, upper) for i in range(n)])
    s = "databases/Education/"+str(i+1)+".txt"
    f = open(s,"r")
    p = Point([int(f.readline()) for i in range(n)])
    f.close()
    return p

def plotClusters(data):
    '''
    Use the plotly API to plot data from clusters.
    
    Gets a plot URL from plotly and then uses subprocess to 'open' that URL
    from the command line. This should open your default web browser.
    '''
    
    # List of symbols each cluster will be displayed using    
    symbols = ['circle', 'cross', 'triangle-up', 'square']

    # Convert data into plotly format.
    traceList = []
    for i, c in enumerate(data):
        data = []
        for p in c.points:
            data.append(p.coords)
        # Data
        trace = {}
        trace['x'], trace['y'] = zip(*data)
        trace['marker'] = {}
        trace['marker']['symbol'] = symbols[i]
        trace['name'] = "Cluster " + str(i)
        traceList.append(trace)
        # Centroid (A trace of length 1)
        centroid = {}
        centroid['x'] = [c.centroid.coords[0]]
        centroid['y'] = [c.centroid.coords[1]]
        centroid['marker'] = {}
        centroid['marker']['symbol'] = symbols[i]
        centroid['marker']['color'] = 'rgb(200,10,10)'
        centroid['name'] = "Centroid " + str(i)
        traceList.append(centroid)
    
    # Log in to plotly
    py = plotly(username=PLOTLY_USERNAME, key=PLOTLY_KEY)

    # Style the chart
    datastyle = {'mode':'markers',
             'type':'scatter',
             'marker':{'line':{'width':0},
                       'size':12,
                       'opacity':0.6,
                       'color':'rgb(74, 134, 232)'}}
    
    resp = py.plot(*traceList, style = datastyle)
    
    # Display that plot in a browser
    cmd = "open " + resp['url']
    subprocess.call(cmd, shell=True)

if __name__ == "__main__": 
    main()
