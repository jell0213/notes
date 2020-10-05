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
