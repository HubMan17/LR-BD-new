import time
import yadisk

def start_load(flink, folder, fname):
    y = yadisk.YaDisk(token="y0_AgAAAABoyOlVAAkyOwAAAADdUV3IXphxoyDHR_OTVzxFeszpLfNIJwI")

    if y.check_token():
        
        try:
            # Создаёт новую папку "/test-dir"
            y.mkdir(f"/{folder}")
            
        except:
            # Безвозвратно удаляет "/file-to-remove"
            y.remove(f"/{folder}", permanently=True)
            
            time.sleep(1)
            # Создаёт новую папку "/test-dir"
            y.mkdir(f"/{folder}")
            
        # Загружает "file_to_upload.txt" в "/destination.txt"
        y.upload(flink, f"/{folder}/{fname}")
        
        t = list(y.listdir(f"/{folder}"))[0]
        return t["file"]
    
    else:
        print("Error authorization on disk")
