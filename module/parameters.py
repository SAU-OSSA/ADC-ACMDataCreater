import module.defineClass


class defaultPara(object):

    def __init__(self):
        self.Code = ".\\code\\main.cpp"
        self.Check1Code = ".\\code\\check1.cpp"
        self.Check2Code = ".\\code\\check2.cpp"

        self.TmpPath = ".\\code\\debug\\"
        self.InpPath = ".\\data\\testData\\"
        self.OupPath = ".\\data\\testData\\"
        self.CheckPath = ".\\data\\check\\"

        self.DataNum = 40

        self.OupModel = "out"
        self.Check1Model = "check1"
        self.Check2Model = "check2"


module.defineClass.val("defaultPara", defaultPara())
