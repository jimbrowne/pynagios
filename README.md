# PyNagios

PyNagios is a simple Python library meant to make writing
[Nagios](http://www.nagios.org/) plugins much easier. Nagios
plugins have [quite a few guidelines](http://nagiosplug.sourceforge.net/developer-guidelines.html)
to adhere to, and PyNagios provides helpers to make this
easy.

## Install

To install, simply use `pip` or `easy_install`:

    pip install pynagios

## Features

The core features supported by PyNagios:

  * Parsing command line arguments such that the standard expected
    arguments (such as `-H`, `-w`, `-c`) are accepted.
  * Returning proper POSIX exit code based on status.
  * Parsing Nagios range formats (such as "@10:20", "~:50", "10", etc.)
  * Outputting status and message.
  * Outputting performance data.

## Example

What all these nice features result in is a concise, simple, and
guidelines-compliant Python-based Nagios plugin:

```python
from pynagios import Plugin

if __name__ == 'main':
    # Pretend you got this from some outside source.
    users = 27

    # Create an instance of the plugin and parse the command line
    # arguments.
    plugin = Plugin()
    plugin.parse_command_line()

    # Add some performance data.
    plugin.add_perf_data("users", users)
    plugin.add_perf_data("memory", 814, "MB")

    # This will get the status for the value given the ranges
    # for warning and critical given by command line arguments
    status = plugin.status_for_value(users)

    # Exit with the status and message.
    plugin.exit(status, "system has %d users logged in" % users)
```
