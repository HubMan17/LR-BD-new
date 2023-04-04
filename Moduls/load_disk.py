import yadisk

# addr_from = 'stestpython5mtp482@yandex.ru' 
#     password  = 'Qaz2584561297'    

# y = yadisk.YaDisk(token="<6105a5b1f19b40c888b1287316745b43>")
y = yadisk.YaDisk(token="y0_AgAAAABoyOlVAAkyOwAAAADdUV3IXphxoyDHR_OTVzxFeszpLfNIJwI")

# Проверяет, валиден ли токен
print(y.check_token())


# Загружает "file_to_upload.txt" в "/destination.txt"
# y.upload(r"C:\Users\User\Desktop\АФХД (1).docx", "/test/АФХД (1).docx")

# Выводит содержимое "/some/path"
# print(list(y.listdir("/test"))[0])
t = list(y.listdir("/test"))[0]
print(t["file"])

# Получает общую информацию о диске
# print(y.get_disk_info())