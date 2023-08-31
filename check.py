from .Connection import ConnectionTcpMTProxyFakeTLS
from .lib.tcpmtproxy import ConnectionTcpMTProxyRandomizedIntermediate, ConnectionTcpMTProxyAbridged, ConnectionTcpMTProxyIntermediate
import logging

loggers = {'MTPCheck.lib.connection': logging.getLogger(__name__)}


async def fake_tls_handshake_check(server, port, secret, dc_id, timeout):
    proxy = (server, port, secret)
    conn = ConnectionTcpMTProxyFakeTLS(dc_id, loggers=loggers, proxy=proxy)
    await conn.connect(timeout)
    await conn.disconnect()


async def randomized_intermediate_check(server, port, secret, dc_id, timeout):
    proxy = (server, port, secret)
    conn = ConnectionTcpMTProxyRandomizedIntermediate(dc_id, loggers=loggers, proxy=proxy)
    await conn.connect(timeout)
    await conn.disconnect()


