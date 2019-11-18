# 使用说明

该包为gmapping各种参数和地图更换测试使用

### launch文件夹

totalmove_gmapping为配置好的launch文件,直接roslaunch运行即可实现启动gazebo,gmapping,rviz,automove等初始配置

```
roslaunch omtb_test totalmove_gmapping_room1.launch 
```

#### 保存map格式文件

不同地图需修改map的信息名称

```
rosrun map_server map_saver map:=/robot1/map -f ~/catkin_slam/src/omtb/omtb_test/map/mapname
```

#### rosbag文件记录

在SLAM过程中记录文件

```
rosbag record -a   //目前如果在launch文件中引用那么会报错直接exit,
rosbag record ~/catkin_slam/src/omtb/omtb_test/bag/ /om_with_tb3/scan /robot1/map /robot1/scan /robot1/odom

```

记录文件后重放

```
roslaunch omtb_slam2d slam.launch  //已经将slam.launch修改为默认启动gmapping
rosbag play bagname.bag     //在omtb_test/bag内打开终端,或者填写完整地址
```

