| **Component** | **Your Current Tech** | **Goal/Function** | **Recommended Stack/Bridge** |
| --- | --- | --- | --- |
| **Perception** | Orbbec Gemini 2L & ORB-SLAM3 | Provide accurate, drift-free pose (Odometry) and Mapping data. | **Working (ROS 2 ORB-SLAM3 Node)** |
| **Navigation Stack** | *(Missing)* | Generate a safe, collision-free **3D path** based on a goal and map data. | **Aerostack2** (or Nav2 Adaptation) |
| **Flight Control Bridge** | *(Missing)* | Translate the high-level ROS 2 path/velocity commands into MAVLink commands. | **Micro-XRCE-DDS Client** (for PX4) or **MAVROS** |
| **Autopilot/Actuation** | ArduPilot or PX4 | Execute the low-level flight control and stability commands. | **ArduPilot/PX4** (Onboard Flight Controller |
