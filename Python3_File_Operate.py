__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/4/13
"""
Description:
    1. 文件操作的步骤：
        打开文件 -> 操作文件 -> 关闭文件
        【切记：最后要关闭文件（否则可能会有意想不到的结果）】
    2. 为了防止忘记关闭文件，可以使用上下文管理器来打开文件
        with open('文件路径','模式') as 文件句柄:
    3. 打开文件的模式有：
        r，只读模式（默认）。
        w，只写模式。【不可读；不存在则创建；存在则删除内容；】
        a，追加模式。【可读；   不存在则创建；存在则只追加内容；】
        r+，可读写文件。【可读；可写；可追加】
        w+，写读
        "U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）
        rU
        r+U
        "b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）
        rb
        wb
        ab
    4. 关闭文件
        文件句柄.close()
    5. 操作文件：
        detach
    6. #占位
       fileno（返回文件描述符,用于底层操作系统的 I/O 操作）
       fid = 文件句柄.fileno()
       print(fid)
    7. flush（刷新缓冲区，将缓冲区中的数据立刻写入文件）
         文件句柄.flush()
    8. isatty（判断文件是否连接到一个终端设备，返回布尔值）
         文件句柄.isatty()
    9. read（从文件中读取指定的字符数，默认读取全部）
         str = 文件句柄.read()      #读取整个文件
         str1 = 文件句柄.read(10)   #读取文件前10个字符
         readable（判断文件是否可读，返回布尔值）
         文件句柄.readable()
    10 readline（每次最多读取一行数据，每行的最后包含换行符'\n'）
         print(文件句柄.readline())   #读取第一行数据
         print(文件句柄.readline(3))  #读取第二行前3个字符
         print(文件句柄.readline())   #读取第二行剩余字符
         print(文件句柄.readline())   #读取第三行
    11. seek（移动文件读取的指针，如果文件中包含中文，移动指针必须是3的倍数，不然会报错，因为一个中文字符等于3个字节）
         文件句柄.seek(6)
    12. seekable（判断文件指针是否可用，返回布尔值）
         文件句柄.seekable()

    13. tell（获取指针位置）
            文件句柄.tell()

    14. truncate（截断，把指针后面的内容删除，并写入文件，要在可写模式下操作）
            f = open('text.txt','r+',encoding='utf-8')
            f.seek(9)   #把指针移动到第9个字节后面（即第3个中文后面）
            f.truncate()  #把第3个中文后面的字符删除，并写入文件
            f.close()

    15. writable（判断文件是否可写，返回布尔值）
            文件句柄.writable()
            write（把字符串写入文件，并返回字符数）
            文件句柄.write('字符串')
"""

if __name__ == '__main__':
    pass

