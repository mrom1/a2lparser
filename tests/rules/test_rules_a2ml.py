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


def test_rules_a2ml_empty():
    """
    Tests parsing an empty A2ML section.
    """
    project_content = """
    ASAP2_VERSION 1 71
    /begin PROJECT Empty_A2ML_Project "ProjectIdentifier"

      /begin MODULE Example ""

      /begin A2ML
      /end A2ML

      /end MODULE
    /end PROJECT
    """
    ast = A2LYacc().generate_ast(project_content)
    assert ast

    project = ast["PROJECT"]
    assert project
    assert project["Name"] == "Empty_A2ML_Project"
    assert project["LongIdentifier"] == '"ProjectIdentifier"'

    module = project["MODULE"]
    assert module
    assert module["Name"] == "Example"
    assert module["LongIdentifier"] == '""'
    assert module["A2ML"] == ""


def test_rules_a2ml_only():
    """
    Function to test the rules for A2ML only, including parsing a2ml_block and asserting the AST.
    """
    a2ml_block = """
    /begin A2ML
      block "IF_DATA" taggedunion if_data {
          "XCP" struct {
              taggedstruct {
                  block "PROTOCOL_LAYER" struct {
                    uint;
                    uint;
                    uint;
                    };
              };
          };
      };
    /end A2ML
    """
    parser = A2LYacc()
    ast = parser.generate_ast(a2ml_block)
    assert ast
    a2ml_content = a2ml_block.split("/begin A2ML", 1)[1].rsplit("/end A2ML", 1)[0].strip()
    assert ast["A2ML"] == {"FormatSpecification": a2ml_content}


def test_rules_a2ml_full_content():
    """
    Function to test the rules for parsing a more complete MODULE example including a A2ML section.
    """
    a2ml_full_content = """
    ASAP2_VERSION 1 71
    /begin PROJECT ASAP2_Example ""

      /begin HEADER "ASAP2 Example File"
        VERSION "V1.7.1"
        PROJECT_NO P2016_09_AE_MCD_2MC_BS_V1_7_1_main
      /end HEADER

      /begin MODULE Example ""

        /begin A2ML

          block "IF_DATA" taggedunion if_data {


    /*  ======================================================================================  */
    /*                                                                                          */
    /*  ASAM XCP AML                                                                            */
    /*                                                                                          */
    /*  ======================================================================================  */

            "XCP" struct {
              taggedstruct {
                block "PROTOCOL_LAYER" struct {
                  uint;
                  uint;
                  uint;
                  uint;
                  uint;
                  uint;
                  uint;
                  uint;
                  uchar;
                  uint;
                  enum {
                    "BYTE_ORDER_MSB_LAST" = 0,
                    "BYTE_ORDER_MSB_FIRST" = 1
                  };
                  enum {
                    "ADDRESS_GRANULARITY_BYTE" = 1,
                    "ADDRESS_GRANULARITY_WORD" = 2,
                    "ADDRESS_GRANULARITY_DWORD" = 4
                  };
                  taggedstruct {
                    ("OPTIONAL_CMD" enum {
                      "GET_COMM_MODE_INFO" = 251,
                      "GET_ID" = 250,
                      "SET_REQUEST" = 249,
                      "GET_SEED" = 248,
                      "UNLOCK" = 247,
                      "SET_MTA" = 246,
                      "UPLOAD" = 245,
                      "SHORT_UPLOAD" = 244,
                      "BUILD_CHECKSUM" = 243,
                      "TRANSPORT_LAYER_CMD" = 242,
                      "USER_CMD" = 241,
                      "DOWNLOAD" = 240,
                      "DOWNLOAD_NEXT" = 239,
                      "DOWNLOAD_MAX" = 238,
                      "SHORT_DOWNLOAD" = 237,
                      "MODIFY_BITS" = 236,
                      "SET_CAL_PAGE" = 235,
                      "GET_CAL_PAGE" = 234,
                      "GET_PAG_PROCESSOR_INFO" = 233,
                      "GET_SEGMENT_INFO" = 232,
                      "GET_PAGE_INFO" = 231,
                    })*;
                    "COMMUNICATION_MODE_SUPPORTED" taggedunion {
                      "BLOCK" taggedstruct {
                        "SLAVE" ;
                        "MASTER" struct {
                          uchar;
                          uchar;
                        };
                      };
                      "INTERLEAVED" uchar;
                    };
                    "SEED_AND_KEY_EXTERNAL_FUNCTION" char[256];
                  };
                };
    /end A2ML

    /begin MOD_COMMON ""
      DEPOSIT ABSOLUTE
      BYTE_ORDER MSB_LAST
      ALIGNMENT_BYTE 1
      ALIGNMENT_WORD 2
      ALIGNMENT_LONG 4
      ALIGNMENT_FLOAT32_IEEE 4
      ALIGNMENT_FLOAT64_IEEE 4
    /end MOD_COMMON

    /end MODULE
    /end PROJECT
    """
    parser = A2LYacc()
    ast = parser.generate_ast(a2ml_full_content)
    assert ast
    asap2_version = ast["ASAP2_VERSION"]
    project = ast["PROJECT"]
    header = project["HEADER"]
    module = project["MODULE"]
    a2ml_content = a2ml_full_content.split("/begin A2ML", 1)[1].rsplit("/end A2ML", 1)[0].strip()

    assert asap2_version == {"VersionNo": "1", "UpgradeNo": "71"}
    assert project["Name"] == "ASAP2_Example"
    assert project["LongIdentifier"] == '""'
    assert header == {
        "Comment": '"ASAP2 Example File"',
        "PROJECT_NO": "P2016_09_AE_MCD_2MC_BS_V1_7_1_main",
        "VERSION": '"V1.7.1"',
    }
    assert module["A2ML"] == a2ml_content
    assert module["MOD_COMMON"] == {
        "Comment": '""',
        "ALIGNMENT_BYTE": "1",
        "ALIGNMENT_FLOAT32_IEEE": "4",
        "ALIGNMENT_FLOAT64_IEEE": "4",
        "ALIGNMENT_LONG": "4",
        "ALIGNMENT_WORD": "2",
        "BYTE_ORDER": "MSB_LAST",
        "DEPOSIT": "ABSOLUTE",
    }
