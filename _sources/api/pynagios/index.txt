:mod:`pynagios` -- Python Library for Writing Nagios Plugins
============================================================

.. automodule:: pynagios
   :synopsis: Python library for writing Nagios plugins.

   .. autodata:: version
   .. data:: PerfData

     Alias for :class:`pynagios.perf_data.PerfData`

   .. data:: Plugin

     Alias for :class:`pynagios.plugin.Plugin`

   .. data:: Range

     Alias for :class:`pynagios.range.Range`

   .. data:: Response

     Alias for :class:`pynagios.response.Response`

   .. data:: Status

     Alias for :class:`pynagios.status.Status`

   .. data:: OK

     A :class:`~pynagios.status.Status` object representing the OK
     response status.

   .. data:: WARNING

     A :class:`~pynagios.status.Status` object representing the WARNING
     response status.

   .. data:: CRITICAL

     A :class:`~pynagios.status.Status` object representing the CRITICAL
     response status.

   .. data:: UNKNOWN

     A :class:`~pynagios.status.Status` object representing the UNKNOWN
     response status.

Sub-modules:

.. toctree::
   :maxdepth: 2

   perf_data
   plugin
   response
   range
   status
