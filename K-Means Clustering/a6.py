# a6.py
# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""Classes to perform KMeans Clustering"""

import math
import random
import numpy
import sys

# HELPER FUNCTIONS FOR ASSERTS GO HERE

def valid_dimension(dimension):
    assert type(dimension)==int, str(dimension) + 'is not an int'
    assert dimension > 0, str(dimension) + 'is not greater than zero'
    
def valid_2D(contents,dim):
    assert contents is None or type(contents)==list, str(contents)+ 'is not a list'
    if type(contents)==list:
        for k in contents:
            assert type(k) == list, str(k) + 'is not a 2-D list'
            assert contents != [], str(contents) + 'is an empty list'
            assert len(k) == dim, str(dim) + 'has invalid dimensions'
            
            for i in range(len(k)):
                assert type(i)==int or type(i)==float, str(i) + 'is neither an int nor a float'
                   
    
    

"""contents is either None or 
        it is a 2D list of numbers (int or float). If contents is not None, 
        then contents is not empty and the number of columns of contents is 
        equal to dim.
        """

def is_point(thelist):
    """Return: True if thelist is a list of int or float"""
    if (type(thelist) != list):
        return False
    
    # All float
    okay = True
    for x in thelist:
        if (not type(x) in [int,float]):
            okay = False
    
    return okay


# CLASSES
class Dataset(object):
    """Instance is a dataset for k-means clustering.

    The data is stored as a list of list of numbers
    (ints or floats).  Each component list is a data point.

    Instance Attributes:
        _dimension [int > 0. Value never changes after initialization]:
            the point dimension for this dataset
        _contents  [a 2D list of numbers (float or int), possibly empty]:
            the dataset contents
        
    Additional Invariants:
        The number of columns in _contents is equal to _dimension.  That is,
        for every item _contents[i] in the list _contents, 
        len(_contents[i]) == dimension.
    
    None of the attributes should be accessed directly outside of the class
    Dataset (e.g. in the methods of class Cluster or KMeans). Instead, this class 
    has getter and setter style methods (with the appropriate preconditions) for 
    modifying these values.
    """
    
    def __init__(self, dim, contents= None):   #leave = None???
        """Initializer: Makes a database for the given point dimension.
    
        The parameter dim is the initial value for attribute _dimension.  
  
        The optional parameter contents is the initial value of the
        attribute _contents. When assigning contents to the attribute
        _contents it COPIES the list contents. If contents is None, the 
        initializer assigns _contents an empty list. The parameter contents 
        is None by default.
    
        Precondition: dim is an int > 0. contents is either None or 
        it is a 2D list of numbers (int or float). If contents is not None, 
        then contents if not empty and the number of columns of contents is 
        equal to dim.
        """
        valid_dimension(dim)
        valid_2D(contents,dim)
        self._dimension = dim
         
        contents_copy = []
        if contents != None:
            for inner_list in contents:
                copy_inner_list = inner_list[:]   #why's this bad?
                contents_copy.append(copy_inner_list)
        
        self._contents = contents_copy
    
    def getDimension(self):
        """Return: The point dimension of this data set.
        """
        return self._dimension 
    
    def getSize(self):
        """Return: the number of elements in this data set.
        """
        return len(self._contents)
    
    def getContents(self):
        """Return: The contents of this data set as a list.
        
        This method returns the attribute _contents directly.  Any changes
        made to this list will modify the data set.  If you want to access
        the data set, but want to protect yourself from modifying the data,
        use getPoint() instead.
        """
        
        return self._contents   
    
    def getPoint(self, i):
        """Returns: A COPY of the point at index i in this data set.
        
        Often, we want to access a point in the data set, but we want a copy
        to make sure that we do not accidentally modify the data set.  That
        is the purpose of this method.  
        
        If you actually want to modify the data set, use the method getContents().
        That returns the list storing the data set, and any changes to that
        list will alter the data set.
        While it is possible, to access the points of the data set via
        the method getContents(), that method 
        
        Precondition: i is an int that refers to a valid position in the data
        set (e.g. i is between 0 and getSize()).
        """
        point = self._contents[i]
        copy_point = point[:]
        return copy_point
    
    
    def addPoint(self,point):
        """Adds a COPY of point at the end of _contents.
        
        This method does not add the point directly. It adds a copy of the point.
    
        Precondition: point is a list of numbers (int or float),  
        len(point) = _dimension.
        """
        
        copy_point = point[:]
        self._contents.append(copy_point)
        
    
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._contents)
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)


