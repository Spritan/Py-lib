## User manual

https://pyudev.readthedocs.io/en/latest/guide.html#getting-started

## Notes

### Getting started

- Import pyudev and verify that you’re using the latest version:

```python
>>> import pyudev
>>> pyudev.__version__
u'0.16'
>>> pyudev.udev_version()
181
```

### Emulating devices

- A common use case is to enumerate available devices, or a subset thereof. But before you can do anything with pyudev, you need to establish a “connection” to the udev device database first. This connection is represented by a library [`Context`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Context):

> **udev** is a device manager for the Linux kernel. As the successor of devfsd and hotplug, **udev** primarily manages device nodes in the /dev directory. At the same time, **udev** also handles all user space events raised while hardware devices are added into the system or removed from it, including firmware loading as required by certain devices.

```python
context = pyudev.Context()
```

- The [`Context`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Context) is the central object of **pyudev** and [libudev](http://www.kernel.org/pub/linux/utils/kernel/hotplug/libudev/). You will need a [`Context`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Context) object for almost anything in **pyudev**. With the `context` you can now enumerate the available devices:

```
>>> for device in context.list_devices(): 
...     device
...
Device(u'/sys/devices/LNXSYSTM:00')
Device(u'/sys/devices/LNXSYSTM:00/LNXCPU:00')
Device(u'/sys/devices/LNXSYSTM:00/LNXCPU:01')
...
```

- By default, `list_devices()` yields all devices available on the system as [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) objects, but you can filter the list of devices with keyword arguments to enumerate all available partitions for example:

```
>>> for device in context.list_devices(subsystem='block', DEVTYPE='partition'):
...    print(device)
...
Device(u'/sys/devices/pci0000:00/0000:00:0d.0/host2/target2:0:0/2:0:0:0/block/sda/sda1')
Device(u'/sys/devices/pci0000:00/0000:00:0d.0/host2/target2:0:0/2:0:0:0/block/sda/sda2')
Device(u'/sys/devices/pci0000:00/0000:00:0d.0/host2/target2:0:0/2:0:0:0/block/sda/sda3')
```

> The choice of the right filters depends on the use case and generally requires some knowledge about how udev classifies and categories devices. This is out of the scope of this guide.
>
>  **Poke around in `/sys/` to get a feeling for the udev-way of device handling, read the udev documentation or one of the tutorials in the net.**

- The keyword arguments of `list_devices()` provide the most common filter operations. You can apply other, less common filters by calling one of the `match_*` methods on the [`Enumerator`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Enumerator) returned by of `list_devices()`.

## [Accessing individual devices directly](https://pyudev.readthedocs.io/en/latest/guide.html#id5)

If you just need a single specific [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device), you don’t need to enumerate all devices with a specific filter criterion. Instead, you can directly create [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) objects from a device path ([`Devices.from_path()`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Devices.from_path)), by from a subsystem and device name ([`Devices.from_name()`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Devices.from_name)) or from a device file ([`Devices.from_device_file()`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Devices.from_device_file)). The following code gets the [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) object for the first hard disc in three different ways:

```
>>> pyudev.Devices.from_path(context, '/sys/block/sda')
Device(u'/sys/devices/pci0000:00/0000:00:0d.0/host2/target2:0:0/2:0:0:0/block/sda')
>>> pyudev.Devices.from_name(context, 'block', 'sda')
Device(u'/sys/devices/pci0000:00/0000:00:0d.0/host2/target2:0:0/2:0:0:0/block/sda')
>>> pyudev.Devices.from_device_file(context, '/dev/sda')
Device(u'/sys/devices/pci0000:00/0000:00:0d.0/host2/target2:0:0/2:0:0:0/block/sda')
```

- As you can see, you need to pass a [`Context`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Context) to both methods as reference to the udev database from which to retrieve information about the device.

#### Note:

> The [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) objects created in the above example refer to the same device. Consequently, they are considered equal:

```
>>> pyudev.Devices.from_path(context, '/sys/block/sda') == pyudev.Devices.from_name(context, 'block', 'sda')
True
```

> Whereas [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) objects referring to different devices are unequal:

```
>>> pyudev.Devices.from_name(context, 'block', 'sda') == pyudev.Devices.from_name(context, 'block', 'sda1')
False
```

## [Querying device information](https://pyudev.readthedocs.io/en/latest/guide.html#id6)

As you’ve seen, [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) represents a device in the udev database. Each such device has a set of “device properties” (not to be confused with Python properties as created by `property()`!) that describe the capabilities and features of this device as well as its relationship to other devices.

Common device properties are also available as properties of a [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) object. For instance, you can directly query the `device_node` and the `device_type` of block devices:

```
>>> for device in context.list_devices(subsystem='block'):
...     print('{0} ({1})'.format(device.device_node, device.device_type))
...
/dev/sr0 (disk)
/dev/sda (disk)
/dev/sda1 (partition)
/dev/sda2 (partition)
/dev/sda3 (partition)
```

For all other properties, [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) provides a dictionary-like interface to directly access the device properties. You’ll get the same information as with the generic properties:

```
>>> for device in context.list_devices(subsystem='block'):
...    print('{0} ({1})'.format(device['DEVNAME'], device['DEVTYPE']))
...
/dev/sr0 (disk)
/dev/sda (disk)
/dev/sda1 (partition)
/dev/sda2 (partition)
/dev/sda3 (partition)
```

Warning

 

When filtering devices, you have to use the device property names. The names of corresponding properties of [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) will generally **not** work. Compare the following two statements:

```
>>> [device.device_node for device in context.list_devices(subsystem='block', DEVTYPE='partition')]
[u'/dev/sda1', u'/dev/sda2', u'/dev/sda3']
>>> [device.device_node for device in context.list_devices(subsystem='block', device_type='partition')]
[]
```

But you can also query many device properties that are not available as Python properties on the [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) object with a convenient mapping interface, like the filesystem type. [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) provides a convenient mapping interface for this purpose:

```
>>> for device in context.list_devices(subsystem='block', DEVTYPE='partition'):
...     print('{0} ({1})'.format(device.device_node, device.get('ID_FS_TYPE')))
...
/dev/sda1 (ext3)
/dev/sda2 (swap)
/dev/sda3 (ext4)
```

Note

 

Such device specific properties may not be available on devices. Either use `get()` to specify default values for missing properties, or be prepared to catch [`KeyError`](http://docs.python.org/library/exceptions.html#exceptions.KeyError).

Most device properties are computed by udev rules from the driver- and device-specific “device attributes”. The [`Device.attributes`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device.attributes) mapping gives you access to these attributes, but generally you should not need these. Use the device properties whenever possible.

## [Examing the device hierarchy](https://pyudev.readthedocs.io/en/latest/guide.html#id7)

A [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) is part of a device hierarchy, and can have a [`parent`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device.parent) device that more or less resembles the physical relationship between devices. For instance, the [`parent`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device.parent) of partition devices is a [`Device`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device) object that represents the disc the partition is located on:

```
>>> for device in context.list_devices(subsystem='block', DEVTYPE='partition'):
...    print('{0} is located on {1}'.format(device.device_node, device.parent.device_node))
...
/dev/sda1 is located on /dev/sda
/dev/sda2 is located on /dev/sda
/dev/sda3 is located on /dev/sda
```

Generally, you should not rely on the direct parent-child relationship between two devices. Instead of accessing the parent directly, search for a parent within a specific subsystem, e.g. for the parent `block` device, with [`find_parent()`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Device.find_parent):

```
>>> for device in context.list_devices(subsystem='block', DEVTYPE='partition'):
...    print('{0} is located on {1}'.format(device.device_node, device.find_parent('block').device_node))
...
/dev/sda1 is located on /dev/sda
/dev/sda2 is located on /dev/sda
/dev/sda3 is located on /dev/sda
```

This also save you the tedious work of traversing the device tree manually, if you are interested in grand parents, like the name of the PCI slot of the SCSI or IDE controller of the disc that contains a partition:

```
>>> for device in context.list_devices(subsystem='block', DEVTYPE='partition'):
...    print('{0} attached to PCI slot {1}'.format(device.device_node, device.find_parent('pci')['PCI_SLOT_NAME']))
...
/dev/sda1 attached to PCI slot 0000:00:0d.0
/dev/sda2 attached to PCI slot 0000:00:0d.0
/dev/sda3 attached to PCI slot 0000:00:0d.0
```

## [Monitoring devices](https://pyudev.readthedocs.io/en/latest/guide.html#id8)

### [Synchronous monitoring](https://pyudev.readthedocs.io/en/latest/guide.html#id9)

The Linux kernel emits events whenever devices are added, removed (e.g. a USB stick was plugged or unplugged) or have their attributes changed (e.g. the charge level of the battery changed). With [`pyudev.Monitor`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Monitor) you can react on such events, for example to react on added or removed mountable filesystems:

```
>>> monitor = pyudev.Monitor.from_netlink(context)
>>> monitor.filter_by('block')
>>> for device in iter(monitor.poll, None):
...     if 'ID_FS_TYPE' in device:
...         print('{0} partition {1}'.format(device.action, device.get('ID_FS_LABEL')))
...
add partition MULTIBOOT
remove partition MULTIBOOT
```

After construction of a monitor, you can install an event filter on the monitor using [`filter_by()`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Monitor.filter_by). In the above example only events from the `block` subsystem are handled.

Note

 

Always prefer [`filter_by()`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Monitor.filter_by) and [`filter_by_tag()`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Monitor.filter_by_tag) over manually filtering devices (e.g. by `device.subsystem == 'block'` or `tag in device.tags`). These methods install the filter on the *kernel side*. A process waiting for events is thus only woken up for events that match these filters. This is much nicer in terms of power consumption and system load than executing filters in the process itself.

Eventually, you can receive events from the monitor. As you can see, a [`Monitor`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Monitor) is iterable and synchronously yields occurred events. If you iterate over a [`Monitor`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.Monitor), you will synchronously receive events in an endless loop, until you raise an exception, or `break` the loop.

This is the quick and dirty way of monitoring, suitable for small scripts or quick experiments. In most cases however, simply iterating over the monitor is not sufficient, because it blocks the main thread, and can only be stopped if an event occurs (otherwise the loop is not entered and you have no chance to `break` it).

### [Asynchronous monitoring](https://pyudev.readthedocs.io/en/latest/guide.html#id10)

For such use cases, pyudev provides asynchronous monitoring with [`MonitorObserver`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.MonitorObserver). You can use it to log added and removed mountable filesystems to a file, for example:

```
>>> monitor = pyudev.Monitor.from_netlink(context)
>>> monitor.filter_by('block')
>>> def log_event(action, device):
...    if 'ID_FS_TYPE' in device:
...        with open('filesystems.log', 'a+') as stream:
...            print('{0} - {1}'.format(action, device.get('ID_FS_LABEL')), file=stream)
...
>>> observer = pyudev.MonitorObserver(monitor, log_event)
>>> observer.start()
```

The `observer` gets an event handler (`log_event()` in this case) which is asynchronously invoked on every event emitted by the underlying `monitor` after the observer has been started using [`start()`](http://docs.python.org/library/threading.html#threading.Thread.start).

Warning

 

The callback is invoked from a *different* thread than the one in which the `observer` was created. Be sure to protect access to shared resource properly when you access them from the callback (e.g. by locking).

The `observer` can be stopped at any moment using `stop()`()`:

```
>>> observer.stop()
```

Warning

 

Do *not* call [`stop()`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.MonitorObserver.stop) from the event handler, neither directly nor indirectly. Use [`send_stop()`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.MonitorObserver.send_stop) if you need to stop monitoring from inside the event handler.

### [GUI toolkit integration](https://pyudev.readthedocs.io/en/latest/guide.html#id11)

If you’re using a GUI toolkit, you already have the event system of the GUI toolkit at hand. pyudev provides observer classes that seamlessly integration in the event system of the GUI toolkit and relieve you from caring with synchronisation issues that would occur with thread-based monitoring as implemented by [`MonitorObserver`](https://pyudev.readthedocs.io/en/latest/api/pyudev.html#pyudev.MonitorObserver).

pyudev supports all major GUI toolkits available for Python:

- [Qt](http://qt.io/developers/) 5 using `pyudev.pyqt5`
- [Qt](http://qt.io/developers/) 4 using `pyudev.pyqt4` for the [PyQt4](https://riverbankcomputing.co.uk/software/pyqt/intro) binding or `pyudev.pyside` for the [PySide](http://wiki.qt.io/PySide) binding
- [PyGtk](http://www.pygtk.org/) 2 using [`pyudev.glib`](https://pyudev.readthedocs.io/en/latest/api/pyudev.glib.html#module-pyudev.glib)
- [wxWidgets](http://wxwidgets.org/) and [wxPython](http://www.wxpython.org/) using [`pyudev.wx`](https://pyudev.readthedocs.io/en/latest/api/pyudev.wx.html#module-pyudev.wx)

Each of these modules provides an observer class that observers the monitor asynchronously and emits proper signals upon device events.

For instance, the above example would look like this in a [PySide](http://wiki.qt.io/PySide) application:

```
>>> from pyudev.pyside import QUDevMonitorObserver
>>> monitor = pyudev.Monitor.from_netlink(context)
>>> observer = QUDevMonitorObserver(monitor)
>>> observer.deviceEvent.connect(log_event)
>>> monitor.start()
```

### [Device objects as booleans](https://pyudev.readthedocs.io/en/latest/guide.html#id12)

The use of a Device object in a boolean context as a shorthand for a comparison with None is an error.

The Device class inherits from the abstract Mapping class, as it maps udev property names to their values. Consequently, if a Device object has no udev properties, an unusual but not impossible occurance, the object is interpreted as False in a boolean context.