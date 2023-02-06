class stylesheet:
    def default():
        return("# 0 2 5 2 4")
    def defaultBorder():
        return("1 px")
    class tag:
        def h1():
            return("h1")
    class instruction:
        def color():
            return("You have to write it like that: [# 0 0 0 0 0 0] ")
        def border():
            return("You have to write it like that: [0 px] ")
        def align():
            return("You have to write it like that: [0 sfx] ")
        def posix():
            return("You have to write it like that: [0 psx] ")
        def overflow():
            return("You have to write it like that: [0 ovw] ")
        def outline():
            return("You have to write it like that: [0 cm] ")
    def color(tag,col):
        parts=col.split(None)
        hetest=str(parts[0])
        if hetest=='#':
            return("set "+tag+" to "+col)
        else:
            return("Not valid HEX dezimal code")
    def border(tag,px):
        parts=px.split(None)
        hetest=str(parts[1])
        if hetest=='px':
            return("set "+tag+" to "+px)
        else:
            return("Not valid px")
    def align(tag,loc):
        parts=loc.split(None)
        hetest=str(parts[1])
        if hetest=='sfx':
            return("set "+tag+" to "+loc)
        else:
            return("Not valid sfx")
    def posix(tag,psx):
        parts=psx.split(None)
        hetest=str(parts[1])
        if hetest=='psx':
            return("set "+tag+" to "+psx)
        else:
            return("Not valid posix")
    def overflow(tag,ow):
        parts=ow.split(None)
        hetest=str(parts[1])
        if hetest=='ovw':
            return("set "+tag+" to "+ow)
        else:
            return("Not valid overflow")
    def outline(tag,out):
        parts=out.split(None)
        hetest=str(parts[1])
        if hetest=='cm':
            return("set "+tag+" to "+out)
        else:
            return("Not valid outline")