class Cluster(object):
    """An instance is a cluster, a subset of the points in a dataset.

    A cluster is represented as a list of integers that give the indices
    in the dataset of the points contained in the cluster.  For instance,
    a cluster consisting of the points with indices 0, 4, and 5 in the
    dataset's data array would be represented by the index list [0,4,5].

    A cluster instance also contains a centroid that is used as part of
    the k-means algorithm.  This centroid is an n-D point (where n is
    the dimension of the dataset), represented as a list of n numbers,
    not as an index into the dataset.  (This is because the centroid
    is generally not a point in the dataset, but rather is usually in between
    the data points.)

    Instance attributes:
        _dataset [Dataset]: the dataset this cluster is a subset of
        _indices [list of int]: the indices of this cluster's points in the dataset
        _centroid [list of numbers]: the centroid of this cluster
    Extra Invariants:
        len(_centroid) == _dataset.getDimension()
        0 <= _indices[i] < _dataset.getSize(), for all 0 <= i < len(_indices)
    """
    
    # Part A
    def __init__(self, ds, centroid):
        """A new empty cluster whose centroid is a copy of <centroid> for the
        given dataset ds.
    
        Pre: ds is an instance of a subclass of Dataset.
             centroid is a list of ds.getDimension() numbers.
        """
        assert isinstance(ds, Dataset), str(ds) + 'is not an instance of a subclass of Dataset'
        assert type(centroid) == list, str(centroid) + 'is not a list'
        assert len(centroid) == ds.getDimension(), str(centroid) + 'is not a list of ds.getDimension() numbers'
        
        copy_centroid = centroid[:]
        
        self._dataset = ds
        self._centroid = copy_centroid
        self._indices = []

    def getCentroid(self):
        """Returns: the centroid of this cluster.
        
        This getter method is to protect access to the centroid.
        """
        return self._centroid
    
    def getIndices(self):
        """Returns: the indices of points in this cluster
        
        This method returns the attribute _indices directly.  Any changes
        made to this list will modify the cluster.
        """
        
        return self._indices
    
    def addIndex(self, index):
        """Add the given dataset index to this cluster.
        
        If the index is already in this cluster, this method leaves the
        cluster unchanged.
        
        Precondition: index is a valid index into this cluster's dataset.
        That is, index is an int in the range 0.._dataset.getSize().
        """
        assert type(index) == int, str(index) + 'is not an int'
        assert index >= 0 and index <= self._dataset.getSize() 
        
        if not index in self._indices:
            self._indices.append(index)
            
    
    def clear(self):
        """Remove all points from this cluster, but leave the centroid unchanged.
        """
        
        self._indices = []  
    
    def getContents(self):
        """Return: a new list containing copies of the points in this cluster.
        
        The result is a list of list of numbers.  It has to be computed from
        the indices.
        """
        
        
        new_list = []
        for k in self._indices:
            new_list.append(self._dataset.getPoint(k))
        
        return new_list
        
    
    # Part B
    def distance(self, point):
        """Return: The euclidean distance from point to this cluster's centroid.
    
        Pre: point is a list of numbers (int or float)
             len(point) = _ds.getDimension()
        """
        assert is_point(point)
        assert len(point) == self._dataset.getDimension(), 'point incorrect dimensions' #ehhh???
        
        dimension = self._dataset.getDimension()
        
        list_add_points = []
        for j in range(dimension):
            list_add_points.append((point[j] - self._centroid[j])**2)
        
        sum_points = 0
        for k in list_add_points:
            sum_points = sum_points + k
        
        distance = math.sqrt(sum_points)
        return distance
        
        
        
        
    
    def updateCentroid(self):
        """Returns: Trues if the centroid remains the same after recomputation,
        and False otherwise.
        
        This method recomputes the _centroid attribute of this cluster. The
        new _centroid attribute is the average of the points of _contents
        (To average a point, average each coordinate separately).  
    
        Whether the centroid "remained the same" after recomputation is
        determined by numpy.allclose.  The return value should be interpreted
        as an indication of whether the starting centroid was a "stable"
        position or not.
    
        If there are no points in the cluster, the centroid does not change.
        """
        
        first_centroid = self._centroid[:]
        final_centroid = []
        if self._indices == []:
            return True 
          
        
        for element in range(self._dataset.getDimension()):
            sum_points = 0.0
            for index in self._indices:
                point = self._dataset.getPoint(index)
                sum_points = sum_points + point[element]
            final_centroid.append(sum_points/(len(self._indices)))
        self._centroid = final_centroid
        
        return numpy.allclose(first_centroid, self._centroid)
    
    
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._centroid)
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)


