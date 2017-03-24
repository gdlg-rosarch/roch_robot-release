Name:           ros-kinetic-roch-bringup
Version:        2.0.13
Release:        0%{?dist}
Summary:        ROS roch_bringup package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roch_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-astra-launch
Requires:       ros-kinetic-depthimage-to-laserscan
Requires:       ros-kinetic-diagnostic-aggregator
Requires:       ros-kinetic-freenect-launch
Requires:       ros-kinetic-imu-filter-madgwick
Requires:       ros-kinetic-imu-transformer
Requires:       ros-kinetic-laser-filters
Requires:       ros-kinetic-microstrain-3dmgx2-imu
Requires:       ros-kinetic-nmea-comms
Requires:       ros-kinetic-nmea-navsat-driver
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-openni2-launch
Requires:       ros-kinetic-realsense-camera
Requires:       ros-kinetic-rgbd-launch
Requires:       ros-kinetic-robot-localization
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-robot-upstart
Requires:       ros-kinetic-roch-base
Requires:       ros-kinetic-roch-capabilities
Requires:       ros-kinetic-roch-control
Requires:       ros-kinetic-roch-description
Requires:       ros-kinetic-roch-safety-controller
Requires:       ros-kinetic-roch-sensorpc
Requires:       ros-kinetic-rocon-app-manager
Requires:       ros-kinetic-rocon-app-manager-msgs
Requires:       ros-kinetic-rocon-bubble-icons
Requires:       ros-kinetic-rocon-interaction-msgs
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rplidar-ros
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-tf2-ros
Requires:       ros-kinetic-zeroconf-avahi
Requires:       scipy
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roslaunch
BuildRequires:  ros-kinetic-rospy

%description
SawYer roch installation and integration package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Mar 24 2017 Carl <wzhang@softrobtech.com> - 2.0.13-0
- Autogenerated by Bloom

