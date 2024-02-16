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


from a2lparser.a2l.a2l_yacc import A2LYacc


def test_rules_blob_minimal():
    """
    Test A2L section BLOB.
    """
    blob_minimal = """
    /begin BLOB
        Data_Blob // blob name
        "binary blob for xyz" // description
        0x4477112 // start address
        1024 // number of bytes in blob
    /end BLOB
    """
    ast = A2LYacc().generate_ast(blob_minimal)

    assert ast
    blob = ast["BLOB"]

    assert blob["Name"] == "Data_Blob"
    assert blob["LongIdentifier"] == '"binary blob for xyz"'
    assert blob["Address"] == "0x4477112"
    assert blob["Size"] == "1024"