class ClusterGroup(object):
    """An instance is a set of clusters of the points in a dataset.

    Instance attributes:
        _dataset [Dataset]: the dataset which this is a clustering of
        _clusters [list of Cluster]: the clusters in this clustering (not empty)
    """
    
    # Part A
    def __init__(self, ds, k, seed_inds=None):
        """A clustering of the dataset ds into k clusters.
        
        The clusters are initialized by randomly selecting k different points
        from the database to be the centroids of the clusters.  If seed_inds
        is supplied, it is a list of indices into the dataset that specifies
        which points should be the initial cluster centroids.
        
        Pre: ds is an instance of a subclass of Dataset.
             k is an int, 0 < k <= ds.getSize().
             seed_inds is None, or a list of k valid indices into ds.
        """
        
        assert type(ds) == Dataset, str(ds) + 'is not of type Dataset'
        assert type(k) == int, str(k) + 'is not an int'
        assert k >= 0 and k <= ds.getSize()
        assert seed_inds is None or type(seed_inds) == list
        
        self._dataset = ds
        self._k = k
        
        self._seed_inds = []
        
        cluster_list = []
        if seed_inds != None:
            for k in seed_inds:
                centroid1 = ds.getPoint(k)
                cluster1 = Cluster(ds, centroid1)
                cluster_list.append(cluster1)
        else:
            centroid1 = random.sample(ds._contents,k)
            for point in centroid1:
                print point
                cluster1 = Cluster(ds,point)
                if cluster1 not in cluster_list:
                    cluster_list.append(cluster1)
                    
        
        self._clusters = cluster_list
                
                
                
                
            
        
    def getClusters(self):
        """Return: The list of clusters in this object.
        
        This method returns the attribute _clusters directly.  Any changes
        made to this list will modify the set of clusters.
        """ 
        return self._clusters
    
    
    # Part B
    
    def _nearest_cluster(self, point):
        """Returns: Cluster nearest to point
    
        This method uses the distance method of each Cluster to compute
        the distance between point and the cluster centroid. It returns
        the Cluster that is the closest.
        
        Ties are broken in favor of clusters occurring earlier in the
        list of self._clusters.
        
        Pre: point is a list of numbers (int or float),
             len(point) = self._dataset.getDimension().
        """
        
        current_nearest_cluster = [sys.float_info.max,[]] #max value to ensure correct start
        for cluster in self._clusters:
            cluster_centroid = cluster.getCentroid()
            distance_to = cluster.distance(point)
            if distance_to < current_nearest_cluster[0]:
                current_nearest_cluster[0] = distance_to
                current_nearest_cluster[1] = cluster
        
        return current_nearest_cluster[1]
            
        
    
    def _partition(self):
        """Repartition the dataset so each point is in exactly one Cluster.
        """
        # First, clear each cluster of its points.  Then, for each point in the
        # dataset, find the nearest cluster and add the point to that cluster.
        
        ds_contents = self._dataset.getContents()
        
        for cluster in self._clusters:
            cluster.clear()
        
        for k in range(len(ds_contents)):
            nearest_cluster = self._nearest_cluster(ds_contents[k])
            nearest_cluster.addIndex(k)
            
            
        
    
    # Part C
    def _update(self):
        """Return:True if all centroids are unchanged after an update; False otherwise.
        
        This method first updates the centroids of all clusters'.  When it is done, it
        checks whether any of them have changed. It then returns the appropriate value.
        """
        bool_list = [] 
        for cluster in self._clusters:
            bool_list.append(cluster.updateCentroid())
        
        if False in bool_list:
            return False 
        return True        
    
    def step(self):
        """Return: True if the algorithm converges after one step; False otherwise.
        
        This method performs one cycle of the k-means algorithm. It then checks if
        the algorithm has converged and returns the appropriate value.
        """
        # In a cycle, we partition the points and then update the means.
        
        self._partition()
        return self._update()
        
    
    # Part D
    def run(self, maxstep):
        """Continue clustering until either it converges or maxstep steps 
        (which ever comes first).
        """
        # Call step repeatedly, up to maxstep times, until the algorithm
        # converges.  Stop after maxstep iterations even if the algorithm has not
        # converged.
        
        counter = 0
        while counter < maxstep:
            self.step()
            counter = counter + 1
    
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._clusters)
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)

