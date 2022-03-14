# -*- coding: utf-8 -*-
"""
Constants
"""


from struct import pack
from typing import Tuple


DOUBLE = Tuple[float, float]
TRIPLE = Tuple[float, float, float]
QUADRUPLE = Tuple[float, float, float, float]

WGS84 = 4326
SRS_ID = 'srs_id'

GP_MAGIC = b'GP'
EMPTY = b''
BYTE_UINT = '<BI'
COUNT_UNIT = '<I'

WKB_POINT_PRE = pack(BYTE_UINT, 1, 1)
WKB_POINT_Z_PRE = pack(BYTE_UINT, 1, 1001)
WKB_POINT_M_PRE = pack(BYTE_UINT, 1, 2001)
WKB_POINT_ZM_PRE = pack(BYTE_UINT, 1, 3001)

WKB_LINESTRING_PRE = pack(BYTE_UINT, 1, 2)
WKB_LINESTRING_Z_PRE = pack(BYTE_UINT, 1, 1002)
WKB_LINESTRING_M_PRE = pack(BYTE_UINT, 1, 2002)
WKB_LINESTRING_ZM_PRE = pack(BYTE_UINT, 1, 3002)

WKB_POLYGON_PRE = pack(BYTE_UINT, 1, 3)
WKB_POLYGON_Z_PRE = pack(BYTE_UINT, 1, 1003)

WKB_MULTI_POINT_PRE = pack(BYTE_UINT, 1, 4)
WKB_MULTI_POINT_Z_PRE = pack(BYTE_UINT, 1, 1004)
WKB_MULTI_POINT_M_PRE = pack(BYTE_UINT, 1, 2004)
WKB_MULTI_POINT_ZM_PRE = pack(BYTE_UINT, 1, 3004)

WKB_MULTI_LINESTRING_PRE = pack(BYTE_UINT, 1, 5)
WKB_MULTI_LINESTRING_Z_PRE = pack(BYTE_UINT, 1, 1005)
WKB_MULTI_LINESTRING_M_PRE = pack(BYTE_UINT, 1, 2005)
WKB_MULTI_LINESTRING_ZM_PRE = pack(BYTE_UINT, 1, 3005)

WKB_MULTI_POLYGON_PRE = pack(BYTE_UINT, 1, 6)
WKB_MULTI_POLYGON_Z_PRE = pack(BYTE_UINT, 1, 1006)


if __name__ == '__main__':
    pass
