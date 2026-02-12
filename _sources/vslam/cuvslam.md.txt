# cuVSLAM and PyCuVSLAM

## Overview
isaac_ros_visual_slam provides a high-performance, GPU-accelerated Visual SLAM solution.

## Resources

### Documentation & Code
- **cuVSLAM Paper**: [arxiv.org/pdf/2506.04359](https://arxiv.org/pdf/2506.04359)
- **cuVSLAM Repository**: [NVIDIA-ISAAC-ROS/isaac_ros_visual_slam](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam)
- **cuVSLAM Documentation**: [isaac_ros_docs](https://nvidia-isaac-ros.github.io/isaac_ros_visual_slam/)
- **PyCuVSLAM Repository**: [NVlabs/PyCuVSLAM](https://github.com/NVlabs/PyCuVSLAM)
- **PyCuVSLAM Documentation**: [PyCuVSLAM documentation](https://pycuvslam.readthedocs.io/en/latest/)

### Tutorials & Forums
- [SeedStudio Wiki: PyCuVSLAM on reComputer](https://wiki.seeedstudio.com/pycuvslam_recomputer_robotics/)
- [NVIDIA Developer Forum: PyCuVSLAM in Aerial Outdoor Environment](https://forums.developer.nvidia.com/t/pycuvslam-in-aerial-outdoor-environment/342176)
- [Andrew Bernas: Robotics/VSLAM Tutorials](https://www.andrewbernas.com/docs/tutorials/robots/vslam)

### Video Demonstrations
- **VSLAM UAV Pipeline using Isaac ROS**: [YouTube Link](https://www.youtube.com/watch?v=ImaltGOlEDc)
    > Demonstration of my VSLAM UAV pipeline using Isaac ROS Visual SLAM. The motion capture cameras visible in the video are used solely for ground truth pose validation. The UAV relies entirely on visual-inertial odometry (VIO) and the flight controller's IMU, fused through an Extended Kalman Filter (EKF), for local pose estimation during flight. Code: [bandofpv/VSLAM-UAV](https://github.com/bandofpv/VSLAM-UAV)