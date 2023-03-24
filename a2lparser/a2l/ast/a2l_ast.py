# pylint: disable-all
#-----------------------------------------------------------------
# *** IMPORTENT ***
# This code was generated from the config file:
# /home/mrom/development/a2lparser/a2lparser/configs/A2L_ASAM.cfg
#
# If you wish to edit this code use the generator in the subfolder gen
# and adjust the config file, not the code itself!
# Don't edit this file manually!
# *** IMPORTENT ***
#
#
# Abstract Syntax Tree (AST) Node Classes.
#
#-----------------------------------------------------------------


import sys


class Node(object):
    __slots__ = ()

    def children(self):
        pass


class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for ast_class_name, ast_class in node.children():
            self.visit(ast_class)


class Abstract_Syntax_Tree (Node):
    __slots__ = ('node', '__weakref__')
    def __init__(self, node):
        self.node = node

    def children(self):
        nodelist = []
        for i, child in enumerate(self.node or []):
            nodelist.append(("node[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()


class A2ml_Version(Node):
    __slots__ = ('VersionNo', 'UpgradeNo', '__weakref__')
    def __init__(self, VersionNo, UpgradeNo):
        self.VersionNo = VersionNo
        self.UpgradeNo = UpgradeNo

    def children(self):
        nodelist = []
        if self.VersionNo is not None: nodelist.append(("VersionNo", self.VersionNo))
        if self.UpgradeNo is not None: nodelist.append(("UpgradeNo", self.UpgradeNo))
        return tuple(nodelist)

    attr_names = ()


class Addr_Epk(Node):
    __slots__ = ('Address', '__weakref__')
    def __init__(self, Address):
        self.Address = Address

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Address', )


class Alignment_Byte(Node):
    __slots__ = ('AlignmentBorder', '__weakref__')
    def __init__(self, AlignmentBorder):
        self.AlignmentBorder = AlignmentBorder

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('AlignmentBorder', )


class Alignment_Float32_Ieee(Node):
    __slots__ = ('AlignmentBorder', '__weakref__')
    def __init__(self, AlignmentBorder):
        self.AlignmentBorder = AlignmentBorder

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('AlignmentBorder', )


class Alignment_Float64_Ieee(Node):
    __slots__ = ('AlignmentBorder', '__weakref__')
    def __init__(self, AlignmentBorder):
        self.AlignmentBorder = AlignmentBorder

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('AlignmentBorder', )


class Alignment_Int64(Node):
    __slots__ = ('AlignmentBorder', '__weakref__')
    def __init__(self, AlignmentBorder):
        self.AlignmentBorder = AlignmentBorder

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('AlignmentBorder', )


class Alignment_Long(Node):
    __slots__ = ('AlignmentBorder', '__weakref__')
    def __init__(self, AlignmentBorder):
        self.AlignmentBorder = AlignmentBorder

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('AlignmentBorder', )


class Alignment_Word(Node):
    __slots__ = ('AlignmentBorder', '__weakref__')
    def __init__(self, AlignmentBorder):
        self.AlignmentBorder = AlignmentBorder

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('AlignmentBorder', )


class Annotation(Node):
    __slots__ = ('OptionalParams', '__weakref__')
    def __init__(self, OptionalParams = None):
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ()


class Annotation_Opt(Node):
    __slots__ = ('Annotation_Label', 'Annotation_Origin', 'Annotation_Text', '__weakref__')
    def __init__(self, Annotation_Label = None, Annotation_Origin = None, Annotation_Text = None):
        self.Annotation_Label = Annotation_Label
        self.Annotation_Origin = Annotation_Origin
        self.Annotation_Text = Annotation_Text

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Annotation_Label', 'Annotation_Origin', 'Annotation_Text', )


class Annotation_Label(Node):
    __slots__ = ('label', '__weakref__')
    def __init__(self, label):
        self.label = label

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('label', )


class Annotation_Origin(Node):
    __slots__ = ('origin', '__weakref__')
    def __init__(self, origin):
        self.origin = origin

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('origin', )


class Annotation_Text(Node):
    __slots__ = ('annotation_text', '__weakref__')
    def __init__(self, annotation_text):
        self.annotation_text = annotation_text

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('annotation_text', )


class Array_Size(Node):
    __slots__ = ('Number', '__weakref__')
    def __init__(self, Number):
        self.Number = Number

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Number', )


class Asap2_Version(Node):
    __slots__ = ('VersionNo', 'UpgradeNo', '__weakref__')
    def __init__(self, VersionNo, UpgradeNo):
        self.VersionNo = VersionNo
        self.UpgradeNo = UpgradeNo

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('VersionNo', 'UpgradeNo', )


class Axis_Descr(Node):
    __slots__ = ('Attribute', 'InputQuantity', 'Conversion', 'MaxAxisPoints', 'LowerLimit', 'UpperLimit', 'OptionalParams', '__weakref__')
    def __init__(self, Attribute, InputQuantity, Conversion, MaxAxisPoints, LowerLimit, UpperLimit, OptionalParams = None):
        self.Attribute = Attribute
        self.InputQuantity = InputQuantity
        self.Conversion = Conversion
        self.MaxAxisPoints = MaxAxisPoints
        self.LowerLimit = LowerLimit
        self.UpperLimit = UpperLimit
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Attribute', 'InputQuantity', 'Conversion', 'MaxAxisPoints', 'LowerLimit', 'UpperLimit', )


class Axis_Descr_Opt (Node):
    __slots__ = ('Annotation', 'Axis_Pts_Ref', 'Byte_Order', 'Curve_Axis_Ref', 'Deposit', 'Extended_Limits', 'Fix_Axis_Par', 'Fix_Axis_Par_Dist', 'Fix_Axis_Par_List', 'Format', 'Max_Grad', 'Monotony', 'Phys_Unit', 'Read_Only', 'Step_Size', '__weakref__')
    def __init__(self, Annotation = None, Axis_Pts_Ref = None, Byte_Order = None, Curve_Axis_Ref = None, Deposit = None, Extended_Limits = None, Fix_Axis_Par = None, Fix_Axis_Par_Dist = None, Fix_Axis_Par_List = None, Format = None, Max_Grad = None, Monotony = None, Phys_Unit = None, Read_Only = None, Step_Size = None):
        self.Annotation = Annotation
        self.Axis_Pts_Ref = Axis_Pts_Ref
        self.Byte_Order = Byte_Order
        self.Curve_Axis_Ref = Curve_Axis_Ref
        self.Deposit = Deposit
        self.Extended_Limits = Extended_Limits
        self.Fix_Axis_Par = Fix_Axis_Par
        self.Fix_Axis_Par_Dist = Fix_Axis_Par_Dist
        self.Fix_Axis_Par_List = Fix_Axis_Par_List
        self.Format = Format
        self.Max_Grad = Max_Grad
        self.Monotony = Monotony
        self.Phys_Unit = Phys_Unit
        self.Read_Only = Read_Only
        self.Step_Size = Step_Size

    def children(self):
        nodelist = []
        if self.Extended_Limits is not None: nodelist.append(("Extended_Limits", self.Extended_Limits))
        if self.Fix_Axis_Par is not None: nodelist.append(("Fix_Axis_Par", self.Fix_Axis_Par))
        if self.Fix_Axis_Par_Dist is not None: nodelist.append(("Fix_Axis_Par_Dist", self.Fix_Axis_Par_Dist))
        if self.Fix_Axis_Par_List is not None: nodelist.append(("Fix_Axis_Par_List", self.Fix_Axis_Par_List))
        for i, child in enumerate(self.Annotation or []):
            nodelist.append(("Annotation[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Axis_Pts_Ref', 'Byte_Order', 'Curve_Axis_Ref', 'Deposit', 'Format', 'Max_Grad', 'Monotony', 'Phys_Unit', 'Read_Only', 'Step_Size', )


class Axis_Pts(Node):
    __slots__ = ('Name', 'LongIdentifier', 'Address', 'InputQuantity', 'Deposit_Ref', 'MaxDiff', 'Conversion', 'MaxAxisPoints', 'LowerLimit', 'UpperLimit', 'OptionalParams', '__weakref__')
    def __init__(self, Name, LongIdentifier, Address, InputQuantity, Deposit_Ref, MaxDiff, Conversion, MaxAxisPoints, LowerLimit, UpperLimit, OptionalParams = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.Address = Address
        self.InputQuantity = InputQuantity
        self.Deposit_Ref = Deposit_Ref
        self.MaxDiff = MaxDiff
        self.Conversion = Conversion
        self.MaxAxisPoints = MaxAxisPoints
        self.LowerLimit = LowerLimit
        self.UpperLimit = UpperLimit
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', 'Address', 'InputQuantity', 'Deposit_Ref', 'MaxDiff', 'Conversion', 'MaxAxisPoints', 'LowerLimit', 'UpperLimit', )


class Axis_Pts_Opt (Node):
    __slots__ = ('Annotation', 'Byte_Order', 'Calibration_Access', 'Display_Identifier', 'Deposit', 'Ecu_Address_Extension', 'Extended_Limits', 'Format', 'Function_List', 'Guard_Rails', 'If_Data', 'Monotony', 'Phys_Unit', 'Read_Only', 'Ref_Memory_Segment', 'Step_Size', 'Symbol_Link', '__weakref__')
    def __init__(self, Annotation = None, Byte_Order = None, Calibration_Access = None, Display_Identifier = None, Deposit = None, Ecu_Address_Extension = None, Extended_Limits = None, Format = None, Function_List = None, Guard_Rails = None, If_Data = None, Monotony = None, Phys_Unit = None, Read_Only = None, Ref_Memory_Segment = None, Step_Size = None, Symbol_Link = None):
        self.Annotation = Annotation
        self.Byte_Order = Byte_Order
        self.Calibration_Access = Calibration_Access
        self.Display_Identifier = Display_Identifier
        self.Deposit = Deposit
        self.Ecu_Address_Extension = Ecu_Address_Extension
        self.Extended_Limits = Extended_Limits
        self.Format = Format
        self.Function_List = Function_List
        self.Guard_Rails = Guard_Rails
        self.If_Data = If_Data
        self.Monotony = Monotony
        self.Phys_Unit = Phys_Unit
        self.Read_Only = Read_Only
        self.Ref_Memory_Segment = Ref_Memory_Segment
        self.Step_Size = Step_Size
        self.Symbol_Link = Symbol_Link

    def children(self):
        nodelist = []
        if self.Extended_Limits is not None: nodelist.append(("Extended_Limits", self.Extended_Limits))
        if self.Function_List is not None: nodelist.append(("Function_List", self.Function_List))
        if self.Symbol_Link is not None: nodelist.append(("Symbol_Link", self.Symbol_Link))
        for i, child in enumerate(self.Annotation or []):
            nodelist.append(("Annotation[%d]" % i, child))
        for i, child in enumerate(self.If_Data or []):
            nodelist.append(("If_Data[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Byte_Order', 'Calibration_Access', 'Display_Identifier', 'Deposit', 'Ecu_Address_Extension', 'Format', 'Guard_Rails', 'Monotony', 'Phys_Unit', 'Read_Only', 'Ref_Memory_Segment', 'Step_Size', )


class Axis_Pts_Ref(Node):
    __slots__ = ('AxisPoints', '__weakref__')
    def __init__(self, AxisPoints):
        self.AxisPoints = AxisPoints

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('AxisPoints', )


class Axis_Pts_X (Node):
    __slots__ = ('Position', 'Datatype', 'IndexIncr', 'Addressing', '__weakref__')
    def __init__(self, Position, Datatype, IndexIncr, Addressing):
        self.Position = Position
        self.Datatype = Datatype
        self.IndexIncr = IndexIncr
        self.Addressing = Addressing

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', 'IndexIncr', 'Addressing', )


class Axis_Pts_Y (Node):
    __slots__ = ('Position', 'Datatype', 'IndexIncr', 'Addressing', '__weakref__')
    def __init__(self, Position, Datatype, IndexIncr, Addressing):
        self.Position = Position
        self.Datatype = Datatype
        self.IndexIncr = IndexIncr
        self.Addressing = Addressing

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', 'IndexIncr', 'Addressing', )


class Axis_Pts_Z (Node):
    __slots__ = ('Position', 'Datatype', 'IndexIncr', 'Addressing', '__weakref__')
    def __init__(self, Position, Datatype, IndexIncr, Addressing):
        self.Position = Position
        self.Datatype = Datatype
        self.IndexIncr = IndexIncr
        self.Addressing = Addressing

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', 'IndexIncr', 'Addressing', )


class Axis_Pts_Z4 (Node):
    __slots__ = ('Position', 'Datatype', 'IndexIncr', 'Addressing', '__weakref__')
    def __init__(self, Position, Datatype, IndexIncr, Addressing):
        self.Position = Position
        self.Datatype = Datatype
        self.IndexIncr = IndexIncr
        self.Addressing = Addressing

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', 'IndexIncr', 'Addressing', )


class Axis_Pts_Z5 (Node):
    __slots__ = ('Position', 'Datatype', 'IndexIncr', 'Addressing', '__weakref__')
    def __init__(self, Position, Datatype, IndexIncr, Addressing):
        self.Position = Position
        self.Datatype = Datatype
        self.IndexIncr = IndexIncr
        self.Addressing = Addressing

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', 'IndexIncr', 'Addressing', )


class Axis_Rescale_X(Node):
    __slots__ = ('Position', 'Datatype', 'MaxNumberOfRescalePairs', 'IndexIncr', 'Addressing', '__weakref__')
    def __init__(self, Position, Datatype, MaxNumberOfRescalePairs, IndexIncr, Addressing):
        self.Position = Position
        self.Datatype = Datatype
        self.MaxNumberOfRescalePairs = MaxNumberOfRescalePairs
        self.IndexIncr = IndexIncr
        self.Addressing = Addressing

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', 'MaxNumberOfRescalePairs', 'IndexIncr', 'Addressing', )


class Bit_Mask(Node):
    __slots__ = ('Mask', '__weakref__')
    def __init__(self, Mask):
        self.Mask = Mask

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Mask', )


class Bit_Operation (Node):
    __slots__ = ('OptionalParams', '__weakref__')
    def __init__(self, OptionalParams = None):
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ()


class Bit_Operation_Opt (Node):
    __slots__ = ('Left_Shift', 'Right_Shift', 'Sign_Extend', '__weakref__')
    def __init__(self, Left_Shift = None, Right_Shift = None, Sign_Extend = None):
        self.Left_Shift = Left_Shift
        self.Right_Shift = Right_Shift
        self.Sign_Extend = Sign_Extend

    def children(self):
        nodelist = []
        if self.Left_Shift is not None: nodelist.append(("Left_Shift", self.Left_Shift))
        if self.Right_Shift is not None: nodelist.append(("Right_Shift", self.Right_Shift))
        if self.Sign_Extend is not None: nodelist.append(("Sign_Extend", self.Sign_Extend))
        return tuple(nodelist)

    attr_names = ()


class Byte_Order(Node):
    __slots__ = ('Byte_Order', '__weakref__')
    def __init__(self, Byte_Order):
        self.Byte_Order = Byte_Order

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Byte_Order', )


class Calibration_Access (Node):
    __slots__ = ('Type', '__weakref__')
    def __init__(self, Type):
        self.Type = Type

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Type', )


class Calibration_Handle (Node):
    __slots__ = ('Handle', 'Calibration_Handle_Text', '__weakref__')
    def __init__(self, Handle, Calibration_Handle_Text = None):
        self.Handle = Handle
        self.Calibration_Handle_Text = Calibration_Handle_Text

    def children(self):
        nodelist = []
        if self.Calibration_Handle_Text is not None: nodelist.append(("Calibration_Handle_Text", self.Calibration_Handle_Text))
        return tuple(nodelist)

    attr_names = ('Handle', )


class Calibration_Handle_Opt (Node):
    __slots__ = ('Calibration_Handle_Text', '__weakref__')
    def __init__(self, Calibration_Handle_Text = None):
        self.Calibration_Handle_Text = Calibration_Handle_Text

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Calibration_Handle_Text', )


class Calibration_Handle_Text(Node):
    __slots__ = ('Text', '__weakref__')
    def __init__(self, Text):
        self.Text = Text

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Text', )


class Calibration_Method(Node):
    __slots__ = ('Method', 'Version', 'Calibration_Handle', '__weakref__')
    def __init__(self, Method, Version, Calibration_Handle = None):
        self.Method = Method
        self.Version = Version
        self.Calibration_Handle = Calibration_Handle

    def children(self):
        nodelist = []
        for i, child in enumerate(self.Calibration_Handle or []):
            nodelist.append(("Calibration_Handle[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Method', 'Version', )


class Characteristic(Node):
    __slots__ = ('Name', 'LongIdentifier', 'Type', 'Address', 'Deposit_Ref', 'MaxDiff', 'Conversion', 'LowerLimit', 'UpperLimit', 'OptionalParams', '__weakref__')
    def __init__(self, Name, LongIdentifier, Type, Address, Deposit_Ref, MaxDiff, Conversion, LowerLimit, UpperLimit, OptionalParams = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.Type = Type
        self.Address = Address
        self.Deposit_Ref = Deposit_Ref
        self.MaxDiff = MaxDiff
        self.Conversion = Conversion
        self.LowerLimit = LowerLimit
        self.UpperLimit = UpperLimit
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', 'Type', 'Address', 'Deposit_Ref', 'MaxDiff', 'Conversion', 'LowerLimit', 'UpperLimit', )


class Characteristic_Opt (Node):
    __slots__ = ('Annotation', 'Axis_Descr', 'Bit_Mask', 'Byte_Order', 'Calibration_Access', 'Comparison_Quantity', 'Dependent_Characteristic', 'Discrete', 'Display_Identifier', 'Ecu_Address_Extension', 'Extended_Limits', 'Format', 'Function_List', 'Guard_Rails', 'If_Data', 'Map_List', 'Matrix_Dim', 'Max_Refresh', 'Number', 'Phys_Unit', 'Read_Only', 'Ref_Memory_Segment', 'Step_Size', 'Symbol_Link', 'Virtual_Characteristic', '__weakref__')
    def __init__(self, Annotation = None, Axis_Descr = None, Bit_Mask = None, Byte_Order = None, Calibration_Access = None, Comparison_Quantity = None, Dependent_Characteristic = None, Discrete = None, Display_Identifier = None, Ecu_Address_Extension = None, Extended_Limits = None, Format = None, Function_List = None, Guard_Rails = None, If_Data = None, Map_List = None, Matrix_Dim = None, Max_Refresh = None, Number = None, Phys_Unit = None, Read_Only = None, Ref_Memory_Segment = None, Step_Size = None, Symbol_Link = None, Virtual_Characteristic = None):
        self.Annotation = Annotation
        self.Axis_Descr = Axis_Descr
        self.Bit_Mask = Bit_Mask
        self.Byte_Order = Byte_Order
        self.Calibration_Access = Calibration_Access
        self.Comparison_Quantity = Comparison_Quantity
        self.Dependent_Characteristic = Dependent_Characteristic
        self.Discrete = Discrete
        self.Display_Identifier = Display_Identifier
        self.Ecu_Address_Extension = Ecu_Address_Extension
        self.Extended_Limits = Extended_Limits
        self.Format = Format
        self.Function_List = Function_List
        self.Guard_Rails = Guard_Rails
        self.If_Data = If_Data
        self.Map_List = Map_List
        self.Matrix_Dim = Matrix_Dim
        self.Max_Refresh = Max_Refresh
        self.Number = Number
        self.Phys_Unit = Phys_Unit
        self.Read_Only = Read_Only
        self.Ref_Memory_Segment = Ref_Memory_Segment
        self.Step_Size = Step_Size
        self.Symbol_Link = Symbol_Link
        self.Virtual_Characteristic = Virtual_Characteristic

    def children(self):
        nodelist = []
        if self.Dependent_Characteristic is not None: nodelist.append(("Dependent_Characteristic", self.Dependent_Characteristic))
        if self.Extended_Limits is not None: nodelist.append(("Extended_Limits", self.Extended_Limits))
        if self.Function_List is not None: nodelist.append(("Function_List", self.Function_List))
        if self.Map_List is not None: nodelist.append(("Map_List", self.Map_List))
        if self.Matrix_Dim is not None: nodelist.append(("Matrix_Dim", self.Matrix_Dim))
        if self.Max_Refresh is not None: nodelist.append(("Max_Refresh", self.Max_Refresh))
        if self.Symbol_Link is not None: nodelist.append(("Symbol_Link", self.Symbol_Link))
        if self.Virtual_Characteristic is not None: nodelist.append(("Virtual_Characteristic", self.Virtual_Characteristic))
        for i, child in enumerate(self.Annotation or []):
            nodelist.append(("Annotation[%d]" % i, child))
        for i, child in enumerate(self.Axis_Descr or []):
            nodelist.append(("Axis_Descr[%d]" % i, child))
        for i, child in enumerate(self.If_Data or []):
            nodelist.append(("If_Data[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Bit_Mask', 'Byte_Order', 'Calibration_Access', 'Comparison_Quantity', 'Discrete', 'Display_Identifier', 'Ecu_Address_Extension', 'Format', 'Guard_Rails', 'Number', 'Phys_Unit', 'Read_Only', 'Ref_Memory_Segment', 'Step_Size', )


class Coeffs(Node):
    __slots__ = ('a', 'b', 'c', 'd', 'e', 'f', '__weakref__')
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('a', 'b', 'c', 'd', 'e', 'f', )


class Coeffs_Linear(Node):
    __slots__ = ('a', 'b', '__weakref__')
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('a', 'b', )


class Comparison_Quantity(Node):
    __slots__ = ('Name', '__weakref__')
    def __init__(self, Name):
        self.Name = Name

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Name', )


class Compu_Method (Node):
    __slots__ = ('Name', 'LongIdentifier', 'ConversionType', 'Format', 'Unit', 'OptionalParams', '__weakref__')
    def __init__(self, Name, LongIdentifier, ConversionType, Format, Unit, OptionalParams = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.ConversionType = ConversionType
        self.Format = Format
        self.Unit = Unit
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', 'ConversionType', 'Format', 'Unit', )


class Compu_Method_Opt (Node):
    __slots__ = ('Coeffs', 'Coeffs_Linear', 'Compu_Tab_Ref', 'Formula', 'Ref_Unit', 'Status_String_Ref', '__weakref__')
    def __init__(self, Coeffs = None, Coeffs_Linear = None, Compu_Tab_Ref = None, Formula = None, Ref_Unit = None, Status_String_Ref = None):
        self.Coeffs = Coeffs
        self.Coeffs_Linear = Coeffs_Linear
        self.Compu_Tab_Ref = Compu_Tab_Ref
        self.Formula = Formula
        self.Ref_Unit = Ref_Unit
        self.Status_String_Ref = Status_String_Ref

    def children(self):
        nodelist = []
        if self.Coeffs is not None: nodelist.append(("Coeffs", self.Coeffs))
        if self.Coeffs_Linear is not None: nodelist.append(("Coeffs_Linear", self.Coeffs_Linear))
        if self.Formula is not None: nodelist.append(("Formula", self.Formula))
        return tuple(nodelist)

    attr_names = ('Compu_Tab_Ref', 'Ref_Unit', 'Status_String_Ref', )


class Compu_Tab (Node):
    __slots__ = ('Name', 'LongIdentifier', 'ConversionType', 'NumberValuePairs', 'Axis_Points', 'OptionalParams', '__weakref__')
    def __init__(self, Name, LongIdentifier, ConversionType, NumberValuePairs, Axis_Points, OptionalParams = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.ConversionType = ConversionType
        self.NumberValuePairs = NumberValuePairs
        self.Axis_Points = Axis_Points
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', 'ConversionType', 'NumberValuePairs', 'Axis_Points', )


class Compu_Tab_Opt (Node):
    __slots__ = ('Default_Value', 'Default_Value_Numeric', '__weakref__')
    def __init__(self, Default_Value = None, Default_Value_Numeric = None):
        self.Default_Value = Default_Value
        self.Default_Value_Numeric = Default_Value_Numeric

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Default_Value', 'Default_Value_Numeric', )


class Compu_Tab_Ref (Node):
    __slots__ = ('ConversionTable', '__weakref__')
    def __init__(self, ConversionTable):
        self.ConversionTable = ConversionTable

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('ConversionTable', )


class Compu_Vtab (Node):
    __slots__ = ('Name', 'LongIdentifier', 'ConversionType', 'NumberValuePairs', 'InVal_OutVal', 'Default_Value', '__weakref__')
    def __init__(self, Name, LongIdentifier, ConversionType, NumberValuePairs, InVal_OutVal, Default_Value = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.ConversionType = ConversionType
        self.NumberValuePairs = NumberValuePairs
        self.InVal_OutVal = InVal_OutVal
        self.Default_Value = Default_Value

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', 'ConversionType', 'NumberValuePairs', 'InVal_OutVal', 'Default_Value', )


class Compu_Vtab_Range (Node):
    __slots__ = ('Name', 'LongIdentifier', 'NumberValueTriples', 'InVal_MinMax_OutVal', 'Default_Value', '__weakref__')
    def __init__(self, Name, LongIdentifier, NumberValueTriples, InVal_MinMax_OutVal, Default_Value = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.NumberValueTriples = NumberValueTriples
        self.InVal_MinMax_OutVal = InVal_MinMax_OutVal
        self.Default_Value = Default_Value

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', 'NumberValueTriples', 'InVal_MinMax_OutVal', 'Default_Value', )


class Cpu_Type (Node):
    __slots__ = ('CPU', '__weakref__')
    def __init__(self, CPU):
        self.CPU = CPU

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('CPU', )


class Curve_Axis_Ref(Node):
    __slots__ = ('CurveAxis', '__weakref__')
    def __init__(self, CurveAxis):
        self.CurveAxis = CurveAxis

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('CurveAxis', )


class Customer(Node):
    __slots__ = ('Customer', '__weakref__')
    def __init__(self, Customer):
        self.Customer = Customer

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Customer', )


class Customer_No(Node):
    __slots__ = ('Number', '__weakref__')
    def __init__(self, Number):
        self.Number = Number

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Number', )


class Data_Size(Node):
    __slots__ = ('Size', '__weakref__')
    def __init__(self, Size):
        self.Size = Size

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Size', )


class Def_Characteristic(Node):
    __slots__ = ('Identifier', '__weakref__')
    def __init__(self, Identifier):
        self.Identifier = Identifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Identifier', )


class Default_Value (Node):
    __slots__ = ('display_string', '__weakref__')
    def __init__(self, display_string):
        self.display_string = display_string

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('display_string', )


class Default_Value_Numeric(Node):
    __slots__ = ('display_value', '__weakref__')
    def __init__(self, display_value):
        self.display_value = display_value

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('display_value', )


class Dependent_Characteristic(Node):
    __slots__ = ('Formula', 'Characteristic', '__weakref__')
    def __init__(self, Formula, Characteristic):
        self.Formula = Formula
        self.Characteristic = Characteristic

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Formula', 'Characteristic', )


class Deposit (Node):
    __slots__ = ('Mode', '__weakref__')
    def __init__(self, Mode):
        self.Mode = Mode

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Mode', )


class Discrete(Node):
    __slots__ = ('Boolean', '__weakref__')
    def __init__(self, Boolean):
        self.Boolean = Boolean

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Boolean', )


class Display_Identifier (Node):
    __slots__ = ('display_name', '__weakref__')
    def __init__(self, display_name):
        self.display_name = display_name

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('display_name', )


class Dist_Op_X (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Dist_Op_Y (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Dist_Op_Z (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Dist_Op_Z4 (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Dist_Op_Z5 (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Ecu (Node):
    __slots__ = ('ControlUnit', '__weakref__')
    def __init__(self, ControlUnit):
        self.ControlUnit = ControlUnit

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('ControlUnit', )


class Ecu_Address (Node):
    __slots__ = ('Address', '__weakref__')
    def __init__(self, Address):
        self.Address = Address

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Address', )


class Ecu_Address_Extension (Node):
    __slots__ = ('Extension', '__weakref__')
    def __init__(self, Extension):
        self.Extension = Extension

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Extension', )


class Ecu_Calibration_Offset (Node):
    __slots__ = ('Offset', '__weakref__')
    def __init__(self, Offset):
        self.Offset = Offset

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Offset', )


class Epk (Node):
    __slots__ = ('Identifier', '__weakref__')
    def __init__(self, Identifier):
        self.Identifier = Identifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Identifier', )


class Error_Mask (Node):
    __slots__ = ('Mask', '__weakref__')
    def __init__(self, Mask):
        self.Mask = Mask

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Mask', )


class Extended_Limits (Node):
    __slots__ = ('LowerLimit', 'UpperLimit', '__weakref__')
    def __init__(self, LowerLimit, UpperLimit):
        self.LowerLimit = LowerLimit
        self.UpperLimit = UpperLimit

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('LowerLimit', 'UpperLimit', )


class Fix_Axis_Par (Node):
    __slots__ = ('Offset', 'Shift', 'Numberapo', '__weakref__')
    def __init__(self, Offset, Shift, Numberapo):
        self.Offset = Offset
        self.Shift = Shift
        self.Numberapo = Numberapo

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Offset', 'Shift', 'Numberapo', )


class Fix_Axis_Par_Dist (Node):
    __slots__ = ('Offset', 'Distance', 'Numberapo', '__weakref__')
    def __init__(self, Offset, Distance, Numberapo):
        self.Offset = Offset
        self.Distance = Distance
        self.Numberapo = Numberapo

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Offset', 'Distance', 'Numberapo', )


class Fix_Axis_Par_List (Node):
    __slots__ = ('AxisPts_Value', '__weakref__')
    def __init__(self, AxisPts_Value):
        self.AxisPts_Value = AxisPts_Value

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('AxisPts_Value', )


class Fix_No_Axis_Pts_X (Node):
    __slots__ = ('NumberOfAxisPoints', '__weakref__')
    def __init__(self, NumberOfAxisPoints):
        self.NumberOfAxisPoints = NumberOfAxisPoints

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('NumberOfAxisPoints', )


class Fix_No_Axis_Pts_Y (Node):
    __slots__ = ('NumberOfAxisPoints', '__weakref__')
    def __init__(self, NumberOfAxisPoints):
        self.NumberOfAxisPoints = NumberOfAxisPoints

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('NumberOfAxisPoints', )


class Fix_No_Axis_Pts_Z (Node):
    __slots__ = ('NumberOfAxisPoints', '__weakref__')
    def __init__(self, NumberOfAxisPoints):
        self.NumberOfAxisPoints = NumberOfAxisPoints

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('NumberOfAxisPoints', )


class Fix_No_Axis_Pts_Z4 (Node):
    __slots__ = ('NumberOfAxisPoints', '__weakref__')
    def __init__(self, NumberOfAxisPoints):
        self.NumberOfAxisPoints = NumberOfAxisPoints

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('NumberOfAxisPoints', )


class Fix_No_Axis_Pts_Z5 (Node):
    __slots__ = ('NumberOfAxisPoints', '__weakref__')
    def __init__(self, NumberOfAxisPoints):
        self.NumberOfAxisPoints = NumberOfAxisPoints

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('NumberOfAxisPoints', )


class Fnc_Values (Node):
    __slots__ = ('Position', 'Datatype', 'IndexMode', 'AddressType', '__weakref__')
    def __init__(self, Position, Datatype, IndexMode, AddressType):
        self.Position = Position
        self.Datatype = Datatype
        self.IndexMode = IndexMode
        self.AddressType = AddressType

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', 'IndexMode', 'AddressType', )


class Format (Node):
    __slots__ = ('FormatString', '__weakref__')
    def __init__(self, FormatString):
        self.FormatString = FormatString

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('FormatString', )


class Formula (Node):
    __slots__ = ('f_x', 'Formula_Inv', '__weakref__')
    def __init__(self, f_x, Formula_Inv = None):
        self.f_x = f_x
        self.Formula_Inv = Formula_Inv

    def children(self):
        nodelist = []
        if self.Formula_Inv is not None: nodelist.append(("Formula_Inv", self.Formula_Inv))
        return tuple(nodelist)

    attr_names = ('f_x', )


class Formula_Inv (Node):
    __slots__ = ('g_x', '__weakref__')
    def __init__(self, g_x):
        self.g_x = g_x

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('g_x', )


class Frame (Node):
    __slots__ = ('Name', 'LongIdentifier', 'ScalingUnit', 'Rate', 'OptionalParams', '__weakref__')
    def __init__(self, Name, LongIdentifier, ScalingUnit, Rate, OptionalParams = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.ScalingUnit = ScalingUnit
        self.Rate = Rate
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', 'ScalingUnit', 'Rate', )


class Frame_Opt (Node):
    __slots__ = ('Frame_Measurement', 'If_Data', '__weakref__')
    def __init__(self, Frame_Measurement = None, If_Data = None):
        self.Frame_Measurement = Frame_Measurement
        self.If_Data = If_Data

    def children(self):
        nodelist = []
        for i, child in enumerate(self.If_Data or []):
            nodelist.append(("If_Data[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Frame_Measurement', )


class Frame_Measurement (Node):
    __slots__ = ('Identifier', '__weakref__')
    def __init__(self, Identifier):
        self.Identifier = Identifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Identifier', )


class Function (Node):
    __slots__ = ('Name', 'LongIdentifier', 'OptionalParams', '__weakref__')
    def __init__(self, Name, LongIdentifier, OptionalParams = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', )


class Function_Opt (Node):
    __slots__ = ('Annotation', 'Def_Characteristic', 'Function_Version', 'If_Data', 'In_Measurement', 'Loc_Measurement', 'Out_Measurement', 'Ref_Characteristic', 'Sub_Function', '__weakref__')
    def __init__(self, Annotation = None, Def_Characteristic = None, Function_Version = None, If_Data = None, In_Measurement = None, Loc_Measurement = None, Out_Measurement = None, Ref_Characteristic = None, Sub_Function = None):
        self.Annotation = Annotation
        self.Def_Characteristic = Def_Characteristic
        self.Function_Version = Function_Version
        self.If_Data = If_Data
        self.In_Measurement = In_Measurement
        self.Loc_Measurement = Loc_Measurement
        self.Out_Measurement = Out_Measurement
        self.Ref_Characteristic = Ref_Characteristic
        self.Sub_Function = Sub_Function

    def children(self):
        nodelist = []
        if self.Def_Characteristic is not None: nodelist.append(("Def_Characteristic", self.Def_Characteristic))
        if self.In_Measurement is not None: nodelist.append(("In_Measurement", self.In_Measurement))
        if self.Loc_Measurement is not None: nodelist.append(("Loc_Measurement", self.Loc_Measurement))
        if self.Out_Measurement is not None: nodelist.append(("Out_Measurement", self.Out_Measurement))
        if self.Ref_Characteristic is not None: nodelist.append(("Ref_Characteristic", self.Ref_Characteristic))
        for i, child in enumerate(self.Annotation or []):
            nodelist.append(("Annotation[%d]" % i, child))
        for i, child in enumerate(self.If_Data or []):
            nodelist.append(("If_Data[%d]" % i, child))
        for i, child in enumerate(self.Sub_Function or []):
            nodelist.append(("Sub_Function[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Function_Version', )


class Function_List (Node):
    __slots__ = ('Name', '__weakref__')
    def __init__(self, Name):
        self.Name = Name

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Name', )


class Function_Version (Node):
    __slots__ = ('VersionIdentifier', '__weakref__')
    def __init__(self, VersionIdentifier):
        self.VersionIdentifier = VersionIdentifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('VersionIdentifier', )


class Group (Node):
    __slots__ = ('GroupName', 'GroupLongIdentifier', 'OptionalParams', '__weakref__')
    def __init__(self, GroupName, GroupLongIdentifier, OptionalParams = None):
        self.GroupName = GroupName
        self.GroupLongIdentifier = GroupLongIdentifier
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('GroupName', 'GroupLongIdentifier', )


class Group_Opt (Node):
    __slots__ = ('Annotation', 'Function_List', 'If_Data', 'Ref_Characteristic', 'Ref_Measurement', 'Root', 'Sub_Group', '__weakref__')
    def __init__(self, Annotation = None, Function_List = None, If_Data = None, Ref_Characteristic = None, Ref_Measurement = None, Root = None, Sub_Group = None):
        self.Annotation = Annotation
        self.Function_List = Function_List
        self.If_Data = If_Data
        self.Ref_Characteristic = Ref_Characteristic
        self.Ref_Measurement = Ref_Measurement
        self.Root = Root
        self.Sub_Group = Sub_Group

    def children(self):
        nodelist = []
        if self.Function_List is not None: nodelist.append(("Function_List", self.Function_List))
        if self.Ref_Characteristic is not None: nodelist.append(("Ref_Characteristic", self.Ref_Characteristic))
        if self.Ref_Measurement is not None: nodelist.append(("Ref_Measurement", self.Ref_Measurement))
        if self.Sub_Group is not None: nodelist.append(("Sub_Group", self.Sub_Group))
        for i, child in enumerate(self.Annotation or []):
            nodelist.append(("Annotation[%d]" % i, child))
        for i, child in enumerate(self.If_Data or []):
            nodelist.append(("If_Data[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Root', )


class Guard_Rails (Node):
    __slots__ = ('Boolean', '__weakref__')
    def __init__(self, Boolean):
        self.Boolean = Boolean

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Boolean', )


class Header (Node):
    __slots__ = ('Comment', 'OptionalParams', '__weakref__')
    def __init__(self, Comment, OptionalParams = None):
        self.Comment = Comment
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Comment', )


class Header_Opt (Node):
    __slots__ = ('Project_No', 'Version', '__weakref__')
    def __init__(self, Project_No = None, Version = None):
        self.Project_No = Project_No
        self.Version = Version

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Project_No', 'Version', )


class Identification (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class If_Data (Node):
    __slots__ = ('Name', 'OptionalParams', '__weakref__')
    def __init__(self, Name, OptionalParams = None):
        self.Name = Name
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', )


class If_Data_Opt (Node):
    __slots__ = ('DataParams', 'If_Data_Block', '__weakref__')
    def __init__(self, DataParams = None, If_Data_Block = None):
        self.DataParams = DataParams
        self.If_Data_Block = If_Data_Block

    def children(self):
        nodelist = []
        for i, child in enumerate(self.If_Data_Block or []):
            nodelist.append(("If_Data_Block[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('DataParams', )


class If_Data_Block (Node):
    __slots__ = ('Name', 'DataParams', 'If_Data_Block', '__weakref__')
    def __init__(self, Name = None, DataParams = None, If_Data_Block = None):
        self.Name = Name
        self.DataParams = DataParams
        self.If_Data_Block = If_Data_Block

    def children(self):
        nodelist = []
        for i, child in enumerate(self.If_Data_Block or []):
            nodelist.append(("If_Data_Block[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Name', 'DataParams', )


class In_Measurement (Node):
    __slots__ = ('Identifier', '__weakref__')
    def __init__(self, Identifier):
        self.Identifier = Identifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Identifier', )


class Layout (Node):
    __slots__ = ('IndexMode', '__weakref__')
    def __init__(self, IndexMode):
        self.IndexMode = IndexMode

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('IndexMode', )


class Left_Shift (Node):
    __slots__ = ('Bitcount', '__weakref__')
    def __init__(self, Bitcount):
        self.Bitcount = Bitcount

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Bitcount', )


class Loc_Measurement (Node):
    __slots__ = ('Identifier', '__weakref__')
    def __init__(self, Identifier):
        self.Identifier = Identifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Identifier', )


class Map_List (Node):
    __slots__ = ('Name', '__weakref__')
    def __init__(self, Name):
        self.Name = Name

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Name', )


class Matrix_Dim (Node):
    __slots__ = ('xDim', 'yDim', 'zDim', '__weakref__')
    def __init__(self, xDim, yDim, zDim):
        self.xDim = xDim
        self.yDim = yDim
        self.zDim = zDim

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('xDim', 'yDim', 'zDim', )


class Max_Grad (Node):
    __slots__ = ('MaxGradient', '__weakref__')
    def __init__(self, MaxGradient):
        self.MaxGradient = MaxGradient

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('MaxGradient', )


class Max_Refresh (Node):
    __slots__ = ('ScalingUnit', 'Rate', '__weakref__')
    def __init__(self, ScalingUnit, Rate):
        self.ScalingUnit = ScalingUnit
        self.Rate = Rate

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('ScalingUnit', 'Rate', )


class Measurement (Node):
    __slots__ = ('Name', 'LongIdentifier', 'Datatype', 'Conversion', 'Resolution', 'Accuracy', 'LowerLimit', 'UpperLimit', 'OptionalParams', '__weakref__')
    def __init__(self, Name, LongIdentifier, Datatype, Conversion, Resolution, Accuracy, LowerLimit, UpperLimit, OptionalParams = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.Datatype = Datatype
        self.Conversion = Conversion
        self.Resolution = Resolution
        self.Accuracy = Accuracy
        self.LowerLimit = LowerLimit
        self.UpperLimit = UpperLimit
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', 'Datatype', 'Conversion', 'Resolution', 'Accuracy', 'LowerLimit', 'UpperLimit', )


class Measurement_Opt (Node):
    __slots__ = ('Annotation', 'Array_Size', 'Bit_Mask', 'Bit_Operation', 'Byte_Order', 'Discrete', 'Display_Identifier', 'Ecu_Address', 'Ecu_Address_Extension', 'Error_Mask', 'Format', 'Function_List', 'If_Data', 'Layout', 'Matrix_Dim', 'Max_Refresh', 'Phys_Unit', 'Read_Write', 'Ref_Memory_Segment', 'Symbol_Link', 'Virtual', '__weakref__')
    def __init__(self, Annotation = None, Array_Size = None, Bit_Mask = None, Bit_Operation = None, Byte_Order = None, Discrete = None, Display_Identifier = None, Ecu_Address = None, Ecu_Address_Extension = None, Error_Mask = None, Format = None, Function_List = None, If_Data = None, Layout = None, Matrix_Dim = None, Max_Refresh = None, Phys_Unit = None, Read_Write = None, Ref_Memory_Segment = None, Symbol_Link = None, Virtual = None):
        self.Annotation = Annotation
        self.Array_Size = Array_Size
        self.Bit_Mask = Bit_Mask
        self.Bit_Operation = Bit_Operation
        self.Byte_Order = Byte_Order
        self.Discrete = Discrete
        self.Display_Identifier = Display_Identifier
        self.Ecu_Address = Ecu_Address
        self.Ecu_Address_Extension = Ecu_Address_Extension
        self.Error_Mask = Error_Mask
        self.Format = Format
        self.Function_List = Function_List
        self.If_Data = If_Data
        self.Layout = Layout
        self.Matrix_Dim = Matrix_Dim
        self.Max_Refresh = Max_Refresh
        self.Phys_Unit = Phys_Unit
        self.Read_Write = Read_Write
        self.Ref_Memory_Segment = Ref_Memory_Segment
        self.Symbol_Link = Symbol_Link
        self.Virtual = Virtual

    def children(self):
        nodelist = []
        if self.Bit_Operation is not None: nodelist.append(("Bit_Operation", self.Bit_Operation))
        if self.Function_List is not None: nodelist.append(("Function_List", self.Function_List))
        if self.Matrix_Dim is not None: nodelist.append(("Matrix_Dim", self.Matrix_Dim))
        if self.Max_Refresh is not None: nodelist.append(("Max_Refresh", self.Max_Refresh))
        if self.Symbol_Link is not None: nodelist.append(("Symbol_Link", self.Symbol_Link))
        if self.Virtual is not None: nodelist.append(("Virtual", self.Virtual))
        for i, child in enumerate(self.Annotation or []):
            nodelist.append(("Annotation[%d]" % i, child))
        for i, child in enumerate(self.If_Data or []):
            nodelist.append(("If_Data[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Array_Size', 'Bit_Mask', 'Byte_Order', 'Discrete', 'Display_Identifier', 'Ecu_Address', 'Ecu_Address_Extension', 'Error_Mask', 'Format', 'Layout', 'Phys_Unit', 'Read_Write', 'Ref_Memory_Segment', )


class Memory_Layout (Node):
    __slots__ = ('PrgType', 'Address', 'Size', 'Offset', 'If_Data', '__weakref__')
    def __init__(self, PrgType, Address, Size, Offset, If_Data = None):
        self.PrgType = PrgType
        self.Address = Address
        self.Size = Size
        self.Offset = Offset
        self.If_Data = If_Data

    def children(self):
        nodelist = []
        for i, child in enumerate(self.If_Data or []):
            nodelist.append(("If_Data[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('PrgType', 'Address', 'Size', 'Offset', )


class Memory_Segment (Node):
    __slots__ = ('Name', 'LongIdentifier', 'PrgType', 'MemoryType', 'Attribute', 'Address', 'Size', 'Offset', 'If_Data', '__weakref__')
    def __init__(self, Name, LongIdentifier, PrgType, MemoryType, Attribute, Address, Size, Offset, If_Data = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.PrgType = PrgType
        self.MemoryType = MemoryType
        self.Attribute = Attribute
        self.Address = Address
        self.Size = Size
        self.Offset = Offset
        self.If_Data = If_Data

    def children(self):
        nodelist = []
        for i, child in enumerate(self.If_Data or []):
            nodelist.append(("If_Data[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', 'PrgType', 'MemoryType', 'Attribute', 'Address', 'Size', 'Offset', )


class Mod_Common (Node):
    __slots__ = ('Comment', 'OptionalParams', '__weakref__')
    def __init__(self, Comment, OptionalParams = None):
        self.Comment = Comment
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Comment', )


class Mod_Common_Opt (Node):
    __slots__ = ('Alignment_Byte', 'Alignment_Float32_Ieee', 'Alignment_Float64_Ieee', 'Alignment_Int64', 'Alignment_Long', 'Alignment_Word', 'Byte_Order', 'Data_Size', 'Deposit', '__weakref__')
    def __init__(self, Alignment_Byte = None, Alignment_Float32_Ieee = None, Alignment_Float64_Ieee = None, Alignment_Int64 = None, Alignment_Long = None, Alignment_Word = None, Byte_Order = None, Data_Size = None, Deposit = None):
        self.Alignment_Byte = Alignment_Byte
        self.Alignment_Float32_Ieee = Alignment_Float32_Ieee
        self.Alignment_Float64_Ieee = Alignment_Float64_Ieee
        self.Alignment_Int64 = Alignment_Int64
        self.Alignment_Long = Alignment_Long
        self.Alignment_Word = Alignment_Word
        self.Byte_Order = Byte_Order
        self.Data_Size = Data_Size
        self.Deposit = Deposit

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Alignment_Byte', 'Alignment_Float32_Ieee', 'Alignment_Float64_Ieee', 'Alignment_Int64', 'Alignment_Long', 'Alignment_Word', 'Byte_Order', 'Data_Size', 'Deposit', )


class Mod_Par (Node):
    __slots__ = ('Comment', 'OptionalParams', '__weakref__')
    def __init__(self, Comment, OptionalParams = None):
        self.Comment = Comment
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Comment', )


class Mod_Par_Opt (Node):
    __slots__ = ('Addr_Epk', 'Calibration_Method', 'Cpu_Type', 'Customer', 'Customer_No', 'Ecu', 'Ecu_Calibration_Offset', 'Epk', 'Memory_Layout', 'Memory_Segment', 'No_Of_Interfaces', 'Phone_No', 'Supplier', 'System_Constant', 'User', 'Version', '__weakref__')
    def __init__(self, Addr_Epk = None, Calibration_Method = None, Cpu_Type = None, Customer = None, Customer_No = None, Ecu = None, Ecu_Calibration_Offset = None, Epk = None, Memory_Layout = None, Memory_Segment = None, No_Of_Interfaces = None, Phone_No = None, Supplier = None, System_Constant = None, User = None, Version = None):
        self.Addr_Epk = Addr_Epk
        self.Calibration_Method = Calibration_Method
        self.Cpu_Type = Cpu_Type
        self.Customer = Customer
        self.Customer_No = Customer_No
        self.Ecu = Ecu
        self.Ecu_Calibration_Offset = Ecu_Calibration_Offset
        self.Epk = Epk
        self.Memory_Layout = Memory_Layout
        self.Memory_Segment = Memory_Segment
        self.No_Of_Interfaces = No_Of_Interfaces
        self.Phone_No = Phone_No
        self.Supplier = Supplier
        self.System_Constant = System_Constant
        self.User = User
        self.Version = Version

    def children(self):
        nodelist = []
        for i, child in enumerate(self.Addr_Epk or []):
            nodelist.append(("Addr_Epk[%d]" % i, child))
        for i, child in enumerate(self.Calibration_Method or []):
            nodelist.append(("Calibration_Method[%d]" % i, child))
        for i, child in enumerate(self.Memory_Layout or []):
            nodelist.append(("Memory_Layout[%d]" % i, child))
        for i, child in enumerate(self.Memory_Segment or []):
            nodelist.append(("Memory_Segment[%d]" % i, child))
        for i, child in enumerate(self.System_Constant or []):
            nodelist.append(("System_Constant[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Cpu_Type', 'Customer', 'Customer_No', 'Ecu', 'Ecu_Calibration_Offset', 'Epk', 'No_Of_Interfaces', 'Phone_No', 'Supplier', 'User', 'Version', )


class Module (Node):
    __slots__ = ('Name', 'LongIdentifier', 'OptionalParams', '__weakref__')
    def __init__(self, Name, LongIdentifier, OptionalParams = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', )


class Module_Opt (Node):
    __slots__ = ('Axis_Pts', 'Characteristic', 'Compu_Method', 'Compu_Tab', 'Compu_Vtab', 'Compu_Vtab_Range', 'Frame', 'Function', 'Group', 'If_Data', 'Measurement', 'Mod_Common', 'Mod_Par', 'Record_Layout', 'Unit', 'User_Rights', 'Variant_Coding', '__weakref__')
    def __init__(self, Axis_Pts = None, Characteristic = None, Compu_Method = None, Compu_Tab = None, Compu_Vtab = None, Compu_Vtab_Range = None, Frame = None, Function = None, Group = None, If_Data = None, Measurement = None, Mod_Common = None, Mod_Par = None, Record_Layout = None, Unit = None, User_Rights = None, Variant_Coding = None):
        self.Axis_Pts = Axis_Pts
        self.Characteristic = Characteristic
        self.Compu_Method = Compu_Method
        self.Compu_Tab = Compu_Tab
        self.Compu_Vtab = Compu_Vtab
        self.Compu_Vtab_Range = Compu_Vtab_Range
        self.Frame = Frame
        self.Function = Function
        self.Group = Group
        self.If_Data = If_Data
        self.Measurement = Measurement
        self.Mod_Common = Mod_Common
        self.Mod_Par = Mod_Par
        self.Record_Layout = Record_Layout
        self.Unit = Unit
        self.User_Rights = User_Rights
        self.Variant_Coding = Variant_Coding

    def children(self):
        nodelist = []
        if self.Mod_Common is not None: nodelist.append(("Mod_Common", self.Mod_Common))
        if self.Mod_Par is not None: nodelist.append(("Mod_Par", self.Mod_Par))
        if self.Variant_Coding is not None: nodelist.append(("Variant_Coding", self.Variant_Coding))
        for i, child in enumerate(self.Axis_Pts or []):
            nodelist.append(("Axis_Pts[%d]" % i, child))
        for i, child in enumerate(self.Characteristic or []):
            nodelist.append(("Characteristic[%d]" % i, child))
        for i, child in enumerate(self.Compu_Method or []):
            nodelist.append(("Compu_Method[%d]" % i, child))
        for i, child in enumerate(self.Compu_Tab or []):
            nodelist.append(("Compu_Tab[%d]" % i, child))
        for i, child in enumerate(self.Compu_Vtab or []):
            nodelist.append(("Compu_Vtab[%d]" % i, child))
        for i, child in enumerate(self.Compu_Vtab_Range or []):
            nodelist.append(("Compu_Vtab_Range[%d]" % i, child))
        for i, child in enumerate(self.Frame or []):
            nodelist.append(("Frame[%d]" % i, child))
        for i, child in enumerate(self.Function or []):
            nodelist.append(("Function[%d]" % i, child))
        for i, child in enumerate(self.Group or []):
            nodelist.append(("Group[%d]" % i, child))
        for i, child in enumerate(self.If_Data or []):
            nodelist.append(("If_Data[%d]" % i, child))
        for i, child in enumerate(self.Measurement or []):
            nodelist.append(("Measurement[%d]" % i, child))
        for i, child in enumerate(self.Record_Layout or []):
            nodelist.append(("Record_Layout[%d]" % i, child))
        for i, child in enumerate(self.Unit or []):
            nodelist.append(("Unit[%d]" % i, child))
        for i, child in enumerate(self.User_Rights or []):
            nodelist.append(("User_Rights[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()


class Monotony (Node):
    __slots__ = ('Monotony', '__weakref__')
    def __init__(self, Monotony):
        self.Monotony = Monotony

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Monotony', )


class No_Axis_Pts_X (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class No_Axis_Pts_Y (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class No_Axis_Pts_Z (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class No_Axis_Pts_Z4 (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class No_Axis_Pts_Z5 (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class No_Of_Interfaces  (Node):
    __slots__ = ('Num', '__weakref__')
    def __init__(self, Num):
        self.Num = Num

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Num', )


class No_Rescale_X  (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Number (Node):
    __slots__ = ('Number', '__weakref__')
    def __init__(self, Number):
        self.Number = Number

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Number', )


class Offset_X (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Offset_Y (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Offset_Z (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Offset_Z4 (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Offset_Z5 (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Out_Measurement (Node):
    __slots__ = ('Identifier', '__weakref__')
    def __init__(self, Identifier):
        self.Identifier = Identifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Identifier', )


class Phone_No (Node):
    __slots__ = ('Telnum', '__weakref__')
    def __init__(self, Telnum):
        self.Telnum = Telnum

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Telnum', )


class Phys_Unit (Node):
    __slots__ = ('Unit', '__weakref__')
    def __init__(self, Unit):
        self.Unit = Unit

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Unit', )


class Project (Node):
    __slots__ = ('Name', 'LongIdentifier', 'OptionalParams', '__weakref__')
    def __init__(self, Name, LongIdentifier, OptionalParams = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', )


class Project_Opt (Node):
    __slots__ = ('Header', 'Module', '__weakref__')
    def __init__(self, Header = None, Module = None):
        self.Header = Header
        self.Module = Module

    def children(self):
        nodelist = []
        if self.Header is not None: nodelist.append(("Header", self.Header))
        for i, child in enumerate(self.Module or []):
            nodelist.append(("Module[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()


class Project_No (Node):
    __slots__ = ('ProjectNumber', '__weakref__')
    def __init__(self, ProjectNumber):
        self.ProjectNumber = ProjectNumber

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('ProjectNumber', )


class Read_Only (Node):
    __slots__ = ('Boolean', '__weakref__')
    def __init__(self, Boolean):
        self.Boolean = Boolean

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Boolean', )


class Read_Write (Node):
    __slots__ = ('Boolean', '__weakref__')
    def __init__(self, Boolean):
        self.Boolean = Boolean

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Boolean', )


class Record_Layout (Node):
    __slots__ = ('Name', 'OptionalParams', '__weakref__')
    def __init__(self, Name, OptionalParams = None):
        self.Name = Name
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', )


class Record_Layout_Opt (Node):
    __slots__ = ('Alignment_Byte', 'Alignment_Float32_Ieee', 'Alignment_Float64_Ieee', 'Alignment_Int64', 'Alignment_Long', 'Alignment_Word', 'Axis_Pts_X', 'Axis_Pts_Y', 'Axis_Pts_Z', 'Axis_Pts_Z4', 'Axis_Pts_Z5', 'Axis_Rescale_X', 'Dist_Op_X', 'Dist_Op_Y', 'Dist_Op_Z', 'Dist_Op_Z4', 'Dist_Op_Z5', 'Fix_No_Axis_Pts_X', 'Fix_No_Axis_Pts_Y', 'Fix_No_Axis_Pts_Z', 'Fix_No_Axis_Pts_Z4', 'Fix_No_Axis_Pts_Z5', 'Fnc_Values', 'Identification', 'No_Axis_Pts_X', 'No_Axis_Pts_Y', 'No_Axis_Pts_Z', 'No_Axis_Pts_Z4', 'No_Axis_Pts_Z5', 'No_Rescale_X', 'Offset_X', 'Offset_Y', 'Offset_Z', 'Offset_Z4', 'Offset_Z5', 'Reserved', 'Rip_Addr_X', 'Rip_Addr_W', 'Rip_Addr_Y', 'Rip_Addr_Z', 'Rip_Addr_Z4', 'Rip_Addr_Z5', 'Src_Addr_X', 'Src_Addr_Y', 'Src_Addr_Z', 'Src_Addr_Z4', 'Src_Addr_Z5', 'Shift_Op_X', 'Shift_Op_Y', 'Shift_Op_Z', 'Shift_Op_Z4', 'Shift_Op_Z5', 'Static_Record_Layout', '__weakref__')
    def __init__(self, Alignment_Byte = None, Alignment_Float32_Ieee = None, Alignment_Float64_Ieee = None, Alignment_Int64 = None, Alignment_Long = None, Alignment_Word = None, Axis_Pts_X = None, Axis_Pts_Y = None, Axis_Pts_Z = None, Axis_Pts_Z4 = None, Axis_Pts_Z5 = None, Axis_Rescale_X = None, Dist_Op_X = None, Dist_Op_Y = None, Dist_Op_Z = None, Dist_Op_Z4 = None, Dist_Op_Z5 = None, Fix_No_Axis_Pts_X = None, Fix_No_Axis_Pts_Y = None, Fix_No_Axis_Pts_Z = None, Fix_No_Axis_Pts_Z4 = None, Fix_No_Axis_Pts_Z5 = None, Fnc_Values = None, Identification = None, No_Axis_Pts_X = None, No_Axis_Pts_Y = None, No_Axis_Pts_Z = None, No_Axis_Pts_Z4 = None, No_Axis_Pts_Z5 = None, No_Rescale_X = None, Offset_X = None, Offset_Y = None, Offset_Z = None, Offset_Z4 = None, Offset_Z5 = None, Reserved = None, Rip_Addr_X = None, Rip_Addr_W = None, Rip_Addr_Y = None, Rip_Addr_Z = None, Rip_Addr_Z4 = None, Rip_Addr_Z5 = None, Src_Addr_X = None, Src_Addr_Y = None, Src_Addr_Z = None, Src_Addr_Z4 = None, Src_Addr_Z5 = None, Shift_Op_X = None, Shift_Op_Y = None, Shift_Op_Z = None, Shift_Op_Z4 = None, Shift_Op_Z5 = None, Static_Record_Layout = None):
        self.Alignment_Byte = Alignment_Byte
        self.Alignment_Float32_Ieee = Alignment_Float32_Ieee
        self.Alignment_Float64_Ieee = Alignment_Float64_Ieee
        self.Alignment_Int64 = Alignment_Int64
        self.Alignment_Long = Alignment_Long
        self.Alignment_Word = Alignment_Word
        self.Axis_Pts_X = Axis_Pts_X
        self.Axis_Pts_Y = Axis_Pts_Y
        self.Axis_Pts_Z = Axis_Pts_Z
        self.Axis_Pts_Z4 = Axis_Pts_Z4
        self.Axis_Pts_Z5 = Axis_Pts_Z5
        self.Axis_Rescale_X = Axis_Rescale_X
        self.Dist_Op_X = Dist_Op_X
        self.Dist_Op_Y = Dist_Op_Y
        self.Dist_Op_Z = Dist_Op_Z
        self.Dist_Op_Z4 = Dist_Op_Z4
        self.Dist_Op_Z5 = Dist_Op_Z5
        self.Fix_No_Axis_Pts_X = Fix_No_Axis_Pts_X
        self.Fix_No_Axis_Pts_Y = Fix_No_Axis_Pts_Y
        self.Fix_No_Axis_Pts_Z = Fix_No_Axis_Pts_Z
        self.Fix_No_Axis_Pts_Z4 = Fix_No_Axis_Pts_Z4
        self.Fix_No_Axis_Pts_Z5 = Fix_No_Axis_Pts_Z5
        self.Fnc_Values = Fnc_Values
        self.Identification = Identification
        self.No_Axis_Pts_X = No_Axis_Pts_X
        self.No_Axis_Pts_Y = No_Axis_Pts_Y
        self.No_Axis_Pts_Z = No_Axis_Pts_Z
        self.No_Axis_Pts_Z4 = No_Axis_Pts_Z4
        self.No_Axis_Pts_Z5 = No_Axis_Pts_Z5
        self.No_Rescale_X = No_Rescale_X
        self.Offset_X = Offset_X
        self.Offset_Y = Offset_Y
        self.Offset_Z = Offset_Z
        self.Offset_Z4 = Offset_Z4
        self.Offset_Z5 = Offset_Z5
        self.Reserved = Reserved
        self.Rip_Addr_X = Rip_Addr_X
        self.Rip_Addr_W = Rip_Addr_W
        self.Rip_Addr_Y = Rip_Addr_Y
        self.Rip_Addr_Z = Rip_Addr_Z
        self.Rip_Addr_Z4 = Rip_Addr_Z4
        self.Rip_Addr_Z5 = Rip_Addr_Z5
        self.Src_Addr_X = Src_Addr_X
        self.Src_Addr_Y = Src_Addr_Y
        self.Src_Addr_Z = Src_Addr_Z
        self.Src_Addr_Z4 = Src_Addr_Z4
        self.Src_Addr_Z5 = Src_Addr_Z5
        self.Shift_Op_X = Shift_Op_X
        self.Shift_Op_Y = Shift_Op_Y
        self.Shift_Op_Z = Shift_Op_Z
        self.Shift_Op_Z4 = Shift_Op_Z4
        self.Shift_Op_Z5 = Shift_Op_Z5
        self.Static_Record_Layout = Static_Record_Layout

    def children(self):
        nodelist = []
        if self.Axis_Pts_X is not None: nodelist.append(("Axis_Pts_X", self.Axis_Pts_X))
        if self.Axis_Pts_Y is not None: nodelist.append(("Axis_Pts_Y", self.Axis_Pts_Y))
        if self.Axis_Pts_Z is not None: nodelist.append(("Axis_Pts_Z", self.Axis_Pts_Z))
        if self.Axis_Pts_Z4 is not None: nodelist.append(("Axis_Pts_Z4", self.Axis_Pts_Z4))
        if self.Axis_Pts_Z5 is not None: nodelist.append(("Axis_Pts_Z5", self.Axis_Pts_Z5))
        if self.Axis_Rescale_X is not None: nodelist.append(("Axis_Rescale_X", self.Axis_Rescale_X))
        if self.Dist_Op_X is not None: nodelist.append(("Dist_Op_X", self.Dist_Op_X))
        if self.Dist_Op_Y is not None: nodelist.append(("Dist_Op_Y", self.Dist_Op_Y))
        if self.Dist_Op_Z is not None: nodelist.append(("Dist_Op_Z", self.Dist_Op_Z))
        if self.Dist_Op_Z4 is not None: nodelist.append(("Dist_Op_Z4", self.Dist_Op_Z4))
        if self.Dist_Op_Z5 is not None: nodelist.append(("Dist_Op_Z5", self.Dist_Op_Z5))
        if self.Fnc_Values is not None: nodelist.append(("Fnc_Values", self.Fnc_Values))
        if self.Identification is not None: nodelist.append(("Identification", self.Identification))
        if self.No_Axis_Pts_X is not None: nodelist.append(("No_Axis_Pts_X", self.No_Axis_Pts_X))
        if self.No_Axis_Pts_Y is not None: nodelist.append(("No_Axis_Pts_Y", self.No_Axis_Pts_Y))
        if self.No_Axis_Pts_Z is not None: nodelist.append(("No_Axis_Pts_Z", self.No_Axis_Pts_Z))
        if self.No_Axis_Pts_Z4 is not None: nodelist.append(("No_Axis_Pts_Z4", self.No_Axis_Pts_Z4))
        if self.No_Axis_Pts_Z5 is not None: nodelist.append(("No_Axis_Pts_Z5", self.No_Axis_Pts_Z5))
        if self.No_Rescale_X is not None: nodelist.append(("No_Rescale_X", self.No_Rescale_X))
        if self.Offset_X is not None: nodelist.append(("Offset_X", self.Offset_X))
        if self.Offset_Y is not None: nodelist.append(("Offset_Y", self.Offset_Y))
        if self.Offset_Z is not None: nodelist.append(("Offset_Z", self.Offset_Z))
        if self.Offset_Z4 is not None: nodelist.append(("Offset_Z4", self.Offset_Z4))
        if self.Offset_Z5 is not None: nodelist.append(("Offset_Z5", self.Offset_Z5))
        if self.Rip_Addr_X is not None: nodelist.append(("Rip_Addr_X", self.Rip_Addr_X))
        if self.Rip_Addr_W is not None: nodelist.append(("Rip_Addr_W", self.Rip_Addr_W))
        if self.Rip_Addr_Y is not None: nodelist.append(("Rip_Addr_Y", self.Rip_Addr_Y))
        if self.Rip_Addr_Z is not None: nodelist.append(("Rip_Addr_Z", self.Rip_Addr_Z))
        if self.Rip_Addr_Z4 is not None: nodelist.append(("Rip_Addr_Z4", self.Rip_Addr_Z4))
        if self.Rip_Addr_Z5 is not None: nodelist.append(("Rip_Addr_Z5", self.Rip_Addr_Z5))
        if self.Src_Addr_X is not None: nodelist.append(("Src_Addr_X", self.Src_Addr_X))
        if self.Src_Addr_Y is not None: nodelist.append(("Src_Addr_Y", self.Src_Addr_Y))
        if self.Src_Addr_Z is not None: nodelist.append(("Src_Addr_Z", self.Src_Addr_Z))
        if self.Src_Addr_Z4 is not None: nodelist.append(("Src_Addr_Z4", self.Src_Addr_Z4))
        if self.Src_Addr_Z5 is not None: nodelist.append(("Src_Addr_Z5", self.Src_Addr_Z5))
        if self.Shift_Op_X is not None: nodelist.append(("Shift_Op_X", self.Shift_Op_X))
        if self.Shift_Op_Y is not None: nodelist.append(("Shift_Op_Y", self.Shift_Op_Y))
        if self.Shift_Op_Z is not None: nodelist.append(("Shift_Op_Z", self.Shift_Op_Z))
        if self.Shift_Op_Z4 is not None: nodelist.append(("Shift_Op_Z4", self.Shift_Op_Z4))
        if self.Shift_Op_Z5 is not None: nodelist.append(("Shift_Op_Z5", self.Shift_Op_Z5))
        for i, child in enumerate(self.Reserved or []):
            nodelist.append(("Reserved[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Alignment_Byte', 'Alignment_Float32_Ieee', 'Alignment_Float64_Ieee', 'Alignment_Int64', 'Alignment_Long', 'Alignment_Word', 'Fix_No_Axis_Pts_X', 'Fix_No_Axis_Pts_Y', 'Fix_No_Axis_Pts_Z', 'Fix_No_Axis_Pts_Z4', 'Fix_No_Axis_Pts_Z5', 'Static_Record_Layout', )


class Ref_Characteristic (Node):
    __slots__ = ('Identifier', '__weakref__')
    def __init__(self, Identifier):
        self.Identifier = Identifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Identifier', )


class Ref_Group (Node):
    __slots__ = ('Identifier', '__weakref__')
    def __init__(self, Identifier):
        self.Identifier = Identifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Identifier', )


class Ref_Measurement (Node):
    __slots__ = ('Identifier', '__weakref__')
    def __init__(self, Identifier):
        self.Identifier = Identifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Identifier', )


class Ref_Memory_Segment (Node):
    __slots__ = ('Name', '__weakref__')
    def __init__(self, Name):
        self.Name = Name

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Name', )


class Ref_Unit (Node):
    __slots__ = ('Unit', '__weakref__')
    def __init__(self, Unit):
        self.Unit = Unit

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Unit', )


class Reserved (Node):
    __slots__ = ('Position', 'DataSize', '__weakref__')
    def __init__(self, Position, DataSize):
        self.Position = Position
        self.DataSize = DataSize

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'DataSize', )


class Right_Shift (Node):
    __slots__ = ('Bitcount', '__weakref__')
    def __init__(self, Bitcount):
        self.Bitcount = Bitcount

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Bitcount', )


class Rip_Addr_X  (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Rip_Addr_W  (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Rip_Addr_Y  (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Rip_Addr_Z  (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Rip_Addr_Z4 (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Rip_Addr_Z5 (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Root (Node):
    __slots__ = ('Boolean', '__weakref__')
    def __init__(self, Boolean):
        self.Boolean = Boolean

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Boolean', )


class Shift_Op_X (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Shift_Op_Y (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Shift_Op_Z (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Shift_Op_Z4 (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Shift_Op_Z5 (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Sign_Extend (Node):
    __slots__ = ('Boolean', '__weakref__')
    def __init__(self, Boolean):
        self.Boolean = Boolean

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Boolean', )


class Si_Exponents (Node):
    __slots__ = ('Length', 'Mass', 'Time', 'ElectricCurrent', 'Temperature', 'AmountOfSubstance', 'LuminousIntensity', '__weakref__')
    def __init__(self, Length, Mass, Time, ElectricCurrent, Temperature, AmountOfSubstance, LuminousIntensity):
        self.Length = Length
        self.Mass = Mass
        self.Time = Time
        self.ElectricCurrent = ElectricCurrent
        self.Temperature = Temperature
        self.AmountOfSubstance = AmountOfSubstance
        self.LuminousIntensity = LuminousIntensity

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Length', 'Mass', 'Time', 'ElectricCurrent', 'Temperature', 'AmountOfSubstance', 'LuminousIntensity', )


class Src_Addr_X (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Src_Addr_Y (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Src_Addr_Z (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Src_Addr_Z4 (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Src_Addr_Z5 (Node):
    __slots__ = ('Position', 'Datatype', '__weakref__')
    def __init__(self, Position, Datatype):
        self.Position = Position
        self.Datatype = Datatype

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Position', 'Datatype', )


class Static_Record_Layout (Node):
    __slots__ = ('Boolean', '__weakref__')
    def __init__(self, Boolean):
        self.Boolean = Boolean

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Boolean', )


class Status_String_Ref (Node):
    __slots__ = ('ConversionTable', '__weakref__')
    def __init__(self, ConversionTable):
        self.ConversionTable = ConversionTable

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('ConversionTable', )


class Step_Size (Node):
    __slots__ = ('StepSize', '__weakref__')
    def __init__(self, StepSize):
        self.StepSize = StepSize

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('StepSize', )


class Sub_Function (Node):
    __slots__ = ('Identifier', '__weakref__')
    def __init__(self, Identifier):
        self.Identifier = Identifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Identifier', )


class Sub_Group (Node):
    __slots__ = ('Identifier', '__weakref__')
    def __init__(self, Identifier):
        self.Identifier = Identifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Identifier', )


class Supplier (Node):
    __slots__ = ('Manufacturer', '__weakref__')
    def __init__(self, Manufacturer):
        self.Manufacturer = Manufacturer

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Manufacturer', )


class Symbol_Link (Node):
    __slots__ = ('SymbolName', 'Offset', '__weakref__')
    def __init__(self, SymbolName, Offset):
        self.SymbolName = SymbolName
        self.Offset = Offset

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('SymbolName', 'Offset', )


class System_Constant (Node):
    __slots__ = ('Name', 'Value', '__weakref__')
    def __init__(self, Name, Value):
        self.Name = Name
        self.Value = Value

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Name', 'Value', )


class Unit (Node):
    __slots__ = ('Name', 'LongIdentifier', 'Display', 'Type', 'OptionalParams', '__weakref__')
    def __init__(self, Name, LongIdentifier, Display, Type, OptionalParams = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.Display = Display
        self.Type = Type
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', 'Display', 'Type', )


class Unit_Opt (Node):
    __slots__ = ('Ref_Unit', 'Si_Exponents', 'Unit_Conversion', '__weakref__')
    def __init__(self, Ref_Unit = None, Si_Exponents = None, Unit_Conversion = None):
        self.Ref_Unit = Ref_Unit
        self.Si_Exponents = Si_Exponents
        self.Unit_Conversion = Unit_Conversion

    def children(self):
        nodelist = []
        if self.Si_Exponents is not None: nodelist.append(("Si_Exponents", self.Si_Exponents))
        if self.Unit_Conversion is not None: nodelist.append(("Unit_Conversion", self.Unit_Conversion))
        return tuple(nodelist)

    attr_names = ('Ref_Unit', )


class Unit_Conversion (Node):
    __slots__ = ('Gradient', 'Offset', '__weakref__')
    def __init__(self, Gradient, Offset):
        self.Gradient = Gradient
        self.Offset = Offset

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Gradient', 'Offset', )


class User (Node):
    __slots__ = ('UserName', '__weakref__')
    def __init__(self, UserName):
        self.UserName = UserName

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('UserName', )


class User_Rights (Node):
    __slots__ = ('UserLevelId', 'OptionalParams', '__weakref__')
    def __init__(self, UserLevelId, OptionalParams = None):
        self.UserLevelId = UserLevelId
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('UserLevelId', )


class User_Rights_Opt (Node):
    __slots__ = ('Read_Only', 'Ref_Group', '__weakref__')
    def __init__(self, Read_Only = None, Ref_Group = None):
        self.Read_Only = Read_Only
        self.Ref_Group = Ref_Group

    def children(self):
        nodelist = []
        for i, child in enumerate(self.Ref_Group or []):
            nodelist.append(("Ref_Group[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Read_Only', )


class Var_Address (Node):
    __slots__ = ('Address', '__weakref__')
    def __init__(self, Address):
        self.Address = Address

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Address', )


class Var_Characteristic  (Node):
    __slots__ = ('Name', 'CriterionName', 'Var_Address', '__weakref__')
    def __init__(self, Name, CriterionName, Var_Address = None):
        self.Name = Name
        self.CriterionName = CriterionName
        self.Var_Address = Var_Address

    def children(self):
        nodelist = []
        if self.Var_Address is not None: nodelist.append(("Var_Address", self.Var_Address))
        return tuple(nodelist)

    attr_names = ('Name', 'CriterionName', )


class Var_Criterion (Node):
    __slots__ = ('Name', 'LongIdentifier', 'Value', 'OptionalParams', '__weakref__')
    def __init__(self, Name, LongIdentifier, Value, OptionalParams = None):
        self.Name = Name
        self.LongIdentifier = LongIdentifier
        self.Value = Value
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ('Name', 'LongIdentifier', 'Value', )


class Var_Criterion_Opt (Node):
    __slots__ = ('Var_Measurement', 'Var_Selection_Characteristic', '__weakref__')
    def __init__(self, Var_Measurement = None, Var_Selection_Characteristic = None):
        self.Var_Measurement = Var_Measurement
        self.Var_Selection_Characteristic = Var_Selection_Characteristic

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Var_Measurement', 'Var_Selection_Characteristic', )


class Var_Forbidden_Comb (Node):
    __slots__ = ('CriterionList', '__weakref__')
    def __init__(self, CriterionList):
        self.CriterionList = CriterionList

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('CriterionList', )


class Var_Measurement (Node):
    __slots__ = ('Name', '__weakref__')
    def __init__(self, Name):
        self.Name = Name

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Name', )


class Var_Naming (Node):
    __slots__ = ('Tag', '__weakref__')
    def __init__(self, Tag):
        self.Tag = Tag

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Tag', )


class Var_Selection_Characteristic (Node):
    __slots__ = ('Name', '__weakref__')
    def __init__(self, Name):
        self.Name = Name

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Name', )


class Var_Separator (Node):
    __slots__ = ('Separator', '__weakref__')
    def __init__(self, Separator):
        self.Separator = Separator

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Separator', )


class Variant_Coding (Node):
    __slots__ = ('OptionalParams', '__weakref__')
    def __init__(self, OptionalParams = None):
        self.OptionalParams = OptionalParams

    def children(self):
        nodelist = []
        if self.OptionalParams is not None: nodelist.append(("OptionalParams", self.OptionalParams))
        return tuple(nodelist)

    attr_names = ()


class Variant_Coding_Opt (Node):
    __slots__ = ('Var_Characteristic', 'Var_Criterion', 'Var_Forbidden_Comb', 'Var_Naming', 'Var_Separator', '__weakref__')
    def __init__(self, Var_Characteristic = None, Var_Criterion = None, Var_Forbidden_Comb = None, Var_Naming = None, Var_Separator = None):
        self.Var_Characteristic = Var_Characteristic
        self.Var_Criterion = Var_Criterion
        self.Var_Forbidden_Comb = Var_Forbidden_Comb
        self.Var_Naming = Var_Naming
        self.Var_Separator = Var_Separator

    def children(self):
        nodelist = []
        for i, child in enumerate(self.Var_Characteristic or []):
            nodelist.append(("Var_Characteristic[%d]" % i, child))
        for i, child in enumerate(self.Var_Criterion or []):
            nodelist.append(("Var_Criterion[%d]" % i, child))
        for i, child in enumerate(self.Var_Forbidden_Comb or []):
            nodelist.append(("Var_Forbidden_Comb[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('Var_Naming', 'Var_Separator', )


class Version (Node):
    __slots__ = ('VersoinIdentifier', '__weakref__')
    def __init__(self, VersoinIdentifier):
        self.VersoinIdentifier = VersoinIdentifier

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('VersoinIdentifier', )


class Virtual (Node):
    __slots__ = ('MeasuringChannel', '__weakref__')
    def __init__(self, MeasuringChannel):
        self.MeasuringChannel = MeasuringChannel

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('MeasuringChannel', )


class Virtual_Characteristic (Node):
    __slots__ = ('Formula', 'Characteristic', '__weakref__')
    def __init__(self, Formula, Characteristic):
        self.Formula = Formula
        self.Characteristic = Characteristic

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('Formula', 'Characteristic', )


