:mod:`plugin` -- Plugin Class
============================================

.. automodule:: pynagios.plugin

   .. autoclass:: pynagios.plugin.Plugin()

      .. attribute:: options

         Dictionary of parsed command line options and their values. As an
         example, to get the ``hostname`` passed in via the command line:::

             options.hostname

      .. automethod:: check
      .. automethod:: response_for_value
