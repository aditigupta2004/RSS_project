# scara — SCARA robot using ROS 2

![SCARA manipulator](assets/scara_manipulator.png)

Project
-------
Purpose: a complete SCARA robot project for simulation, control, and motion planning.

Components:
- `src/scara_description`: robot model (URDF/xacro), visuals, and meshes.
- `src/scara_controller`: ROS 2 controller configurations and controller manager integrations.
- `src/scara_moveit`: MoveIt 2 configuration for planning (SRDF, planning groups, and launch files).

Architecture:
- Model: `xacro` defines links, joints, inertias, and transmissions used by controllers.
- Hardware Abstraction: `ros2_control` interfaces bridge the model to controller plugins.
- Controllers: joint and trajectory controllers run under `controller_manager` to accept commands and publish states.
- Planning Stack: `move_group` uses the robot model and controllers to plan and execute trajectories; RViz provides visualization and teleoperation.

Quick links:
- Description URDF: [src/scara_description/urdf/basic_scara.urdf.xacro](src/scara_description/urdf/basic_scara.urdf.xacro)
- Controller package: [src/scara_controller](src/scara_controller)
- MoveIt config: [src/scara_moveit](src/scara_moveit)

**Requirements**
- ROS 2 (Humble or later recommended)
- colcon build tool
- Gazebo (if using the provided simulation launch)
- MoveIt 2

Installation
-----------
1. Install ROS 2 and required packages for your platform. See the ROS 2 installation guide for your distro.
2. From the workspace root, install package dependencies using rosdep:

```bash
sudo apt update
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

Build
-----

```bash
colcon build --symlink-install
source install/setup.bash
```

Run / Launch
------------

- Start Gazebo (robot description spawn):

```bash
ros2 launch scara_description gazebo.launch.py
```

- Launch controllers and verify:

```bash
ros2 control list_controllers
# to load/start controllers (example):
# ros2 control load_start_controller <controller_name>
```

- Start MoveIt (planning and RViz):

```bash
ros2 launch scara_moveit move_group.launch.py
ros2 launch scara_moveit moveit_rviz.launch.py
```

Notes
-----
- URDF/xacro: edit [src/scara_description/urdf/basic_scara.urdf.xacro](src/scara_description/urdf/basic_scara.urdf.xacro) to change link or joint properties.
- Controller configs are in `src/scara_controller` — check YAML files and `controller_manager` usage.
- MoveIt configs live in `src/scara_moveit` and include planning groups, SRDF, and launch files.

