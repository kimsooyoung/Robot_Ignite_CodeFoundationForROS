# Robot Ignite Code Foundation for ROS Prerequisites Exam

### Project Status:

![issue_badge](https://img.shields.io/badge/exam%20score-6.5-orange) 

### Robot Ignite의 첫번째 코스 Code Foundation for ROS의 시험 솔루션입니다.


**Exam** This exam is based on a Turtlebot robot, which you already know pretty well since it has been used alongside the Courses.

## Installation

### Ubuntu

```bash
$> sudo apt install libpcl-dev
$> cd ~
$> git clone https://github.com/udacity/SFND_Lidar_Obstacle_Detection.git
$> cd SFND_Lidar_Obstacle_Detection
$> mkdir build && cd build
$> cmake ..
$> make
$> ./environment
```

### Windows

http://www.pointclouds.org/downloads/windows.html

### MAC

#### Install via Homebrew

1. install [homebrew](https://brew.sh/)
2. update homebrew
   ```bash
   $> brew update
   ```
3. add homebrew science [tap](https://docs.brew.sh/Taps)
   ```bash
   $> brew tap brewsci/science
   ```
4. view pcl install options
   ```bash
   $> brew options pcl
   ```
5. install PCL
   ```bash
   $> brew install pcl
   ```

#### Prebuilt Binaries via Universal Installer

http://www.pointclouds.org/downloads/macosx.html  
NOTE: very old version

#### Build from Source

[PCL Source Github](https://github.com/PointCloudLibrary/pcl)

[PCL Mac Compilation Docs](http://www.pointclouds.org/documentation/tutorials/compiling_pcl_macosx.php)

### This project contains

- How to handle pcl library
- Segmentaion (Separate ground points and obstacle points)
- Clustering Obstacle points
- Handle Real World Data
- Stream Real World Data with Real-Time Clustering

## Additional works for project submission

> implement own Clustering/Segmentation algorithms, using RANSAC, KD-Tree, and Euclidean clustering that learned from previsous lessons.

#### 1. Segmentation using RANSAC

See `RANSAC3DSegment` function in `processPointClouds.h`

```c++
std::pair<typename pcl::PointCloud<PointT>::Ptr, typename pcl::PointCloud<PointT>::Ptr> RANSAC3DSegment(typename pcl::PointCloud<PointT>::Ptr cloud, int maxIterations, float distanceThreshold);

```

#### 2. Clustering using KD-Tree, and Euclidean Proximity

See `EuclideanClustering`, `euclideanCluster`, `clusterHelper` function in `processPointClouds.h`

```c++
void clusterHelper(int pointIdx, const std::vector<std::vector<float>>& points, std::vector<int>& cluster, std::vector<bool>& processed, KdTree* tree, float distanceTol);

std::vector<std::vector<int>> euclideanCluster(const std::vector<std::vector<float>>& points, KdTree* tree, float distanceTol);

std::vector<typename pcl::PointCloud<PointT>::Ptr> EuclideanClustering(typename pcl::PointCloud<PointT>::Ptr cloud, float clusterTolerance, int minSize, int maxSize);
```
