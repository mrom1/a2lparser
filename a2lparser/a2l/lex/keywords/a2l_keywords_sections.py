#######################################################################################
# a2lparser: https://github.com/mrom1/a2lparser                                       #
# author: https://github.com/mrom1                                                    #
#                                                                                     #
# This file is part of the a2lparser package.                                         #
#                                                                                     #
# a2lparser is free software: you can redistribute it and/or modify it                #
# under the terms of the GNU General Public License as published by the               #
# Free Software Foundation, either version 3 of the License, or (at your option)      #
# any later version.                                                                  #
#                                                                                     #
# a2lparser is distributed in the hope that it will be useful,                        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY      #
# or FITNESS FOR A PARTICULAR PURPOSE.                                                #
# See the GNU General Public License for more details.                                #
#                                                                                     #
# You should have received a copy of the GNU General Public License                   #
# along with a2lparser. If not, see <https://www.gnu.org/licenses/>.                  #
#######################################################################################


class A2LKeywordsSections:
    """
    Keywords for parsing A2L sections.
    All section keywords are enclosed by an
    interpreted "/begin" and an "/end" token.

    Example Section:
        /begin VAR_ADDRESS
          0x8840
          0x8858
          0x8870
          0x8888
        /end VAR_ADDRESS
    """

    keywords: list = [
        # A2ML format keyword
        "A2ML",
        # Annotation
        "ANNOTATION",
        "ANNOTATION_TEXT",
        # Axis description and points
        "AXIS_DESCR",
        "AXIS_PTS",
        # Calibartion
        "CALIBRATION_HANDLE",
        "CALIBRATION_METHOD",
        # Characteristic section
        "CHARACTERISTIC",
        # Computation
        "COMPU_METHOD",
        "COMPU_TAB",
        "COMPU_VTAB",
        "COMPU_VTAB_RANGE",
        # Dependent characteristic
        "DEPENDENT_CHARACTERISTIC",
        # Fix axis par
        "FIX_AXIS_PAR_LIST",
        # Formula
        "FORMULA",
        # Frame
        "FRAME",
        # Function
        "FUNCTION",
        "FUNCTION_LIST",
        # Group
        "GROUP",
        # Header
        "HEADER",
        # Interface data
        "IF_DATA",
        # Measurement
        "IN_MEASUREMENT",
        "LOC_MEASUREMENT",
        "MEASUREMENT",
        # MAP_LIST
        "MAP_LIST",
        # MEMORY_LAYOUT
        "MEMORY_LAYOUT",
        # MEMORY_SEGMENT
        "MEMORY_SEGMENT",
        # MOD_COMMON
        "MOD_COMMON",
        # MOD_PAR
        "MOD_PAR",
        # MODULE
        "MODULE",
        # OUT_MEASUREMENT
        "OUT_MEASUREMENT",
        # PROJECT
        "PROJECT",
        # RECORD_LAYOUT
        "RECORD_LAYOUT",
        # REF_CHARACTERISTIC
        "REF_CHARACTERISTIC",
        "REF_GROUP",
        "REF_MEASUREMENT",
        # SUB_FUNCTION
        "SUB_FUNCTION",
        # SUB_GROUP
        "SUB_GROUP",
        # UNIT
        "UNIT",
        # USER_RIGHTS
        "USER_RIGHTS",
        # Variant sections
        "VAR_ADDRESS",
        "VAR_CHARACTERISTIC",
        "VAR_CRITERION",
        "VAR_FORBIDDEN_COMB",
        "VARIANT_CODING",
        # Virtual
        "VIRTUAL",
        "VIRTUAL_CHARACTERISTIC",
    ]
