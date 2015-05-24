# coding=utf-8
__author__ = 'zhangyanni'

import os
import glob

class path2json(object):
    # Unlimited recursive path generated JSON string for jsTree to generate a directory tree data source.
    # 无限递归路径生成json串，用于jstree生成目录树的数据源

    @staticmethod
    def getJson(path):
        jsonstr="["
        parent=0
        Id=0
        jsonstr=path2json.ToJson(path,parent,jsonstr,Id)+"]"
        return jsonstr

    @staticmethod
    def ToJson(path,parent,jsonstr,Id):
        for i,fn in enumerate(glob.glob(path + os.sep + '*' )):
            if os.path.isdir(fn):
                jsonstr+='''{"attributes":{"id":"'''+ str(Id)+'''"},"parent":"'''+str(parent)+'''","state":{"opened":false},"text":"'''+os.path.basename(fn)+'''","children":['''
                parent=Id
                Id+=1
                for j,li in enumerate(glob.glob(fn + os.sep + '*' )):
                    if os.path.isdir(li):
                        jsonstr+='''{"attributes":{"id":"'''+ str(Id)+'''"},"parent":"'''+str(parent)+'''","state":{"opened":false},"text":"'''+os.path.basename(li)+'''","children":['''
                        parent=Id
                        Id+=1
                        path2json.ToJson(li,parent,jsonstr,Id)
                        jsonstr+="]}"
                        if j<len(glob.glob(fn + os.sep + '*' ))-1:
                            jsonstr+=","
                    else:
                        jsonstr+='''{"attributes":{"id":"'''+ str(Id)+'''"},"parent":"'''+str(parent)+'''","state":{"opened":false},"text":"'''+os.path.basename(li)+'''","type":"leaf"}'''
                        Id+=1
                        if j<len(glob.glob(fn + os.sep + '*' ))-1:
                            jsonstr+=","
                jsonstr+="]}"
                if i<len(glob.glob(path + os.sep + '*' ))-1:
                    jsonstr+=","
            else:

                jsonstr+='''{"attributes":{"id":"'''+ str(Id)+'''"},"parent":"'''+str(parent)+'''","state":{"opened":false},"text":"'''+os.path.basename(fn)+'''","type":"leaf"}'''
                Id+=1
                if i<len(glob.glob(path + os.sep + '*' ))-1:
                    jsonstr+=","
        return jsonstr



#result=path2json .getJson("G:\\PyCharm")
#output=open("G:\\jsonstr.json","w")
#output.write(result )
#output.close()

