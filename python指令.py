1.excel 檔案
2.計時器
3.格式化輸出
#######################################  excel 檔案
wb = Workbook()
ws = wb.active
ws.append([folder_name,"mod="+str(num_mod)])
ws.append(["","","文字檔","","","","圖片檔"])
ws.append(["檔名","嵌密量","大小(bit)","壓縮大小","檔案壓縮","嵌密壓縮","大小(bit)","壓縮大小","檔案壓縮","嵌密壓縮"])
wb.save(dir_out)
wb = openpyxl.load_workbook(dir_out)
ws = wb['Sheet']
ws.append([file_name,
               count,
               size_lc,
               size_lc_gz,
               str(round(compress_lc,3))+' %',
               str(round(compress_code_lc,3))+' %',
               size_image_lc,
               size_image_lc_gz,
               str(round(compress_image_lc,3))+' %',
               str(round(compress_code_image_lc,3))+' %'])            
wb.save(dir_out)#寫檔後存檔


#######################################計時器
# -*- coding: utf-8 -*-
import time
tStart = time.time()#計時開始
 
#模擬要測量的function
time.sleep(2)
print "abc"
for x in range(1000):
    x += 1
    print x
#end of 模擬要測量的function
 
tEnd = time.time()#計時結束
#列印結果
print "It cost %f sec" % (tEnd - tStart)#會自動做近位
print tEnd - tStart#原型長這樣


########################################格式化輸出
print("{:08d}abc{:08d}".format(i,i))#多變數
