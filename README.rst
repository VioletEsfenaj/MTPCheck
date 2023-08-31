MTProxy Checker
========================
.. epigraph::
A python module to check Telegram MTProto proxies connection (Fake-Tls, Randomized, Intermidiate)


Usage:
----------

Fake TLS Check (ee)
-----------------
| Check MTProto Fake-TLS (ee) proxies by compeleting Fake-TLS handshake

| You can use a base64 secret or hex one,
| But remember to
| Remove "ee" from the starting of hex secret
| And
| Remove "7" from the starting of the base64 secret.

.. code-block:: python

    Example:
    ee9b43b87555bf9464e02bdcd2db8932b07777772e736974652e636f6d -> 9b43b87555bf9464e02bdcd2db8932b07777772e736974652e636f6d
    7gEBAQEBAQEBAQEBAQEBAQFsaWIuYXJ2YW5jbG91ZC5jb20= -> gEBAQEBAQEBAQEBAQEBAQFsaWIuYXJ2YW5jbG91ZC5jb20=


.. code-block:: python

  from MTPCheck import fake_tls_handshake_check
  await fake_tls_handshake_check(server, port, secret, dc_id, timeout)


Random padding/Intermediate Check
-----------------
| to check other versions of MTProto proxies (dd)
| Secret should be in hex format

.. code-block:: python

    from MTPCheck import randomized_intermediate_check
    await randomized_intermediate_check(server, port, secret, dc_id, timeout)





